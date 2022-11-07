#!/usr/bin/env python
# coding: utf-8

# # 1. Start off by importing the cars.csv file in the jupyter notebook.

# In[51]:


import pandas as pd


# In[52]:


data = pd.read_csv('cars-1.csv')


# In[53]:


data


# # 2. Generate a line plot graph for the column ‘model’ and ‘hp’.
# a. Map the ‘model’ column on the x-axis.
# b. Map the ‘hp’ column on the y-axis.
# c. Provide the x-axis label as Models of the cars.
# d. Provide the y-axis label as Horse-Power of Cars.
# e. Set the title as Model Names vs HorsePower.

# In[67]:


data.columns


# In[73]:


import numpy as np 

import matplotlib.pyplot as plt


# In[74]:


data.head(1)


# In[75]:


data.columns


# In[76]:


x = data['model']
y = data['hp']


# In[153]:


plt.plot(y,x)
plt.xticks(rotation=90)
plt.title('Model Names vs Horsepower')
plt.xlabel('Models of the cars')
plt.ylabel('Horse-power of cars')
plt.show()


# 1. Generate a bar plot graph for the columns ‘carbs’ and ‘gear’.
# a. Map the ‘carbs’ onto the x-axis.
# b. Map the ‘gear’ onto the y-axis.
# c. Provide the x-axis label as Number of carburetors.
# d. Provide the y-axis label as Number of forward gears.
# e. Set the title as carbs vs gear. 

# In[80]:


data.columns


# In[83]:


x =data['carb']
y =data['gear']


# In[90]:


plt.bar(x,y)

plt.xlabel('Number of carburetors')
plt.ylabel('Number of forward gear')
plt.title('carbs vs gears')
plt.show()


# # 1. Plot a histogram for the column ‘wt’.
# a. Map the ‘wt’ onto the x-axis.
# b. Provide the x-axis label as ‘weight of the cars’.
# c. Provide the y-axis label as ‘Count’
# d. Set the number of bins as 30.
# e. Set the title as ‘Histogram for the weight values
# 

# In[91]:


data.columns


# In[103]:


his=data['wt']


# In[110]:


plt.plot(his)


# In[120]:


plt.hist(his,bins=30)
plt.title('Histogram for the weight values')
plt.xlabel("weight of the cars")
plt.ylabel('count')
plt.show()


# # 1. Plot a pie chart for columns: ‘cyl’ and ‘model’ form the mtcars.csv data frame.

# In[155]:


data.head(10)


# In[157]:


x=data['cyl']
y = data['model']

fig= plt.figure(figsize=(25,20))
plt.pie(x,labels=y)

plt.show()


# # 1. Plot the area chart for the colmns: ‘am’ and ‘carb’.
# a. Set the ‘am’ on the x-axis.
# b. Set the ‘carb’ on the y-axis.
# c. Provide the x-axis label as Transmission.
# d. Provide the y-axis labe as Number of carburetors.
# e. Provide the title as Transmission vs Number of carburetors. 

# In[158]:


plt.plot(data['am'], data['carb'])
plt.title('Transmission vs Number of carburetors')
plt.xlabel('Transmission')
plt.ylabel('Number of carburetors')
plt.show()


# In[161]:


x=data['am']
y = data['carb']
plt.title('Transmission vs Number of carburetors')
plt.xlabel('Transmission')
plt.ylabel('Number of carburetors')
plt.stackplot(x,y)


# In[ ]:




