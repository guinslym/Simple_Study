#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sqlite3
import sys
import threading
import time

db_filename = 'todo.db'
isolation_level = None #autocommit mode

def reader(conn):
    my_name = threading.currentThread().name
    print 'Starting thread'
    try:
        cursor = conn.cursor()
        cursor.execute('select * from task')
        result = cursor.fetchall()
        print 'result fetched'
    except Exception, e:
        print 'ERROR:',e
    return

if __name__ == '__main__':
    with sqlite3.connect(db_filename,
                                    isolation_level=isolation_level,
                                    ) as conn:
       t = threading.Thread(name='Reader 1',
                                     target=reader,
                                     args=(conn,),)
       t.start()
       t.join()