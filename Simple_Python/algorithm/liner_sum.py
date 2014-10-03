# -*- coding:utf8 -*-
def linear_sum(S,n):
	'''
	本函数主要是线性递归,利用逐次加上上1个元素然后最终返回结果。
	'''
	if n==0:
		return 0
	else:
		return linear_sum(S,n-1)+S[n-1]

print linear_sum([4,3,6,2,8],5)