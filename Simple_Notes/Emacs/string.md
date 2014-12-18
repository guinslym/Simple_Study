字符和字符串类型.md
1个字符就是代表单个文本字符的Lisp对象。在Emacs Lisp中,字符是简单的整数。
字符串是1个定长的字符,它是一种称为数组的序列,这意味这它的长度是固定的,一旦被创建就不能被改变。  
因为字符串是数组,因为序列也好,你可以使用普通的数组和序列函数的方法。例如,你可以使用或改变单个的字符通过数组的`aref`和`aset`方法。另外,长度`length`不能被用于计算字符串显示的宽度,取而代之是`string-width`函数。  
在Emacs字符串中有2种文本来表示非ASCII字符,单字节和多字节。
##指示字符串##

1. stringp函数,用于判断1个对象是否为1个字符串。
2. string-or-null-p函数,用于判断1个对象是否为1个字符串或nil.
3. char-or-string-p函数,用于判断1个对象是否为1个字符串或字符

```
(char-or-string-p #o77)       =>T
```

##创建字符串##

1. make-function函数,返回1个指定数量字符的字符串。如果数量为负数,将标记为1个错误。
2. string函数返回包含字符的1个字符串。
3. substring函数,返回1个在开始和结尾范围内的新的字符串.如果范围是负数,索引-1代表最后的那个字符。与Python是一致的。另外,该函数可以接受1个vector作为第1个参数。
4. substring-no-properties函数工作方式与substring函数类似,其返回1个复制后去除所有属性的字符串。
5. concat函数,返回1个传入参数后拼接的新字符串.参数可以是字符串,列表数字或vector数字。如果它没有接受到任何参数将返回1个空字符串。
6. split-string函数根据正则分隔符将字符串拆分成子字符串,返回1个列表。
7. 变量split-string-default-separators,其默认值是"[ \f\t\n\r\v]+".

```
(make-string 5 ?x)         =>"xxxxx"
(make-string 5 #o77)       =>"?????"
(string 98 56 126)         =>"b8~"
(string ?a ?b ?c)          =>"abc"
(substring "abcdefg" 0 3） =>"abc"
(substring "abcdefg" -3 -1)=>"ef"
(substring [a b (c) "d"] 1 3)=>[b (c)]
(concat '(1 2 3 4))        =>"^A^B^C^D"
(concat [1 2 3 4])         =>"^A^B^C^D"
(concat "abc" (list 120 121) [122])   =>"abcxyz"
 (split-string "  two words "
                        split-string-default-separators)
               => ("" "two" "words" "")
(split-string "Soup is good food" "o")
               => ("S" "up is g" "" "d f" "" "d")
```

##修改字符串##

1. store-substring函数,可以修改字符串的部分内容,通过储存对象在开始的索引位置。参数OBJ可以是1个字符或1段字符串。
2. clear-string函数主要用于清除1个包含密码的字符串,它字符化1个单字节字符串并清除它的内容为0.

```
(store-substring "abc" 1 111)        =>"aoc"
(clear-string "abcd")                =>nil
```

##字符或字符串比较##

1. char-equal函数,如果参数是相同的字符则返回t.
2. string=函数,用于如果2个字符串能够匹配,则返回t.
3. string-equal函数的另1个名字是`string=`.
4. string<,用于匹配2个字符串在另1个字符串的字符是否都小于另1个字符串。
5. string-lessp函数的另1个名字是`string<`.

```
(string< "abc" "abd")
   => t
(string< "abd" "abc")
   => nil
(string< "123" "abc")
   => t
```


