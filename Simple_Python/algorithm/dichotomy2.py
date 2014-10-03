#coding:utf-8
import math

def bsearch(data,value,start=0):
	'''
	本函数主要是利用二分法来实现查找数组中元素的索引,
	主要是利用目标值与中间值进行比较来实现的查找工作。
	当数组中的数值与目标值相同时,将其返回出去。
	而当数组中的数组小于目标值时,将所有的范围缩小为中间值到数组长度。
	由于数组中只能传入整数,需要使用int函数强制转换
	'''
	length=len(data)
	middle=int(math.floor((start+length)/2))
	num=0
	while start < length-1:
		if data[middle]==value:
			print 'Has Found',num,'times'
			return middle +1
		elif data[middle] < value:
			start = middle
			middle=int(math.floor((start+length)/2))
		else:
			length=middle
			middle=int(math.floor((start+length)/2))
		num +=1
	
	return False

print bsearch(range(-1,100),1)