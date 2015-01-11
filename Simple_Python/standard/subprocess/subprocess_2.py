#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import subprocess

# Command with shell expansion
subprocess.call('echo $HOME',shell=True)