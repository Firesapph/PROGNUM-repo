# code for interate_user_function.py
import numpy as np
from numpy import sin, cos, exp, pi
from scipy.integrate import quad
f = input('Function you want to integrate: ')
try:
    a = eval(input('Lower limit: '))
    b = eval(input('Upper limit: '))
except (ValueError, NameError, TypeError):
    print('Please input a number, sin(), cos(), exp() or pi')

# Monte Carlo
def calc_integral(f, a, b, N=100000):
    '''Calculates monte carlo integral and quad integral from input function and input boundaries a and b'''
    try: 
        # Quad integral
        def func(x):
            return eval(f)
        quad_integral = quad(func, a, b)[0]

        # Monte Carlo integral
        x = np.random.uniform(a,b, N)
        monte_integral = (b-a) * np.mean(func(x))
        return monte_integral, quad_integral
    except (ValueError, TypeError): 
        print('Please type numbers or use x, sin(), cos(), exp() or pi')
        return (None, None)
    except SyntaxError:
        print('Please use correct syntax)')
        return (None, None)
    except OverflowError:
        print('The calculation was too large, the integral might be divergent or slowly convergent')
        return (None, None)

monte, quad = calc_integral(f, a, b)
print(f'Monte Carlo integral: {monte}')
print(f'quad integral: {quad}')