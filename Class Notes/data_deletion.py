#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
corpus = pd.read_csv('D:/data/dataset.csv')


# In[3]:


corpus


# In[4]:


comp_data = []
symbols = ['Nan' ,'?','&']
for row in corpus:
    if set(row) & set(symbols):
        print(row) 
    else: 
        comp_data.append(row)


# In[5]:


comp_data


# In[6]:


items = corpus.iloc[:,2].values


# In[7]:


items


# In[8]:


import numpy as np
median = np.median(items)


# In[10]:


median


# In[11]:


cutoff = median * 3 # k can be from (1-4)
lower= median - cutoff
upper = median + cutoff


# In[12]:


cutoff


# In[13]:


lower


# In[14]:


upper


# In[16]:


for i in items:
 if  i>upper:
        print(i)


# In[ ]:





# In[ ]:





# In[ ]:




