#!/usr/bin/env python
# coding: utf-8

# 1. Load the dataset using pandas
# 2. Extract data fromOutcome column is a variable named Y
# 3. Extract data from every column except Outcome column in a variable named X.
# 4. Divide the dataset into two parts for training and testing in 70% and 30% proportion
# 5. Create and train Random Forest Model on training set
# 6. Make predictions based on the testing set using the trained model
# 7. Check the performance by calculating the confusion matrix and accuracy score of the model 

# In[ ]:


import pandas as pd 


# In[13]:


data = pd.read_csv('diabetes.csv')
data.columns


# In[12]:


Y = data['Outcome']


# In[14]:


X = data[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']]


# In[15]:


from sklearn.model_selection import train_test_split


# In[16]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.3)


# In[19]:


from sklearn.ensemble import RandomForestClassifier
model =RandomForestClassifier()


# In[20]:


model.fit(X_train,Y_train)


# In[21]:


y_pred = model.predict(X_test)


# In[22]:


from sklearn.metrics import accuracy_score , confusion_matrix

acc = accuracy_score(Y_test,y_pred)
cm = confusion_matrix(y_pred,Y_test)


# In[23]:


print(acc)
print(cm)


# In[ ]:




