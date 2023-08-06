
import optuna
from optuna.storages._cached_storage import _CachedStorage
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import inspect
from collections import defaultdict
from functools import partial
from joblib import parallel_backend

class Study(optuna.study.Study):
    """
    Extension to an optuna Study. This extension caches the target functions and plot_hyperparameters
    provides a good side-by-side overvew of the hyperparameters over the targets.
    
    For more information, check out Optuna Study.
    """
    
    def __init__(self, study, *target, trainer=None, grid=None):
        """
        Call create_study to instantiate a study
        """
        super().__init__(study.study_name, study._storage, study.sampler, study.pruner)
        assert len(target) > 0, 'You need to define at least one target'
        for t in target:
            assert type(t) == str, 'Only str names for targets are currently supported'
        self.target = target
        self.trainer = trainer
        self.grid = grid
        self._filter_sd = None
        self._filter_upper = None
        self._filter_lower = None
        
    @classmethod
    def create_study(cls, *target, trainer=None, storage=None, sampler=None, pruner=None, 
                     study_name=None, direction=None, directions=None, load_if_exists=False, grid=None):
        """
        Uses optuna.create_study to create a Study. This extension registers the target metrics for inspection.
        
        Arguments:
            *target: 'loss', str, callable, Trainer or Evaluator
                When called with no targets, this is set to 'loss'
                When called with a trainer, this is set to 'loss' + all metrics that are registered 
                by the trainer.
                When called with an evaluator, this is set all metrics that are registered 
                by the evaluator.
                Otherwise call with a sequence of callables or strings in the same order they are registered by
                the Trainer that is used, e.g. a `Trainer(metrics='f1_score')` will have the `optimum` function return
                `(loss, f1_score)`, therefore, register the study with `Study.create_study('loss', f1_score)`.
                When direction is omitted, loss is set to minimize and all other directions to maximize.
            other arguments: check optuna
        """
        if grid is not None:
            assert type(grid) == dict, 'You have to pass a dict to grid'
            sampler = optuna.samplers.GridSampler(grid)
        if len(target) == 0:
            target = ['loss']
        if len(target) == 1:
            from ..train.trainer import Trainer
            if type(target[0]) == Trainer:
                trainer=target[0]
                target = ['loss'] + [ m.__name__ for m in target[0].metrics ]
            from .evaluate import Evaluator
            if type(target[0]) == Evaluator:
                trainer=target[0]
                target = [ m.__name__ for m in target[0].metrics ]
        if direction is None and directions is None:
            if len(target) > 1:
                directions = [ 'minimize' if t == 'loss' else 'maximize' for t in target ]
            else:
                direction = 'minimize' if target[0] == 'loss' else 'maximize'
        study = optuna.create_study(storage=storage, sampler=sampler, pruner=pruner,
                                    study_name=study_name, direction=direction, directions=directions, 
                                    load_if_exists=load_if_exists)
        return cls(study, *target, trainer=trainer, grid=grid)
    
    def ask(self, fixed_distributions=None):
        if not self._optimize_lock.locked():
            if is_heartbeat_enabled(self._storage):
                warnings.warn("Heartbeat of storage is supposed to be used with Study.optimize.")

        fixed_distributions = fixed_distributions or {}
        fixed_distributions = {
            key: _convert_old_distribution_to_new_distribution(dist)
            for key, dist in fixed_distributions.items()
        }

        # Sync storage once every trial.
        if isinstance(self._storage, _CachedStorage):
            self._storage.read_trials_from_remote_storage(self._study_id)

        trial_id = self._pop_waiting_trial_id()
        if trial_id is None:
            trial_id = self._storage.create_new_trial(self._study_id)
        trial = Trial(self, trial_id)

        for name, param in fixed_distributions.items():
            trial._suggest(name, param)

        return trial
    
    def optimize(self, func, n_trials=None, timeout=None, catch=(), callbacks=None, 
                 gc_after_trial=False, show_progress_bar=False):
        """
        See Optuna's optimize, this extensions adds passing the trainer to the trial function.
        """
        
        args = len(inspect.getargspec(func)[0])
        if args == 2:
            assert self.trainer is not None, 'You can only pass a func with two arguments when trainer/evaluator is set'
            func = partial(func, self.trainer)
        try:
            del self._rules
        except: pass
        try:
            del self._results
        except: pass
        super().optimize(func, n_trials=n_trials, timeout=timeout, catch=catch, callbacks=callbacks,
                      gc_after_trial=gc_after_trial, show_progress_bar=show_progress_bar)        
    
    def __repr__(self):
        return repr(self.validate())
    
    #def filter_targets(self, results):
    #    return [ results[t] for t in self.target ]
    
    @property
    def parameters(self):
        return self.trials[0].params.keys()

    @property
    def results(self):
        try:
            return self._results
        except:
            table = []
            for t in self.trials:
                for param, paramv in t.params.items():
                    for target, value in zip(self.target, t.values):
                        table.append((t.number, param, paramv, target, value))
            if len(table) > 0:
                return pd.DataFrame(table, columns=['trial', 'parameter', 'parametersetting', 
                                                    'target', 'targetvalue'])
            for t in self.trials:
                for target, value in zip(self.target, t.values):
                    table.append((t.number, target, value))
            self._results = pd.DataFrame(table, columns=['trial', 'target', 'targetvalue'])
            return self._results
            
    def _filtered_target(self):
        r = set(self.results.trial)
        df = self.results[self.results.trial.isin(self.filtered_trials())]
        if self._filter_sd is not None:
            firstp = list(self.parameters)[0]
            t = df[df.parameter == firstp].targetvalue
            mean = np.mean(t)
            sd = np.std(t)
            s = set(df[(df.targetvalue > mean - self._filter_sd * sd) & (df.targetvalue < mean + self._filter_sd * sd)].trial)
            r = r.intersection(s)
        if self._filter_lower is not None:
            s = set(df[(df.targetvalue > self._filter_lower)].trial)
            r = r.intersection(s)
        if self._filter_upper is not None:
            s = set(df[(df.targetvalue < self._filter_upper)].trial)
            r = r.intersection(s)
        return r
    
    def filter_target(self, sd=None, lower=None, upper=None):
        """
        Filter the results so that points are excluded based on the following rules:
        
        Args:
            sd: float (None)
                when set, compute the mean and std for the target and exclude 
                all results outside 
                [ mean(target) - sd * std(target), mean(target) + sd * std(target)]
                
            lower: float (None)
                when set, exclude points with a targetvalue lower that the given threshold
                
            higher: float (None)
                when set, exclude points with a targetvalue higher that the given threshold
        """
        self._filter_sd = sd
        self._filter_lower = lower
        self._filter_upper = upper
    
    @property
    def rules(self):
        try:
            return self._rules
        except:
            if len(self.trials) > 0:
                #t = self._filtered_target()
                self._rules = pd.DataFrame(columns=['parameter', 'low', 'high'])
                t = self.trials[0]
                for parameter, dist in t.distributions.items():
                    self._rules.loc[len(self._rules)] = (parameter, dist.low, dist.high)
                return self._rules
            
    def filtered_trials(self):
        df = self.results
        for i, r in self.rules.iterrows():
            f = (df.parameter == r.parameter) & (df.parametersetting  >= r.low) & (df.parametersetting  <= r.high)
            if i > 0:
                s = s.intersection(set(df[f].trial))
            else:
                s = set(df[f].trial)
        return s
    
    def filtered_results(self):
        df = self.results
        df = df[df.trial.isin(self._filtered_target())]
        df = df[df.trial.isin(self.filtered_trials())]  
        return df

    def pivotted_results(self):
        from pipetorch.data import DFrame
        targetvalues = self.results[['trial', 'targetvalue']].drop_duplicates().set_index('trial')
        trials = self.results.pivot(index='trial', columns='parameter', values='parametersetting')
        data = trials.join(targetvalues)
        return DFrame(data)
    
    def rule(self, parameter, low=None, high=None):
        if low is not None:
            self.rules.loc[self.rules.parameter == parameter, 'low'] = low
        if high is not None:
            self.rules.loc[self.rules.parameter == parameter, 'high'] = high   

    def distribution(self, param):
        dist = self.trials[0].distributions[param]
        return dist
    
    def is_log_distribution(self, param):
        return self.distribution(param).__class__.__name__.startswith('Log')
    
    def plot_hyperparameters(self, figsize=None, logscale=['loss']):
        """
        Plots the sensitivity of each hyperparameter over each recorded metric.
        
        Arguments:
            figsize: (width, height) None
                controls the size of the figure displayed
            logscale: ['loss']
                list of metrics whose y-axis is shown as a log scale. By default this is done for the loss
                because the learning rate is often sampled from a log distribution and this makes it easier
                to estimate the optimum.
        """
        results = self.results
        trials = self.filtered_trials().intersection(self._filtered_target())
        parameters = self.parameters
        if figsize is None:
            figsize = (4 * len(parameters), 4 * len(self.target))
        
        fig, axs = plt.subplots(len(self.target), len(parameters), sharex='col', sharey='row', figsize=figsize)
        
        if len(parameters) == 1:
            if len(self.target) == 1:
                axs = np.array([[axs]])
            else:
                axs = np.expand_dims(axs, axis=1)
        elif len(self.target) == 1:
            axs = np.expand_dims(axs, axis=0)
        for parami, param in enumerate(parameters):
            for targeti, target in enumerate(self.target):
                subset = results[(results.parameter == param) & (results.target == target) & results.trial.isin(trials)]
                self._subplot(axs[targeti, parami], subset)
                subset = results[(results.parameter == param) & (results.target == target) & ~results.trial.isin(trials)]
                self._subplot_hidden(axs[targeti, parami], subset)
                if targeti == 0:
                    axs[targeti, parami].set_title(param)
                    if self.is_log_distribution(param):
                        axs[targeti, parami].set_xscale('log')
                if target in logscale:
                    axs[targeti, parami].set_yscale('log')
                if parami == 0:
                    axs[targeti, parami].set_ylabel(target)

    def plot_targets(self, *targets, parameter=None, **kwargs):
        """
        Plots the target results in a single figure
        
        Arguments:
            *targets: str (None)
                the targets to plot
            parameter: str (None)
                the parameter to plot, or None to plot all data which is fine when there is only one parameter
            **kwargs: dict
                arguments for Pandas DataFrame.plot
                
        Returns: matplotlib.axes.Axes
            of the plotted figure, which can be used to extend or modify the figure
        """
        r = self.results
        if parameter is not None:
            r = r[r.parameter == parameter]
        targets = targets if len(targets) > 0 else self.target
        
        
        curves = [ r[r.target==t].sort_values(by='parametersetting') for t in targets ]
        for t, c in zip(self.target, curves):
            try:
                c.plot(x='parametersetting', y='targetvalue', label=t, ax=ax)
            except:
                ax = c.plot(x='parametersetting', y='targetvalue', label=t, **kwargs)
        plt.legend()
        return ax
                    
    def trial_targets(self):
        """
        lists to metrics over the trials.
        """
        l = defaultdict(list)
        for t in self.trials:
            for target, value in zip(self.target, t.values):
                l[target].append(value)
        return pd.DataFrame.from_dict(l)        
       
    def validate(self):
        """
        Reports the mean and variance for each metric over the trials, providing more stable outcomes using
        n-fold cross validation.
        """
        l = defaultdict(list)
        for t in self.trials:
            for target, value in zip(self.target, t.values):
                l[target].append(value)
        mean = []
        std = []
        for target, values in l.items():
            mean.append(np.mean(values))
            std.append(np.std(values))
        return pd.DataFrame({'target':self.target, 'mean':mean, 'std':std})        
        
    def _subplot(self, ax, subset):
        x = subset.parametersetting.astype(np.float64)
        y = subset.targetvalue.astype(np.float64)
        z = subset.trial
        ax.scatter(x, y, c=z, cmap='plasma')
        
    def _subplot_hidden(self, ax, subset):
        x = subset.parametersetting.astype(np.float64)
        y = subset.targetvalue.astype(np.float64)
        ax.scatter(x, y, s=1)
        
    def plot(self):
        optuna.visualization.plot_slice(self, params=["hidden"],
                                  target_name="F1 Score")
    
class Trial(optuna.trial.Trial):
    def suggest_lr(self, name, low, high):
        sequence = [ l * 10 for l in range ]
        
    def suggest_categorical(self, name, choices=None):
        try:
            choices = choices or self.study.grid[name]
        except: pass
        return super().suggest_categorical(name, choices)
