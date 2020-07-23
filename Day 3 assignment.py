#!/usr/bin/env python
# coding: utf-8

# In[2]:


sum = 0
a = int(input("enter a "))
while(a>0):
    sum = sum + a
    a = a - 1
print("The sum is",sum)


# In[16]:


n = int(input("Enter n"))
if n>1:
    for i in range(2,n):
        if (n%i == 0):
            print(n,"is not a prime number")
            break
            
    else:
        print(n,"is prime number")
else:
    print(n,"is not a prime number")


# In[ ]:





# In[ ]:




