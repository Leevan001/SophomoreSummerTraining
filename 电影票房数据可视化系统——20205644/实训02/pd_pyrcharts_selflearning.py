# -*- coding = utf-8 -*-
# @Time : 2022/6/25 14:17
# @Author : CQU20205644
# @File : pd_pyrcharts_selflearning.py
# @Software : PyCharm
import sqlite3
import numpy as np
import pandas as pd
from pyecharts.charts import Bar
#导入设置系列配置和全局配置
from pyecharts import options as opts
from pyecharts.charts import Line
import os
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
from pyecharts.charts import TreeMap

# bar = Bar()
# bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
# bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# bar.render()
# os.system("render.html")
from pyecharts.commons.utils import JsCode


# conn = sqlite3.connect("movieTop2016_2022.db")
# #sql_data = pd.read_sql("select * from movieTop200", con=conn)
# #print(sql_data)
# color_function = """
#         function (params) {
#             if (params.value > 100000 ) {
#                 return 'red';
#             } else if (params.value > 70000 ) {
#                 return 'pink';
#             }
#             return 'blue';
#         }
#         """
# sql = '''
#     select * from movieTop200 where year=2016
# '''
# sql_data = pd.read_sql(sql, con=conn)
# print(type(sql_data))
# df1 = np.array(sql_data[0:15]) #先使用array()将DataFrame转换一下
# df2 = df1.tolist()#再将转换后的数据用tolist()转成列表
# name=[]
# gain=[]
# for i in range(len(df2)):
#     name.append(df2[i][1])
#     gain.append(int(df2[i][2]/10000))
# print(name)
# print(gain)
# bar = Bar()
# bar.add_xaxis(name)
# bar.set_series_opts(label_opts=opts.LabelOpts(is_show=True,position="inside"))
# bar.add_yaxis("电影票房：", gain,itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))
# bar.set_global_opts(title_opts=opts.TitleOpts(title="2016年电影票房收入TOP15(单位:万美元)"))
# bar.render()
# os.system("render.html")
# conn.close()


#饼状图

# -*- coding: utf-8 -*-
# inner_x_data = ["直达", "营销广告", "搜索引擎"]
# inner_y_data = [335, 679, 1548]
# inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]
# c = (
#     Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#     .add(
#         "电影制作公司：",
#         #[list(z) for z in zip(Faker.choose(), Faker.values())],
#         data_pair=inner_data_pair,
#         # 饼图的半径，数组的第一项是内半径，第二项是外半径
#         # 默认设置成百分比，相对于容器高宽中较小的一项的一半
#         radius=["40%", "75%"],
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="Pie-Radius"),
#         legend_opts=opts.LegendOpts(
#             orient="vertical", #图例垂直放置
#             pos_top="15%",# 图例位置调整
#             pos_left="2%"),
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     .render("pie_radius.html")
# )
# os.system("pie_radius.html")


# conn = sqlite3.connect("F:\电影票房数据可视化系统——20205644\实训01\movieCompany.db")
# sql_data = pd.read_sql("select * from movieCompanyTop45", con=conn)
# #print(sql_data)
# df1 = np.array(sql_data[0:15])  # 先使用array()将DataFrame转换一下
# df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
# Company_name = []
# Company_gain = []
# for i in range(len(df2)):
#     Company_name.append(df2[i][1])
#     Company_gain.append(int(df2[i][2] / 10000))
# print(Company_name)
# print(Company_gain)
# conn.close()

# conn = sqlite3.connect("movieTop2016_2022.db")
# year_gain_list=[]
# for year in range(2016,2023):
#     sql = 'select * from movieTop200 where year='+str(year)
#     #print(sql)
#     title=str(year)+"年电影票房收入TOP15(单位:万美元)"
#     html_Name=str(year)+'年电影TOP15柱状图.html'
#     sql_data = pd.read_sql(sql, con=conn)
#     df1 = np.array(sql_data)  # 先使用array()将DataFrame转换一下
#     df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
#     # print(df2)
#     # print('----------')
#     # print(df2[1][0])
#     # print(df2[1][1])
#     # print(df2[1][2])    --->所要找的点以哦那个票房收入
#     year_gain=0
#     for i in range(len(df2)):
#         year_gain+=df2[i][2]
#     print(str(year)+'年Top200的电影的总票房为：'+str(year_gain))
#     year_gain_list.append(year_gain)
# print(year_gain_list)
# conn.close()

#研究折线图怎么画


# def line_base() -> Line:
#     attr = ["10.13", "10.14", "10.15", "10.16" , "10.17" , "\
#     10.18"]
#     v1 = [1650, 1700, 1461, 1350, 1100, 1500]
#     #v2 = [1020, 575, 400, 350, 330, 480]
#
#     c = (
#         Line()
#         .add_xaxis(attr)
#         .add_yaxis("成都fly北京", v1)
#         #.add_yaxis("成都fly昆明", v2)
#         .set_global_opts(title_opts=opts.TitleOpts(title="航班价格折线图"))
#     )
#     return c
# m=line_base()
# m.render()
# os.system('render.html')
# year_list=[]
# for i in range(2016,2023):
#     year_list.append(str(i)+'年')
# print(year_list)

# conn = sqlite3.connect("movieTop2016_2022.db")
# sql_data = pd.read_sql("select * from movieTop200", con=conn)
# df=sql_data.sort_values(by=['total_gain'],ascending=False)
# print(df)
# df1 = np.array(df[0:100])  # 先使用array()将DataFrame转换一下
# df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
# print(df2)
# year_count= dict.fromkeys(range(2016,2023), 0)
# for i in range(len(df2)):
#     year_count[df2[i][3]]+=1
# #print(year_count)
# x_data = list(year_count.keys())
# y_data = list(year_count.values())
# data_pair = [list(z) for z in zip(x_data,y_data)]
# c = (
#     Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#     .add(
#         "电影制作公司：",
#         #[list(z) for z in zip(Faker.choose(), Faker.values())],
#         data_pair=data_pair,
#         center=(600,280),
#         # 饼图的半径，数组的第一项是内半径，第二项是外半径
#         # 默认设置成百分比，相对于容器高宽中较小的一项的一半
#         radius=["30%", "60%"],
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="2016~2022年全球电影票房Top100的年代分布饼状图：",subtitle='单位：部'),
#         legend_opts=opts.LegendOpts(
#             orient="vertical", #图例垂直放置
#             pos_top="15%",# 图例位置调整
#             pos_left="1%"),
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     .render("2016~2022Top100电影发布年份图.html")
# )
# os.system("2016~2022Top100电影发布年份图.html")




# # 内部饼图
# inner_x_data = ["直达", "营销广告", "搜索引擎"]
# inner_y_data = [335, 679, 1548]
# inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]
# # [['直达', 335], ['营销广告', 679], ['搜索引擎', 1548]]
#
#
# # 外部环形（嵌套）
# outer_x_data = ["直达", "营销广告", "搜索引擎", "邮件营销", "联盟广告", "视频广告", "百度", "谷歌"]
# outer_y_data = [335, 310, 234, 135, 1048, 251, 147, 102]
# outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]
# ...
# # 观察一下怎么嵌套的
# # 1.内部——直达335 = 外部 直达335
# # 2.内部——营销广告679 = 外部 营销广告310 + 搜索引擎234 + 邮件营销135
# # 3.内部——搜索引擎1548 = 外部 联盟广告1048 + 视频广告251 + 百度147 + 谷歌102
# [['直达', 335],
#
#  ['营销广告', 310],
#  ['搜索引擎', 234],
#  ['邮件营销', 135],
#
#  ['联盟广告', 1048],
#  ['视频广告', 251],
#  ['百度', 147],
#  ['谷歌', 102]]
# ...
#
# c = (
#     # 初始化
#     Pie(init_opts=opts.InitOpts(
#         width="900px",
#         height="800px",
#         theme=ThemeType.SHINE))
#
#         # 内部饼图
#         .add(
#         series_name="访问来源",  # 系列名称
#         center=["50%", "35%"],
#         data_pair=inner_data_pair,  # 系列数据项，格式为 [(key1, value1), (key2, value2)]
#         radius=[0, "30%"],  # 饼图半径 数组的第一项是内半径，第二项是外半径
#         label_opts=opts.LabelOpts(position="inner"),  # 标签设置在内部
#     )
#
#         # 外部嵌套环形图
#         .add(
#         series_name="访问来源",  # 系列名称
#         center=["50%", "35%"],
#         radius=["40%", "55%"],  # 饼图半径 数组的第一项是内半径，第二项是外半径
#         data_pair=outer_data_pair,  # 系列数据项，格式为 [(key1, value1), (key2, value2)]
#         # 标签配置项 参考上面的例子
#         label_opts=opts.LabelOpts(
#             position="outside",
#             formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
#             background_color="#eee",
#             border_color="#aaa",
#             border_width=1,
#             border_radius=4,
#             rich={
#                 "a": {"color": "#999",
#                       "lineHeight": 22,
#                       "align": "center"},
#
#                 "abg": {
#                     "backgroundColor": "#e3e3e3",
#                     "width": "100%",
#                     "align": "right",
#                     "height": 22,
#                     "borderRadius": [4, 4, 0, 0],
#                 },
#
#                 "hr": {
#                     "borderColor": "#aaa",
#                     "width": "100%",
#                     "borderWidth": 0.5,
#                     "height": 0,
#                 },
#
#                 "b": {"fontSize": 16, "lineHeight": 33},
#
#                 "per": {
#                     "color": "#eee",
#                     "backgroundColor": "#334455",
#                     "padding": [2, 4],
#                     "borderRadius": 2,
#                 },
#             },
#         ),
#     )
#         # 全局配置项
#         .set_global_opts(legend_opts=opts.LegendOpts(
#         pos_left="left",
#         orient="vertical"))
#
#         # 系统配置项
#         .set_series_opts(
#         tooltip_opts=opts.TooltipOpts(
#             trigger="item",
#             formatter="{a} <br/>{b}: {c} ({d}%)"
#         )
#     )
#         .render("nested_pies.html")
# )
# os.system("nested_pies.html")
#利用pyecharts画矩形树状图

# conn = sqlite3.connect("movieTop2016_2022.db")
# sql_data = pd.read_sql("select * from movieTop200", con=conn)
# df=sql_data.sort_values(by=['total_gain'],ascending=False)
# df1 = np.array(df[0:100])  # 先使用array()将DataFrame转换一下
# df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
# print(df2)
# year_count= dict.fromkeys(range(2016,2023), 0)
# for i in range(len(df2)):
#     year_count[df2[i][3]]+=1
# #print(year_count)
# x_data = list(year_count.keys())
# y_data = list(year_count.values())
# data_pair = [list(z) for z in zip(x_data,y_data)]
# data = [
#     {"value": 40, "name": "我是A"},
#     {
#         "value": 76,
#         "name": "我是B",
#         "children": [
#             {
#                 "value": 76,
#                 "name": "我是B.children",
#                 "children": [
#                     {"value": 12, "name": "我是B.children.a"},
#                     {"value": 28, "name": "我是B.children.b"},
#                     {"value": 20, "name": "我是B.children.c"},
#                     {"value": 16, "name": "我是B.children.d"},
#                 ],
#             }
#         ],
#     },
# ]
#
# c = (
#     TreeMap()
#     .add("演示数据", data)
#     .set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-基本示例"))
#     .render("treemap_base.html")
# )
# os.system('treemap_base.html')
#
#
# c = (
#     TreeMap()
#     .add(
#         series_name="演示数据",
#         data=data,
#         levels=[
#             opts.TreeMapLevelsOpts(
#                 treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
#                     border_color="#555", border_width=4, gap_width=4
#                 )
#             ),
#             opts.TreeMapLevelsOpts(
#                 color_saturation=[0.3, 0.6],
#                 treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
#                     border_color_saturation=0.7, gap_width=2, border_width=2
#                 ),
#             ),
#             opts.TreeMapLevelsOpts(
#                 color_saturation=[0.3, 0.5],
#                 treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
#                     border_color_saturation=0.6, gap_width=1
#                 ),
#             ),
#             opts.TreeMapLevelsOpts(color_saturation=[0.3, 0.5]),
#         ],
#     )
#     .set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-Levels-配置"))
#     .render("treemap_levels.html")
# )
# os.system('treemap_levels.html')
#
# import os
# import sqlite3
#
# import numpy as np
# import pandas as pd
# import pyecharts.options as opts
# from pyecharts.charts import Pie, TreeMap
# from pyecharts.globals import ThemeType
#
#
#
# conn = sqlite3.connect("movieTop2016_2022.db")
# sql_data = pd.read_sql("select * from movieTop200", con=conn)
# df=sql_data.sort_values(by=['total_gain'],ascending=False)
# df1 = np.array(df[0:100])  # 先使用array()将DataFrame转换一下
# df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
# #print(df2)
# name_message= dict.fromkeys(range(2016,2023), [])
# gain_message= dict.fromkeys(range(2016,2023), [])
# year_totalgain=dict.fromkeys(range(2016,2023), 0)
# for i in range(len(df2)):
#     name_message[df2[i][3]].append(df2[i][1])
#     gain_message[df2[i][3]].append(df2[i][2])
#     year_totalgain[df2[i][3]]+=df2[i][2]
# print(year_totalgain)
#
# #print(name_message[2016][0])
# # print(gain_message[2016][0])
# # print(name_message[2016][1])
# # print(gain_message[2016][1])
# # print(name_message[2016][2])
# # print(gain_message[2016][3])
# data=[]
# for year in range(2016,2023):
#     year_data=[]
#     for i in range(len(name_message[year])):
#         tmp_dic = {"value": 0, "name": ""}
#         tmp_dic['value']=gain_message[year][i]
#         tmp_dic['name']=name_message[year][i]
#         #print(tmp_dic)
#         year_data.append(tmp_dic)
#     danyuan = {
#         "value": year_totalgain[year],
#         "name": str(year)+'年',
#         "children": [
#              {
#                 "value": year_totalgain[year],
#                 "name":  str(year)+'年的电影',
#                 "children": year_data,
#             }
#         ],
#     }
#     data.append(danyuan)
#
# c = (
#     TreeMap()
#     .add("演示数据", data)
#     .set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-基本示例"))
#     .render("treemap_base.html")
# )
# os.system('treemap_base.html')
#
#
# import os
# import sqlite3
#
# import numpy as np
# import pandas as pd
# import pyecharts.options as opts
# from pyecharts.charts import Pie, TreeMap
# from pyecharts.globals import ThemeType
#
#
#
# conn = sqlite3.connect("movieTop2016_2022.db")
# sql_data = pd.read_sql("select * from movieTop200", con=conn)
# df=sql_data.sort_values(by=['total_gain'],ascending=False)
# df1 = np.array(df[0:100])  # 先使用array()将DataFrame转换一下
# df2 = df1.tolist()  # 再将转换后的数据用tolist()转成列表
# #print(df2)
# name_message= [[],[],[],[],[],[],[]]
# gain_message= [[],[],[],[],[],[],[]]
# year_totalgain=dict.fromkeys(range(2016,2023), 0)
# for i in range(len(df2)):
#     name_message[df2[i][3]-2016].append(df2[i][1])
#     gain_message[df2[i][3]-2016].append(df2[i][2])
#     year_totalgain[df2[i][3]]+=df2[i][2]
#
# data=[]
# for year in range(2016,2023):
#     year_data=[]
#     for i in range(len(name_message[year-2016])):
#         tmp_dic = {"value": 0, "name": ""}
#         tmp_dic['value']=gain_message[year-2016][i]
#         tmp_dic['name']=name_message[year-2016][i]
#         #print(tmp_dic)
#         year_data.append(tmp_dic)
#     danyuan = {
#         "value": year_totalgain[year],
#         "name": str(year)+'年',
#         "children": [
#              {
#                 "value": year_totalgain[year],
#                 "name":  str(year)+'年的电影',
#                 "children": year_data,
#             }
#         ],
#     }
#     data.append(danyuan)
# data=str(data)
# data=data.replace("'name'","name")
# data=data.replace("'value'",'value')
# data=data.replace("'children'",'children')
# print(data)

import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import sqlite3
con=sqlite3.connect('F:\电影票房数据可视化系统——20205644\实训01\movie.db')
cur=con.cursor()
sql='select introduction from movie250'
data=cur.execute(sql)
text=''
for item in data:
    text+=item[0]
#print(text)
cur.close()
con.close()
re_move = ['的','是','上','猪','更','拉','却','才','并','了','不']  # 无效数据

# 去除无关数据
for i in re_move:
    text = text.replace(i, "")
cut=jieba.cut(text)
string='   '.join(cut)
img=Image.open(r'F:\电影票房数据可视化系统——20205644\实训01\img.png')
img_array=np.array(img)
wc=WordCloud(background_color='white',mask=img_array,font_path='HGZK_CNKI.TTF').generate_from_text(string)
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')
plt.show()
plt.savefig('word.jpg',dpi=500)








