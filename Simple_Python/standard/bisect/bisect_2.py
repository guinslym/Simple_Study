import bisect
import random

random.seed(list)
print "New Pos Contents"
print "-"*30
list=[]
for i in range(1,15):
	r=random.randint(1,100)
	position=bisect.bisect_left(list,r)
	bisect.insort_left(list,r)
	print "%3d %3d"%(r,position),list