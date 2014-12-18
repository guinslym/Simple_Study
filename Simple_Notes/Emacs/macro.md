宏.md
宏能让你定义新的控制结构和其他语言特性。  
1和宏被定义成类似1个函数,不过它不是告诉我们如何计算1个值,而是告诉我们如何计算另1个Lisp表达式并返回计算的值。我们称这个表达式为扩展宏。

   Macros can do this because they operate on the unevaluated
expressions for the arguments, not on the argument values as functions
do.  They can therefore construct an expansion containing these
argument expressions or parts of them.
你可以使用宏取做任何普通函数可以做的事情。
