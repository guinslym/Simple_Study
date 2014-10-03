# -*- coding:utf-8 -*-

def quickSort(data):
	n=len(data)
	recQuickSort(data,0,n-1)

def recQuickSort(data,first,last):
	if first>=last:
		return
	else:
		pivot=data[first]
		pos=partitionSeq(data,first,last)
		recQuickSort(data,first,pos-1)
		recQuickSort(data,pos+1,last)

def partitionSeq(data,first,last):
	pivot=data[first]
	left=first+1
	right=last
	while left<=right:
		while left<right and data[left]<pivot:
			left+=1
		while right>=left and data[right]>=pivot:
			right -=1
		if left<right:
			tmp=data[left]
			data[left]=data[right]
			data[right]=tmp

	if right !=first:
		data[first]=data[right]
		data[right]=pivot
	print data
	return right

print quickSort([2,34,22,12,56,6,3,45,25])