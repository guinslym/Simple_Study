#coding:utf-8
def linear(data,value):
	num=0
	size=len(data)
	while num<size:
		if data[num]==value:
			print '找到了',value,'它的位置是',num
		else:
			print '没有找到'
		num=num+1

if __name__ == '__main__':
	new=[1,2,3,4,5,6,2]
	linear(new,2)