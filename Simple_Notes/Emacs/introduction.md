##nil和t##
在Emacs Lisp中,nil符号有3种不同的含义:

1. 1个名为nil的符号
2. 逻辑数值false
3. 空列表,0个元素的列表

当我们使用变量时,nil总有1个值是nil。对于Lisp读取器而言,"()"和"nil"是相同的,都是相同的对象nil。  
在本手册中,我们书写()当我们需要强调它代表空列表时,我们书写nil当我们强调它带白哦值false时。下面是1个很好的使用lisp编程的例子:

```
(cons 'foo ())                ;强调是空列表
(setq foo-flag nil)           ;强调是值false
```

在上下文中,当期望是1个真值时,任何不是nil的值都被认识是true的。那么,t就是先前的方式来代表真值true.符号t总有1个值t.  
在Emacs Lisp中,nil和t是能赋值自己的特殊符号。因此你不需要使用引号对它们进行包裹,在程序中将其作为常量使用时。任何尝试修改它们值的结果都会跑出1个setting-constant错误。

```
(setq nil 500)        ;Attempt to set constant symbol: nil
```

##赋值符号记法##
你赋值的1个Lisp表达式称为表。赋值给1个表经常会生成1个结果,1个Lisp对象。在本手册中,它使用"=>"进行指示:

```
(car '(1 2))          =>1
```

当表使用宏调用时,它将Lisp的赋值展开为1个新的表。我们使用“->"来表示展开的结果。  

```
(third '(a b c))         ->(car (cdr (cdr '(a b c))))      =>c
```

有时为了描述1个表与我们生成的另1个表是相同的结果,我们使用"≡"来指示这2张表的相同。

```
(make-sparse-keymap)≡ (list 'keymap)
```

##打印符号记法##
本手册中的例子打印出来的文本使用"-|"来指示,表运算出来的值在后面跟着1个"=>"分割。

```
 (progn (prin1 'foo) (princ "\n") (prin1 'bar))
          -| foo
          -| bar
          => bar
```

##错误信息##
一些信号错误的例子,在echo区正常显示1条消息。我们显示这个错误消息,使用开始为"error-->"的1行。需要注意的是"error-->"不会在echo区显示。

##1个简单函数的描述##
在1个函数描述中,函数名是第1个被描述的,紧接着在同行后面的是参数名。这些名字也经常在描述的主体中。使用,表示参数的值,所有保留的参数列表传递给函数。  
关键字'&optional'在参数列表中表示子序列参数可能会省略,省略的参数默认是nil。在你调用函数时不要写"&optional"。  
关键字'&rest'代表后面可以填入任意数量的参数(必须跟随1个参数名),"&rest"接受单个参数作为它的值。

##1个简单变量例子的描述##
1个变量是能被1个对象绑定或设置的名字。对象绑定的变量称为值,通常我们称变量保存值。虽然,几乎所有的变量用户都可以设置。一般情况,变量和用户选项都能使用1种像函数一样的格式进行描述,除非它们没有参数。  
下面是1个关于"electric-future-map"的描述:
<pre>
 -- Variable: electric-future-map
     The value of this variable is a full keymap used by Electric
     Command Future mode.  The functions in this map allow you to edit
     commands you have not yet thought about executing.
</pre>

用户选项描述也是同样的格式,只是'Variable'替换为'User Option'。

##版本信息##
以下工具提供了使用的Emacs的版本信息:

`(emacs-version)`函数返回1个描述正在运行的Emacs字符串。  
`emacs-build-time`变量指示了Emacs创建的时候,这是1个4位整数的列表。  
`emacs-major-version`变量表示Emacs的主版本,是1个整数。而`emacs-minor-version`表示分支的版本,是1个整数。

