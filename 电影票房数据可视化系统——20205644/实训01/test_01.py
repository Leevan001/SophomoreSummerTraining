# -*- coding = utf-8 -*-
# @Time : 2022/6/23 18:35
# @Author : CQU20205644
# @File : test_01.py
# @Software : PyCharm
'''
a='$26,508,132'
a=a[1:]
a=a.replace(',','')
print(a)
a=int(a)
print(type(a))
'''
# for year in range(2016,2022):
#     # time.sleep(10)
#     url=''
#     url = 'https://www.boxofficemojo.com/year/world/'+str(year)+'/'
#     print(url)
data=['我','12']
year=1200
sql = '''
    insert into movieTop200(
    name,total_gain,year) values
    ("''' +data[0]+'",'+data[1]+','+str(year)+')'
print(sql)