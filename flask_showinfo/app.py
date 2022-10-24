# -*- coding = utf-8 -*-
# @Time : 2022/6/24 11:23
# @Author : CQU20205644
# @File : app.py
# @Software : PyCharm
import datetime
import os
import sqlite3
import pandas as pd
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path_douban = os.path.join(BASE_DIR, "movie.db")
db_path_boxoffice=os.path.join(BASE_DIR, "movieTop2016_2022.db")
db_path_Company=os.path.join(BASE_DIR,'movieCompany.db')
@app.route('/')
def first_page():
    datalist=[]
    conn = sqlite3.connect(db_path_douban)
    cur=conn.cursor()
    sql='select * from movie250'
    data=cur.execute(sql)
    for item in data:
        datalist.append(item)
    conn = sqlite3.connect(db_path_boxoffice)
    cur=conn.cursor()
    name_total=[]
    gain_total=[]
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

    year_gain_list = []
    year_name_list = []
    for year in range(2016, 2023):
        sql = 'select * from movieTop200 where year=' + str(year)
        # print(sql)
        title = str(year) + "年电影票房收入TOP15(单位:万美元)"
        html_Name = str(year) + '年电影TOP15柱状图.html'
        sql_data = pd.read_sql(sql, con=conn)
        df1 = np.array(sql_data)  # 先使用array()将DataFrame转换一下
        df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
        year_gain = 0
        for i in range(len(df2)):
            year_gain += df2[i][2]
        year_name_list.append(str(year) + '年Top200总票房')
        year_gain_list.append(year_gain)



    sql_data = pd.read_sql("select * from movieTop200", con=conn)
    df = sql_data.sort_values(by=['total_gain'], ascending=False)
    df1 = np.array(df[0:100])  # 先使用array()将DataFrame转换一下
    df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
    year_totalgain = dict.fromkeys(range(2016, 2023), 0)
    # print(df2)
    name_message = [[], [], [], [], [], [], []]
    gain_message = [[], [], [], [], [], [], []]
    for i in range(len(df2)):
        name_message[df2[i][3] - 2016].append(df2[i][1])
        gain_message[df2[i][3] - 2016].append(df2[i][2])
        year_totalgain[df2[i][3]] += df2[i][2]
    data_tree = []
    for year in range(2016, 2023):
        year_data = []
        for i in range(len(name_message[year - 2016])):
            tmp_dic = {"value": 0, "name": ""}
            tmp_dic['value'] = gain_message[year - 2016][i]
            tmp_dic['name'] = name_message[year - 2016][i]
            # print(tmp_dic)
            year_data.append(tmp_dic)
        danyuan = {
            "value": year_totalgain[year],
            "name": str(year) + '年',
            "children": [
                {
                    "value": year_totalgain[year],
                    "name": str(year) + '年的电影',
                    "children": year_data,
                }
            ],
        }
        data_tree.append(danyuan)
    conn = sqlite3.connect(db_path_Company)
    sql_data = pd.read_sql("select * from movieCompanyTop45", con=conn)
    # print(sql_data)
    df1 = np.array(sql_data[0:15])  # 先使用array()将DataFrame转换一下
    df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
    Company_name = []
    Company_gain = []
    for i in range(len(df2)):
        Company_name.append(df2[i][1])
        Company_gain.append(int(df2[i][2] / 10000))
    inner_x_data = Company_name
    inner_y_data = Company_gain
    inner_data_pair = []
    for i in range(len(inner_x_data)):
        b = {
            "value": inner_y_data[i],
            "name": inner_x_data[i]
        }
        inner_data_pair.append(b)
    return render_template('home_page.html',movies=datalist,name_total=name_total,gain_total=gain_total,data_tree=data_tree,inner_data_pair =inner_data_pair,year_name_list=year_name_list,year_gain_list=year_gain_list)
# @app.route('/Home')
# def home():
#     return render_template('/static/Home.html')

if __name__ == '__main__':
    #app.run(debug=True, host='127.0.0.1', port='5000')
    app.run(debug=True)

