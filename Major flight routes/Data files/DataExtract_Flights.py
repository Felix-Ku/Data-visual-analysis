# -*- coding: utf-8 -*-
"""
@author: Ku Sze Hung, Felix (3035370363)

@Project: FINA2390 Project 5: Preliminary Data Extract
@Sub-Project: 1. Visualizing Major flight routes around the world in 2014
"""

""" Reference
Source of data: https://openflights.org/data.html
Author of data: Jani Patokallio and Contentshare
"""

import pandas as pd
import numpy as np


''' To extract the location of airports as nodes'''
# Get the data from web
df_airports=pd.read_csv("https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat",header=None)

# Select the interested columns
airports_data=[df_airports[4],df_airports[6],df_airports[7],df_airports[1]]

# Assign new headers
headers=["id","latitude","longitude","Label"]

# Create new dataframe
df1=pd.concat(airports_data, axis=1, keys=headers)

# Drop the null rows (The data originally uses "\N" to represent Null, therefore replace function is needed)
df1=df1.replace(r"\N",np.NaN).dropna()

# Make the index start from 1
df1.index += 1
 
# Output
df1.to_csv("nodes.csv",index=False)



''' To extract the routes of flights as edges (Similar process)'''
# Get the data from web
df_routes=pd.read_csv("https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat",header=None)

# Select the interested columns
routes_data=[df_routes[2],df_routes[4],df_routes[0]]

# Assign new headers
headers=["Source","Target","Airline Code"]

# Create new dataframe
df2=pd.concat(routes_data, axis=1, keys=headers)

# Drop the null rows (The data originally uses "\N" to represent Null, therefore replace function is needed)
df2=df2.replace(r"\N",np.NaN).dropna()

# Make the index start from 1
df2.index += 1 

# Output
df2.to_csv("edges.csv",index=False)