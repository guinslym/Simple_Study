import difflib

text_1="This is a test of Python"
text_2="That is a test of Javascript"
d=difflib.Differ()
diff=d.compare(text_1,text_2)
print "".join(diff)
