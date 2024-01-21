#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
heights = np.array([160, 155, 172, 165, 180, 158, 175, 163, 171, 168])


# In[74]:


#Calculate mean, median and standard deviation of the students heights
mean =np.mean(heights)
median = np.median(heights)
std = np.std(heights)

print("Mean =" ,mean,"cm ,Median =" ,median,"cm and Standard-deviation =", std,".")


# In[55]:


#New array with a normalized height
new = np.random.normal(167,8,size = 10)
new


# In[77]:


#Talest and shortest student in class
talest = np.argmax(heights)
print(talest)
shortest = np.argmin(heights)
print(shortest)
print("The tallest student is ", heights[4],"cm while the shortest is" ,heights[1],"cm.") 


# In[81]:


#Difference between the the tallest and shortest student
print("The difference between the tallest and shortest student is", heights[4]-heights[1],"cm.")


# In[87]:


#Randomly select five heights form the dataset without replacement
random =  np.random.choice(heights, 5, replace=False)
print(random)

