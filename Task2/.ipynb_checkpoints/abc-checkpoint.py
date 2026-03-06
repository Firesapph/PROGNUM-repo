#!/usr/bin/env python
# coding: utf-8

# In[4]:


print('Enter the values of a, b and c for the function: f(x)=ax^2+bx+c')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
D = b**2 -4*a*c
if D<0:
    print('No solutions could be found')
elif D==0:
    print(f'1 solution was found: x={-b/(2*a)}')
else:
    print(f'2 solutions were found: x1={(-b+D**0.5)/(2*a)} and x2={(-b-D**0.5)/(2*a)}')


# In[ ]:




