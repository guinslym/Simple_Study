import decimal
x=decimal.Decimal("3.4")
y=decimal.Decimal("4.5")
a=x*y
b=x/y
print a,b
print "-"*30
decimal.getcontext().prec=3
c=x*y
d=x/y
print c,d
print "-"*30
with decimal.localcontext(decimal.Context(prec=10)):
	e=x*y
	f=x/y
	print e,f