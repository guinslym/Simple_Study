#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os

link_name = '/tmp/'+os.path.basename(__file__)
print 'Creating link %s->%s' % (link_name,__file__)
os.symlink(__file__,link_name)

stat_info = os.lstat(link_name)
print 'Permissions:',oct(stat_info.st_mode)
print 'Points to:',os.readlink(link_name)

# Cleanup
os.unlink(link_name)