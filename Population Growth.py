#!/usr/bin/env python
# coding: utf-8

# In[72]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
countries=pd.read_csv('population.csv')
china=countries[countries.country=='China']
india=countries[countries.country=='India']
usa=countries[countries.country=='United States']
usa_population_growth=usa.population / usa.population.iloc[0]
china_population_growth=china.population / china.population.iloc[0]
india_population_growth=india.population / india.population.iloc[0]


# In[73]:


india_population_growth


# In[51]:


usa_population_growth


# In[52]:


china_population_growth


# In[53]:


plt.plot(india.year, india.population, label='India')
plt.plot(usa.year, usa.population, label='Usa')
plt.plot(china.year, china.population, label='China')
plt.xlabel('Year', color='blue')
plt.ylabel('Population', color='blue')
plt.title('Population Comparision of India, China and Usa')
plt.legend()
plt.show()


# In[54]:


plt.plot(india.year, india_population_growth, label='India')
plt.plot(usa.year, usa_population_growth, label='Usa')
plt.plot(china.year, china_population_growth, label='China')
plt.title('Comparision of Population Growth of India, Usa and China')
plt.xlabel('Year', color='red')
plt.ylabel('Population Growth', color='red')
plt.legend()
plt.show()

