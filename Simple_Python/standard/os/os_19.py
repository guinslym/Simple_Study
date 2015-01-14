#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
child_pid = os.fork()
if child_pid:
    os.waitpid(child_pid,0)
else:
    os.execlp('pwd','pwd','-P')