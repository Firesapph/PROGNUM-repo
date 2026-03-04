# 4.6
import numpy as np

userfunc = input('Function: ')
a = input('First boundary a: ')
b = input('Second boundary b: ')

def calc_integral(f, a, b, N=10000):
    '''Calculates integral from input function and input boundaries a and b'''
    a, b = float(a), float(b)
    
    x = np.random.uniform(a,b, N)
    integral = (b-a) * np.sum(eval(f)) / N
    
    return integral

print(f'Calculated integral: {calc_integral(userfunc, a, b)}')