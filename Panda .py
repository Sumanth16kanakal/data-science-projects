#!/usr/bin/env python
# coding: utf-8

# # 1. Write a function that takes start and end of a range returns a Pandas series object containingnumbers within that range. 

# In[4]:


import pandas as pd 
s = pd.Series([1,10],index=['start','end'])


# In[3]:


s


# 2. Create a function that takes in two lists named keys and values as arguments.
# Keys would be strings and contain n string values.
# Values would be a list containing n lists. 

# In[51]:


def create_dataframe(keys,vlaues):
    return pd.DataFrame(vlaues, index=keys).T

df1 = create_dataframe(['name','age'],[['sumanth','pratyush','sonu'],[22,23,12]])
df1


# In[44]:


df2 = pd.DataFrame(['name','age'],[['ram','jay'],[22,21]])
df2


# 3. Create a function that concatenates two dataframes. Use previously created function to create
# two dataframes and pass them as parameters Make sure that the indexes are reset before
# returning:

# In[52]:


def con_df(df1, df2):
    df = pd.concat( axis=0, ignore_index = True)
    df


# In[53]:


df


# In[66]:


vertical_concat=pd.concat([df1,df2], axis=0)


# In[67]:


vertical_concat


# # 4. Write code to load data from cars.csv into a dataframe and print its details. Details like: 'count','mean', 'std', 'min', '25%', '50%', '75%', 'max'.

# In[70]:


data =pd.read_csv('cars-4-1.csv')


# In[71]:


data


# In[72]:


data.info()


# In[79]:


data.describe()


# 5. Write a method that will take a column name as argument and return the name of the column
# with which the
# given column has the highest correlation.
# The data to be used is the cars dataset.
# The returned value should not the column named that was passed as the parameters.
# E.G: get_max_correlated_column('mpg') -> should return 'drat' 

# In[81]:


def max_correlated_col(col, dataset):
    dic = {}
    list1 = [x for x in dataset.columns if dataset[x].dtypes == float]
    for i in list1:
        dic[i] = abs(dataset[col].corr(dataset[i]))
    return max(dic)

