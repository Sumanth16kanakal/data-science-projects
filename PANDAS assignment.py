#!/usr/bin/env python
# coding: utf-8

# In[2]:



import pandas as pd
df =pd.read_csv("customer_churn-4-1.csv")


# In[3]:


df


# In[4]:


#Now select the rows from 20th index till 200th index (exclusive), and columns from 2nd index till 15th index value


# In[5]:


df.head()


# In[9]:


df.iloc[20:201,2:16]


# 1. Display the top 100 records from the original data frame.

# In[10]:


df.head(100)


# 2. Display the last 10 records from the data frame.

# In[12]:


df.tail(10)


# 3. Display the last record from the data frame.

# In[14]:


df.tail(1)


# 1. Now from the churn data frame, try to sort the data by the tenure column according to the
# descending order.

# In[15]:


df.columns


# In[21]:


df.sort_values(by='tenure',ascending=False)


# # 2. Fetch all the records that are satisfying the following condition:
# a. Tenure>50 and the gender as ‘Female’.
# b. Gender as ‘Male’ and SeniorCitizen as 0.
# c. TechSupport as ‘Yes’ and Churn as ‘No’.
# d. Contract type as ‘Month-to-month’ and Churn as‘Yes’.

# In[26]:


x=df['tenure'].sort_values(ascending=False)


# In[29]:


pd.DataFrame(x)


# In[30]:


pd.Series(x)


# In[42]:


filtering = df['tenure']>50


# In[43]:


datanew=df[filtering]


# In[44]:


datanew


# In[47]:


df.head(1)


# In[59]:


x = df['tenure']>50
x


# In[60]:


newdata= df[x]


# In[61]:


newdata


# In[63]:


y = df['gender'] == 'female'
y


# In[66]:


newdata = df[y]
newdata


# In[67]:


newdata


# In[68]:


df.head()


# In[71]:


#a. Tenure>50 and the gender as ‘Female’


# In[76]:


df.columns


# In[89]:


newdata=df[df['tenure']>50]
newdata


# In[91]:


newdata[newdata['gender']=='female']


# In[92]:


#b. Gender as ‘Male’ and SeniorCitizen as 0.


# In[100]:


df.head(1)


# In[103]:


male=df[df['gender']== 'Male']


# In[106]:


male[male['SeniorCitizen']==0]


# # c. TechSupport as ‘Yes’ and Churn as ‘No’.

# In[108]:


df.head(1)


# In[111]:


techsupport=df[df['TechSupport'] == 'Yes' ]


# In[114]:


ANSC=techsupport[techsupport['Churn']== 'No']


# In[115]:


ANSC


# # d. Contract type as ‘Month-to-month’ and Churn as‘Yes’.

# In[120]:


ANSC.head(10)


# In[119]:


df.columns


# In[125]:


mto=df[df['Contract']=='Month-to-month']


# In[127]:


ANSD=mto[mto['Churn']=='Yes']


# In[128]:


ANSD


# # 1. Use a for loop to calculate the number of customers that are getting the tech support and are male senior citizen.

# In[133]:


ts=df["TechSupport"].value_counts()


# In[139]:


ts


# In[147]:


ts=df[df['TechSupport']=='Yes']


# In[149]:


sencit=ts[ts['SeniorCitizen'] == 1]


# In[151]:


ANS=sencit[sencit['gender']=='Male']


# In[152]:


ANS


# In[154]:


df['TechSupport']='Yes':
    while(df['gender']='Male',
         df['SeniorCitizen'])
    print('d')


# In[156]:


ANS.info()


# In[ ]:




