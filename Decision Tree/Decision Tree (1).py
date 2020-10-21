#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("iris(1).csv")
data
data.head()
data['Species'].unique()
data


# In[6]:


data.Species.value_counts()


# In[8]:


colnames = list(data.columns)
colnames


# In[10]:


predictors = colnames[:4]
target = colnames[4]


# In[13]:


import numpy as np
from sklearn.model_selection import train_test_split
train,test = train_test_split(data,test_size = 0.2)
train
test


# In[18]:


from sklearn.tree import  DecisionTreeClassifier
help(DecisionTreeClassifier)
model = DecisionTreeClassifier(criterion = 'entropy')
model.fit(train[predictors],train[target])
sklearn.tree.plot_tree(model)


# In[15]:


preds = model.predict(test[predictors]) # predicting on test data set 
pd.Series(preds).value_counts() # getting the count of each category 


# In[16]:


pd.crosstab(test[target],preds)


# In[17]:


np.mean(preds==test.Species)

