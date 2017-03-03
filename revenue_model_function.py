import scipy.special as sp
import numpy as np
import scipy.integrate as itg
import matplotlib.pyplot as plt
from spend_function import SpendFunction
from time_function_expression import TimeFunction

class RevenueModel():

    def __init__(self, spend_pars, time_pars, revenue_max, window_time):

        self.spend_pars = spend_pars
        self.time_pars = time_pars
        self.window_time = window_time
        self.revenue_max = revenue_max

    def calculate_expected_revenue(self, spend_array):

        time_model = TimeFunction(*self.time_pars)
        expected_revenue = 0
        current_day = len(spend_array)

        for t in range(self.window_time-1, current_day):
            revenue_response = 0
            for s_window in range(t-self.window_time, t):
                revenue_response += SpendFunction.calculate_spend_resp(spend_array[s_window], self.spend_pars)
            revenue_response /= self.window_time
            lower_bound = current_day-t-self.window_time
            upper_bound = current_day-t+1
            time_response = itg.quad(time_model.time_function, lower_bound, upper_bound)

            expected_revenue += revenue_response*time_response[0]

        return expected_revenue * self.revenue_max

if __name__ == "__main__":

    spend_array = [10, 14, 20, 12, 5, 10, 20, 10, 0, 14, 18, 3, 0, 19, 20, 12, 3, 0, 14, 15, 20, 13]
    spend_pars = [15, 0.6]
    time_pars = [4, 0.5, 0.2]
    revenue_max = 1000
    window_time = 3
    revenue_model = RevenueModel(spend_pars, time_pars, revenue_max, window_time)

    revenue = []

    for i in range(1, len(spend_array)):
        revenue.append(revenue_model.calculate_expected_revenue(spend_array[0:i]))
    plt.figure()
    plt.plot(revenue)
    plt.show()

