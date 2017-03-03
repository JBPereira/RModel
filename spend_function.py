import scipy.special as sp
import numpy as np
import matplotlib.pyplot as plt

class SpendFunction():

    @staticmethod
    def calculate_spend_resp(spend, spend_pars):

        '''
        :param spend: spend for that day
        :param spend_pars: spend array with parameters k (shape parameter) and teta (scale parameter)
        :return:
        '''

        return sp.gammainc(spend_pars[0], spend / spend_pars[1])

if __name__ == "__main__":

    sample_array = np.arange(0, 20, 1)
    spend_response = []
    for i in sample_array:
        spend_response.append(SpendFunction.calculate_spend_resp(i, [15, 0.6]))

    plt.figure()
    plt.plot(spend_response)
    plt.show()
