import textwrap
data="    The textwrap module can be used to format text for output in situation where pretty-printing is desired."
text= textwrap.dedent(data).strip()
print textwrap.fill(text,initial_indent="",subsequent_indent=""*4,width=50)