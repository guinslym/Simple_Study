##调用函数##
PostgreSQL允许通过positional或named符号来调用带有已命名参数的函数。
对于带有大量参数的函数来说，命名符号是非常有用的，因为它使参数和实际参数之间的关联更加明确和可靠。  
对位置符号，函数调用时，它的参数值的顺序与在函数声明时的顺序相同。 对命名符号，参数名与函数的参数名相匹配，并且可以以任意顺序书写。

对任意一个符号，函数声明时带有缺省值的参数，在调用时完全不需要写上。
对命名符号，因为参数的任意组合可以省略，所以刚才的方法会非常有用，而位置符号只能从右到左省略。

PostgreSQL同样支持位置与命名符号结合的mixed符号. 在这种情况下，先写位置符号，再写命名符号。

下例说明了这三种符号的使用，首先如下定义函数：

```
CREATE FUNCTION concat_lower_or_upper(a text, b text, uppercase boolean DEFAULT false)
RETURNS text
AS
$$
 SELECT CASE
        WHEN $3 THEN UPPER($1 || ' ' || $2)
        ELSE LOWER($1 || ' ' || $2)
        END;
$$
LANGUAGE SQL IMMUTABLE STRICT;
```

`concat_lower_or_upper`函数有两个强制参数，a和b，以及一个可选参数uppercase（ 缺省false）。  
a和b在输入时会被串联，然后根据uppercase参数来决定使用大写或小写。 相比之下，剩下的函数定义就不重要了。

###使用positional符号###

在PostgreSQL中，位置符号是传统的，将参数传递给函数的机制。如下例：

```
SELECT concat_lower_or_upper('Hello', 'World', true);
```

<pre>
 concat_lower_or_upper
-----------------------
 HELLO WORLD
(1 row)
</pre>

所有的参数顺序声明。由于uppercase参数声明为true，所以输出结果为大写。 另一个示例：

```
SELECT concat_lower_or_upper('Hello', 'World');
```

<pre>
 concat_lower_or_upper
-----------------------
 hello world
(1 row)
</pre>

此例中，uppercase参数被忽略，因此使用缺省值false，这样，输出结果就为小写。 在位置符号中，只要参数带有缺省值，那么可以从右到左忽略。

###使用named符号###

对命名符号，每个参数的名子用:=进行声明，以与参数表达式分开。如：

```
SELECT concat_lower_or_upper(a := 'Hello', b := 'World');
```

<pre>
 concat_lower_or_upper
-----------------------
 hello world
(1 row)
</pre>

同样，uppercase参数被忽略，从而使用缺省值。 使用命名参数的一个好处是，参数可以以任意顺序声明，如：

```
SELECT concat_lower_or_upper(a := 'Hello', b := 'World', uppercase := true);
```

<pre>
 concat_lower_or_upper
-----------------------
 HELLO WORLD
(1 row)
</pre>

```
SELECT concat_lower_or_upper(a := 'Hello', uppercase := true, b := 'World');
```

<pre>
 concat_lower_or_upper
-----------------------
 HELLO WORLD
(1 row)
</pre>

###使用mixed符号###

该符号是位置和命名符号的组合，然而，正如已提到的，命名符号不能在位置符号之前，如：

```
SELECT concat_lower_or_upper('Hello', 'World', uppercase := true);
```

<pre>
 concat_lower_or_upper
-----------------------
 HELLO WORLD
(1 row)
</pre>

在上面所有的查询中，a和b参数被声明为positional型，而uppercase被声明为name型。 那些带有默认值，名或混合符号的复杂的具有许多参数的函数可以极大的节省写进程，并且降低错误几率。
