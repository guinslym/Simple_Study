# -*- coding:utf-8 -*-

def mergeSort(data,list):
	'''
	本函数主要实现的是对2个数组的归并排序,其原理如下。
	有2个数组A,B。首先比较的是2个数组的第1项,哪个数值小就插入到新的数组中去。  
	然后较大那个数组中第1项与较小的第2项进行比较,如果数值小于它则插入到数组中去。
	依此类推,最终得到1个排列有序的列表。
	在代码的书写过程中,我们将其分成2部分来进行:
	1. 让2个数组长度都一致进行相同情况下数值的比较,采用计数的方式来控制索引,进而实现错位比较。
	2. 当数组长度1方超出时,此时将2组数组中剩余的元素依次插入到新的数组中去。
	因为此时剩余的数值比另1个数组的最大要大。
	'''
	length=len(data)
	count=len(List)
	newList=[]
	a,b,num=0,0,1
	while a<length and b<count:
		if data[a]<List[b]:
			newList.append(data[a])
			a+=1
		else:
			newList.append(List[b])
			b+=1
		print newList
		num+=1
	
	while a<length:
		newList.append(data[a])
		a+=1
		print newList
		num+=1
	
	while b<count:
		newList.append(List[b])
		b+=1
		print newList
		num+1
	print 'Has Run',num,'times'
	return newList

data=[2,8,15,23,37]
List=[4,6,15,20]
print mergeSort(data,List)