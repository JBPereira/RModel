import scipy as sp
import numpy as np
import scipy.integrate as itg
import matplotlib.pyplot as plt

class TimeFunction():

    def __init__(self, mean, std, decay):
        self.mean = mean
        self.std = std
        self.decay = decay

    def time_function(self, time_point):

        half_inv_decay = 1.0/(2.0 * self.decay)

        exp_factor = half_inv_decay * sp.exp(half_inv_decay * (2.0 * self.mean + (self.std**2 / self.decay) - 2.0 * time_point))

        x2 = lambda x: sp.exp(-x**2)
        lower_bound = self.erfc_par(time_point)
        upper_bound = np.inf
        erfc_integral_component = itg.quad(x2, lower_bound, upper_bound)
        erfc = 2.0 / sp.sqrt(sp.pi) * erfc_integral_component[0]

        return exp_factor * erfc

    def erfc_par(self, t):
        return (self.mean + (self.std**2.0 / self.decay) - t) / (sp.sqrt(2.0) * self.std)