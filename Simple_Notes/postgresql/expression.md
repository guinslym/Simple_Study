值表达式用在各种语法环境中，比如在SELECT命令的 目标列表中，在INSERT或者UPDATE中用作新的列值， 或者在许多命令的搜索条件中使用。  
我们有时候把值表达式 的结果叫做scalar(数量)，以便与一个表表达式的结果相区别(是一个表)。因此值表达式也叫做scalar expressions(或简称 expressions)。  
表达式语法允许对来自基本部分的数值进行算术、逻辑、集合、和其它运算。

值表达式是下列内容之一：

- 一个常量或者字面值
- 一个字段引用
- 一个位置参数引用(在函数声明体中或预编写的语句中)
- 一个下标表达式
- 一个字段选择表达式
- 一个操作符调用
- 一个函数调用
- 一个聚集表达式
- 窗口函数调用
- 一个类型转换
- 一个标量子查询
- 一个数组构造器
- 一个行构造器

一个在圆括弧里面的值表达式(可用于子表达式分组和覆盖优先级)。

除了这个列表以外，还有许多构造可以归类为表达式，但是不遵循任何通用的语法规则。它们通常有函数或操作符的语义。一个例子是IS NULL子句。

##子段引用##

子段可以以下述格式被引用：

correlation.columnname
correlation(关联)是一个表的名字(可能有模式修饰)，或者是用FROM子句这样的方法定义的表的别名， 而其它相关的名字可以用于任意SQL语句中)。
如果在当前查询所使用的所有表中，该字段名字是唯一的，那么这个相关名字和分隔用的点就可以省略。  
例如,表weather下的字段city，表示为weather.city。

##位置参数##

位置参数引用用于标识从外部给SQL语句的参数。参数用于SQL函数定义语句和预编写的查询。  
有些客户端库还支持在SQL命令字符串外边声明数据值，这种情况下参数用于引用SQL字符串行外的数据。一个参数的形式如下：

<pre>
$number
</pre>

比如下面这个dept函数的定义

```
CREATE FUNCTION dept(text) RETURNS dept
    AS $$ SELECT * FROM dept WHERE name = $1 $$
    LANGUAGE SQL;
```

在函数被调用的时候这里的`$1`将引用第一个参数。

##下标##

如果一个表达式生成一个数组类型的数值，那么我们可以通过下面这样的 表达式来提取数组中的元素

- expression[subscript]

如果是多个相邻的元素(an "array slice")可以用下面的方法抽取

- expression[lower_subscript:upper_subscript]

每个subscript自己都是一个表达式， 它必须生成一个整数值。

通常，数组expression必须用圆括弧包围， 但如果只是一个子段引用或者一个位置参数，那么圆括弧可以省略。同样， 如果源数组是多维的，那么多个下标可以连接在一起。比如：

```
mytable.arraycolumn[4]
mytable.two_d_column[17][34]
$1[10:42]
(arrayfunction(a,b))[42]
```

最后一个例子里的圆括弧是必须的。参阅Section 8.14 获取有关数组的更多信息。

##子段选择##

如果一个表达式生成一个复合类型(行类型)，那么用下面的方法可以抽取一个指定的子段

- expression.fieldname

通常，行expression必须用圆括弧包围， 但是如果要选取的表达式只是一个表引用或者位置参数，可以省略圆括弧。 比如

```
mytable.mycolumn
$1.somecolumn
(rowfunction(a,b)).col3
```

因此，一个全称的子段引用实际上只是一个子段选择语法的特例。

一个重要的特殊情形是提取的表列是一个复合型的子段：

<pre>
(compositecol).somefield
(mytable.compositecol).somefield
</pre>

在这里，括号是必须的，用来指出compositecol是列名而不是表名， mytable是表名而不是模式名。

##操作符调用##

操作符调用有三种语法：

<pre>
expression operator expression (双目中缀操作符)
operator expression (单目前缀操作符)
expression operator (单目后缀操作符)
</pre>

这里的operator记号遵循节Section 4.1.3的语法规则， 或者是记号AND,OR,NOT之一，或者是一个被修饰的操作符名
OPERATOR(schema.operatorname).
具体存在哪个操作符以及它们是单目还是双目取决于系统或用户定义了什么操作符。

##函数调用##

函数调用的语法是合法函数名(可能有模式名修饰)后面跟着包含参数列表的圆括弧：

<pre>
function_name ([expression [, expression ... ]] )
</pre>

比如，下面的代码计算2的平方根：

- sqrt(2)

内置函数的列表在章Chapter 9里，其它函数可由用户添加。

可选的可附加名子的参数，参阅Section 4.3。

##聚集表达式##

一个aggregate expression代表一个聚集 函数对查询选出的行的处理。  
一个聚集函数把多个输入缩减为 一个输出值，比如给输入求和或求平均。一个聚集表达式的语法是 下列之一：

<pre>
aggregate_name (expression [ , ... ] [ order_by_clause ] )
aggregate_name (ALL expression [ , ... ] [ order_by_clause ] )
aggregate_name (DISTINCT expression [ , ... ] [ order_by_clause ] )
aggregate_name ( * )
</pre>

这里的aggregate_name是 前面定义的聚集(可能是带有模式的全称)， 而expression是一个本身不包含聚集表达式或窗口调用函数的任意值表达式。  
order_by_clause是ORDER BY子句的一个选项，下面会有描述。

第一种形式的聚集表达式为为每个输入行调用聚集。 第二种形式与第一种等价(因为ALL是缺省值)。 第三种形式为所有输入行中所有唯一的非NULL值调用聚集。 最后一种形式调用一次聚集为每个输入行调用一次聚集， 因为没有声明特定的输入值。通常它只用于count(*)聚集函数

大多数的聚集函数在输入时忽略了NULL，因此在一个或多个yield类型表达式中的行中的NULL被省略。  
对所有的内置聚集函数而言，这样做是可以的，除非另行定义。

比如，count(*)生成输入行的总数；count(f1)生成f1不为NULL的输入行数： 因为count忽略空值;count(distinct f1)生 成f1唯一且非NULL的行数。

一般情况下，输入行会以非特定顺序放入到聚集函数中，在许多情况下，这样做是没有影响的；无论以什么顺序输入，min输出相同的结果。
然而，一些聚集函数（如`array_agg`和`string_agg`）并非如此。 当使用这种聚集函数时，可以用order_by_clause选项指定输入的顺序。  
除了它的表达式仅仅只是表达式，不能输出列名或列数之外，order_by_clause与ORDER BY查询子句有相同的语法结构， 在Section 7.5中有描述，如：

```
SELECT array_agg(a ORDER BY b DESC) FROM table;
```

在处理多参数聚集函数时需要注意，ORDER BY子句得再所有的聚集函数之后，如：

```
SELECT string_agg(a, ',' ORDER BY a) FROM table;
```

而不是:

```
SELECT string_agg(a ORDER BY a, ',') FROM table;  -- incorrect
```

后者在语法上是有效的，但它表示的是，通过两个ORDER BY关键子的单参数的聚集函数的调用（第二个是无用的，因为它是一个常量）。

如果`order_by_clause`中声明了DISTINCT，那么所有的ORDER BY表达式必须 匹配常用的聚集参数，也就是说，不能对没有包含在DISTINCT列表中的表达式进行排序。

Note: PostgreSQL扩展可以在一个聚集函数中声明DISTINCT和ORDER BY。

预定义的聚集函数在节Section 9.18里描述。 其它聚集函数可以由用户增加。

一个聚集表达式只能在SELECT命令的结果列表或者HAVING子句里出现。禁止在其它子句里出现(比如WHERE子句)， 因为这些子句逻辑上在生成聚集结果之前计算。

如果一个聚集表达式出现在一个子查询里(参阅节Section 4.2.10和Section 9.20)， 聚集通常是在子查询中进行计算。  
但是如果聚集的参数只包含外层查询的变量则例外：这个聚集会属于离他最近的外层查询，并且在该查询上进行计算。  
该聚集表达式整体上属于它出现的子查询对外层查询的引用，其作用相当于 子查询每一次计算中的一个常量。  
前述限制(聚集表达式只能出现在结果列 或者HAVING子句中)只适用于聚集所属的查询层。

##窗口调用函数##

通过查询筛选出的行的某些部分，窗口调用函数实现了类似于聚集函数的功能。
不同的是，窗口调用函数不需要将查询结果打包成一行输出，在查询输出中，每一行都是分开的。  
然而，窗口调用函数可以扫描所有的行，根据窗口调用函数的分组规范(PARTITION BY列)，这些行可能会是当前行所在组的一部分。
一个窗口调用函数的语法如下：

<pre>
function_name ([expression [, expression ... ]]) OVER ( window_definition )
function_name ([expression [, expression ... ]]) OVER window_name
function_name ( * ) OVER ( window_definition )
function_name ( * ) OVER window_name
</pre>

window_definition具有如下语法：

<pre>
[ existing_window_name ]
[ PARTITION BY expression [, ...] ]
[ ORDER BY expression [ ASC | DESC | USING operator ] [ NULLS { FIRST | LAST } ] [, ...] ]
[ frame_clause ]
</pre>

同时，选项frame_clause可以是：

<pre>
[ RANGE | ROWS ] frame_start
[ RANGE | ROWS ] BETWEEN frame_start AND frame_end
</pre>

frame_start and frame_end可以是：

<pre>
UNBOUNDED PRECEDING
value PRECEDING
CURRENT ROW
value FOLLOWING
UNBOUNDED FOLLOWING
</pre>

在这里，expression表示的是任何自己不含窗口调用函数的值表达式。 PARTITION BY和ORDER BY列.  
本质上，与所有查询中的GROUP BY和ORDER BY具有相同的语法或语义， 除了它们的表达式只能作为表达式不能作为输出列的名子或数。
window_name引用的是查询语句中WINDOW子句定义的命名窗口规范。
命名窗口规范通常只是用OVER window_name来引用，但它也可以在括号里写一个窗口名，并且 可以有选择的使用排序和/或结构子句（如果应用这些子句的话，那么被引用的窗口必须不能有这些子句）。 后者语法遵循相同的规则（修改WINDOW子句中已有的窗口名）。

对这些窗口函数（在这个框架而不是整个分区上的），frame_clause指定构成window frame的行。
如果frame_end将它的缺省值省略为 CURRENT ROW，会有如下限制： frame_start不能为UNBOUNDED FOLLOWING，frame_end不能为UNBOUNDED PRECEDING，并且 相比frame_start，在上述列表中，frame_end选项不能出现的早。
例如：不允许RANGE BETWEEN CURRENT ROW AND valuePRECEDING。 默认的帧选项是RANGE UNBOUNDED PRECEDING，该选项与RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW相同；
它将帧设置为允许所有分区中的行通过ORDER BY中最后出现的当前行启动（如果没有ORDER BY，那么就是所有行）。
一般情况下，UNBOUNDED PRECEDING意味着帧从分区中的第一行启动，同样类似的UNBOUNDED FOLLOWING表示帧以分区中的最后一行结束 （不管RANGE或ROWS模式）。
ROWS模式中，CURRENT ROW表示帧以当前行启动或结束； 但是在RANGE模式中是以ORDER BY中第一次出现的行启动，最后一次出现的行结束。  
valuePRECEDING和valueFOLLOWING目前只允许ROWS模式。 这也就意味着，帧从当前行之前或之后的许多行启动或结束。  
value必须是整型表达式，而不能包含变量，聚集函数，或者窗口函数。 值不能为空或负，但可以是零，表示选择当前行本身。

其他窗口函数，用户可以自己添加。同样，任意内置或用户自定义聚集函数可以在窗口函数中使用。

使用*的语法可以用来调用参数的聚集函数为窗口函数，如`count(*) OVER (PARTITION BY x ORDER BY y)`。  
`*`通常不用于非聚集的窗口函数。与通常的聚集函数不同，聚集窗口函数不允许在 函数参数列中使用DISTINCT或ORDER BY。

窗口调用函数只能在SELECT列，或ORDER BY子句中使用。

##类型转换##

一个类型转换声明一个从一种数据类型到另外一种数据类型的转换。PostgreSQL接受两种等效的类型转换语法：

<pre>
CAST ( expression AS type )
expression::type
</pre>

CAST语法遵循SQL标准：::语法是PostgreSQL历史用法。

如果对一个已知类型的值表达式应用转换，它代表一个运行时类型转换。 只有在已经定义了合适的类型转换操作的情况下，该转换才能成功。
一个应用于字符串文本的 转换表示给该字符串文本的值赋予一个初始类型，因此它对于任何类型 都会成功(如果字符串文本的内容符合该数据类型的输入语法)。

如果一个值表达式的值对某类型而言不存在混淆的情况，那么我们可以省略明确的类型转换(比如，在给一个表子段赋值的时候)，而由系统自动执行类 型转换。  
不过，自动转换只适用于那些系统表中标记着"OK to apply implicitly"的转换函数。  
其它转换函数必须用明确的转换语法调用。这些限制是为了避免一些怪异的转换被自动的应用。

我们也可以用函数风格的语法声明一个类型转换：

<pre>
typename ( expression )
</pre>

不过，这个方法只能用于那些类型名同时也是有效函数名的类型。 比如，double precision就不能这么用。 同样，interval,time和timestamp如果加了双引号也只能这么用， 因为存在语法冲突。因此，函数风格的类型转换会导致不一致，所以应该避免这么使用。

Note: 函数样语法实际上就是一个函数调用。如果使用两种标准转换语法做运行时转换，那么它将在内部调用一个已注册的函数执行转换。  
通常， 这种转换函数和它们的输出类型同名，但是可以移植的程序不能依赖这一点。 详情请参阅CREATE CAST.

## 标量子查询##

一个标量子查询是一个放在圆括弧里只返回一行一列的普通SELECT查询.  
该SELECT将被执行，而其返回值将在周围的值表达式中使用。  
把一个返回超过一行或者超过一列的查询用做标量查询是错误的。不过，子查询不返回行则不算错误(标量结果被认为是 NULL)。  
子查询可以引用外围查询的变量， 这些变量在每次子查询中当做常量使用。

比如，下面的查询找出每个州中的最大人口数量的城市：

```
SELECT name, (SELECT max(pop) FROM cities WHERE cities.state = states.name)
    FROM states;
```

##数组构造器##

一个数组构造器是一个表达式，它从自身成员元素上构造一个数组值。  
一个简单的数组构造器由关键子ARRAY,一个左方括弧[,一个或多个表示数组元素值的表达式(用逗号分隔),一个右方括弧]组成。 比如:

```
SELECT ARRAY[1,2,3+4];
```

<pre>
  array
---------
 {1,2,7}
(1 row)
</pre>

数组元素类型是常见的表达式成员类型，决定了对UNION或CASE结构使用相同的规则（可查阅Section 10.5）。 你可以通过将数据结构构造成需要的类型来对此重写，如：

```
SELECT ARRAY[1,2,22.7]::integer[];
```

<pre>
  array
----------
 {1,2,23}
(1 row)
</pre>

这样做与将每个表达式逐个构造成数据元素类型具有相同效果。 更多信息可参阅Section 4.2.9。

多维数组值可以通过嵌套数组构造器的方法来制作。内层构造器中的ARRAY关键子可以省略。比如，下面的两句生成同样的结果：

```
SELECT ARRAY[ARRAY[1,2], ARRAY[3,4]];
```

<pre>
     array
---------------
 {{1,2},{3,4}}
(1 row)

SELECT ARRAY[[1,2],[3,4]];
     array
---------------
 {{1,2},{3,4}}
(1 row)
</pre>

因为多维数组必须是方形，所以同层的内层构造器必须生成同维的子数组。 任何应用到外ARRAY构造上的构造器自动将其传到所有的内构造上。

多维数组构造器元素可以是任何生成合适数组的东西，而不仅仅是一个子ARRAY构造。比如：

```
CREATE TABLE arr(f1 int[], f2 int[]);
INSERT INTO arr VALUES (ARRAY[[1,2],[3,4]], ARRAY[[5,6],[7,8]]);
SELECT ARRAY[f1, f2, '{{9,10},{11,12}}'::int[]] FROM arr;
```

<pre>
                     array
------------------------------------------------
 {{{1,2},{3,4}},{{5,6},{7,8}},{{9,10},{11,12}}}
(1 row)
</pre>

因为数组必须得有类型，因此在构造一个空数组时，必须明确的将其构造成需要的类型，如：

<pre>
SELECT ARRAY[]::integer[];
 array
-------
 {}
(1 row)
</pre>

我们也可以从一个子查询的结果中构造一个数组。此时，数组构造器是关键子ARRAY跟着一个用圆括弧(不是方括弧)包围的子查询。比如：

```
SELECT ARRAY(SELECT oid FROM pg_proc WHERE proname LIKE 'bytea%');
```

<pre>
                          ?column?
-------------------------------------------------------------
 {2011,1954,1948,1952,1951,1244,1950,2005,1949,1953,2006,31}
(1 row)
</pre>

子查询必须只返回一个单独的子段。生成的一维数组将为子查询里每行结果 生成一个元素，元素类型匹配子查询的输出子段。

用ARRAY建立的数组下标总是从壹开始。有关数组的 更多信息，参阅节Section 8.14。

##行构造器##

行构造器是一个从提供给它的成员子段数值中构造行值(也叫复合类型值)的表达式。 一个行构造器由关键子ROW、一个左圆括弧、零个或多个 作为行子段值的表达式(用逗号分隔)、一个右圆括弧组成。比如：

```
SELECT ROW(1,2.5,'this is a test');
```

如果在列表里有多个表达式，那么关键子ROW是可选的。

行构造器可以包含`rowvalue.*`语法，它将被扩展 为行值元素的列表，就像将`.*`语法用于一个SELECT列表顶层一样。例如，如果表t有f1和f2两个子段， 那么下面两句是等价的：

```
SELECT ROW(t.*, 42) FROM t;
SELECT ROW(t.f1, t.f2, 42) FROM t;
```

Note: 在PostgreSQL8.2之前，`.*`语法是不会被扩展的，所以ROW(t.*, 42)将创建一个两子段的行， 其第一个子段是另一行的值。  
新的行为通常更有用。如果你需要旧式的嵌套行 值的做法，请将内部的行值写成不含有.*，例如ROW(t, 42)。

缺省时，ROW表达式创建的值是一个匿名的记录类型。如果必要， 你可以把它转换成一个命名的复合类型(既可以是一个表的行类型，也可以是 一个用CREATE TYPE AS创建的复合类型)。可能会需要一个明确 的转换以避免歧义。比如：

```
CREATE TABLE mytable(f1 int, f2 float, f3 text);
CREATE FUNCTION getf1(mytable) RETURNS int AS 'SELECT $1.f1' LANGUAGE SQL;
-- No cast needed since only one getf1() exists
```

```
SELECT getf1(ROW(1,2.5,'this is a test'));
```

<pre>
 getf1
-------
     1
(1 row)
</pre>

```
CREATE TYPE myrowtype AS (f1 int, f2 text, f3 numeric);
CREATE FUNCTION getf1(myrowtype) RETURNS int AS 'SELECT $1.f1' LANGUAGE SQL;
-- Now we need a cast to indicate which function to call:
SELECT getf1(ROW(1,2.5,'this is a test'));
ERROR:  function getf1(record) is not unique
```

```
SELECT getf1(ROW(1,2.5,'this is a test')::mytable);
```

<pre>
 getf1
-------
     1
(1 row)
</pre>

```
SELECT getf1(CAST(ROW(11,'this is a test',2.5) AS myrowtype));
```

<pre>
 getf1
-------
    11
(1 row)
</pre>

行构造器可以用于制作存储在复合类型子段中的复合类型值，或者是传递给一个接受复合类型参数的函数。另外，我们也可以用它比较两个行值或者用IS NULL IS NOT NULL测试一个行值，比如：

```
SELECT ROW(1,2.5,'this is a test') = ROW(1, 3, 'not the same');
SELECT ROW(table.*) IS NULL FROM table;  -- detect all-null rows
```

行构造器 还可以用于连接子查询，这些在节Section 9.20里面有详细讨论。

##表达式计算规则##

子表达式的计算顺序是没有定义的。特别要指出的是，一个操作符或者函数的 输入并不一定是按照从左向右的顺序或者以某种特定的顺序进行计算的。

另外，如果一个表达式的结果可以通过只判断它的一部分就可以得到， 那么其它子表达式就可以完全不计算了。比如，如果我们这么写

```
SELECT true OR somefunc();
```

那么somefunc()就(可能)根本不会被调用。 即使像下面这样写也是一样

```
SELECT somefunc() OR true;
```

请注意这和某些编程语言里从左向右"short-circuiting"是不一样的。

因此，用有副作用的函数作为复杂表达式的一部分是不明智的。 在WHERE和HAVING子句里依赖副作用或者是计算顺序是 特别危险的，因为这些子句都是作为生成一个执行规划的一部分进行了大量的再处理。
在这些子句里的布尔表达式(AND/OR/NOT的组合) 可以用布尔代数运算律允许的任何方式进行识别。

如果需要强制计算顺序，那么可以使用CASE构造(参阅节Section 9.16)。比如，下面是 一种企图避免在WHERE子句里被零除的不可靠方法：

```
SELECT ... WHERE x > 0 AND y/x > 1.5;--一切很正常
SELECT ... WHERE CASE WHEN x > 0 THEN y/x > 1.5 ELSE false END;
```

使用该方式的CASE结构会阻止优化，因此只有在需要的时候才可以使用。 （特别是在这个例子中，通过使用y > 1.5*x可以很好的解决该问题）
