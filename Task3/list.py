#!/usr/bin/env python
# coding: utf-8

# In[10]:


# 3.1
masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

# Filters out masses less than the moon
updated_masses = []
for mass in masses:
    if mass > masses[9]:
        updated_masses.append(mass)
print(f"New masses list: {updated_masses}")    

# new list with last 5 masses and calculating average
five_masses = masses[-5:]        
mass_avg = sum(five_masses) / len(five_masses)
print(f"Average mass from original list of last five items: {mass_avg}")

