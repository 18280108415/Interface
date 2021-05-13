#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: Dfly
@site:
@software: PyCharm
@time: 2021/5/11 10:58
read conf
"""
import configparser
#读取数据库需要的信息，host，username，port，password，db，sql等
confi = configparser.ConfigParser()
fileopen = open("../data/mysql.ini")
confi.read_file(fileopen)
print(confi.sections())
host1 = confi.get('db','host')
username = confi.get('db', 'username')
password = confi.get('db', 'password')
port = confi.get('db', 'port')
db = confi.get('db', 'user')
sql = confi.get('sql','selectUser')
'''class ReadConf():


    def read_conf(path):
        print(path)
        confi = configparser.ConfigParser()
        fileopen = open(path)
        confi.read_file(fileopen)
        print(confi.sections())
        host1 = confi.get('db','host')
        username = confi.get('db', 'username')
        password = confi.get('db', 'password')
        port = confi.get('db', 'port')
        db = confi.get('db', 'user')
        print(host1,username,password,port,db)
        #return host,username,password,port,db

if __name__ == '__main__':
    path1 = "../data/mysql.ini"
    ReadConf.read_conf(path1)'''
