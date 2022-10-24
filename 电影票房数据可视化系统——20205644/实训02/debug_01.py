# -*- coding = utf-8 -*-
# @Time : 2022/6/25 19:33
# @Author : CQU20205644
# @File : debug_01.py
# @Software : PyCharm
import os
import sqlite3

import numpy as np
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Pie, TreeMap
from pyecharts.globals import ThemeType


conn = sqlite3.connect("movieTop2016_2022.db")
year_gain_list=[]
year_name_list=[]
for year in range(2016,2023):
    sql = 'select * from movieTop200 where year='+str(year)
    #print(sql)
    title=str(year)+"年电影票房收入TOP15(单位:万美元)"
    html_Name=str(year)+'年电影TOP15柱状图.html'
    sql_data = pd.read_sql(sql, con=conn)
    df1 = np.array(sql_data)  # 先使用array()将DataFrame转换一下
    df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
    year_gain=0
    for i in range(len(df2)):
        year_gain+=df2[i][2]
    year_name_list.append(str(year)+'年Top200总票房')
    year_gain_list.append(year_gain)
print(year_gain_list)
print(year_name_list)
