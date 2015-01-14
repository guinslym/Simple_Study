#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
os.spawnlp(os.P_WAIT,'pwd','ls','-P')