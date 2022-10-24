# -*- coding = utf-8 -*-
# @Time : 2022/6/23 15:04
# @Author : CQU20205644
# @File : BOX_OFFICE.py
# @Software : PyCharm

#Box Office Mojo是亚马逊公司旗下一个系统性计算电影票房的网站，创办人Brandon Gray在1998年8月创办了这个网站。
# 到现在这个网站一个月平均流量有一百万人次。Box Office Mojo的论坛也是这个网站的特色之一。
import re
import sqlite3
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

def init_database():
    conn = sqlite3.connect("movieTop2016_2022.db")  # 打开或创建数据库
    print("Open database successfully!")
    c = conn.cursor()  # 获取游标
    ''''''
    sql = '''
        create table movieTop200
        (id integer primary key autoincrement,
        name text not null,
        total_gain  numeric not null,
        year numeric not null
        );
    '''
    c.execute(sql)  # 执行sql语句
    conn.commit()  # 提交数据库操作
    print("成功建表")
    conn.close()  # 关闭数据库连接

def insert_message(data,year):
    conn=sqlite3.connect('movieTop2016_2022.db')
    curr=conn.cursor()
    for i in range(0,len(data),2):
        sql = '''
            insert into movieTop200(
            name,total_gain,year) values
            ("''' + data[i] + '",' + data[i+1] + ',' + str(year) + ')'
        print(sql)
        curr.execute(sql)
        conn.commit()
    curr.close()
    conn.close()


def get_info():
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }  # 用户代理
    for year in range(2016,2023):#爬取2016~2022年世界票房排名的前200名
        time.sleep(10)
        url = 'https://www.boxofficemojo.com/year/world/' + str(year) + '/'
        print(url)
        html=requests.get(url=url,headers=head).text
        soup= BeautifulSoup(html,"lxml")
        #print(html)
        items = soup('tr')
        print(len(items))
        findTotalMoney = re.compile(
            r'<td class=\"a-text-right mojo-field-type-money\">(.*?)</td><td class="a-text-right')
        i = 0
        #发现第0个不是所找目标，所以从第一个开始分析
        data=[]
        for item in items[1:]:
            i+=1
            item=str(item)
            str_specfic = r'ref_=bo_ydw_table_' + str(i) + r'\">(.*?)</a></td><td'
            findTitle = re.compile(str_specfic)#获取电影名的正则
            title=re.findall(findTitle,item)[0]
            total_gain=re.findall(findTotalMoney,item)[0]
            data.append(title)
            total_gain=total_gain[1:]#将美元符号去除
            total_gain=total_gain.replace(',','')
            data.append(total_gain)
        insert_message(data,year)
if __name__ == "__main__":
    # init_database()
    # get_info()
    conn = sqlite3.connect("movieTop2016_2022.db")
    sql_data = pd.read_sql("select * from movieTop200", con=conn)
    print(sql_data)
    conn.close()
