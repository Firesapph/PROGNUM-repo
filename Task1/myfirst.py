#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
print(sys.version)


# ![fish.jpg](attachment:fish.jpg)

# In[1]:


from scipy.constants import h,c


# In[2]:


print(h, c)


# In[3]:


f = 2.42e28
wavelength = c/f


# In[4]:


energy = h * c / wavelength
print(energy)


# In[5]:


from scipy.constants import G
mass_moon = 7.342e22
mass_earth = 5.9722e24


# In[8]:


r = 385000.6*1000
F = G*mass_moon*mass_earth/r**2
print(F)


# In[ ]:




