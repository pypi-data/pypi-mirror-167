#!/usr/bin/python
"""
==================================================
LASSOBench
High-Dimensional Hyperparameter
Optimization Benchmark
Contact: kenan.sehic@cs.lth.se
=================================================
"""
import numpy as np
from celer import Lasso

from sparse_ho.models import WeightedLasso
from sparse_ho.criterion import HeldOutMSE, CrossVal
from sparse_ho.utils import Monitor

from celer.datasets import make_correlated_data

from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import f1_score


class Synt_bench():
    def __init__(self, n_features=1280, n_samples=640,
                 snr_level=1, corr_level=0.6, dense_nnz=0.0078125,
                 w_true=None, n_splits=5, test_size=0.15,
                 tol_level=1e-4, eps_support=1e-6, seed=42):
        """
        Synthetic Benchmark that is used to test a HPO algorithm
        on different conditions. It is based on the cross-validation critetion.
        Args:
            input_config: numpy array sampled within [-1, 1] with d number of elements
            n_features: the size of search space d>0 (i.e., the number of features)
            n_samples: the number of samples in a dataset
            snr_level: the level of noise with SNR=1 being very noisy and SNR=10 is almost noiseless.
            corr_level: the level of correlation withint features
            dense_nnz: the density of nonzero elements in true reg coef betas
            w_true: the predefined reg coef betas
            n_splits: the number of data splits for cross-validation
            test_size: the percentage of test data
            eps_support: the support threshold
            seed: the seed number
        Return:
            evaluate: val_loss (the cross-validation loss for evaluate)
            test: mspe_div (the mean-squared prediction error divided by the oracle error)
                  fscore (the F-measure for support recovery)
        """

        self.tol_level = tol_level

        X, y, self.w_true = make_correlated_data(
            n_samples=n_samples, n_features=n_features,
            corr=corr_level, w_true=w_true,
            snr=snr_level, density=dense_nnz,
            random_state=seed)

        # split train and test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=seed)

        self.kf = KFold(shuffle=True, n_splits=n_splits, random_state=seed)

        alpha_max = np.max(np.abs(
            self.X_train.T @ self.y_train)) / len(self.y_train)
        alpha_min = alpha_max / 1e2

        self.log_alpha_min = np.log(alpha_min)
        self.log_alpha_max = np.log(alpha_max)

        self.eps_support = eps_support

        self.coef_true_support = np.abs(self.w_true) > self.eps_support
        self.mspe_oracle = mean_squared_error(
            self.X_test @ self.w_true, self.y_test)

    def scale_domain(self, input_config):
        # Scaling the domain
        input_config_copy = np.copy(input_config)
        old_min = -1
        old_max = 1
        scale_input = ((input_config_copy - old_min) / (old_max - old_min)) * (
            self.log_alpha_max - self.log_alpha_min)
        scale_input = scale_input + self.log_alpha_min

        return scale_input

    def evaluate(self, input_config):
        scaled_x = self.scale_domain(input_config)

        estimator = Lasso(fit_intercept=False, max_iter=100, warm_start=True)
        model = WeightedLasso(estimator=estimator)
        monitor = Monitor()
        sub_criterion = HeldOutMSE(None, None)
        criterion = CrossVal(sub_criterion, cv=self.kf)
        val_loss = criterion.get_val(model, self.X_train, self.y_train,
                                     log_alpha=scaled_x,
                                     monitor=monitor, tol=self.tol_level)

        return val_loss

    def test(self, input_config):
        scaled_x = self.scale_domain(input_config)
        estimator = Lasso(fit_intercept=False, max_iter=100, warm_start=True)
        estimator.weights = np.exp(scaled_x)
        estimator.fit(self.X_train, self.y_train)

        coef_hpo_support = np.abs(estimator.coef_) > self.eps_support
        fscore = f1_score(self.coef_true_support, coef_hpo_support)
        mspe = mean_squared_error(estimator.predict(self.X_test), self.y_test)
        mspe_div = mspe/self.mspe_oracle

        return mspe_div, fscore
