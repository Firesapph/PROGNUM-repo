#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    def __init__(self):
        self.fibo = [0, 1]
	
    def nterm(self, N):
        '''Calculates N-th term in the Fibonacci sequence'''
        self.fibo = [0, 1]
        for i in range(N):
            self.fibo.append(self.fibo[i]+self.fibo[i+1])
        return self.fibo[N-1]
    
    def dividable(self, N, M):
        '''Calculates fibo sequence less than the N-th term and dividable by M'''
        nth_term = self.nterm(N)
        new_fibo = [x for x in self.fibo if x%M==0 and x<nth_term]
        return new_fibo
    
fibo1 = Fibonacci()
example = fibo1.dividable(100, 7)
print(example)
print(fibo1.nterm(2))

