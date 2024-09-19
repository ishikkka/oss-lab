#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


cities = np.array(['City X','City Y', 'City Z'])


# In[3]:


cities


# In[4]:


x = np.array([100,120,85,90,110,95])
y = np.array([80,75,60,95,85,90])
z = np.array([150,140,135,160,155,170])


# In[5]:


x,y,z


# In[64]:


xyz = np.array((x,y,z))


# In[65]:


xyz


# In[15]:


print("Total rainfall for city x :", np.sum(x))
print("Total rainfall for city y :", np.sum(y))
print("Total rainfall for city z :", np.sum(z))


# In[16]:


print("Average monthly rainfall for city x :", np.average(x))
print("Average monthly rainfall for city y :", np.average(y))
print("Average monthly rainfall for city z :", np.average(z))


# In[72]:


def calculateAvg(arr):
    total = 0
    for i in arr :
        total += i
    print("Monthly Average Rainfall for 6 months :", total/len(arr))


# In[73]:


calculateAvg(x)


# In[23]:


calculateAvg(y)


# In[24]:


calculateAvg(z)


# In[85]:


num = np.array([1,2,3,4,5,6])
plt.plot(num, x, label="city x", color='r', linewidth=3)
plt.plot(num, y, label="city y", color='b', linewidth=3)
plt.plot(num, z, label="city z", color='m', linewidth=3)
plt.legend(loc='best')
plt.xlabel('Months')
plt.ylabel('Rainfall (in mm)')
plt.title('Rainfall Trend for 6 Months')


# In[89]:


def calculateRange(arr) :
    rng = np.max(arr) - np.min(arr)
    print('Range :', rng)
    return rng


# In[90]:


calculateRange(x)


# In[91]:


calculateRange(y)


# In[92]:


calculateRange(z)


# In[88]:


plt.bar(num, x, label='City x', color='b')
plt.bar(x, y, label='City y', color='r')
plt.bar(y, z, label='City z', color='m')
plt.legend()
plt.xlabel('Months')
plt.ylabel('Rainfall (in mm)')
plt.title('Rainfall Distribution Comparison')


# In[98]:


plt.bar([1], calculateRange(x), label='City x', color='b', linewidth=0.5)
plt.bar([2], calculateRange(y), label='City y', color='r',linewidth=0.5)
plt.bar([3], calculateRange(z), label='City z', color='m',linewidth=0.5)
plt.legend()
plt.xlabel('Number')
plt.ylabel('Range of Rainfall (in mm)')
plt.title('Range of Rainfall for each city')


# In[63]:


plt.bar(num, x, label='City x', color='b', linewidth=0.8)
plt.legend(loc='upper right')
plt.xlabel('Months')
plt.ylabel('Rainfall (in mm)')
plt.title('Rainfall Distribution Graph for City X')


# In[61]:


plt.bar(num, y, label='City y', color='r', linewidth=0.8)
plt.legend()
plt.xlabel('Months')
plt.ylabel('Rainfall (in mm)')
plt.title('Rainfall Distribution Graph for City Y')


# In[60]:


plt.bar(num, z, label='City z', color='m', linewidth=0.8)
plt.legend()
plt.xlabel('Months')
plt.ylabel('Rainfall (in mm)')
plt.title('Rainfall Distribution Graph for City Z')


# In[ ]:




