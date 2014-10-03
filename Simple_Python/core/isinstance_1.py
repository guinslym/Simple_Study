def NumType(num):
	print num,"is",
	if isinstance(num,(int,long,float,complex)):
		print "a number of type:",type(num).__name__
	else:
		print "Not a number at all"

NumType(-69)
NumType(-32L)