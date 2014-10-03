import Cookie
C=Cookie.SimpleCookie()
C["fig"]="newton"
C["sugar"]="wafer"
print C
print "-"*30
C["rocky"]="road"
C["rocky"]["path"]="/Cookie"
print C.output(header="Cookie:")
print "-"*30
print C.output(attrs=[],header="Cookie:")
print "-"*30
C.load("chips=ahoy; vienna=finger") 
print C.output()
print C["chips"].value