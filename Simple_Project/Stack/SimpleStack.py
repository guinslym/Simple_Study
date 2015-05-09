# -*- coding: utf-8 -*-
# /usr/bin/env/python

class SimpleStack(object):
    """"1个简单的堆栈类"""
    def __init__(self,start=[]):
        self.stack = []
        for x in start:
            self.push(x)
        self.reverse()
        
    def push(self,obj):
        """将1个元素推入堆栈"""
        self.stack = [obj]+self.stack
        
    def pop(self):
        """弹出堆栈元素"""
        if not self.stack:
            raise Exception('underflow')
        top,self.stack = self.stack[0],self.stack[1:]
        return top
    
    def top(self):
        """弹出堆栈顶部元素"""
        if not self.stack:
            raise Exception('underflow')
        return self.stack[0]
    
    def isEmpty(self):
        """判断堆栈是否为空"""
        return not self.stack
    
    def __repr__(self):
        """打印实例里调用"""
        return '[Stack:%s]' % self.stack
    
    def __eq__(self,other):
        """2个堆栈是否相同"""
        return self.stack == other.stack
        
    def __len__(self):
        """堆栈的长度"""
        return len(self.stack)
        
    def  __add__(self,other):
        """堆栈相加"""
        return SimpleStack(self.stack+other.stack)
    
    def __mul__(self,reps):
        """堆栈相乘"""
        return SimpleStack(self.stack*reps)
        
    def __getitem__(self,offset):
        """获取堆栈某个索引的数值"""
        return self.stack[offset]
    
    def __getattr__(self,name):
        """获取堆栈的属性"""
        return getattr(self.stack,name)