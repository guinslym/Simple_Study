#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

#d是字典，存储从词频表读取的词频数据。defaultdic的好处是，如果词频表没有某个词组，就返回1。
d = collections.defaultdict(lambda:1)
filename='/home/tim/Freq/SogouLabDic.dic'

#从词频表里读取词频数。
def init(filename =filename):
    total = 0
    f = open(filename)
    for line in f.readlines():
        word, freq = line.split('\t')[0:2]
        total += 1
        try:
            d[word.decode('gbk')] = int(freq)
        except:
            d[word] = int(freq)
    d['total'] = total

#分词函数
def solve(s):
    l = len(s)
    #p表示概率，初始值是0
    p = [0 for i in range(l+1)]
    #最后一位是为了方便计算，设置成1
    p[l] = 1
    #词频数太大了，不能使用除法，会有精度问题，把分子分母分开存储
    div = [1 for i in range(l+1)]
    #记录拆分位置
    t = [1 for i in range(l)]
    #dp算法做拆分
    for i in range(l-1,-1, -1):
        print "\ni = ", i,
        for k in range(1, l-i+1):
            print " k = ", k
            if k > 1 and d[s[i:i+k]] == 1:
                print "continue"
                continue
            #判断子句的概率大小，以计算拆分位置
            if d[s[i:i+k]]*p[i+k]*div[i] > p[i]*d['total']*div[i+k]:
                p[i] = d[s[i:i+k]]*p[i+k]
                div[i] = d['total'] * div[i+k]
                t[i] = k
    i = 0
    while i < l:
        print s[i:i+t[i]].encode("utf8")+'/',
        i = i+t[i]

if __name__ == '__main__':
    init()
    s="其中最简单的就是最大匹配的中文分词"
    s=s.decode('utf8')
    solve(s)