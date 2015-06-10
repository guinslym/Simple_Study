# -*- coding:utf-8 -*-

import psycopg2

class PSQL(object):
    def __init__(self,**kargs):
        """初始化连接选项,需要传入dbname,password,user"""
        dsn = ''
        for x in kargs:
            dsn += '%s=%s ' % (x,kargs[x])
        self.pgObj=psycopg2.connect(dsn)
        self.cur = self.pgObj.cursor()
    
    def query(self,str):
        """执行查询语句"""
        self.data = self.cur.execute(str)
    
    def fetchall(self):
        """查询所有的结果"""
        return self.cur.fetchall()
    
    def fetchone(self):
        return self.cur.fetchone()
    
    def __del__(self):
        self.pgObj.close()

p = PSQL(dbname='tim',host='localhost')
p.query('select * from weibo_user')
for x in p.fetchall():
    print x