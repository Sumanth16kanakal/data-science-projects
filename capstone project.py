#!/usr/bin/env python
# coding: utf-8

# Problem Statement:
# You are the Data Scientist at a telecom company “Neo” whose customers are churning out to
# its competitors. You have to analyse the data of your co
# mpany and find insights and stop your
# customers from churning out to other telecom companies. 

# In[1]:


import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt


# In[3]:


customer_churn= pd.read_csv('customer_churn-4-1.csv')


# In[5]:


customer_churn.head()


# In[6]:


customer_churn.columns


# # A) Data Manipulation:
# a. Extract the 5th column & store it in ‘customer_5’
# b. Extract the 15th column & store it in ‘customer_15’
# c. Extract all the male senior citizens whose Payment Method is Electronic check &
# store the result in ‘senior_male_electronic’
# d. Extract all those customers whose tenure is greater than 70 months or their
# Monthly charges is more than 100$ & store the result in ‘customer_total_tenure’
# e. Extract all the customers whose Contract is of two years, payment method is Mailed
# check & the value of Churn is ‘Yes’ & store the result in ‘two_mail_yes’
# f. Extract 333 random records from the customer_churndataframe& store the result in
# ‘customer_333’
# g. Get the count of different levels from the ‘Churn’ column

# In[8]:


#a. Extract the 5th column & store it in ‘customer_5’
c_5=customer_churn.iloc[:,4]
c_5.head()


# In[10]:


#b. Extract the 15th column & store it in ‘customer_15’

c_15 = customer_churn.iloc[:,14]
c_15.head()


# In[15]:


#c. Extract all the male senior citizens whose Payment Method is Electronic check &
#store the result in ‘senior_male_electronic’
(customer_churn['gender']=='Male')&(customer_churn['SeniorCitizen']==1)&(customer_churn['PaymentMethod']=='Electronic check')


# In[16]:


###d. Extract all those customers whose tenure is greater than 70 months or their
###Monthly charges is more than 100$ & store the result in ‘customer_total_tenure
senior_male_electronic=customer_churn[(customer_churn['gender']=='Male')&(customer_churn['SeniorCitizen']==1)&(customer_churn['PaymentMethod']=='Electronic check')
]
senior_male_electronic.head()


# In[30]:


##e. Extract all the customers whose Contract is of two years, payment method is Mailed
##check & the value of Churn is ‘Yes’ & store the result in ‘two_mail_yes’
c_t_t=customer_churn[(customer_churn['tenure']>70)|(customer_churn['MonthlyCharges']>100)]


# In[31]:


c_t_t.head()


# In[32]:


##e. Extract all the customers whose Contract is of two years, payment method is Mailed check & 
##the value of Churn is ‘Yes’ & store the result in ‘two_mail_yes’
t_m_y=customer_churn[customer_churn[(customer_churn['Contract']=='Two year') &(customer_churn['PaymentMethod']=='Mailed check')&(customer_churn['Churn']=='Yes')]


# In[33]:


t_m_y


# In[34]:


##f. Extract 333 random records from the customer_churn dataframe& store the result in ‘customer_333’
c_333=customer_churn.sample(n=333)
c_333


# In[35]:


##g. Get the count of different levels from the ‘Churn’ column
customer_churn['Churn'].value_counts()


# # B) Data Visualization:
# a. Build a bar-plot for the ’InternetService’ column:
# i. Set x-axis label to ‘Categories of Internet Service’
# ii. Set y-axis label to ‘Count of Categories’
# iii. Set the title of plot to be ‘Distribution of Internet Service’
# iv. Set the color of the bars to be ‘orange’
# b. Build a histogram for the ‘tenure’ column:
# i. Set the number of bins to be 30
# ii. Set the color of the bins to be ‘green’
# iii. Assign the title ‘Distribution of tenure’
# c. Build a scatter-plot between ‘MonthlyCharges’ & ‘tenure’. Map ‘MonthlyCharges’ to
# the y-axis & ‘tenure’ to the ‘x-axis’:
# i. Assign the points a color of ‘brown’
# ii. Set the x-axis label to ‘Tenure of customer’
# iii. Set the y-axis label to ‘Monthly Charges of customer’
# iv. Set the title to ‘Tenure vs Monthly Charges’
# d. Build a box-plot between ‘tenure’ & ‘Contract’. Map ‘tenure’ on the y-axis &
# ‘Contract’ on the x-axis. 

# a. Build a bar-plot for the ’InternetService’ column:
# i. Set x-axis label to ‘Categories of Internet Service’
# ii. Set y-axis label to ‘Count of Categories’
# iii. Set the title of plot to be ‘Distribution of Internet Service’
# iv. Set the color of the bars to be ‘orange’

# In[45]:


plt.bar(customer_churn['InternetService'].value_counts().keys().tolist(),customer_churn['InternetService'].value_counts().tolist(),
       color='orange')
plt.xlabel('Categories of Internet Service')
plt.ylabel('ount of Categories')
plt.title('Distribution of Internet Service')


# b. Build a histogram for the ‘tenure’ column:
# i. Set the number of bins to be 30
# ii. Set the color of the bins to be ‘green’
# iii. Assign the title ‘Distribution of tenure’

# In[48]:


plt.hist(customer_churn['tenure'],color='green',bins=30)
plt.title('Distribution of tenure')


# # c. Build a scatter-plot between ‘MonthlyCharges’ & ‘tenure’. 
# Map ‘MonthlyCharges’ to the y-axis & ‘tenure’ to the ‘x-axis’:
# i. Assign the points a color of ‘brown’
# ii. Set the x-axis label to ‘Tenure of customer’
# iii. Set the y-axis label to ‘Monthly Charges of customer’
# iv. Set the title to ‘Tenure vs Monthly Charges’

# In[52]:


y = customer_churn['MonthlyCharges']
x= customer_churn['tenure']
plt.scatter(x,y,color='pink')
plt.xlabel('Tenure of customer')
plt.ylabel('Monthly Charges of customer')
plt.title('Tenure vs Monthly Charges')


# d. Build a box-plot between ‘tenure’ & ‘Contract’. Map ‘tenure’ on the y-axis &
# ‘Contract’ on the x-axis

# In[58]:


customer_churn.boxplot(column=['tenure'],by=['Contract'])


# ) Linear Regression:
# a. Build a simple linear model where dependent variable is ‘MonthlyCharges’ and
# independent variable is ‘tenure’
# i. Divide the dataset into train and test sets in 70:30 ratio.
# ii. Build the model on train set and predict the values on test set
# iii. After predicting the values, find the root mean square error
# iv. Find out the error in prediction & store the result in ‘error’
# v. Find the root mean square error

# In[59]:


from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

y =customer_churn[['MonthlyCharges']]
x= customer_churn[['tenure']]


# In[60]:


y.head(),x.head()


# In[64]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)


# In[66]:


x_train.shape,x_test.shape,y_train.shape,y_test.shape


# In[67]:


regressor =LinearRegression()

regressor.fit(x_train,y_train)


# In[73]:


y_pred=regressor.predict(x_test)
y_pred[:5],y_test[:5]


# In[74]:


from sklearn.metrics import mean_squared_error

np.sqrt(mean_squared_error(y_test,y_pred))


# In[75]:


x=customer_churn[['MonthlyCharges','tenure']]
y=customer_churn[['Churn']] 


# In[84]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=0)


# In[90]:


from sklearn.linear_model import LogisticRegression

log_model = LogisticRegression()

log_model.fit(x_train,y_train)


# In[91]:


y_pred=log_model.predict(x_test)


# In[92]:


from sklearn.metrics import confusion_matrix , accuracy_score


# In[93]:


confusion_matrix(y_test,y_pred),accuracy_score(y_test,y_pred)


# In[95]:


(1041)/(1041+368)


# E) Decision Tree:
# a. Build a decision tree model where dependent variable is ‘Churn’ & independent
# variable is ‘tenure’
# i. Divide the dataset in 80:20 ratio
# ii. Build the model on train set and predict the values on test set
# iii. Build the confusion matrix and calculate the accuracy 

# In[97]:


x= customer_churn[['tenure']]
y = customer_churn[['Churn']]

from sklearn.tree import DecisionTreeClassifier

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=0)


# In[98]:


my_tree = DecisionTreeClassifier()

my_tree.fit(x_train,y_train)


# In[101]:


y_pred=my_tree.predict(x_test)


# In[102]:


from sklearn.metrics import confusion_matrix,accuracy_score


# In[104]:


confusion_matrix(y_test,y_pred)


# In[105]:


(965+87)/(965+87+281+76)


# F) Random Forest:
# a. Build a Random Forest model where dependent variable is ‘Churn’ & independent
# variables are ‘tenure’ and ‘MonthlyCharges’
# i. Divide the dataset in 70:30 ratio
# ii. Build the model on train set and predict the values on test set
# iii. Build the confusion matrix and calculate the accuracy

# In[106]:


from sklearn.ensemble import RandomForestClassifier 

rf = RandomForestClassifier()
rf.fit(x_train,y_train)


# In[107]:


rf.predict(x_test)


# In[108]:


confusion_matrix(y_test,y_pred)


# In[109]:


accuracy_score(y_test,y_pred)


# In[ ]:




