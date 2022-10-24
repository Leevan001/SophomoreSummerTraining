# -*- coding = utf-8 -*-
# @Time : 2022/7/1 10:17
# @Author : CQU20205644
# @File : maoyan_info.py
# @Software : PyCharm
import time,random,hashlib,requests,jsonpath,re,ddddocr,io,uuid
from fontTools.ttLib import TTFont
from PIL import ImageFont, Image, ImageDraw
import sqlite3

ocr = ddddocr.DdddOcr()
index=random.randint(1,10)
ts=int(time.time()*1000)
key="A013F70DB97834C0A5492378BD76C53A"
head="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
hash_str=f'method=GET&timeStamp={ts}&User-Agent={head}&index={index}&channelId=40011&sVersion=1&key={key}'
print(hash_str)
film_index=1200486
signkey=hashlib.md5(hash_str.encode(encoding='UTF-8')).hexdigest()
print(signkey)
referer='https://www.maoyan.com/films/'+str(film_index)
url=f'https://www.maoyan.com/ajax/films/{film_index}?&timeStamp={ts}&index={index}&signKey={signkey}&channelId=40011&sVersion=1&webdriver=false'
headers = {
    'Accept': '*/*',
    'Referer': referer,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
print(url)
html = requests.get(url, headers=headers)
print(html.text)
with open('tempt.html', 'w', encoding='utf-8') as fp:
    fp.write(html.text)
# print(html.json())