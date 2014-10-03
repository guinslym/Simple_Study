import collections
d=collections.deque()
d.extend("abcdegf")
print "Extend:",d
d.append("h")
print "Append:",d
f=collections.deque()
f.extendleft(xrange(8))
print "ExtendLeft:",f
f.appendleft(8)
print "Appendleft:",f