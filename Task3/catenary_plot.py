#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#3.22
from math import cosh
import numpy as np
import matplotlib.pyplot as plt
y_values = []
x_values = []
for x in range(-5, 6):
    x_values.append(x)
    y_values.append(cosh(x))
plt.plot(x_values, y_values, marker='o', markersize=5, label='cosh(x)')
plt.title('Catenary plot')
plt.grid()
plt.xlabel('x values', fontsize=12)
plt.ylabel('cosh(x)', fontsize=12)
plt.legend()
plt.show()

x = np.arange(-5, 6)
y_values2 = np.cosh(x)
plt.plot(x, y_values2, marker='o', markersize=5, label='cosh(x)')
plt.title('Catenary plot using numpy')
plt.grid()
plt.xlabel('x values', fontsize=12)
plt.ylabel('cosh(x)', fontsize=12)
plt.legend()
plt.show()

