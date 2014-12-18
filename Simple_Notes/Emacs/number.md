数字.md
##指示数字##
这1节的函数用于检测数字或特殊类型的数字。函数integerp和floatp能使用任何类型的对象作为参数。但是zerop需要使用1个数字作为参数。

1. (floatp object)函数,指示它的参数是否为1个浮点。
2. (numbererp object)函数,指示它的参数是否为1个数字(整数或浮点数)。
3. (integerp object)函数
4. (natnump object)函数,指示它的参数是0或自然数字。
5. (zerop object)函数,指示它的参数是否为0.其中,`(zerop x)`与`(= x 0)`相等。

```
(floatp 100.0)       =>T
(integerp 100)       =>T
(zerop "1")          =>*** - ZEROP: "11" is not a number
(zerop 1)            =>NIL
(natnump 0)          =>T
(natnump 10)         =>T
```

##数字比较##
测试数字是否相等,你可能会使用"="而不是"eq".如果你使用"eq"来比较它们,你可以测试2个数值是否为同1个对象。相反,"="只会比较2个对象的数值。  
在Emacs Lisp,每个整数值都是1个唯一的Lisp对象。  
因此,"eq"在比较整数时与"="相等。有时,使用"eq"可以很方便的比较1个未知的整数值,因为"eq"在1个未知数值不是1个数字时不会报告1个错误,它可以接受任何类型的参数。  
相反,"="在参数不是数字或标记时将发出错误的信号。因此,编程联系中最好尽可能使用"="来比较整数。  
有些时候,你可以非常有用的使用`equal`来比较数字,它将比较2个数字是否具有相同的数据类型(都是整数或浮点数)和相同的值。相反,`=`只能比较1个浮点数和整数是否相等。

```
(= 1 1.0)   =>T   
(= 1 'a) ;Wrong type argument: number-or-marker-p, a
```

由于浮点数是不精确的,是否比较2个浮点数是否相等是不明智的。但可以通过下面方法进行相等的比较:

```
(defvar fuzz-factor 1.0e-6)
     (defun approx-equal (x y)
       (or (and (= x 0) (= y 0))
           (< (/ (abs (- x y))
                 (max (abs x) (abs y)))
              fuzz-factor)))
```

##数值转换##
将1个整数转换为1个浮点数,可以使用`float`函数。  
有4种方法将1个浮点数转换为1个整数,区别在于舍去范围。它们都接受1个数字参数以及额外的除法(divisor)参数。  
2个参数可能是整数或浮点数。如果除法参数不为空,它们使用相除后再将结果转换为1个整数。如果除法参数为0,Emacs将发出`arith-error`错误信号。

1. truncate函数,返回1个整数,将小数部分向0舍去。
2. floor函数,
3. ceiling函数,返回1个数字,向上舍去。
4. round函数

```
(floor 6 4)         =>1
(floor 6.7)         =>6
(round -1.7)        =>-2
(ceiling 1.7)       =>2
```

##舍取操作##
函数`ffloor`、`fceiling`、`fround`、`dtruncate`将1个浮点数作为参数,并返回1个数值最接近的浮点数。

```
(ffloor 6.7)      =>6.0
(fceiling 6.7)    =>7.0
```

##位操作##
在计算机中,1个整数代表1个二进制数字,1个位的序列(数字只能是1或0).在Emacs Lisp中,位操作只支持整数。  

1. lsh函数,是logical shift的的缩略名,位左移.它与所有Emacs Lisp算数函数一样,不会检查溢出。
2. ash函数是arithmetic shift的简写。它与lsh得到的结果一样,除了在整数和位移动位数都是负数时。区别在于lsh在符号位使用0,而ash留空。
3. logand函数返回逻辑与。
4. logior函数返回逻辑或的结果。
5. logxor函数为位异或。
6. lognot函数为逻辑非。

```
(lsh 5 1)
               => 10
          ;; Decimal 5 becomes decimal 10.
          00000101 => 00001010

(lsh 6 -1)
               => 3
          ;; Decimal 6 becomes decimal 3.位右移
          00000110 => 00000011

(ash -6 -1) => -3
          ;; Decimal -6 becomes decimal -3.
          1111...111010 (30 bits total)
               =>
          1111...111101 (30 bits total)

(lsh -6 -1) => 536870909
          ;; Decimal -6 becomes decimal 536,870,909.
          1111...111010 (30 bits total)
               =>
          0111...111101 (30 bits total)
```

##随机数字##
1个计算机程序无法创建1个真正的随机数字。大多数目标,伪随机数字就足够了。伪随机数字通过种子生成的。  

- (random &optional limit)函数返回1个伪随机整数。  

1. 如果limit参数是正整数。数值将选择非负数并小于limit的值。数值取值范围为变量most-negative-fixnum和most-positive-fixnum之间。
2. 如果limit参数是t,这意味着选择1个根据当前时间和Emacs进程ID数字,新的种子.
3. 如果limit参数是1个字符串,这意味着依据字符串的内容生成1个新的种子。

##指示标记##
你可以测试1个对象是不是1个标记,或者它既是整数或1个标记。  

1. markerp函数,如果对象是1个标记则返回t,否则为nil.需要注意的是,整数不是1个标记,虽然很多函数都可以接受1个整数或标记。
2. integer-or-marker-p函数,如果对象是1个整数或标记则返回t,否则为nil.
3. number-or-marker-p函数,如果对象是1个数字(整数或浮点数)或标记则返回t,否则为nil.
