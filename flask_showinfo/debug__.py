# -*- coding = utf-8 -*-
# @Time : 2022/7/2 18:36
# @Author : CQU20205644
# @File : debug__.py
# @Software : PyCharm
import os
import sqlite3

import numpy as np
import pandas as pd
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path_douban = os.path.join(BASE_DIR, "movie.db")
db_path_boxoffice=os.path.join(BASE_DIR, "movieTop2016_2022.db")
datalist = []
conn = sqlite3.connect(db_path_douban)
cur = conn.cursor()
sql = 'select * from movie250'
data = cur.execute(sql)
for item in data:
    datalist.append(item)
conn = sqlite3.connect(db_path_boxoffice)
cur = conn.cursor()
name_total = []
gain_total = []
for i in range(2020, 2023):
    sql = 'select * from movieTop200 where year=' + str(i)
    sql_data = pd.read_sql(sql, con=conn)
    df1 = np.array(sql_data[0:10])  # 先使用array()将DataFrame转换一下
    df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
    name = []
    gain = []
    for i in range(len(df2)):
        name.append(df2[i][1])
        gain.append(int(df2[i][2] / 10000))
    name_total.append(name)
    gain_total.append(gain)
print(name_total[0])
print(gain_total[0])
