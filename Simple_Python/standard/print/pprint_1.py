#coding:utf8
from pprint import pprint

data=[(1,{"a":"1","b":"2","c":"3"}),
      (2, {"d":"4","e":"5","f":"6","g":"7",
          "h":"8","i":"9"
          }),
      (3, {"d":"4","e":"5","f":"6","g":"7",
          "h":"8","i":"9"
          })
          ]
print "普通打印print:"
print data
print "-"*20

print u"美化版pprint"
pprint(data)
