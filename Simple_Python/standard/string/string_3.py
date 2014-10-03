import string
values={"var":"foolish"}
t=string.Template("""
	Variable   :$var
	Escape     :$$
	Variable in:${var}iable
	""")
print "Template:",t.substitute(values)
s="""
Variable       :%(var)s
Escape         :%%
Variable in    :%(var)siable
"""
print "INTERPOLATION:",s%values