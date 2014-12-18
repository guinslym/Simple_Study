Lisp的数据类型.md
1个Lisp对象是Lisp程序操作的1块数据。我们的目标是,1个类型或数据类型就是可能对象的集合。
每个对象至少属于1个类型。相同类型的对象有相同的结构,并且可能经常被用于相同的上下文中。
类型是可以重叠的,1个对象可以属于2个或更多的类型。通常,我们可以询问1个对象是否属于1个单独的类型,而不是对象的类型。
Emacs只创建了一些基础的对象类型。用于构建全部其他类型的称为原始类型,每个对象都属于1个并且只有1个原始类。这些类型包括'integer(整数)'、'float'、'cons'、'symbol'、'string'、'vector'、'hash-table'、'subr'、'byte-code function',外加几个特殊的类型,例如buffer,与编辑有关的类型。
每个原始类都有1个对应的Lisp函数来检查1个对象是否是这些类型的成员。
Lisp不像其他语言,它的对象都是self-typing(自身类型):原始类型的每个对象都是它们自己。例如,1个对象是vector,没有什么会将其当做是number(数字).Lisp知道它是vector而不是number。
在很多语言,程序必须声明每个变量的数据类型,编译器必须知道这些类型。如此的类型声明在Emacs Lisp中不存在。1个Lisp变量可以是任何类型的值,它将在保存时记住它们的所有值,类型。通常,1小部分Emacs变量只能使用明确类型的值。例如:

`DEFVAR_BOOL`类型的变量只能取值`nil`或't'.尝试赋予其他数值都会将设置为`t`。

```
(let ((display-hourglass 5))
       display-hourglass)
          => t
```

`DEFVAR_INT`类型的变量只能取整数值。尝试赋予它们其他值将触发1个错误。
```
 (setq undo-limit 1000.0)
  error--> Wrong type argument: integerp, 1000.0
```

##打印说明和读取语法##
"printed representation"是1个Lisp输出器(函数prin1)为对象生成的输出格式的对象。每个数据对象都有唯一的打印说明。而"read syntax"是1个Lisp读取器(函数read)为对象生成的输入格式的对象。这个就没必要唯一鳄梨,许多对象类型都至少有1种语法。
在许多情况下,1个打印说明的对象也是读入语法的对象。另外,一些类型没有读取语法,它不能使哪些进入的数据对象具有类似Lisp程序常量的意义。这些对象由"#<"的字符组成,以">"结尾的字符串。例如:

```
(current-buffer)
          => #<buffer objects.texi>
```

在其他语言中,1个表达式是文本,它没有其他的表。在Lisp中,1个表达式是原始的Lisp对象,其次是1个读入语法对象的文本。通常不需要强调它的区别,不过你需要在你的脑海中记住,不然有时你会变得很迷惑。
当你交互的运行1个表达式时,Lisp解释器首先读取它的文本说明,创建1个Lisp对象,然后运行这些对象。另外,运行和读取是分开的操作.读取返回读取文本后的Lisp对象。这些对象可能之后不会被运行。

##整数类型##
Emacs Lisp在32位计算机中的整数范围是-536870912到536870911(30位;, -2**29 to 2**29 - 1).Emacs Lisp算术函数不会检验溢出。例如,30位的整数,(1+ 536870911)的结果是-536870912。
整数读入语法是1个(10进制)序列数字,外加额外的标记在开始之前或结尾。Lisp解析器输出的说明永远不会有1个前置"+"或结尾"."。

```
 -1               ; 整数-1.
 1                ; 整数1.
 1.               ; 也是整数1.
 +1               ; 也是整数1.
```

作为1个特殊的异常,如果1个数字序列的整数值太大或太小而不能成为1个合法的整数对象,Lisp读取器将把它读取为1个浮点数。例如,如果整数是30位,`536870912`将被读取为浮点数`536870912.0`.

##浮点数类型##
浮点数类型主要用于科学说明,你可以将1个浮点数想象称1个10进制有理数。其精确度和可能的指数位都是机器级别。Emacs使用C数字类型"double"存储它的数值,使用2进制而不是10进制。
浮点数的输出说明是1个整数点及指数的组合。例如:`1500.0`, `15e2`, `15.0e2`, `1.5e3`,和`.15e4`是浮点数1500的5种写法,它们都是恒等的。

##字符串类型##
Emacs Lisp中的字符串类型与整数一样频繁使用。换句话说,字符串代表它们的字符串编码,例如:字符串`A`代表整数65.
在程序中偶尔使用单独的字符串,不过经常通过`_strings_`进行工作,1个序列组合的字符串。
字符串和缓冲现在被限制在范围0到4194303--22位。编码0到127是ASCII编码; 剩余的是non-ASCII。

###基础字符语法###
字符其实就是整数,1个字符输出说明就是1个整数。通常字母读入读入语法是1个问号标记后跟1个字符。例如,`?A`代表字符`A`,`?B`代表字符`B',`?a`代表字符`a`.

```
?Q => 81
?q => 113
```

你可以对标点字符使用相同的语法,不过最好的方式是添加1个'\'以便Emacs命令编辑Lisp编码时不会弄混。例如,`？\(`用于书写开括号字符。如果字符是`\`,你必须使用第2个`\`去包裹它:`?\\`。

```
?\a => 7                 ; control-g, C-g
?\b => 8                 ; backspace, <BS>, 'C-h'
?\t => 9                 ; tab, <TAB>, C-i'
?\n => 10                ; newline, C-j'
?\v => 11                ; vertical tab, C-k'
?\f => 12                ; formfeed character, C-l'
?\r => 13                ; carriage return, <RET>, C-m'
?\e => 27                ; escape character, <ESC>, C-['
?\s => 32                ; space character, <SPC>
?\\ => 92                ; backslash character, \'
?\d => 127               ; delete character, <DEL>
```

###通用转义语法###
Emacs提供了几种类型的转义语法以便你可以使用特定的非ASCII文本字符。
首先,你可以使用Unicode值,`?\uNNNN`代表Unicode字符`U+NNNN`,当NNNN是4个整数的16进制数字。反斜杠指示子序列字符是1个转义序列,而u指示是1个Unicode转义序列。
对于特殊大于`U+FFFF`的Unicode字符数值有明显的语法区别, `?\U00NNNNNN'代表字符`U+NNNNNN', 使用的是6个数字的16进制字符. Unicode标准只定义了到`U+10FFFF`的字符, 对于高出这个范围的字符,Emacs会抛出1个错误。
其次,你可以使用16进制字符。1个16进制转义是由1个反斜杠,'x'和16进制字符。例如,`?\x41`代表字符`A`.
最后,你可以使用8进制字符。

##符号类型##
1个符号在GNU Emacs Lisp中就是1个有名字的对象。  
1个以冒号开始的符号称为关键字符号,这些符号会自动扮演这常量的角色。  
在Common Lisp中,小写字符与大写字符一样,但是在Emacs Lisp中,大小写字符都是唯一的。  

```
foo                 ; A symbol named `foo'.
FOO                 ; A symbol named `FOO', different from `foo'.
1+                  ; A symbol named `1+'
                    ; (not `+1', which is an integer).
\+1                 ; A symbol named `+1'
                 ;   (not a very readable name).
\(*\ 1\ 2\)         ; A symbol named `(* 1 2)' (a worse name).
+-*/_~!@$%^&=:<>{}  ; A symbol named `+-*/_~!@$%^&=:<>{}'.
                    ; These characters need not be escaped.
```

##序列类型##
Lisp对象的序列代表1个有序元素的集合。在Emacs Lisp中,有列表和数组这2种序列。  
列表是最常用的序列,1个列表能保存任意类型的元素,它的长度能随着元素添加或删除而被轻易的改变。  
数组是定长序列,在未来它们将被拆分为字符串,容器(vector),字符表和布尔容器。容器可以存储任意类型的元素,虽然字符串元素必须是字符,bool-vector元素必须是t或nil.

##cons cell(单元)和列表类型##
1个cons cell是1个由2个槽(slots)组成的对象,称为CAR槽和CDR槽。每个槽能保存任意Lisp对象。  
1个列表就是1系列的cons cell连接在一起,其下1个元素是CDR槽或空列表。  
对于1个不是cons cell的对象,我们称之为原子(atom).  

```
 (A 2 "A")            ; A list of three elements.3个元素的列表
 ()                   ; A list of no elements (the empty list).
 nil                  ; A list of no elements (the empty list).
 ("A ()")             ; A list of one element: the string `"A ()"'.
 (A ())               ; A list of two elements: `A' and the empty list.
 (A nil)              ; Equivalent to the previous.与上面一样
 ((A B C))            ; A list of one element,1个元素的列表
                      ;(which is a list of three elements).
```

###点号说明###
点号说明是1种用于cons cell通用的语法,清楚的表示CAR和CDR。在这种语法中,`(A . B)`代表1个CAR是对象A而CDR是对象B的cons cell。  
点号说明比列表语法更通用,因为CDR不能是1个列表。  
在点号说明中,列表`(1 2 3)`将被写成`(1 . (2 . (3 . nil)))`.当我们打印列表时,点号说明只有在cons cell的CDR不是1个列表时才被使用。  
下面是1个使用盒子模型的例子来图解点号说明,这个例子显示了`(rose . violet)`。  

         --- ---
        |   |   |--> violet
         --- ---
          |
          |
           --> rose

你可以点号说明与列表说明进行组合来方便的表示1个cons cell的链条,在最后的CDR后面添加1个非nil。你可以在列表的最后1个元素后写上1个点号,紧接着是最后的cons cell的CDR。例如,`(rose violet . buttercup)`等价于`(rose . (violet . buttercup))`.这个对象看起来是这样的:


         --- ---      --- ---
        |   |   |--> |   |   |--> buttercup
         --- ---      --- ---
          |            |
          |            |
           --> rose     --> violet

列表`(rose violet)`等价于`(rose . (violet))`,它看起来是这样的:

         --- ---      --- ---
        |   |   |--> |   |   |--> nil
         --- ---      --- ---
          |            |
          |            |
           --> rose     --> violet

类似的,3个元素的列表`(rose violet buttercup)`等价于`(rose . (violet . (buttercup)))`。它看起来是这样的:

         --- ---      --- ---      --- ---
        |   |   |--> |   |   |--> |   |   |--> nil
         --- ---      --- ---      --- ---
          |            |            |
          |            |            |
           --> rose     --> violet   --> buttercup

###关联列表类型###
1个关联列表类型或alist是1个元素都是cons cell特殊结构的列表。在每个元素中,CAR被认为是键名(key),而CDR被认为是关联的值(associated value). 关联列表经常像栈一样被使用,它可以轻易的在在列表的头部添加或删除关联。例如:

```
 (setq alist-of-colors
       '((rose . red) (lily . white) (buttercup . yellow)))
```

设置变量`alist-of-colors`为1个3个元素的alist.在第1个元素中,`rose`是键名而`red`是值。

##数组类型##
1个数组是由任意数量的槽组成的,用于保存或引用其他Lisp对象,并为其安排1个连续的块内存。

##容器类型##
容器是任何类型的1维数组。容器的打印语法是由1个左方括号,元素和右括号组成。这也是读取的语法。

```
 [1 "two" (three)]      ; A vector of three elements.
          => [1 "two" (three)]
```

##宏类型##
1个Lisp宏是1个用户定义的结构用以扩展Lisp语言。它代表1个非常类似函数的对象,但是带有不同的语义传递参数。  
1个Lisp宏有1个第1个元素是macro符号而CDR是函数对象的列表,包括lambda符号。  
Lisp宏对象经常使用内建`defmacro`函数进行定义,不过任何以macro开始的列表都是1个宏。

##原始函数类型##
1个原始函数是1个Lisp回调函数,但是是使用C语言编写的。原始函数也称为`subrs`或内建函数。单词subr继承于subroutine。许多原始函数在它们调用时运行它们所有的参数。不能运行所有它们参数的称为`special form`。  
原始函数没有读取语法和输出subroutine名的哈希标记。

```
(symbol-function 'car)          ; Access the function cell
                                     ;   of the symbol.
          => #<subr car>
 (subrp (symbol-function 'car))  ; Is this a primitive function?
      => t                       ; Yes.
```