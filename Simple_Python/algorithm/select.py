# -*- coding:utf-8 -*-

def selectSort(data):
	'''
	本函数主要利用的是选择排序法,例如:
	在数组[10,5,12,8,41,14,3,54,31,56,2,-1]中,
	首先将最小的-1找出来放在一边。
	然后对剩下的数组再次进行上述操作,依次取到2,5,10,...54。
	直到所有元素都排序了一边,返回原来的数组。
	而程序实现主要分为以下3个步骤:
	1. 我们将数组中最小的元素查找出来,只需操作数组长度-1即可实现找出它来。我们假设在第x位找到了最小值。
	2. 在剩下的数组中将下1个最小的元素查找出来,只需操作(上1次基础上+1~数组的长度)次即可实现。
	将small的索引改为j,为后面交换做准备。
	3. 对数值进行交换,首尾2个索引不相等的情况下,对是最小值按索引的位置顺序进行数值位置上的交换。
	'''
	n=len(data)
	num=1
	for x in range(0,n-1):
		small=x
		for j in range(x+1,n):
			if data[j]<data[small]:
				small=j
		

		if small !=x:
			tmp=data[x]
			data[x]=data[small]
			data[small]=tmp
		
		num+=1
		print data

	print 'Has Run',num,'times'
	return data

print selectSort([10,5,12,8,41,14,3,54,31,56,2,-1])