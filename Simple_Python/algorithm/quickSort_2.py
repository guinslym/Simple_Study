# -*- coding:utf-8 -*-

def quickSort(seq):
	'''
	本函数将对序列进行快速排序操作,当序列的长度小于等于1时直接返回原序列。
	对于大于1个元素的序列,进行快速排序操作。左部分,参考点,右部分依次等于传入序列后返回的值。
	然后再次将返回的数值再次递归至最后1个元素,并将其按顺序组装后返回。
	'''
	if len(seq)<=1:
		return seq
	lo,pi,hi=partition(seq)
	return quickSort(lo)+[pi]+quickSort(hi)

def partition(seq):
	'''
	本函数主要用于将序列分成2部分将序列的第1个元素作为参考点。
	将小于其数值的为1部分,而大于其数值的为1部分。
	将左部分+参考点+右部分返回,组成1个有序的序列。
	'''
	pi,seq=seq[0],seq[1:]
	lo=[x for x in seq if x<=pi]
	hi=[x for x in seq if x>pi]
	return lo,pi,hi

print quickSort([2,34,22,12,56,6,3,45,18])