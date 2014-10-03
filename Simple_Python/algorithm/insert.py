# -*- coding:utf-8 -*-

def insert(data):
	'''
	本函数主要利用的是插入排序法来实现对于元素的排序。
	插入排序法是类似打桥牌时的操作,首先得到1张牌,当第2张牌的时候,与第1张牌进行比较。
	第3张牌的时候,与第2张牌比较,如果大于,插入到2的位置。  
	再与第1张牌进行比较,当其大于第1张牌插入到原先1的位置上。依次类推直至排序结束。
	我们先用1个变量value将数组中的元素存储起来,用于后面比较使用。
	再使用1个变量pos将数组中的索引存储起来。
	当元素的后1个元素的值小于前1个元素的值时,将二者的数值进行交换。
	依次按索引逐个进行数值的比较与交换,最终完成序列的排序。
	'''
	length=len(data)
	num=1
	for x in range(1,length):
		value=data[x]
		pos=x
		while pos>0 and value<data[pos-1]:
			data[pos]=data[pos-1]
			pos -=1
			data[pos]=value
			#以下方法与上面结果是一样的，但是效率会慢很多
			#tmp=data[pos-1]
			#data[pos-1]=data[pos]
			#data[pos]=tmp
			#pos -=1
			num +=1
			print data

	print 'Has Run',num,'times'
	return data

print insert([2,45,3,29,14,5,34,67,1])