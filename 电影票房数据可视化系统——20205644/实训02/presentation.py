# -*- coding = utf-8 -*-
# @Time : 2022/6/27 21:03
# @Author : CQU20205644
# @File : presentation.py
# @Software : PyCharm
import os

os.system('2016~2022Top电影矩形树状图.html')
for i in range(2016,2023):
    html_Name=str(i)+'年电影TOP15柱状图.html'
    os.system(html_Name)
os.system('Compare2016~2022.html')
os.system("2016~2022Top100电影发布年份图.html")
os.system("Top15Company.html")
