# -*- coding = utf-8 -*-
# @Time : 2022/6/21 17:25
# @Author : CQU20205644
# @File : doubanTop250.py
# @Software : PyCharm
# -*- codeing = utf-8 -*-
# @Time : 2022-02-26 9:34
# @Author : CQU20205644
# @File : spider.py
# @Software : PyCharm


# 得到指定一个URL的网页内容
import urllib.request, urllib.error
import xlwt
from bs4 import BeautifulSoup
import re
import sqlite3
import pandas as pd

findLink = re.compile(r'<a href="(.*?)">')
findImage = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符匹配在字符串中
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findDb = re.compile(r'<p class=""(.*?)</p>', re.S)


def main():
    # 1.爬取网页
    # 2.解析数据
    # 3.保存数据
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getdata(baseurl)
    savepath = "豆瓣TOP250.xls"
    dbpath = "movie.db"
    saveData2(datalist, dbpath)
    #saveData(datalist,savepath)
    # 保存数据


def getdata(baseurl):  # 调用获取页面信息的函数10次
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)

        # 逐一进行解析
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            # print(item) 测试查看电影item的全部信息
            data = []
            item = str(item)
            link = re.findall(findLink, item)[0]
            data.append(link)  # 添加链接
            imgSrc = re.findall(findImage, item)[0]
            data.append(imgSrc)  # 添加图片
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):  # 可能不止一个名字
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去掉/
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append("  ")  # 留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加排名
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 添加评分

            inq = re.findall(findInq, item)
            if (len(inq) != 0):
                inq = inq[0].replace("。", '')  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")
            db = re.findall(findDb, item)[0]
            db = re.sub('<br(\s+)?/>(\s+)?', " ", db)  # 去掉br
            db = re.sub('/', "", db)
            data.append(db.strip())  # 去掉空格

            datalist.append(data)  # 把处理好的一部电影信息放入DATALIST中

            # print(link)
    #   print(datalist)
    return datalist


def saveData(datalist, savepath):
    print("save...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣TOP250', cell_overwrite_ok=True)  # 创建工作表,直接覆盖
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价人数", "概况", "相关信息")
    # worksheet.write(0,0,"好好学习")              #写入数据
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % i)
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])  # 数据
    book.save(savepath)
    # workbook.save('cqu.xls')  # 保存数据表

    pass


def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like; Gecko) Chrome / 98.0; .4758; .102; Safari / 537.36"
    }  # 用户代理

    # 发送消息
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    #     print (html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData2(datalist, dbpath):
    init_db(dbpath)
    conn=sqlite3.connect(dbpath)
    curr=conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index==4 or index==5:
                continue
            data[index]='"'+data[index]+'"'
        sql='''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,introduction,info)
            values(%s)
        '''%",".join(data)
        print(sql)
        curr.execute(sql)
        conn.commit()
    curr.close()
    conn.close()



def init_db(dbpath):
    sql = '''
        create table movie250
        (id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #main()
    #init_db("movietest.db")

    conn=sqlite3.connect("movie.db")
    sql_data=pd.read_sql("select * from movie250",con=conn)
    print(sql_data)
    #print("爬取完毕！")
