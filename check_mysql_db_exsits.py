# -*- coding: utf-8 -*-
import pymysql

try:
    pymysql.connect("10.2.3.3", "monitor", "admin", "ad")
except Exception as e:
    print(Exception, ':', e)
else:
    print(0)
