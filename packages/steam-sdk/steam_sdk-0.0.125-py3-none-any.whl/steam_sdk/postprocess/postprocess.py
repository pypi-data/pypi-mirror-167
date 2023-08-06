from typing import List
import numpy as np
from sklearn.metrics import mean_squared_error

class Metrics:

    metrics_result: List = []

    def __init__(self, metrics_to_do: List[str] = [], var_to_interpolate: list = None, var_to_interpolate_ref: list = None,
                 time_vector: list = None, time_vector_ref: list = None, flag_run: bool = True):

        # Define inputs
        self.metrics_to_do = metrics_to_do
        self.var_to_interpolate = var_to_interpolate
        self.var_to_interpolate_ref = var_to_interpolate_ref
        self.time_vector = time_vector
        self.time_vector_ref = time_vector_ref

        if flag_run:
            self.run_metrics()

    def run_metrics(self):

        # unpack inputs
        metrics_to_do = self.metrics_to_do
        var_of_interest = self.var_to_interpolate
        var_ref = self.var_to_interpolate_ref
        time_vector = self.time_vector
        time_vector_ref = self.time_vector_ref

        # variables which need to be interpolated
        list_metrics_that_need_interpolation = ['maximum_abs_error', 'RMSE', 'RMSE_ratio']
        list_metrics_that_need_interpolation_ref = ['maximum_abs_error', 'RMSE', 'RMSE_ratio']

        # interpolation of variable when necessary using the time_vector of the reference as time_stamps
        if any(n in metrics_to_do for n in list_metrics_that_need_interpolation):
            time_stamps = np.linspace(time_vector_ref[0], time_vector_ref[-1], num=len(time_vector_ref))
            var_of_interest = self._interpolation(time_stamps, time_vector, var_of_interest)
        if any(n in metrics_to_do for n in list_metrics_that_need_interpolation_ref):
                time_stamps_ref = np.linspace(time_vector_ref[0], time_vector_ref[-1], num=len(time_vector_ref))
                var_ref = self._interpolation(time_stamps_ref, time_vector_ref, var_ref)

        # evaluating which metrics will be done and appending results to metrics_result
        self.metrics_result = []
        for metric in metrics_to_do:
            if metric == 'maximum_abs_error':
                result = self._maximum_abs_error(var_of_interest, var_ref)
            elif metric == 'RMSE':
                result = self._RMSE(var_of_interest, var_ref)
            elif metric == 'RMSE_ratio':
                result = self._RMSE_ratio(var_of_interest, var_ref)
            elif metric == 'quench_load_error':
                result = self._quench_load_error(time_vector, var_of_interest, time_vector_ref, var_ref)
            elif metric == 'quench_load':
                result = self._quench_load(time_vector, var_of_interest)
            elif metric == 'max':
                result = self._peak_value(var_of_interest)
            else:
                raise Exception(f'Metric {metric} not understood!')
            self.metrics_result.append(result)

    # calculating metrics
    @staticmethod
    def _interpolation(linspace_time_stamps, time_vector, var_to_interpolate):
        return np.interp(linspace_time_stamps, time_vector, var_to_interpolate) if len(
            var_to_interpolate) != 0 else []

    @staticmethod
    def _maximum_abs_error(y, y_ref):
        return max(abs(y - y_ref))

    @staticmethod
    def _RMSE(y, y_ref):
        return np.sqrt(mean_squared_error(y, y_ref))

    def _RMSE_ratio(self, y, y_ref):
        return np.sqrt(mean_squared_error(y, y_ref))/self._peak_value(y_ref)

    def _quench_load_error(self, time_vector, Ia, time_vector_ref, Ia_ref):
        return self._quench_load(time_vector, Ia) - self._quench_load(time_vector_ref, Ia_ref)

    @staticmethod
    def _quench_load(time_vector, Ia):
        dt = [*np.diff(time_vector), 0]
        quench_load_sum = np.cumsum((Ia ** 2) * dt)
        quench_load = quench_load_sum[-1]

        return quench_load

    @staticmethod
    def _peak_value(signal):
        return max(signal)