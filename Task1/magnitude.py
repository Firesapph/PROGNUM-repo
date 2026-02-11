#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Sirius data
apparentMagnitude = -1.46
absoluteMagnitude = 1.45

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164


# In[16]:


print(f'Distance for Sirius: {d} ly')


# In[19]:


# Sirius data
apparentMagnitude = -1.46
absoluteMagnitude = 1.45

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

print('Apparent magnitude: ', end="")
m = float(input())
print('Absolute magnitude: ', end="")
M = float(input())

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164


# In[20]:


print(f'Distance from input: {d} ly')


# In[ ]:




