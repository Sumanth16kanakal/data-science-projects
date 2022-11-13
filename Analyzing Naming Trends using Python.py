#!/usr/bin/env python
# coding: utf-8

# In[2]:


from io import BytesIO
from zipfile import ZipFile
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


a=ZipFile("C:\\Users\\suman\\Downloads\\names (1).zip").extractall('.')


# In[12]:


a


# In[15]:


years = []
for year in range(1880,2021):
    years.append(pd.read_csv(f'yob{year}.txt',names=['Name','Sex','Babies']))
    years[-1]['Year']=year


# In[16]:


b = pd.concat(years)
b


# In[19]:


c = pd.pivot_table(data=b,index=['Year'],columns=['Sex'],values=['Babies'],aggfunc='sum')
c


# In[20]:


plt.figure(figsize=(10,30))
c.plot(kind='barh',figsize=(18,30));
plt.show()


# In[21]:


pd.options.display.max_rows=100
sort_baby_names=b.sort_values(by='Babies',ascending = False).reset_index(drop=True)
sort_baby_names.head(100)


# In[23]:


top_100_names= sort_baby_names.head(100)
grouped_names = top_100_names[['Name','Babies']].groupby('Name').sum().sort_values(by='Babies',ascending= False)
grouped_names


# In[ ]:




