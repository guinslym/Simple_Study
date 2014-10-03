#coding:utf-8

def facttail(n,a=1):
	if n<0:
		return 0
	elif n==0:
		return 1
	elif n==1:
		return a
	else:
		return facttail(n-1,n*a)

print facttail(4)