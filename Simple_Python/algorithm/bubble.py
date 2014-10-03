# -*- coding:utf-8 -*-

def bubble(data):
	'''
	本函数主要利用的是冒泡排序来实现对元素的排列。
	第1次迭代是将最大的元素推放至列表的最后,执行的次数为数组的长度-1,
	因为是拿第1个元素与后面1个元素进行比较。
	第2次迭代是将已经交换过的元素再次进行交换操作,实现最终的效果。
	当前1个元素的数值大于后1个元素的数值时进行交换,我们采取1个临时变量来完成这个工作。
	当然也可以采用2个数值相加减来实现交换的工作。例如:
	data[j]=4,data[j+1]=3,则data[j]=data[j]+data[j+1]=7
	data[j+1]=data[j]-data[j+1]=7-3=4
	data[j]=data[j]-data[j+1]=7-4=3
	'''
	n=len(data)
	num=0
	print 'origin',data
	for i in range(0,n-1):
		for j in range(0,n-1):
			if data[j]>data[j+1]:
				tmp=data[j]
				#data[j]=data[j]+data[j+1]
				data[j]=data[j+1]
				#data[j+1]=data[j]-data[j+1]
				data[j+1]=tmp
				#data[j]=data[j]-data[j+1]
				print data
				num+=1
	print 'Has Run',num,'times'
	return data

print bubble([10,5,12,8,41,14,3,54,31,56,98])