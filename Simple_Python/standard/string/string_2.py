import string
s="the quick brown fox jumped over the lazy dog"
rep=string.maketrans("abcqrhgd","37290145")
print s
print "-"*40
print s.translate(rep)