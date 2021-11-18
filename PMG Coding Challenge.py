#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import glob, os


files = glob.glob('/Users/mo/Downloads/csv-combiner/fixtures/*.csv')
print (files)

df = pd.concat([pd.read_csv(fp).assign(filename=os.path.basename(fp)) for fp in files])
print (df)


# In[ ]:





# In[ ]:




