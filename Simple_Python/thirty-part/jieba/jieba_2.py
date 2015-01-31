#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import jieba.analyse

text = '结巴中文分词模块是1个非常好用的Python分词组件,请继续发扬'
tags = jieba.analyse.extract_tags(text,2)

print "关键字抽取:",'/'.join(tags)