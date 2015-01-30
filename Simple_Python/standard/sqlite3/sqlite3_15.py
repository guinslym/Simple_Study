#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sqlite3

db_filename = 'todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name,description from project')
    for name,desc in cursor.fetchall():
        print '  ',name
    return

with sqlite3.connect(db_filename) as conn:
    print 'Before changes:'
    show_projects(conn)

    try:
        # Insert
        cursor = conn.cursor()
        cursor.execute("""
        delete from project where name = 'virtualenvwrapper'
        """)
        #show the settings
        print '\nAfter delete:'
        show_projects(conn)

        # Pretend the processing caused an error
        raise RuntimeError('simulated error')
    except Exception, e:
        # Discard the changes
        print 'ERROR:',e
        conn.rollback()
    else:
        # save the changes
        conn.commit()
    # show the results
    print '\nAfter rollback:'
    show_projects(conn)