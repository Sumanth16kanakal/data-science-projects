#!/usr/bin/env python
# coding: utf-8

# # - Load iris data from load_iris function from sklearn.datasets package.
# - From the dataset extract the data property.
# - Train an AgglomerativeClustring model based on the data.
# - Plot dendrogram to visualize the clustering linkage

# In[5]:


import pandas as pd
import numpy  as np 
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[10]:


iris = pd.read_csv("Iris dataset project.csv")
iris.head(10)
iris.describe
iris.info()


# In[11]:


iris.describe


# In[12]:


iris.head()
iris.drop('Id',axis=1,inplace=True)
fig = iris[iris.Species == 'Iris-setosa'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='orange', label='Setosa')
iris[iris.Species == 'Iris-versicolor'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='blue', label='Versicolor', ax=fig)
iris[iris.Species == 'Iris-virginica'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='green', label='Virginica', ax=fig)
fig.set_xlabel('Sepal Length')
fig.set_ylabel('Sepal Width')
fig.set_title('Sepal Length Vs Width')

fig=plt.gcf()
fig.set_size_inches(10, 7)
plt.show()


# In[ ]:




