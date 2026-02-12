
# it_company/__init__.py
import pymysql
# 让 pymysql 伪装成 MySQLdb
pymysql.install_as_MySQLdb()