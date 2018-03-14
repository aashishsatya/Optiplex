# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:08:35 2018

@author: aashishsatya
"""

import numpy as np

class GradientDescent:
    
    """
    The simplest of all gradient descents. It computes x_{t + 1} as x_t - eta_t . grad(f(x_t)).
    In this particular case, no assumptions have been made on the functions.
    (This class can be extended to other variants of gradient descent)
    """
    
    def __init__(self, eta_t, f, grad_f, epsilon):
        
        """
        eta_t is the learning rate at step t
        f is the function we are trying to minimize
        grad_f is the gradient function, it accepts a point (possibly in R^n)
        and returns the gradient of f at that point (as a numpy array)
        """
        
        self.eta_t = eta_t
        self.f = f
        self.grad_f = grad_f
        self.epsilon = epsilon
        
    def find_optimal():
        
        """
        Note that in NONE of this or related implementations will we be able to find the optimal value.
        We will only be able to find a value that is epsilon-close to it.
        """
        
        raise NotImplementedError
        