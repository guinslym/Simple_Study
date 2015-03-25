#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import pprint
import heapq

class Trie:
    def __init__(self):
        self.children = {}

    def add(self,word):
        root = self.children
        l = len(word)
        for i in range(0,l):
            root.setdefault(word[i],{})
            root = root[word[i]]
        root.setdefault('',0)
        root[''] +=1

    def __iter__(self):
        return self.backtrace(self.children,'')

    def backtrace(self,dt,word):
        for k in dt.keys():
            if k == '':
                yield word,dt[k]
                dt.pop(k)
            elif dt == {}:
                break
            else:
                next_string = word + k
                for w,count in self.backtrace(dt[k],next_string):
                    yield w,count

trie = Trie()
trie.add(u'我')
trie.add(u'我们家')
trie.add(u'我家')
trie.add(u'我是')
trie.add(u'我想说')
trie.add(u'我不想说')
trie.add(u'我想说')

pprint.pprint(trie.children,indent=2)
pprint.pprint([dc for dc in trie])
