import scipy as sp
import numpy as np
import scipy.integrate as itg
import matplotlib.pyplot as plt

class TimeFunction():

    def __init__(self, mean, std, decay):
        self.mean = mean
        self.std = std
        self.decay = decay

    def time_function(self, time_array):

        half_inv_decay = 1.0/(2.0 * self.decay)

        exp_factor = half_inv_decay * sp.exp(half_inv_decay * (2.0 * self.mean + (self.std**2 / self.decay) - 2.0 * time_array))

        time_function_array = []
        x2 = lambda x: sp.exp(-x**2)
        for i in range(len(time_array)):
            lower_bound = self.erfc_par(time_array[i])
            upper_bound = np.inf
            this = itg.quad(x2, lower_bound, upper_bound)
           # print exp_factor
            erfc = 2.0 / sp.sqrt(sp.pi) * this[0]
            time_function_array.append(exp_factor[i] * erfc)
        return time_function_array

    def erfc_par(self, t):
        return (self.mean + (self.std**2.0 / self.decay) - t) / (sp.sqrt(2.0) * self.std)

if __name__ == "__main__":
    plt.close()
    plt.figure()
    time = np.arange(-5, 15, 0.01)
    for i in range(8):
        tf = TimeFunction(i, 0.5, 0.1)
        y=tf.time_function(time)
        plt.plot(time, y)
    plt.show()
