#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Import libraries
import quandl
import pandas as pd
import matplotlib.pyplot as plt
#Personal API Key
quandl.ApiConfig.api_key = "TQUQzkUTBHrerch_9RnN"


# In[10]:


#Pull data from quandl

#Short term
nru_st = quandl.get("FRED/NROUST")
#Long term
nru_lt = quandl.get("FRED/NROU")


# In[11]:


#Check the data structures
type(nru_st)
type(nru_lt)


# In[17]:


#Plot the data
plt.plot(nru_st, label='st')
plt.plot(nru_lt, label='lt')
plt.xlabel('Year',fontsize=20)
plt.ylabel('NRU',fontsize=20)
plt.title('Natural rate of unemployment over the years',fontsize=20)
plt.legend(fontsize=20)
fig = plt.gcf()
fig.set_size_inches(16, 8)
plt.show()

#Provide some summary statistics
nru.describe()[1::]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




