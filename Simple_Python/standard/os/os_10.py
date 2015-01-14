#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
import stat

filename = 'os_stat_chmod_example.txt'
if os.path.exists(filename):
    os.unlink(filename)
with open(filename,'wt') as f:
    f.write('contents')

# Determime what permissions are already set using stat 
existing_permissions = stat.S_IMODE(os.stat(filename).st_mode)

if not os.access(filename,os.X_OK):
    print 'Adding execute permissions'
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print 'Removing execute permission'
    # use xor to remove the user execute permission
    new_permissions = existing_permissions ^ stat.S_IXUSR

os.chmod(filename,new_permissions)