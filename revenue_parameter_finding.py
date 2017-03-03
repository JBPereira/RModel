import scipy
import numpy as np
import scipy.integrate as itg
import matplotlib.pyplot as plt
from revenue_model_function import RevenueModel
import random

class RevenueFitter():

    def __init__(self, opt_algorithm = "ls"):
        self.opt_algorithm = opt_algorithm

    def function_to_minimize(self, real_revenue, time_pars, spend_pars, revenue_max, window_time, spend_array):

        '''

        :param real_revenue: array with the actual data up until today
        :param time_pars: parameters to use in time response model (mean, std, decay)
        :param spend_pars: parameters to use in the spend response model (k and teta)
        :param window_time: moving average to use in the revenue estimation
        :param spend_array: array with the costs up until today
        :return: model parameters that minimize the distance of the predicted revenue to the actual revenue
        '''

        revenue_model = RevenueModel(spend_pars, time_pars, revenue_max, window_time)
        total_revenue_difference = 0

        for t in range(window_time, len(real_revenue)):
            expected_revenue_t = revenue_model.calculate_expected_revenue(spend_array[:t])
            total_revenue_difference += (real_revenue[t] - expected_revenue_t)

        return total_revenue_difference

    def fit_parameters(self, real_revenue, spend_array, number_of_seeds):
        bounds = [[1,3], [0.01, 7], [0.01, 7], [0.01, 7], [1, 40], [0.01, 5], [10, 10000]]
        min_distance = scipy.inf
        opt_params = []

        for i in range(number_of_seeds):

            print float(i)/number_of_seeds * 100

            window_time = random.randint(*bounds[0])
            time_pars = [self.rd(*bounds[tp]) for tp in range(1, 4)]
            time_pars.append(window_time)
            spend_pars = [self.rd(*bounds[sp]) for sp in range(4, 6)]
            spend_pars.append(window_time)
            revenue_max = self.rd(*bounds[5])

            iteration_distance = self.function_to_minimize(real_revenue, spend_pars, time_pars, revenue_max, window_time, spend_array)
            if iteration_distance < min_distance:
                min_distance = iteration_distance
                opt_params = [time_pars, spend_pars, revenue_max, window_time]
        return opt_params


    @staticmethod
    def rd(lb, ub):
        return lb + random.random()*ub

if __name__ == "__main__":
    spend_array = [10, 14, 20, 12, 5, 10, 20, 10, 0,
                   14, 18, 3, 0, 19, 20, 12, 3, 0, 14, 15, 20, 13,
                   12, 15, 0, 18, 20, 18, 14, 5, 9, 10, 15]
    actual_revenue = [1, 1.3, 3, 4, 3.45, 5, 4.5, 8, 6.73,
                   5.45, 5.89, 8.45, 7.45, 5.3, 6.7, 8.6, 10, 10.35, 8.32, 7.56, 8.56, 9.56,
                   10.34, 10.78, 11.23, 9.34, 12, 12.3, 12.12, 11.2, 9.2, 8.7, 10]
    RF = RevenueFitter()
    pars = RF.fit_parameters(actual_revenue, spend_array, 1000)
    print pars