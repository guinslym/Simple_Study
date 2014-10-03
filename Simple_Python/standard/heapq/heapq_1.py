import heapq
data=[1,2,3,5,6,78,23,45]
print "all        :",data
print "3 largest  :",heapq.nlargest(3,data)
print "from sort  :",list(reversed(sorted(data)[-3:])
#print "3 smallest :",heapq.nsmallest(3,data)
#print "from sort  :",sorted(data)[:3]