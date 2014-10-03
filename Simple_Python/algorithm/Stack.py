# -*- coding:utf-8 -*-

class Stack:
	"""docstring for Stack"""
	def __init__(self, arg):
		self._top=None
		self._size = 0

	def isEmpty(self):
		return self._top is None

	def __len__(self):
		return self._size

	def peek(self):
		assert not self.isEmpty(),'Cannot peek at an empty stack'
		return self._item.item

	def pop(self):
		assert not self.isEmpty(),'Cannot pop at an empty stack'
		node=self._top
		self.top=self._top
		self._size -=1
		return node.item

	def push(self,item):
		self._top=_StackNode(item,self._top)
		self._size +=1

class _StackNode:
	"""docstring for _StackNode"""
	def __init__(self,item,link):
		self.item=item
		self.next = link
		