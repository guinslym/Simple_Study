#coding:utf-8
import math

def recusion(data,value,start=0):
	'''
	本函数是利用递归法来实现对数组中元素的查找工作。
	当数组索引并没有超过数组长度的时候,对数组中的元素进行递归的查找。
	当数组的元素被查找到的时候,将其返回。
	当数组的元素大于目标元素时,将中间数值的索引减一。
	例如数组的长度为100,从0到100,而此时元素值是50,而目标元素值是40,此时将在值0~49之间进行查找。
	当数组的元素小于目标元素时,将中间数值的索引加一。然后再次进入循环,类似二分法缩小了查找的范围。
	例如数组的长度为100,从0到100,而此时元素值是50,而目标元素值是60,此时将在值51~100之间进行查找。
	'''

	length=len(data)
	num=0
	while start < length:
		middle=start+int(math.floor(length-start)/2)
		if data[middle]==value:
			print 'Has Found',num,'times'
			return middle+1
		elif(data[middle] > value):
			length=middle-1
		else:
			start=middle+1

		num +=1
	
	return False

print recusion(range(-1,100),2)