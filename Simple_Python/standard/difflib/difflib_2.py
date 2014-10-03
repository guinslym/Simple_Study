import difflib

text_1="This is a test of Python"
text_2="That is a test of Javascript"
diff=difflib.unified_diff(text_1,text_2,lineterm="")
print "".join(diff)
