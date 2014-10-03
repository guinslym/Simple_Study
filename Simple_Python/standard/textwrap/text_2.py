import textwrap
data="    The textwrap module can be used to format text for output in situation where pretty-printing is desired."
text= textwrap.dedent(data).strip()
for width in [45,70]:
	print "%d Columns:\n" %width
	print textwrap.fill(text,width=width)