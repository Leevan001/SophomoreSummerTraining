# -*- coding = utf-8 -*-
# @Time : 2022/7/1 20:00
# @Author : CQU20205644
# @File : debug.py
# @Software : PyCharm
import re

from bs4 import BeautifulSoup

htmlfile = open("tempt.html", 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
#print(htmlhandle)
soup= BeautifulSoup(htmlhandle,"html.parser")
a=soup.find_all('a',class_="text-link")[0]
print(a)
a=str(a)
find_tag=re.compile(r'url\(\"(.*?)')
print(re.findall(find_tag,a))
find_woff=re.compile(r',url\("(.*?.woff)\"\);}')
font=soup.find_all('style')
font=str(font[0])
b=re.findall(find_woff,htmlhandle)
print(font)
print(b)