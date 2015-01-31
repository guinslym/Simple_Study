#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import jieba

s = '我来自中国广东省广州市天河区龙洞'
seg_list = jieba.cut(s,cut_all=True)
print 'Full Mode:','/'.join(seg_list)  #全模式

seg_list = jieba.cut(s,cut_all=False)
print 'Default Mode:','/'.join(seg_list) #默认模式

seg_list = jieba.cut(s)
print ','.join(seg_list)