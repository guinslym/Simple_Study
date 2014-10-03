#coding:utf-8
def findIndex(data,value,start=0):
	'''
	本函数主要是利用迭代法来实现对数组中元素的查找工作。
	当查找到目标元素时,将其返回即可。
	因为索引是由0开始的,当查找到目标元素时需要将索引加上1。
	但是不大适合数组长度很大的情况,毕竟工作效率不是很高。
	'''
	length=len(data)
	num=0
	for x in range(start,length):
		if data[x]==value:
			num=x
			print 'Has Found',num,'times'
			return x+1

print findIndex(range(-1,100),99)