# -*- coding = utf-8 -*-
# @Time : 2022/6/25 23:24
# @Author : CQU20205644
# @File : yearMovieCompare.py
# @Software : PyCharm
import sqlite3
import numpy as np
import pandas as pd
from pyecharts.charts import Bar
#导入设置系列配置和全局配置
from pyecharts import options as opts
from pyecharts.charts import Line
import os
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

conn = sqlite3.connect("movieTop2016_2022.db")
sql_data = pd.read_sql("select * from movieTop200", con=conn)
df=sql_data.sort_values(by=['total_gain'],ascending=False)
print(df)
df1 = np.array(df[0:100])  # 先使用array()将DataFrame转换一下
df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
print(df2)
year_count= dict.fromkeys(range(2016,2023), 0)
for i in range(len(df2)):
    year_count[df2[i][3]]+=1
#print(year_count)
x_data = list(year_count.keys())
y_data = list(year_count.values())
data_pair = [list(z) for z in zip(x_data,y_data)]
c = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add(
        "2016~2022年票房TOP100的年代分布图：",
        #[list(z) for z in zip(Faker.choose(), Faker.values())],
        data_pair=data_pair,
        center=(460,280),
        # 饼图的半径，数组的第一项是内半径，第二项是外半径
        # 默认设置成百分比，相对于容器高宽中较小的一项的一半
        radius=["0%", "80%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2016~2022年全球电影票房Top100的年代分布饼状图：",subtitle='单位：部'),
        legend_opts=opts.LegendOpts(
            orient="vertical", #图例垂直放置
            pos_top="20%",# 图例位置调整
            pos_left="5%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("2016~2022Top100电影发布年份图.html")
)
os.system("2016~2022Top100电影发布年份图.html")
