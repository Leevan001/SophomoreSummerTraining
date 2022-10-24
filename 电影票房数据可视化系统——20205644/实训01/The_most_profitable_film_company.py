# -*- coding = utf-8 -*-
# @Time : 2022/6/23 21:25
# @Author : CQU20205644
# @File : The_most_profitable_film_company.py
# @Software : PyCharm
import re
import sqlite3

import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree
'''
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}  # 用户代理
url = 'https://www.boxofficemojo.com/brand/?ref_=bo_nb_ydw_tab'
html = requests.get(url=url, headers=head).text
with open('company.html', 'w', encoding='utf-8') as fp:
    fp.write(html)
'''
def init_database():
    conn = sqlite3.connect("movieCompany.db")  # 打开或创建数据库
    print("Open database successfully!")
    c = conn.cursor()  # 获取游标
    ''''''
    sql = '''
        create table movieCompanyTop45
        (id integer primary key autoincrement,
        name text not null,
        total_gain  numeric not null
        );
    '''
    c.execute(sql)  # 执行sql语句
    conn.commit()  # 提交数据库操作
    print("成功建表")
    conn.close()  # 关闭数据库连接

def insert_message(data):
    conn=sqlite3.connect('movieCompany.db')
    curr=conn.cursor()
    for i in range(0,len(data),2):
        sql = '''
            insert into movieCompanyTop45(
            name,total_gain) values
            ("''' + data[i] + '",' + data[i+1] + ')'
        print(sql)
        curr.execute(sql)
        conn.commit()
    curr.close()
    conn.close()

def get_information():
    htmlfile = open("company.html", 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle, 'lxml')
    items=soup.find_all('td',class_="a-text-left mojo-header-column mojo-truncate mojo-field-type-brand")
    items_1=soup.find_all('td',class_="a-text-right mojo-field-type-money mojo-sort-column mojo-estimatable")
    find_gain=re.compile(r'mojo-estimatable\">(.*?)</td>')
    data=[]
    data1=[]
    data2=[]
    for i in range(len(items)):
            str_re='ref_=bo_bns_table_'+str(i+1)+'\\">(.*?)</a></td>'
            findCompanyName = re.compile(str_re)
            companyName=re.findall(findCompanyName,str(items[i]))[0]
            gain=re.findall(find_gain,str(items_1[i]))[0]
            #print('电影公司名：'+companyName+'总票房收入：'+gain)
            gain=gain[1:]#将美元符号去除
            gain=gain.replace(',','')
            data.append(companyName)
            data.append(gain)
            data1.append(companyName)
            data2.append(gain)
    print(data1)
    print('----------')
    print(data2)
    #print(data)
    #insert_message(data)
# print(items[0])
# print('-------------------')
# print(items[1])
# print('-----------')
# findCompanyName=re.compile(r'ref_=bo_bns_table_1\">(.*?)</a></td>')
# item=str(items[0])
# print(re.findall(findCompanyName,item))

# print(items_1[0])
# print(items_1[1])
# print(re.findall(find_gain,str(items_1[0])))

# data=['Marvel Comics', '16319447992']
# sql = '''
#    insert into movieCompanyTop45(
#     name,total_gain) values
#     ("''' + data[0] + '",' + data[1] + ')'
# print(sql)

if __name__ == "__main__":
    #init_database()
    #get_information()
    conn = sqlite3.connect("movieCompany.db")
    sql_data = pd.read_sql("select * from movieCompanyTop45", con=conn)
    print(sql_data)
    conn.close()



