# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:00:21 2015

@author: tim
"""

class Error(Exception):
    pass

class SimpleQueue(object):
    """1个简单的队列"""
    def __init__(self,start=[]):
      """初始化队列"""
      self.queue = []
      if start:
          for x in start:
            self.enqueue(x)

    def dequeue(self):
      """出队操作"""
      if not self.queue:
        raise Error('The Queue is Empty')
      else:
        return self.queue.pop(0)

    def enqueue(self,value=None):
      """入队操作"""
      if value is None:
        raise Error('The value can not be empty')
      else:
        self.queue.append(value)

    def isEmpty(self):
      """是否为空队列"""
      if not self.queue:
        return True
      else:
        return False

    def __repr__(self):
      """输出队列的信息"""
      return str(self.queue)