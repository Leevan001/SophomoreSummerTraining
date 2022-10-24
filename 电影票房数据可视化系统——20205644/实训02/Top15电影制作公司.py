# -*- coding = utf-8 -*-
# @Time : 2022/6/25 19:55
# @Author : CQU20205644
# @File : Top15电影制作公司.py
# @Software : PyCharm
import sqlite3

import numpy as np
import pandas as pd
from pyecharts.charts import Bar
#导入设置系列配置和全局配置
from pyecharts import options as opts
import os
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

conn = sqlite3.connect("F:\电影票房数据可视化系统——20205644\实训01\movieCompany.db")
sql_data = pd.read_sql("select * from movieCompanyTop45", con=conn)
#print(sql_data)
df1 = np.array(sql_data[0:15])  # 先使用array()将DataFrame转换一下
df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
Company_name = []
Company_gain = []
for i in range(len(df2)):
    Company_name.append(df2[i][1])
    Company_gain.append(int(df2[i][2] / 10000))
# print(Company_name)
# print(Company_gain)
inner_x_data = Company_name
inner_y_data = Company_gain
inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]
print(inner_data_pair)
print(type(inner_data_pair))
c = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add(
        "电影制作公司：",
        #[list(z) for z in zip(Faker.choose(), Faker.values())],
        data_pair=inner_data_pair,
        center=(600,280),
        # 饼图的半径，数组的第一项是内半径，第二项是外半径
        # 默认设置成百分比，相对于容器高宽中较小的一项的一半
        radius=["30%", "60%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Top15电影制作公司（Brands）：",subtitle='单位：万$'),
        legend_opts=opts.LegendOpts(
            orient="vertical", #图例垂直放置
            pos_top="15%",# 图例位置调整
            pos_left="1%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("Top15Company.html")
)
os.system("Top15Company.html")
conn.close()
