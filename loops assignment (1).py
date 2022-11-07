#!/usr/bin/env python
# coding: utf-8

# #  Printe the number from 1 to 10 using while loop 
# 

# In[3]:


a = 1 
while (a<=10):
    print(a )
    a+=1


# # Create a list that is having 10,23,4,26,4,75,24,54 values and with the help of while loop, fetch# the even numbers and print the numbers.

# In[8]:


list1 =[10,23,4,26,4,75,24,54]
num = 0 
while(num<len(list1)):
    if list1[num]%2==0:
        print(list1[num], end =' ')
    num+=1


# # # Create an array that is having user defined inputs and with the help of for loop, fetch all the prime numbers and print the number 
# 

# In[43]:


# Python program to display all the prime numbers within an interval

lower = 1
upper = 40

print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end=',')


# In[41]:





# In[ ]:




