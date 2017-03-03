#import integrate
import scipy.integrate as integrate

def calculate_expected_output(spend_array,
                              time_function,
                              spend_function,
                              time_spend_function_pars,
                              time_window=3):

    '''
    :param spend_array: costs up until current day
    :param time_function: Hard-coded for now as normal, but can be changed in the future
    :param spend_function: Hard-coded for now as gamma function
    :param time_spend_function_pars: For now [mean, standard deviation, decay, k, teta, Rmax
    :param time_window: time interval to consider in the time function
    :return: expected output for given parameters and data
    '''

    number_of_days = len(spend_array)
    output=0
    for i in range(number_of_days):
        cumulative_spend_factor = spend_function(time_spend_function_pars[3,4], spend_array[i])
        output += cumulative_spend_factor * integrate.quad(lambda x: time_function(time_function_pars,x),
                                                           number_of_days-i-time_window, number_of_days-i)
    return output * time_spend_function_pars[5]
