import re
def test_patterns(text,patterns=[]):
	for pattern,desc in patterns:
		print "Pattern %r (%s)\n" % (pattern,desc)
		print "%r" % text
		for match in re.finditer(pattern,text):
			s=match.start()
			e=match.end()
			substr=text[s:e]
			back=text[:s].count("\\")
			prefix="."*(s+back)
			print "%s%r" %(prefix,substr)
		print "End"
	return
if __name__ == '__main__':
	test_patterns("abbaaabbbbaaaa",[("ab","'a' followed by 'b'"),])