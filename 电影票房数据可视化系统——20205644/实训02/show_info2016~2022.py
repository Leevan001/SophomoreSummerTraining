# -*- coding = utf-8 -*-
# @Time : 2022/6/25 16:50
# @Author : CQU20205644
# @File : show_info2016~2022.py
# @Software : PyCharm
import sqlite3
from time import sleep

import numpy as np
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
import os
from pyecharts.commons.utils import JsCode

conn = sqlite3.connect("movieTop2016_2022.db")
color_function = """
        function (params) {
            if (params.value > 100000 ) {
                return 'red';
            } else if (params.value > 70000 ) {
                return 'pink';
            }
            return 'blue';
        }
        """

for i in range(2016,2023):
    sql = 'select * from movieTop200 where year='+str(i)
    print(sql)
    title=str(i)+"年电影票房收入TOP15(单位:万美元)"
    html_Name=str(i)+'年电影TOP15柱状图.html'
    sql_data = pd.read_sql(sql, con=conn)
    df1 = np.array(sql_data[0:15])  # 先使用array()将DataFrame转换一下
    df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
    name = []
    gain = []
    for i in range(len(df2)):
        name.append(df2[i][1])
        gain.append(int(df2[i][2] / 10000))
    print(name)
    print(gain)
    print('-----')
    bar = Bar()
    bar.add_xaxis(name)
    bar.add_yaxis("电影票房：", gain, itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))
    bar.set_global_opts(title_opts=opts.TitleOpts(title=title))
    bar.render(html_Name)
    os.system(html_Name)
    sleep(1)
conn.close()
