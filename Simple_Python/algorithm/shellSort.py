# -*- coding:utf-8 -*-

def shellSort(data):
	temp=1
	j,increament=3,temp
	while increament>0:
		for x in range(0,len(data)):
			j=x
			temp=data[x]
			while j>=increament and data[j-increament]>temp:
				data[j]=data[j-increament]
				j -=increament
			data[j]=temp
		if (increament//2)!=0:
			increament /=2
		elif increament==1:
			increament=0
		else:
			increament=1
	return data

print shellSort([2,34,22,12,56,6,3,45,8])