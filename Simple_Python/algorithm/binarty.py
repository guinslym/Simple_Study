# -*- coding:utf-8 -*-
def binary(data,value):
	'''
	本函数主要利用的二分法进行查找元素。
	在使用二分法之前必须是1个索引数组,且这个数组必须是有序排列的。
	我们选取这个序列中间那个值进行参考值,由于该值已知道,则此时需要比较的元素是(序列元素个数-1)个。
	将序列分成2个部分,当中间值大于目标值时,在左部分中查找目标值。例如:
	1个序列数值为0~100,其中间值为50,需要与其他元素比较的次数为100-1=99次。  
	而目标值为40,则下一步在0~49中进行查找,因为我们已经知道中间值50,则不需要让50与其他元素对其进行比较。
	当中间值小于目标值时,在右部分中查找目标值。
	如果中间值等于目标值,将其返回,表示已经找到该元素。
	'''
 	hign=len(data)-1
 	low=0
 	num=1
 	while low<=hign:
 		mid=(low+hign)//2
 		if data[mid]==value:
 			print 'Has Run',num,'times'
 			return mid
 		elif data[mid]>value:
 		    hign=mid-1
 		else:
 			low=mid+1
 		num+=1
 	return False

data=[1,0,2,85,45,13,29,3,30]
data.sort()
print data
print binary(data,30)
#[0, 1, 2, 3, 13, 29, 30, 45, 85]
#Has Run 2 times
#6
