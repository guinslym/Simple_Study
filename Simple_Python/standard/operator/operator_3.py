from operator import *
class MyObj(object):
	"""docstring for MyObj"""
	def __init__(self, arg):
		super(MyObj, self).__init__()
		self.arg = arg
	def __repr__(self):
		return "MyObj(%s)"%self.arg

list=[MyObj(i) for i in xrange(5)]
print "object :",list

g=attrgetter("arg")
vals=[g(i) for i in list]
print "arg values:",vals

list.reverse()
print "reverse:",list
print "sorted:",sorted(list,key=g)
