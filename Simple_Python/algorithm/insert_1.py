# coding:utf-8

def insert(data):
	length=len(data)
	num=1
	for x in range(0,length-1):
		for j in range(x+1,length):
			if data[j]<data[x]:
				tmp=data[j]
				data[j]=data[x]
				data[x]=tmp
				num+=1
				print data
	print 'Has Run',num,'times'
	return data

print insert([2,45,3,29,14,5,34,67,1])