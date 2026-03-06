#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code for gaussarea.py
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.constants import pi

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

x = np.linspace(-10, 10, 200)
A = float(input('A: '))
x0 = float(input('x0: '))
sig = float(input('sigma: '))
z0 = float(input('z0: '))
a = float(input('Lower integration limit: '))
b = float(input('Upper integration limit: '))

area = quad(gauss, a, b, args=(A, x0, sig, z0))

height = gauss(x, A, x0, sig, z0)
plt.plot(x, height)
plt.fill_between(x, height, where=(x >= a) & (x <= b), color='green', alpha=0.5, label=f'Area: {area[0]:.3f}')
plt.legend(loc='upper right')
plt.show()

