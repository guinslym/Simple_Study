import collections
def default():
	return "default value"
d=collections.defaultdict(default,foo="bar")
print "d:",d
print "foo=>",d["foo"]
print "bar=>",d["bar"]