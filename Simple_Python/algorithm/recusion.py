# coding:utf-8
def fact(n):
	if n<0:
		return 0
	elif n==0 | n==1:
		return n
	else:
		return n*fact(n-1)

print(fact(4)) #24
print(fact(1)) #1

# 1+2+3+4=(1+4)*2
# 10!=(1+10)*5
# 11!=(1+11)*6