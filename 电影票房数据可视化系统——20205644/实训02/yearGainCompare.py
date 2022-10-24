# -*- coding = utf-8 -*-
# @Time : 2022/6/25 20:51
# @Author : CQU20205644
# @File : yearGainCompare.py
# @Software : PyCharm
import sqlite3
import numpy as np
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts   #导入设置系列配置和全局配置
import os

conn = sqlite3.connect("movieTop2016_2022.db")
year_gain_list=[]
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
    print(str(year)+'年Top200的电影的总票房为：'+str(year_gain))
    year_gain_list.append(year_gain)
print(year_gain_list)
conn.close()
year_list=[]
for i in range(2016,2023):
    year_list.append(str(i)+'年')
def line_base() -> Line:
    attr = year_list
    v1 = year_gain_list
    c = (
        Line()
        .add_xaxis(attr)
        .add_yaxis("各年TOP200电影收入总票房", v1)
        .set_global_opts(title_opts=opts.TitleOpts(title="票房收入年份折线图(单位：$)"))

    )
    return c
m=line_base()
m.render('Compare2016~2022.html')
os.system('Compare2016~2022.html')










