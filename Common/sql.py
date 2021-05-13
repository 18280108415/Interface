"""
@version: 1.0
@author: Dfly
@site:
@software: PyCharm
@time: 2021/5/11 10:58
connect to mysql
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import readConf
import readConf
from readConf import *
import pymysql.cursors
#import readConf

print(readConf.host1,readConf.port,readConf.username,readConf.password,readConf.db)
print(type(int(readConf.port)))
'''步骤:
1.创建连接
2.创建游标
3.执行sql
4.提交
5.关闭游标
6.关闭连接
'''
'''class Mysql:
    def __init__(self):
        self= self'''
def mysql():

    #print (cf.host)
    #Create connection
    conn = pymysql.connect(host=readConf.host1, port=int(readConf.port), user=readConf.username, passwd=readConf.password, db=readConf.db)
    #create cursor
    cursor = conn.cursor()
    #execute sql
    cursor.execute(readConf.sql)
    #commit
    conn.commit()
    testData = cursor.fetchone()
    print(testData)
    #close corsor
    cursor.close()
    #close commit
    conn.close()



if __name__ == '__main__':
    mysql()

