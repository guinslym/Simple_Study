import collections
Person=collections.namedtuple("Person","name age gender")
print "Type of Person:",type(Person)
bob=Person(name="bob",age=30,gender="male")
print "\nRepresentation:",bob
jane=Person(name="Jane",age=29,gender="female")
print "\nField by name:",jane.name
print "\nField by index:"
for p in [bob,jane]:
	print "%s is a %d year old %s" %p