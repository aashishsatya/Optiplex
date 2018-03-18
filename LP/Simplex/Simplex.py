# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 04:31:48 2018

@author: aashishsatya

This file implements the simplex method used to solve linear programs (LPs).
We will follow the implementation of simplex followed in Matousek's book titled
Understanding and Using Linear Programming.

Efficiency hasn't been the key concern here (and in the book). The code was
just written as an attempt to thoroughly understand what was being done in the
book.

We're assuming that linear programs are of the form

maximize c^Tx

subject to

Ax = b (notice the equality)
x_i >= 0 for all i

(The book tells you how to clean any linear equation to be of this form)

"""

import numpy
import bisect

from Preprocess import *

def check_feasibility(x_b, x_n, c, A, b):
    
    """
    Checks if the given conditions are feasible for the LP.
    """
    
    c_dash = [0] * len(x_n) + [-1] * len(x_b)
    opt, soln = simplex(x_b, x_n, c_dash, A, b)
    
    if opt == 0 and all(soln[x_n_var] == 0 for x_n_var in x_n):
        return True
    return False

def simplex(x_b, x_n, c, A, b):
    
    """
    Input:
    x_b, list, basic feasible set
    x_n, list, non-basic feasible set
    c, b are vectors (implemented as a list)
    A is a matrix, implemented as a list of lists (list of row entries)
    """
    
    """
    The tableau is represented as
    
    x_b = p + Qx_n
    --------------
    z = z_0 + r^Tx_n
    
    x_b: initial basic feasible set (list)
    x_n: non-basic variables (list)
    
    
    """
    
    # compute Q, r, p
    
    A_tr = numpy.transpose(A) # transpose since we need the columns    
    
    A_B = numpy.transpose(A_tr[x_b]) # this kind of indexing works!
    A_N = numpy.transpose(A_tr[x_n])
    c_N = numpy.array([c[i] for i in x_n])
    c_B = numpy.array([c[i] for i in x_b])
    b = numpy.array(b)    
    
    # the above variables with some operations done on them    
    A_B_inverse = numpy.linalg.inv(A_B)
    c_B_transpose = numpy.transpose(c_B)
    
    
    Q = -1 * numpy.matmul(A_B_inverse, A_N)
    p = numpy.matmul(A_B_inverse, b)
    r = c_N - numpy.transpose(numpy.matmul(numpy.matmul(c_B_transpose, A_B_inverse), A_N))
    
    # check if coefficients in r are all negative
    
    if all(r_coeff <= 0 for r_coeff in r):
        
        # we've reached the optimum
        z_0 = numpy.matmul(numpy.matmul(c_B_transpose, A_B_inverse), b)
        
        # construct the solution
        soln = {}
        for index in range(len(x_b)):
            soln[x_b[index]] = p[index]
        for index in range(len(x_n)):
            soln[x_n[index]] = 0
            
        return (z_0, soln)
    
    # perform a pivot step
    
    # pick the entering variable
    
    entering_vbl_index = 0
    entering_vbl = 0
    
    for index in range(0, len(x_n)):
        if r[index] > 0:
            entering_vbl_index = index
            entering_vbl = x_n[index]
            break
    
    # pick leaving variable
    # not as easy: we need to ensure that the tightest constraint is not violated!
    
    min_val = float('inf')    
    
    for index in range(0, len(x_b)):
        if Q[index][entering_vbl_index] < 0:
            min_val = min(p[index] / (-1 * Q[index][entering_vbl_index]), min_val)
    
    leaving_vbl_index = -1
    leaving_vbl = 0

    for index in range(0, len(x_b)):
        if Q[index][entering_vbl_index] < 0:            
            if p[index] / (-1 * Q[index][entering_vbl_index]) == min_val:                
                leaving_vbl_index = index
                leaving_vbl = x_b[index]
                break
            
    if leaving_vbl_index == -1:
        # LP is unbounded
        print('LP is unbounded.')
        return
    
    del x_n[entering_vbl_index]
    del x_b[leaving_vbl_index]
    bisect.insort(x_n, leaving_vbl)
    bisect.insort(x_b, entering_vbl)
        
    return simplex(x_b, x_n, c, A, b)      
        
def read_input():

    """
    Reads the input from files 'cT.txt' and 'A.txt' and returns c, A, b
    - store c in cT.txt
    - store A in A.txt
    
    Output: c, A, b
    """    
    
    c = []
    A = []
    b = []
    
    # read c 
    
    with open('cT.txt', 'r') as f:
        for line in f:
            line = line[:-1]    # remove '\n'
            c = list(map(float, line.split(' ')))
            break # we need only the first line
            
    # now read A and b
            
    with open('Ab.txt', 'r') as f:
        for line in f:
            line = line[:-1]
            new_row = list(map(float, line.split(' ')))
            A = A + [new_row[:-1]]  # last entry is for b
            b = b + [new_row[-1]]       
    
    return c, A, b
            
c, A, b = read_input()
x_b, x_n, c, A, b = preprocess(c, A, b)

feasible = check_feasibility(x_b, x_n, c, A, b)
if feasible: 
    opt, soln = simplex(x_b, x_n, c, A, b)
    print('Optimum value:', opt)
    print('Solution values:')
    for var in x_b:
        print('x_' + str(var) + ': ' + str(soln[var]))
else:
    print('LP is not feasible.')