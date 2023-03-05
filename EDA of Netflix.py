#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


data = pd.read_csv('E:\\Data\\Netflix_titles\\netflix_titles.csv')


# In[8]:


data.head()


# In[10]:


data.shape


# In[11]:


data.describe()


# In[12]:


data.info()


# In[18]:


data.isna().sum() #Checking for Missing Values


# In[19]:


data.columns


# In[20]:


data.dtypes


# In[23]:


data['date_added'] = pd.to_datetime(data['date_added']) #converting the data type from object to datetime64


# In[24]:


data.dtypes


# In[25]:


data.head()


# In[26]:


# Handling Missing Values


# In[27]:


data.fillna({'rating':'unavailable','cast':'unavailable','country':'unavailable','director':'unavailable'}, inplace = True)


# In[28]:


data.isna().sum()


# In[30]:


data[data.date_added.isnull()] # for checking where is the null value


# In[31]:


most_recent_entry_date=data['date_added'].max()


# In[32]:


data.fillna({'date_added':most_recent_entry_date}, inplace = True)


# In[33]:


data.isna().sum()


# In[35]:


data[data.show_id == 's6067'] #for proof


# In[36]:


#Now for Durations


# In[37]:


data[data.duration.isnull()]


# In[39]:


data[data.director == 'Louis C.K.'].head()


# In[40]:


# overwrite and check by using loc operator


# In[41]:


data.loc[data['director'] == 'Louis C.K.','duration'] = data['rating']


# In[43]:


data[data.director == 'Louis C.K.'].head()


# In[44]:


data.loc[data['director'] == 'Louis C.K.','rating'] = 'unavailable'


# In[45]:


data[data.director == 'Louis C.K.'].head()


# In[46]:


data.isna().sum()


# In[48]:


# VISULIZATIONS


# In[50]:


data.type.value_counts() # Value counts method show us the counts of different categories in a given column


# In[54]:


sns.countplot(x = 'type',data = data)
plt.title('Count Vs Type of Shows')


# In[55]:


# Country Analysis


# In[68]:


data['country'].value_counts().head(10)


# In[73]:


plt.figure(figsize = (12,6))
sns.countplot(y = 'country',order = data['country'].value_counts().index[0:10],data = data)
plt.title('Country Wise content on Netflix')


# In[74]:


# now checking content based on country


# In[81]:


movie_countries = data[data['type'] == 'Movie']
tv_shows_countries = data[data['type'] == 'TV Show']


# In[82]:


plt.figure(figsize = (12,6))
sns.countplot(y = 'country',order = data['country'].value_counts().index[0:10],data = movie_countries)
plt.title('Top 10 Countries producing Movies in Netflix')


plt.figure(figsize = (12,6))
sns.countplot(y = 'country',order = data['country'].value_counts().index[0:10],data = tv_shows_countries)
plt.title('Top 10 Countries producing TV Shows in Netflix')


# In[83]:


# lets check what are the major ratings given on the Netflix


# In[84]:


data.rating.value_counts()


# In[91]:


plt.figure(figsize = (12,6))
sns.countplot(x = 'rating',order = data['rating'].value_counts().index[0:10], data = data )
plt.title('Rating of the Show on Netflix Vs Count')


# In[92]:


# According to Release Year


# In[96]:


data.release_year.value_counts()[0:20]


# In[97]:


plt.figure(figsize = (12,6))
sns.countplot(x = 'release_year',order = data['release_year'].value_counts().index[0:20],data=data)
plt.title('Content release in year in Netflix Vs Count')


# In[98]:


# Popular Genres Analysis


# In[100]:


plt.figure(figsize=(12,6))
sns.countplot(y = 'listed_in',order = data['listed_in'].value_counts().index[0:20],data = data)
plt.title('Top 20 Genres on Netflix')


# In[102]:


#Summary
#1- Netflix has more movies than TV Show.
#2- Most Number Movies and TV show produced by United State,followed by India.
#3- Most of the content on Netflix is for matured Audiences.
#4- 2018 is the year in which Netflix released alot more content.
#5- International movie and Dramas are the most popular genres on Netflix

