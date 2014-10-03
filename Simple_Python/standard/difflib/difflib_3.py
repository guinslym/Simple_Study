import difflib

text_1=[1,2,3,5,6,4]
text_2=[2,3,4,5,6,1]
print "Initial data:"
print "text1=",text_1
print "text2=",text_2
print "text1==text2",text_1==text_2
diff=difflib.SequenceMatcher(None,text_1,text_2)
for tag,i1,i2,j1,j2 in reversed(diff.get_opcodes()):
	if tag=="delete":
		print "Remove %s from position [%d:%d]"% (text_1[i1:i2],i1,i2)
		del text_1[i1:i2]
	elif tag=="equal":
		print "text_1[%d:%d] and text_2[%d:%d] are the same"%(i1,i2,j1,j2)
	elif tag=="insert":
		print "Insert %s from text_2[%d:%d] into s1 at %d"% (text_2[j1:j2],j1,j2,i1)
		text_1[i1:i2]=text_2[j1:j2]
	elif tag=="replace":
		print "Replace %s from text_1[%d:%d] with %s from text_2[%d:%d] "% (text_1[i1:i2],i1,i2,text_2[j1:j2],j1,j2)
		text_1[i1:i2]=text_2[j1:j2]
	print "text_1=",text_1
print "text_1==text_2",text_1==text_2
