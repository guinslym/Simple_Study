目前为止,本书我们描述1个标识是通过书写它们的名字.不过实际上标识在Common Lisp中是1个复合的对象,这意味这它们有几个部分.概念上,1个标识是5个指针的块,1个指针表示当前的标识(symbol)的名字.其他的将在后面被定义.1个内部的标识FRED看起来是这样的:

"FRED"使用引号标记称为字符串.字符串是字符的序列,它们将在第9章被全面介绍到.现在需要记住字符串是用来存储标识名称.1个标识和它的名称实际上是2个不同的事物.
一些标识,像CONS或+,通常用于命名内建Lisp函数.标识CONS在它函数的单元(function cell)里有1个指针指向1个编译代码对象(compiled code object),用于表示机器语言说明去创建1个新的cons cells.  
当我们书写例如(equal 3 5)的cons cell,我们经常书写标识的名字而不是显示其内部结构:

不过如果我们选择显示更多的细节,在表达式(equal 3 5)看起来像是这样的:

我们能展开1个标识的变量组成部分使用Common Lisp的内建函数像SYMBOL-NAME和SYMBOL-FUNCTION.  
```
CL-USER> (symbol-name 'equal)
"EQUAL"
CL-USER> (symbol-function 'equal)
#<FUNCTION EQUAL>
```
