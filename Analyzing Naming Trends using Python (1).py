#!/usr/bin/env python
# coding: utf-8

# Project: Analyzing the naming trends using Python
# 
# Industry: General
# Problem Statement:
# The dataset is in Zipped format, we have to extract the dataset in the program, visualize the number of
# male and female babies born in a particular year, and find out popular baby names.
# 
# Description: This project not only focusses on implementing data manipulation and data visualization
# using Pandas library, but also tests your ability to deal with real word problem statements.
# 
# Dataset: Popular baby names data provided by Social Security Administration (SSA) of United States
# How to download the dataset:
#  Go to https://www.ssa.gov/oact/babynames/limits.html
#  Click on ‘National data’
#  Get the zipped file
# 
# Here’s what the zipped folder looks like,
# 
# 
# Hints:
# 
# 
#  First, use Pandas, zipfile, and BytesIO library to extract the data. Find out a way to extract only
# files that consists useful data.
#  Hint: pd.read_csv(BytesIO(z.read(file_name)), encoding='utf-8', engine='python', header=None)
#  Then, visualize the number of male and female babies born in a particular year with the help of
# pandas.DataFrame.plot, then Analyse baby names by sorting out all birth counts.
#  Then, analyse baby names by sorting out top 100 birth counts and group them by names to find
# out popular baby names 

# In[ ]:


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




