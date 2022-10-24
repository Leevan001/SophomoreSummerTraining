# -*- coding = utf-8 -*-
# @Time : 2022/6/26 10:38
# @Author : CQU20205644
# @File : Movie_year_Compare.py
# @Software : PyCharm
# b={"value": 12, "name": "我是B.children.a"}
# print(type(b))
import os
import sqlite3

import numpy as np
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Pie, TreeMap
from pyecharts.globals import ThemeType



conn = sqlite3.connect("movieTop2016_2022.db")
sql_data = pd.read_sql("select * from movieTop200", con=conn)
df=sql_data.sort_values(by=['total_gain'],ascending=False)
df1 = np.array(df[0:100])  # 先使用array()将DataFrame转换一下
df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
#print(df2)
name_message= [[],[],[],[],[],[],[]]
gain_message= [[],[],[],[],[],[],[]]
year_totalgain=dict.fromkeys(range(2016,2023), 0)
for i in range(len(df2)):
    name_message[df2[i][3]-2016].append(df2[i][1])
    gain_message[df2[i][3]-2016].append(df2[i][2])
    year_totalgain[df2[i][3]]+=df2[i][2]

data=[]
for year in range(2016,2023):
    year_data=[]
    for i in range(len(name_message[year-2016])):
        tmp_dic = {"value": 0, "name": ""}
        tmp_dic['value']=gain_message[year-2016][i]
        tmp_dic['name']=name_message[year-2016][i]
        #print(tmp_dic)
        year_data.append(tmp_dic)
    danyuan = {
        "value": year_totalgain[year],
        "name": str(year)+'年',
        "children": [
             {
                "value": year_totalgain[year],
                "name":  str(year)+'年的电影',
                "children": year_data,
            }
        ],
    }
    data.append(danyuan)

# c = (
#     TreeMap()
#     .add("2016~2022Top电影矩形树状图", data)
#     .set_global_opts(title_opts=opts.TitleOpts(title="2016~2022Top电影矩形树状图(单位：$)"))
#     .render("2016~2022Top电影矩形树状图.html")
# )
# os.system('2016~2022Top电影矩形树状图.html')
c = (
    TreeMap()
    .add(
        series_name="2016~2022Top电影矩形树状图",
        data=data,
        levels=[
            opts.TreeMapLevelsOpts(
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color="#555", border_width=4, gap_width=4
                )
            ),
            opts.TreeMapLevelsOpts(
                color_saturation=[0.3, 0.6],
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color_saturation=0.7, gap_width=0.1, border_width=0.1
                ),
            ),
            opts.TreeMapLevelsOpts(
                color_saturation=[0.3, 0.5],
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color_saturation=0, gap_width=0
                ),
            ),
            opts.TreeMapLevelsOpts(color_saturation=[0.3, 0.5]),
        ],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="2016~2022Top电影矩形树状图(单位：$)"))
    .render("2016~2022Top电影矩形树状图.html")
)
os.system('2016~2022Top电影矩形树状图.html')
