列表.md
1个列表代表1个0个或多个任何对象元素的序列。列表与容器重要的区别在于2个或更多的列表能共享部分的结构。另外,你无须复制整个列表就可以插入或删除1个列表中的元素。  
##Cons cell##
列表在Lisp中并不是原始数据类型,它们是由cons cell构建起来的。1个cons cell是1个数据对象,代表1个排序的对。它有2个槽,每个槽都有保存或指向一些Lisp对象。1个槽是CAR,另1个槽为CDR。  
1个列表是1系列的cons cell连接在一起,所以每个cell都指向下1个。本人感觉有点像链表。  
因为大部分cons cell被用于部分列表,我们将任何由cons cell组成的结构称为列表结构。
##指示列表关系##
下面函数主要测试1个Lisp对象是不是1个原子,1个cons cell或1个列表,以及用于区分对象nil.

1. consp函数,当1个对象是1个cons cell时返回t.nil不是1个cons cell,虽然它是1个列表。
2. atom函数,当1个对象是1个原子时返回t.符号nil是1个原子也是1个列表。`(atom OBJECT) == (not (consp OBJECT))`。
3. listp函数,当1个对象是cons cell或nil时返回t.
4. nlisp函数,取值与listp函数相反。` (listp OBJECT) == (not (nlistp OBJECT))`。
5. null函数,如果对象是nil将返回t.

```
(consp nil)                  =>nil
(consp (list 'a 'b 'c))      =>T
(consp '(a b c)              =>T
(listp '(1))                 => t
(listp '())                  => t
```

##访问列表元素##

1. car函数,返回第1个槽cons cell的值。
2. cdr函数,返回第2个槽cons cell的值。
3. car-safe函数,让你可以读取CAR中其他数据类型,避免发生错误。其等价于:
```
(car-safe OBJECT)
          ==
          (let ((x OBJECT))
            (if (consp x)
                (car x)
              nil))
```
4. pop宏,这个宏可以提供简便的方法将列表的CAR的值1次性取出。它等价于`(prog1 (car listname) (setq listname (cdr listname)))`。
5. nth函数,返回元素的第nth元素。元素以数字0开始。
6. nthcdr函数,返回列表的第nth个CDR。
7. last,返回列表的最后关联的。
8. safe-length函数,返回列表的长度。
9. caar函数,等价于`(car (car CONS-CELL))`.
10. cadr函数,等价于`(car (cdr CONS-CELL))`或`(nth 1 CONS-CELL)`。
11. cddr函数,等价于`(cdr (cdr CONS-CELL))`或`(nthcdr 2 CONS-CELL)`。
12. butlast函数,返回列表最后的元素或最后n个元素。
13. nbutlast函数,是butlast直接修改cdr元素的版本。

```
(car '(a b c))       => a
(car '())            => nil
 x                   => (a b c)
(pop x)              => a
x                    => (b c)
 (nth 2 '(1 2 3 4))
   => 3
(nth 10 '(1 2 3 4))
   => nil
(nth -3 '(1 2 3 4))
   => 1
(nth n x) == (car (nthcdr n x))
 (nthcdr 1 '(1 2 3 4))
   => (2 3 4)
(nthcdr 10 '(1 2 3 4))
   => nil
(nthcdr -3 '(1 2 3 4))
   => (1 2 3 4)
```

##生成cons cell和列表##
cons是1个过程的列表创建函数。cons是1个很基础的创建列表结构的函数,通常用于添加单个元素到列表的前面。  
list函数创建1个对象列表作为它的元素。  
make-list函数创建1个指定长度元素的列表,每个元素都是1个对象。

```
 (cons 1 '(2))
   => (1 2)
(cons 1 '())
   => (1)
(cons 1 2)
   => (1 . 2)

(list 1 2 3 4 5)
   => (1 2 3 4 5)
(list 1 2 '(3 4 5) 'foo)
   => (1 2 (3 4 5) foo)
(list)
   => nil

(make-list 3 'pigs)
   => (pigs pigs pigs)
(make-list 0 'pigs)
   => nil
(setq l (make-list 3 '(a b)))
   => ((a b) (a b) (a b))
(eq (car l) (cadr l))
   => t
```