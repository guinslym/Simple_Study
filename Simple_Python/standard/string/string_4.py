import string
template_text="""
Delimiter :%%
Replaced  :%with_underscore
Igonored  :%notunderscored
"""
d={"with_underscore":"replaced",
   "notunderscored":"not replaced"
}
class MyTemple(string.Template):
	delimiter="%"
	idpattern="[a-z]+_[a-z]+"
t=MyTemple(template_text)
print "Modified ID pattern"
print t.safe_substitute(d)