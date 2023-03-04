#!/usr/bin/env python
# coding: utf-8

# # Sample Jupyter Notebook

# Demo of executability below.
# Loading and plotting sample data from plotly express.

# In[6]:


import pandas
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
fig.show()


# In[1]:


import util

x = 10
y = 20
print(util.dummy_method(x, y))

