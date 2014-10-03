import textwrap
data="The textwrap module can be used to format text for output in situation where pretty-printing is desired."
print "No dedent %s" %data
print "-"*40
print textwrap.fill(data,width=20)