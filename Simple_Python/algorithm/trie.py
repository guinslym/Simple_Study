#! /usr/bin/env/python
# -*- coding:utf-8 -*-

class Node:
    '''节点类,主要用于后面节点的操作'''
    def __init__(self):
        self.value = None
        self.children = {}

class Trie:
    def __init__(self):
        '''初始化根节点'''
        self.root = Node()

    def insert(self,key):
        '''添加节点'''
        node = self.root
        for char in key:
            if char not in node.children:
                child = Node()                        #新建树分支
                node.children[char] = child   #添加到主支上
                node = child                          #以分支作为根节点进行延续
            else:
                node = node.children[char]
        node.value = key

    def search(self,key):
        '''搜索节点'''
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            else:
                node = node.children[char]
        return node.value

    def display_node(self,node):
        '''构建26个字母的字典树'''
        string = ''.join(map(chr,range(97,123)))
        if (node.value != None):
            print node.value
        for char in string:
            if char in node.children:
                self.display_node(node.children[char])
        return None

    def display(self):
        '''构建字典树'''
        self.display_node(self.root)

trie = Trie()
trie.insert('hello')
trie.insert('world')
trie.insert('nice')
trie.insert('to')
trie.insert('meet')
trie.insert('you')
trie.display()

print
print trie.search('to')
print trie.search('To')