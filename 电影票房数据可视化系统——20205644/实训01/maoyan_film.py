# -*- coding = utf-8 -*-
# @Time : 2022/6/22 14:42
# @Author : CQU20205644
# @File : maoyan_film.py
# @Software : PyCharm

#ip被封了，做种爬获了2020年票房最高电影的url
#转战BOX OFFICE(全球票房网站)
import time

import requests
from bs4 import BeautifulSoup
from fontTools.ttLib import TTFont

def get_url():
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }  # 用户代理
    for i in range(0,30,30):
        #time.sleep(10)
        url='https://www.maoyan.com/films?showType=3&yearId=13&sortId=3&offset='+str(i)
        #url="https://movie.douban.com/subject/35295405/"
        html=requests.get(url=url,headers=head).content
        soup= BeautifulSoup(html,"lxml")
        data_1=soup.find_all('div',class_="channel-detail movie-item-title")#保存电影名称
        data_2=soup.find_all('div',class_='channel-detail channel-detail-orange')#电影评分
        #print(html)
        #保存起来慢慢试验，防止访问次数过多被限制访问
        # with open('./my.html', 'w', encoding='utf-8') as fp:
        #     fp.write(html)
        # fp.close()
        #print(data_1)
        # print(data_2)
        num = 0
        for item in data_1:
            num + 1
            url_1 = item.select('a')[0]['href']
            # print(url_1)
            if data_2[num - 1].get_text() != '暂无评分':
                url = 'https://www.maoyan.com' + url_1
                print(url)
                print('--------film url----------')
            else:
                print('The work is done')
                break

def get_message(url):
    data={}


if __name__ == "__main__":
    get_url()

