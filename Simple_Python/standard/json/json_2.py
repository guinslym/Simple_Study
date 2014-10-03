import json
j=json.dumps(
	[1,2,3,{"4":"hello","5":"world"}],
	sort_keys=True,
	indent=4,
	separators=(',',':')
	)
print j