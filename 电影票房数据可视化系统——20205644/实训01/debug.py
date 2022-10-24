# -*- coding = utf-8 -*-
# @Time : 2022/6/22 16:39
# @Author : CQU20205644
# @File : debug.py
# @Software : PyCharm
import re
import sqlite3
import pandas as pd
import requests
from bs4 import BeautifulSoup


#获取每个电影的url
from lxml import etree

'''
htmlfile = open("F:\电影票房数据可视化系统——20205644\实训01\my.html", 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle, 'lxml')
#print(soup)
data_1 = soup.find_all('div', class_="channel-detail movie-item-title")  # 保存电影名称
data_2 = soup.find_all('div', class_='channel-detail channel-detail-orange')  # 电影评分
num=0
print(data_1)
print(data_2)
for item in data_1:
    num+1
    url_1=item.select('a')[0]['href']
    #print(url_1)
    if data_2[num-1].get_text()!='暂无评分':
        url='https://www.maoyan.com'+url_1
        print(url)
        print('--------film url----------')
    else:
        print('The work is done')
        break
'''

'''
#测试破解文字反爬

url='https://www.maoyan.com/films/1397016'
head = {
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like; Gecko) Chrome / 98.0; .4758; .102; Safari / 537.36"
}  # 用户代理
response=requests.get(url=url,headers=head)
html=response.text
#保存起来慢慢试验，防止访问次数过多被限制访问
with open('./my_specific.html', 'w', encoding='utf-8') as fp:
    fp.write(html)

htmlfile = open("F:\电影票房数据可视化系统——20205644\实训01\my_specific.html", 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle, 'lxml')
#print(soup)
#print(htmlhandle)
#寻找woff文件
cmp=re.compile(r'format\(\"embedded-opentype\"\),url\(\"(//.*?.woff)')
rst=cmp.findall(htmlhandle)[0]
print(rst)
'''
'''
OFFICEBOX
'''
htmlfile = open("F:\电影票房数据可视化系统——20205644\实训01\office_box.html", 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle, 'lxml')
#print((soup))
items=soup('tr')
# #print(items[0])
# print(items[1])
# print('------------')
# print(items[2])
# #print(items)
print(len(items))
item=str(items[1])
str_Title=r'ref_=bo_ydw_table_%s\">(.*?)</a></td><td'
#findTitle=re.compile(r'ref_=bo_ydw_table_1\">(.*?)</a></td><td')#对于每一个这个数字在递增，所以要额外拼接一下
# str_specfic=r'ref_=bo_ydw_table_'+str(1)+r'\">(.*?)</a></td><td'
# findTitle=re.compile(str_specfic)
findTotalMoney=re.compile(r'<td class=\"a-text-right mojo-field-type-money\">(.*?)</td><td class="a-text-right')
#title=re.findall(findTitle,item)
# totalMoey=re.findall(findTotalMoney,item)
#print(title)
# print(totalMoey[0])
i=0
# #发现第0个不是所找目标，所以从第一个开始分析


# data=[]
# for item in items[1:]:
#     i+=1
#     item=str(item)
#     str_specfic = r'ref_=bo_ydw_table_' + str(i) + r'\">(.*?)</a></td><td'
#     findTitle = re.compile(str_specfic)
#     title=re.findall(findTitle,item)[0]
#     total_gain=re.findall(findTotalMoney,item)[0]
#     data.append(title)
#     total_gain=total_gain[1:]#将美元符号去除
#     total_gain=total_gain.replace(',','')
#     data.append(total_gain)
#     #print(data)
# #print(data[2])
# #print(len(data))
# conn=sqlite3.connect('test.db')
# curr=conn.cursor()
# for i in range(0,len(data),2):
#     sql = '''
#         insert into movieTop200(
#         name,total_gain) values
#         ("''' +data[i]+'",'+data[i+1]+')'
#     print(sql)
#     curr.execute(sql)
#     conn.commit()
# curr.close()
# conn.close()
    #print(data[i]+','+data[i+1])
    #print('电影名：'+title+' 电影全球票房：'+total_gain)
    #存入数据库

#验证数据库
conn = sqlite3.connect("test.db")
sql_data = pd.read_sql("select * from movieTop200", con=conn)
print(sql_data)
conn.close()

# conn = sqlite3.connect("test.db")  # 打开或创建数据库
# print("Open database successfully!")
# c = conn.cursor()  # 获取游标
# ''''''
# sql = '''
#     create table movieTop200
#     (id integer primary key autoincrement,
#     name text not null,
#     total_gain  numeric not null
#     );
#
# '''
# c.execute(sql)  # 执行sql语句
# conn.commit()  # 提交数据库操作
# print("成功建表")
# conn.close()  # 关闭数据库连接
#
# import time,random,hashlib,requests,jsonpath,re,ddddocr,io,uuid
# from fontTools.ttLib import TTFont
# from PIL import ImageFont, Image, ImageDraw
#
# ocr = ddddocr.DdddOcr()
#
# def main():
#     uid=uuid.uuid4()
#     ts=time.time()*1000
#     key='A013F70DB97834C0A5492378BD76C53A'
#     ua='TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMS4wLjQ5NTEuNjQgU2FmYXJpLzUzNy4zNiBFZGcvMTAxLjAuMTIxMC41Mw=='
#     index=int(1000*random.random()+1)
#     enstr=f'method=GET&timeStamp={ts}&User-Agent={ua}&index={index}&channelId=40009&sVersion=2&key={key}'
#     signkey=hashlib.md5(enstr.encode(encoding='UTF-8')).hexdigest()
#     url=f'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid={uid}&timeStamp={ts}&User-Agent={ua}&index={index}&channelId=40009&sVersion=2&signKey={signkey}'
#     headers={
#         'Accept':'application/json, text/plain, */*',
#         'Referer':'https://piaofang.maoyan.com/dashboard',
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
#     }
#     html=requests.get(url,headers=headers,verify=False)
#     fonturl='http:'+re.search('opentype"\),url\("(//.*?\.woff)"',html.json()['fontStyle']).group(1)
#     r = requests.get(fonturl)
#     with open('temp.woff', 'wb') as f:
#         f.write(r.content)
#         f.close
#     tfont = TTFont("temp.woff")
#     uni_list = tfont.getGlyphOrder()[2:]
#     print('uni列表：',uni_list)
#
#     charList = []
#     font = ImageFont.truetype("temp.woff", 40)
#     #将10个uni字符画到im，进而使用ocr识别获得对应数字
#     for uchar in uni_list:
#         unknown_char = f"\\u{uchar[3:]}".encode().decode("unicode_escape")
#         im = Image.new(mode='RGB', size=(42, 40), color="white")
#         draw = ImageDraw.Draw(im=im)
#         draw.text(xy=(0, 0), text=unknown_char, fill=0, font=font)
#         img_byte = io.BytesIO()
#         im.save(img_byte, format='JPEG')
#         charList.append(ocr.classification(img_byte.getvalue()))
#     print('对应字符：',charList)
#
#     #解析获取需要的数据
#     moviename=jsonpath.jsonpath(html.json(),'$.movieList.data.list..movieInfo.movieName')
#     movieInfo = jsonpath.jsonpath(html.json(), '$.movieList.data.list..movieInfo.releaseInfo')
#     sumBoxDesc = jsonpath.jsonpath(html.json(), '$.movieList.data.list..sumBoxDesc')
#     boxRate = jsonpath.jsonpath(html.json(), '$.movieList.data.list..boxRate') #票房占比
#     showCount = jsonpath.jsonpath(html.json(), '$.movieList.data.list..showCount') #排片场次
#     enNum=jsonpath.jsonpath(html.json(), '$.movieList.data.list..boxSplitUnit.num')
#     enNumDw=jsonpath.jsonpath(html.json(), '$.movieList.data.list..boxSplitUnit.unit')
#
#     #解析票房信息
#     for j in range(len(moviename)):
#         tmpstr=enNum[j].split(';')
#         rstr=''
#         for i in tmpstr:
#             if i =='': continue
#             tmp = 'uni' + i.replace('&#x', '', 1).replace('.','').upper()
#             for k in range(len(uni_list)):
#                 if tmp == uni_list[k]:
#                     if '.' in i:
#                         rstr = rstr + '.'+charList[k]
#                     else:
#                         rstr = rstr + charList[k]
#                     break
#         print(f'{moviename[j]}\t{movieInfo[j]}\t{sumBoxDesc[j]}\t综合票房：{rstr}{enNumDw[j]}\t票房占比：{boxRate[j]}\t排片场次：{showCount[j]}')
#
# if __name__ == '__main__':
#     main()





