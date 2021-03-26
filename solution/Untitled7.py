#!/usr/bin/env python
# coding: utf-8

# In[1]:


def gensquares(N):
    for i in range(N):
        yield i**2


# In[2]:


for x in gensquares(10):
    print(x)


# In[6]:


import random

random.randint(1,10)


# In[7]:


def rand_num(low,high,n):
    
    for i in range(n):
        yield random.randint(low, high)


# In[8]:


for num in rand_num(1,10,12):
    print(num)


# In[ ]:




