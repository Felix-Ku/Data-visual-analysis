# -*- coding: utf-8 -*-
"""
@author: Ku Sze Hung, Felix (3035370363)

@Project: FINA2390 Project 5: Preliminary Data Extract
@Sub-Project: 3. Visualizing Trade volume with European countries around the world
"""

""" Reference
Data source: https://data.wto.org/ (by World Trade Organization)
"""

import pandas as pd

df=pd.read_csv("WtoData_20201101142302.csv")

df1=df.pivot_table(index='Reporting Economy', columns='Partner Economy', values='Value', aggfunc='sum')

df1.to_csv("data_trade.csv")