import string
import re

class MyTemple(string.Template):
	delimiter='{{'
	pattern=r'''\{\{(?:
		(?P<escaped>\{\{)|
		(?P<named>[_a-z][_a-z0-9]*)\}\}|
        (?P<braced>[_a-z][_a-z0-9]*)\}\}|
        (?P<invalid>)
        )
    '''


t=MyTemple('''
	{{{{
	{{var}})
''')

print "MATCHES:",t.pattern.findall(t.template)
print "SUBSTITUTE:",t.safe_substitute(var='replacement')

