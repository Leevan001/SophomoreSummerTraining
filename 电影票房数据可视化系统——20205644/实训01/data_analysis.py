# -*- coding = utf-8 -*-
# @Time : 2022/6/22 13:01
# @Author : CQU20205644
# @File : data_analysis.py
# @Software : PyCharm
import sqlite3

import pandas as pd

if __name__ == "__main__":
    #main()
    #init_db("movietest.db")

    conn=sqlite3.connect("movie.db")
    df=pd.read_sql("select * from movie250",con=conn)
    #print(sql_data)

    print(df.dtypes)
    conn.close()