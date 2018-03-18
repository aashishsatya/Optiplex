# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 19:48:53 2018

@author: aashishsatya
"""

def preprocess(c, A, b):
    
    """
    Makes a tableau from the given values of c, A and b
    
    Input:
    c, b are vectors (implemented as a list)
    A is a matrix, implemented as a list of lists (list of row entries)
    
    Output:
    A list which gives the initial values for every variable in the linear program
    """    
     
    
    m = len(A)  # no of rows (constraints)
    n = len(A[0])   # no of columns (variables)
    
    # we need to come up with an initial feasible solution
    # so solve a different LP as discussed in the text
        
    # add auxiliary variables to each constraint; the number of variables added is m
    
    aux_vbl_coeffs = [0] * m
    
    for i in range(m):
        A[i] = A[i] + aux_vbl_coeffs
        A[i][n + i] = 1
    
    c = c + aux_vbl_coeffs
    
    x_n = list(range(0, n))
    x_b = list(range(n, m + n)) # notice that x_b, x_n are already sorted
    
    # in this case, basic variables are all m + 1
    
    return (x_b, x_n, c, A, b)