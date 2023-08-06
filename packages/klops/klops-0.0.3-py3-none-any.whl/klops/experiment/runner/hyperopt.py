"""_summary_
"""
from typing import Any, Dict, List, Union
from datetime import datetime

from hyperopt import STATUS_OK, fmin
import mlflow
import numpy as np
import pandas as pd
from sklearn import metrics

from klops.experiment.runner import BaseRunner
from klops.experiment.exception import ExperimentFailedException


class HyperOptRunner(BaseRunner):
    """_summary_ The HyperOptRunner Implementation.
    """

    def __init__(self,
                 estimator: Any,
                 x_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 y_train: Union[pd.DataFrame, np.ndarray, List, Dict],
                 x_test: Union[np.ndarray, pd.DataFrame, List[Dict]],
                 y_test: Union[np.ndarray, pd.DataFrame, List],
                 search_spaces: Dict,
                 experiment_name: str,
                 tags: Dict = {},
                 max_evals: int = 20) -> None:
        """_summary_

        Args:
            estimator (Any): _description_
            x_train (Union[pd.DataFrame, np.ndarray, List, Dict]): _description_
            y_train (Union[pd.DataFrame, np.ndarray, List, Dict]): _description_
            x_test (Union[np.ndarray, pd.DataFrame, List[Dict]]): _description_
            y_test (Union[np.ndarray, pd.DataFrame, List]): _description_
            search_spaces (Dict): _description_
            experiment_name (str): _description_
            max_evals (int, optional): _description_. Defaults to 20.
        """
        self.search_spaces = search_spaces
        self.max_evals = max_evals
        self.experiment_name = experiment_name

        super(HyperOptRunner, self).__init__(
            estimator=estimator, x_train=x_train, y_train=y_train,
            x_test=x_test, y_test=y_test, tags=tags)

    def objective(self, hyper_parameters: Dict) -> Dict:
        """_summary_

        Returns:
            Dict: _description_
        """
        run_name = self.experiment_name + "_" + datetime.now().strftime("%Y%m%d:%H%M%S")
        with mlflow.start_run(run_name=run_name):
            result = {"status": STATUS_OK}
            
            mlflow.set_tags({**self.tags, "opt":"hyperopt"})
            mlflow.log_params({
                **hyper_parameters,
                "estimator": self.estimator.__class__.__name__})

            model = self.estimator
            model.fit(self.x_train, self.y_train)
            preds = model.predict(self.x_test)
            rmse = self.call_metrices("rmse", self.y_test, preds)
            for metric, arguments in self.metrices.items():
                metric_name, score = self.call_metrices(metric, self.y_test, preds, **arguments)
                result[metric_name] = score
            return {**result, "loss": rmse}

    def run(self,
            metrices: Dict = {"mean_squared_error": {},
                              "root_mean_squared_error": {}},
            **kwargs: Any) -> Any:
        """_summary_
        Run the experiment using hyperopt.fmin function.
        Args:
            metrices (_type_, optional): _description_.
                Defaults to {"mean_squared_error": {}, "root_mean_squared_error": {}}.
                The sklearn metrices. All metrices method name could be seen here:
                https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
        """
        try:

            self.metrices = metrices
            fmin(
                fn=self.objective,
                space=self.search_spaces,
                max_evals=self.max_evals,
                **kwargs
            )
        except Exception as exception:
            raise ExperimentFailedException(
                message=str(exception)) from exception


__all__ = ["HyperOptRunner"]
