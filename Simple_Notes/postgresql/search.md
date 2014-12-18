##概述##
从数据库中检索数据的过程或命令叫做 查询。 在SELECT里SELECT命令用于 声明查询。SELECT命令的通用语法如下：

<pre>
	[WITH with_queries] SELECT select_list FROM table_expression [sort_specification]
</pre>

随后的几节将描述选择列表、表表达式、排序声明的细节。 WITH 查询被视为最后的，因为它们是一种先进的功能。

简单的查询的形式如下：

```
SELECT * FROM table1;
```

假设有一个table1表，这条命令将从table1中检索所有行和所有字段。 检索的方法取决于客户端的应用程序。  
比如，psql程序将在屏幕上显示一 个ASCII-art表格，客户端库将提供检索独立行和字段的函数。  
选择列表声明为*表示表表达式提供的所有可用字段。一个选择列表也可以选择可用字段的一个子集或者在检索它们之前对字段进行计算；  
比如，如果table1有 名为a，b和c的字段(可能还有其它)，那么你可以用下面的 语句进行查询(假设b和c都是数字数据类型)：

```
SELECT a， b + c FROM table1;
```

FROM table1是一种非常简单的表表达式：它只读取了一个表。通常，表表达式可以是基本 表、连接、子查询的复杂构造。但你也可以省略表表达式而只用SELECT命令当做一个计算器：

```
SELECT 3 * 4;
```

如果选择列表里的表达式返回变化的结果，那么这个东西就更有用了。比如，你可以用这个方法调用函数：

```
SELECT random();
```

##表表达式##
一个表表达式计算一个表，它包含一个FROM子句，该子句可以根据需要选用WHERE，GROUP BY和HAVING子句。  
大部分表表达式只是指向磁盘上的一个所谓的基本表，但是我们可以用更复杂的表表达式以各种方法修改或组合基本表。

表表达式里的WHERE，GROUP BY和HAVING子句声明一系列对源自FROM子句的表的转换操作。所有这些转换最后生成一个虚拟表，传递给选择列表计算输出行。

###FROM子句###
FROM Clause从一个逗号分隔的表引用列表中生成一个虚拟表

```
FROM table_reference [， table_reference [， ...]]
```

表引用可以是一个表名字(可能有模式修饰)或者是一个生成的表，比如子查询、表连接，或它们的复杂组合。  
如果在FROM子句中列出了多于一个表，那么它们被交叉连接(见下文)形成一个派生表，该表可以进行WHERE，GROUP BY和HAVING子句的转换处理，并最后生成表表达式的结果。

如果一个表引用的是一个简单的父表的名字，那么将包括其所有子表的行，除非你在该表名字前面加ONLY关键字(这样任何子表都会被忽略)。

###连接表###
一个连接表是根据特定的连接规则从两个其它表(真实表或生成表)中派生的表。我们支持内连接、外连接、交叉连接。

连接类型

- 交叉连接

<pre>
T1 CROSS JOIN T2
</pre>

对每个来自T1和T2的行进行组合(即笛卡尔积)，生成的表将包含这样的行：所有T1里面的字段后面跟着所有T2里面的字段。  
如果两表分别有N和M行，连接成的表将有N*M行。

`FROM T1 CROSS JOIN T2` 等效于`FROM T1 ,T2 `。它还等效于`FROM T1 INNER JOIN T2 ON TRUE`(见下文)。

- 条件连接

<pre>
T1 { [INNER] | { LEFT | RIGHT | FULL } [OUTER] } JOIN T2 ON boolean_expression
T1 { [INNER] | { LEFT | RIGHT | FULL } [OUTER] } JOIN T2 USING ( join column list )
T1 NATURAL { [INNER] | { LEFT | RIGHT | FULL } [OUTER] } JOIN T2
</pre>

INNER和OUTER对所有连接类型都是可选的。INNER为缺省。LEFT，RIGHT和FULL隐含外连接。

连接条件在ON或USING子句里声明，或者用关键字NATURAL隐含地声明。 连接条件判断来自两个源表中的那些行是"匹配"的，这些我们将在下面详细解释。

ON子句是最常见的连接条件的类型：它接收一个和WHERE子句相同的布尔表达式。
如果两个分别来自T1和T2的行在ON表达式上运算的结果为真，那么它们就算是匹配的行。

USING是个一个连接条件的缩写语法：它接收一个用逗号分隔的字段名列表， 这些字段必须是连接表共有的并且其值必须相同。  
最后，JOIN USING会将每 一对相等的输入字段输出为一个字段，其后跟着所有其它字段。  
因此，USING (a， b， c)等效 于ON (t1.a = t2.a AND t1.b = t2.b AND t1.c = t2.c)，只不过 是如果使用了ON，那么在结果里a，b和c字段都会有两个， 而用USING的时候就只会有一个。(如果SELECT `*`被用的话他们会首先出现)。

最后，NATURAL是USING的一种缩写形式：它自动形成一个由两个表中 同名的字段组成的USING列表(同名字段只出现一次)。

条件连接可能的类型是：

- INNER JOIN
内连接。对于T1中的每一行R1，如果能在T2中找到一个或多个满 足连接条件的行，那么这些满足条件的每一行都在连接表中生成一行。

- LEFT OUTER JOIN
左外连接。首先执行一次内连接。然后为每一个T1中无法在T2中找 到匹配的行生成一行，该行中对应T2的列用NULL补齐。因此，生成的连接表里无条件地包含来自T1里的每一行至少一个副本。

- RIGHT OUTER JOIN
右外连接。首先执行一次内连接。然后为每一个T2中无法在T1中找到匹配的行生成一行，该行中对应T1的列用NULL补齐。因此， 生成的连接表里无条件地包含来自T2里的每一行至少一个副本。

- FULL OUTER JOIN
全连接。首先执行一次内连接。然后为每一个T1与T2中找不到匹配的 行生成一行，该行中无法匹配的列用NULL补齐。因此，生成的连接表里无条 件地包含T1和T2里的每一行至少一个副本。

如果T1和T2之一或全部是可以连接的表，那么所有类型的连接都可以串连或嵌套在一起。 你可以在JOIN子句周围使用圆括弧来控制连接顺序， 如果没有圆括弧，那么JOIN子句从左向右嵌套。

为了解释这些问题，假设我们有一个表t1

<pre>
 num | name
-----+------
   1 | a
   2 | b
   3 | c
和 t2:

 num | value
-----+-------
   1 | xxx
   3 | yyy
   5 | zzz
</pre>  

然后我们用不同的连接方式可以获得各种结果：

<pre>
=> SELECT * FROM t1 CROSS JOIN t2;
 num | name | num | value
-----+------+-----+-------
   1 | a    |   1 | xxx
   1 | a    |   3 | yyy
   1 | a    |   5 | zzz
   2 | b    |   1 | xxx
   2 | b    |   3 | yyy
   2 | b    |   5 | zzz
   3 | c    |   1 | xxx
   3 | c    |   3 | yyy
   3 | c    |   5 | zzz
(9 rows)

=> SELECT * FROM t1 INNER JOIN t2 ON t1.num = t2.num;
 num | name | num | value
-----+------+-----+-------
   1 | a    |   1 | xxx
   3 | c    |   3 | yyy
(2 rows)

=> SELECT * FROM t1 INNER JOIN t2 USING (num);
 num | name | value
-----+------+-------
   1 | a    | xxx
   3 | c    | yyy
(2 rows)

=> SELECT * FROM t1 NATURAL INNER JOIN t2;
 num | name | value
-----+------+-------
   1 | a    | xxx
   3 | c    | yyy
(2 rows)

=> SELECT * FROM t1 LEFT JOIN t2 ON t1.num = t2.num;
 num | name | num | value
-----+------+-----+-------
   1 | a    |   1 | xxx
   2 | b    |     |
   3 | c    |   3 | yyy
(3 rows)

=> SELECT * FROM t1 LEFT JOIN t2 USING (num);
 num | name | value
-----+------+-------
   1 | a    | xxx
   2 | b    |
   3 | c    | yyy
(3 rows)

=> SELECT * FROM t1 RIGHT JOIN t2 ON t1.num = t2.num;
 num | name | num | value
-----+------+-----+-------
   1 | a    |   1 | xxx
   3 | c    |   3 | yyy
     |      |   5 | zzz
(3 rows)

=> SELECT * FROM t1 FULL JOIN t2 ON t1.num = t2.num;
 num | name | num | value
-----+------+-----+-------
   1 | a    |   1 | xxx
   2 | b    |     |
   3 | c    |   3 | yyy
     |      |   5 | zzz
(4 rows)
</pre>

用ON声明的连接条件也可以包含与连接不直接相关的条件。这种功能 可能对某些查询很有用，但是需要我们仔细想清楚。比如：

<pre>
=> SELECT * FROM t1 LEFT JOIN t2 ON t1.num = t2.num AND t2.value = 'xxx';
 num | name | num | value
-----+------+-----+-------
   1 | a    |   1 | xxx
   2 | b    |     |
   3 | c    |     |
(3 rows)
请注意，放置在WHERE条款的限制 产生不同的结果：

=> SELECT * FROM t1 LEFT JOIN t2 ON t1.num = t2.num WHERE t2.value = 'xxx';
 num | name | num | value
-----+------+-----+-------
   1 | a    |   1 | xxx
(1 row)
</pre>

这是因为在ON子句连接之前处理，而WHERE子句在连接之后处理。

###表和列别名###

你可以给表或复杂的表引用起一个临时的表别名，以便被其余的查询引用，称为tablealias.

要创建一个表别名，可以这样：

```
FROM table_reference AS alias
或
FROM table_reference alias
```

AS关键字没有特别的含义。alias可以是任意标识符。

表别名的典型应用是给长表名赋予比较短的标识，好让连接子句更易读一些。比如：

```
SELECT * FROM some_very_long_table_name s JOIN another_fairly_long_name a ON s.id = a.num;
```

别名变成了与当前查询有关的表的名字，之后就不允许再用最初的名字了。因此这是无效的

```
SELECT * FROM my_table AS m WHERE my_table.a > 5;    -- wrong
```

表别名主要是为了方便标记，但对于自连接却是必须的。比如：

```
SELECT * FROM people AS mother JOIN people AS child ON mother.id = child.mother_id;
```

另外，要引用子查询的结果也必须使用别名。

圆括弧用于解决歧义。下面的第一个语句把别名b赋予第二个my_table表； 而第二个语句则把别名b赋予了连接的结果。

```
SELECT * FROM my_table AS a CROSS JOIN my_table AS b ...
SELECT * FROM (my_table AS a CROSS JOIN my_table) AS b ...
```

另外一种形式的表别名除了给表赋予别名外，还给该表的字段也赋予了别名：

```
FROM table_reference [AS] alias ( column1 [， column2 [， ...]] )
```

如果声明的字段别名比表里实际的字段少，那么后面的字段就没有别名。这个语法对于自连接或子查询特别有用。

如果用这些形式中的任何一种给一个JOIN子句的输出结果附加一个别名， 那么该别名就在JOIN里隐藏了其原始的名字。比如

```
SELECT a.* FROM my_table AS a JOIN your_table AS b ON ...
```

是合法SQL，但是

```
SELECT a.* FROM (my_table AS a JOIN your_table AS b ON ...) AS c
```

是不合法的：别名a在别名c的外面是看不到的。

###子查询###

子查询的结果(派生表)必须包围在圆括弧里并 且必须赋予一个别名(参阅Section 7.2.1.2)。比如：

```
FROM (SELECT * FROM table1) AS alias_name
```

这个例子等效于FROM table1 AS alias_name。更有趣的例子是在子 查询里面有分组或聚集的时候，这个时候子查询不能归纳成一个简单的连接。

子查询也可以是一个VALUES列表：

```
FROM (VALUES ('anne'， 'smith')， ('bob'， 'jones')， ('joe'， 'blow'))
     AS names(first， last)
```

这种情况同样也必须要取一个别名。还可以为VALUES列表中的字段取别名， 并且被认为是一个好习惯。更多信息参见Section 7.7。

###表函数###

表函数是那些生成一个行集合的函数，这个集合可以是由基本数据类型(标量类型)组成， 也可以是由复合数据类型(表的行)组成。他们的用法类似一个表、视图或FROM子 句里的子查询。表函数返回的字段可以像一个表、视图、或者子查询字段那 样包含在SELECT，JOIN或者WHERE子句里。

如果表函数返回基本数据类型，那么单一结果字段的名字与函数名相同。如果表函数返回复合 数据类型，那么多个结果字段的名字和该类型的每个属性的名字相同。

可以在FROM子句中为表函数取一个别名，也可以不取别名。如果一个 函数在FROM子句中没有别名，那么将使用函数名作为结果表的名字。

一些例子：

```
CREATE TABLE foo (fooid int， foosubid int， fooname text);

CREATE FUNCTION getfoo(int) RETURNS SETOF foo AS $$
    SELECT * FROM foo WHERE fooid = $1;
$$ LANGUAGE SQL;

SELECT * FROM getfoo(1) AS t1;

SELECT * FROM foo
    WHERE foosubid IN (
                        SELECT foosubid
                        FROM getfoo(foo.fooid) z
                        WHERE z.fooid = foo.fooid
                      );

CREATE VIEW vw_getfoo AS SELECT * FROM getfoo(1);

SELECT * FROM vw_getfoo;
```

有时侯，把一个函数定义成根据不同的调用方法可以返回不同的字段是很有用的。 为了支持这个，表函数可以声明为返回伪类型record。如果在查询里使用这样 的函数，那么我们必须在查询中声明预期的行结构，这样系统才知道如何分析和 规划该查询。让我们看看下面的例子：

```
SELECT *
    FROM dblink('dbname=mydb'， 'SELECT proname， prosrc FROM pg_proc')
      AS t1(proname name， prosrc text)
    WHERE proname LIKE 'bytea%';
```

dblink函数执行一个远程的查询。它声明为返回record，因为它可能会被用于任何类型的查询。实际的字段集必 须在调用它的查询中声明，这样分析器才知道类似*这样的东西应该扩展成什么样子。

###WHERE子句###

WHERE Clause子句的语法是

<pre>
WHERE search_condition
</pre>

这里的search_condition是一个返 回类型为boolean的值表达式。

在完成对FROM子句的处理之后，生成的每一行都会按照search_condition进行检查。  
如果结果是真，那么该行保留在输出表中，否则(结果是假或NULL)就把它抛弃。 搜索条件通常至少要引用一列在FROM子句里生成的列，这不是必须的， 但如果不这样的话，WHERE子句就没什么意义了。

Note: 内连接的连接条件既可以写在WHERE子句里也可以写在JOIN子句里。比如，下面的表表达式是等效的：

```
FROM a， b WHERE a.id = b.id AND b.val > 5
和：

FROM a INNER JOIN b ON (a.id = b.id) WHERE b.val > 5
或者可能还有：

FROM a NATURAL JOIN b WHERE b.val > 5
```

你想用哪个只是风格问题。FROM子句里的JOIN语法可能不那么容易移植到其它产品中。即使它是在SQL标准 对于外连接而言，我们在任何情况下都没有选择：连接条件必须在FROM子句中完成。 外连接的ON或USING子句不等于WHERE条件，因为它判断最终 结果中行的增(那些不匹配的输入行)和删。

这里是一些WHERE子句的例子：

```
SELECT ... FROM fdt WHERE c1 > 5
SELECT ... FROM fdt WHERE c1 IN (1， 2， 3)
SELECT ... FROM fdt WHERE c1 IN (SELECT c1 FROM t2)
SELECT ... FROM fdt WHERE c1 IN (SELECT c3 FROM t2 WHERE c2 = fdt.c1 + 10)
SELECT ... FROM fdt WHERE c1 BETWEEN (SELECT c3 FROM t2 WHERE c2 = fdt.c1 + 10) AND 100
SELECT ... FROM fdt WHERE EXISTS (SELECT c1 FROM t2 WHERE c2 > fdt.c1)
```

在上面的例子里，fdt是从FROM子句中派生的表。那些不符合WHERE子句的搜 索条件的行将从fdt中删除。请注意我们把标量子查询当做一个值表达式来用。
就像其它查询一样，子查询里也可以使用复杂的表表达式。同时还请注意fdt是 如何引用子查询的。  
把c1修饰成fdt.c1只有在c1是该子查询生成的列名字时才是必须的， 但修饰列名字可以增加语句的准确性(即使有时不是必须的)。这个例子就演示了字段名字 范围如何从外层查询扩展到它的内层查询。

###GROUP BY和HAVING子句###
在通过了WHERE过滤器之后，生成的输出表可以继续用GROUP BY子句进行 分组，然后用HAVING子句选取一些分组行

```
SELECT select_list
    FROM ...
    [WHERE ...]
    GROUP BY grouping_column_reference [， grouping_column_reference]...
```

GROUP BY Clause子句用于把那些所有列出的`grouping_column_reference`值都相 同的行聚集在一起，缩减为一行，这样就可以删除输出里的重复和/或计算应用 于这些组的聚集。这些字段的列出顺序无关紧要。比如：

<pre>
=> SELECT * FROM test1;
 x | y
---+---
 a | 3
 c | 2
 b | 5
 a | 1
(4 rows)

=> SELECT x FROM test1 GROUP BY x;
 x
---
 a
 b
 c
(3 rows)
</pre>

在第二个查询里，我们不能写成`SELECT * FROM test1 GROUP BY x`，因为字段y里 没有哪个值可以和每个组关联起来。被分组的字段可以在选择列表中引 用是因为它们每个组都有单一的数值。

如果一个表被分了组，不在GROUP BY列中除了在总表达式不能被引用，那么就只能引用聚集表达式中的字段和分组中的字段。一个带聚集表达式的例子是：

<pre>
=> SELECT x， sum(y) FROM test1 GROUP BY x;
 x | sum
---+-----
 a |   4
 b |   5
 c |   2
(3 rows)
</pre>

这里的sum是一个聚集函数，它在组上计算总和。

Tip: 没有有效的聚合表达式分组可以计算一列中不同值的设置。 这个可以通过DISTINCT子句来实现.

这里是另外一个例子：它计算每种产品的总销售额(而不是所有产品的总销售额)。

```
SELECT product_id， p.name， (sum(s.units) * p.price) AS sales
    FROM products p LEFT JOIN sales s USING (product_id)
    GROUP BY product_id， p.name， p.price;
```

在这个例子里，字段product_id，p.name和p.price必须在GROUP BY子句里， 因为它们都在查询选择列表里被引用了。  
根据产品表具体设置的不同， 名字和价格可能和产品ID完全无关，因此理论上额外的分组可能是不必要的， 但是这些尚未实现。  
s.units字段不必在GROUP BY列表里，因为它只是在一个聚集表达式(sum(...))里使用，它代表一组产品的销售总额。 对于每种产品，这个查询都返回一个该产品的总销售额。

在严格的SQL里，GROUP BY只能对源表的列进行分组，但PostgreSQL把这 个扩展为既允许GROUP BY对选择列表中的字段进行分组，也允许对值表达式进行分组，而不仅仅是简单的字段。

如果一个表已经用GROUP BY子句分了组，然后你又只对其中的某些组感兴趣， 那么就可以用HAVING子句筛选分组。  
必须像WHERE子句，从结果中消除组，语法是

<pre>
SELECT select_list FROM ... [WHERE ...] GROUP BY ... HAVING boolean_expression
</pre>

在HAVING子句中的表达式可以引用分组的表达式和未分组的表达式(后者必须涉及一个聚集函数)。

例子:

```
=> SELECT x， sum(y) FROM test1 GROUP BY x HAVING sum(y) > 3;
 x | sum
---+-----
 a |   4
 b |   5
(2 rows)

=> SELECT x， sum(y) FROM test1 GROUP BY x HAVING x < 'c';
 x | sum
---+-----
 a |   4
 b |   5
(2 rows)
```

然后是一个更现实的例子：

```
SELECT product_id， p.name， (sum(s.units) * (p.price - p.cost)) AS profit
    FROM products p LEFT JOIN sales s USING (product_id)
    WHERE s.date > CURRENT_DATE - INTERVAL '4 weeks'
    GROUP BY product_id， p.name， p.price， p.cost
    HAVING sum(p.price * s.units) > 5000;
```

在上面的例子里，WHERE子句在尚未分组之前根据s.date字段选择数据行 (表达式只是对那些最近四周发生的销售为真)。  
而HAVING子句在分组之后 选择那些销售总额超过5000的组。请注意聚集表达式不需要在查询中的所有地方都一样。

如果一个查询调用了聚合函数，但没有GROUP BY子句，分组仍然发生： 结果是单一组行（或者如果单一行被HAVING所淘汰，那么也许没有行）。  
同样，它包含一个HAVING子句，甚至没有任何聚合函数的调用或GROUP BY子句。

###窗口函数处理###

如果查询包含窗口函数， 这些函数在执行了分组、聚合和HAVING过滤之后被评估。 也就是说，如果查询使用任何的聚合、GROUP BY或HAVING，那么 由窗口函数发现的行是该组行而不是从FROM/WHERE得到的原始表行。

当多个窗口函数被使用的时候，所有的窗口函数依照语法地等效于在它们的窗口定义被单一数据 所评估的PARTITION BY和ORDER BY子句中。  
因此它们将看到同样的排序，即使ORDER BY不唯一确定一个排序。  
然而，不确保所做出的关于评价的功能有不同的PARTITION BY或ORDER BY 规范。（在这种情况下，一个排序步骤通常需要在窗口函数评价和排序不被保证保存看似跟ORDER BY等效的行命令。）

目前，窗口函数总是需要分类数据，所以查询输出将按照一个或另一个窗口函数PARTITION BY/ORDER BY子句。它不是说依赖于此。 如果你想要确保结果是按特定的方式分类那么使用显式的顶级ORDER BY子句。

##选择列表##
如前面的小节说明的那样，在SELECT命令中的表表达式通过组合表、视图、删除行、分组等构造了一个中介性的虚拟表。 这个表最后传递给选择列表处理。选择列表判断最终实际输出虚拟表的哪些字段。

###选择列表项###

最简单的选择列表是*，它输出表表达式生成的所有字段。否则，一个选择 列表是一个逗号分隔的值表达式的列表。 比如，它可能是一个字段名列表：

```
SELECT a， b， c FROM ...
```

字段名a，b和c要么是在FROM子句里引用的表中字段的实际名字， 要么是别名。  
选择列表中的名字空间和WHERE子句中的 名字空间是一样的，除非你使用了分组，否则它和HAVING子句中的名字空间也一样。

如果多个表有重复的字段名，那么你还必须给出表名，例如：

```
SELECT tbl1.a， tbl2.a， tbl1.b FROM ...
```

当使用多个表时，给出表名还有助于引用该表的所有字段：

```
SELECT tbl1.*， tbl2.a FROM ...
```

如果将值表达式用于选择列表，那么它在概念上向返回的表中增加了一个新的虚拟字段。  
值表达式为结果中的每一行进行一次计算，计算之前用该行的数值替换任何表达式里 引用的字段。  
不过选择列表中的这个表达式并非一定要引用来自FROM子句中表表 达式里面的字段，比如，它也可以是任意常量算术表达式。

###字段标签###

在选择列表中的项可以被指定用于后续的名字 处理，如在ORDER BY子句中使用， 或由客户端应用程序中显示。例如：

```
SELECT a AS value， b + c AS sum FROM ...
```

如果没有使用AS声明字段名，那么系统将赋予一个缺省值。对于简单的字段引用，它是该字段名。  
对于函数调用，它是该函数名。对于复杂表达式，系统会生成一个通用的名称。

只有当新列名与任何PostgreSQL关键字不匹配时AS关键字是可选的，但只有当新列名与任何PostgreSQL关键字不匹配时必须使用(参阅Appendix C)。
你可以给列名加上双引号来避免意外匹配关键字。 例如，VALUE是一个关键字，所以这样是不起作用的：

```
SELECT a value， b + c AS sum FROM ...
```

但这样可以:

```
SELECT a "value"， b + c AS sum FROM ...
```

为了防止和未来补充的关键字发生冲突，建议您要么写AS，要么为输出列名加双引号标记。

Note: 输出字段的命名和在FROM子句里的命名是不一样的(参阅节 Section 7.2.1.2)。这样就允许你对同一个字段命名两次，FROM子句里的名字将被选择列表使用， 而选择列表中新取的名字将被最终输出。

###DISTINCT###

在处理完选择列表之后，生成的表可以删除重复行。 直接在SELECT后面写上DISTINCT关键字即可：

```
SELECT DISTINCT select_list ...（如果不用DISTINCT你可以用ALL声明保留所有行的缺省行为。）
```

显然，如果两行里至少有一个字段值不同，那么我们认为这两行是独立的。NULL在这里被认为是相同的。

另外，我们还可以用表达式来判断什么样的行可以认为是独立的：

```
SELECT DISTINCT ON (expression [， expression ...]) select_list ...
```

这里的expression是一个值表达式，它为每一行计算。如果一组行计 算出的该表达式的值都相同，那么就认为这些行是重复的，并只输出第一行 。  
请注意这里的"第一行"是不可预料的，除非你在足够多的字段上对该查询进行了排序， 保证到达DISTINCT过滤器时行的顺序是唯一的(DISTINCT ON将在ORDER BY排序之后处理)。

DISTINCT ON子句不是SQL标准的一部分，有时候是一个糟糕的风格， 因为它的结果是不可判定的。如果有可选的GROUP BY和在FROM中的子查询可 以达到目的，那么我们可以避免使用这个构造，但是通常它是更方便的方法。

##组合查询##
可以对两个查询的结果进行集合操作(并、交、差)。语法是：

<pre>
query1 UNION [ALL] query2
query1 INTERSECT [ALL] query2
query1 EXCEPT [ALL] query2
</pre>

query1和query2是讨论到该点的任何特性的查询。也可以嵌套和连接设置操作，例如：

```
query1 UNION query2 UNION query3
```

它实际上等价于

```
(query1 UNION query2) UNION query3
```

UNION把query2的结果附加到query1的 结果上(不过我们不能保证这就是这些行实际的返回顺序)，并且像DISTINCT那样删除结 果中所有重复的行(除非声明了UNION ALL)。

INTERSECT返回那些同时存在于query1和query2结果中的行。 除非声明了INTERSECT ALL，否则所有重复行都被删除。

EXCEPT返回所有在query1结果中但是不在query2结果中的行(有时侯 这叫做两个查询的差)。除非声明了EXCEPT ALL，否则所有重复行都被删除。

为了能够计算两个查询的并、交、差，这两个查询必须是"并集兼容的"，也就是它们都返回 同样数量的列，并且对应的列有兼容的数据类型。
##行排序##
在查询生成输出表之后，也就是在处理完选择列表之后，你还可以对输出表进行排序。 如果没有排序，那么行将以不可预测的顺序返回(实际顺序将取决于扫描和连接规划类型和在 磁盘上的顺序，但是肯定不能依赖这些东西)。 确定的顺序只能在明确地使用了排序步骤之后才能保证。

ORDER BY子句用于声明排序顺序：

<pre>
SELECT select_list
    FROM table_expression
    ORDER BY sort_expression1 [ASC | DESC] [NULLS { FIRST | LAST }]
             [， sort_expression2 [ASC | DESC] [NULLS { FIRST | LAST }] ...]
</pre>

sort_expression(s)是任何可用于选择列表的表达式，例如：

```
SELECT a， b FROM table1 ORDER BY a + b， c;
```

如果指定了多个排序表达式，那么仅在前面的表达式排序相等的情况下才使用后面的表 达式做进一步排序。每个表达式都可以跟一个可选的ASC(升序，默认)或 DESC(降序) 以设置排序方向。升序先输出小的数值，这里的"小"是以<操作符的角度定义的。 类似的是，降序是以>操作符来判断的。

NULLS FIRST和NULLS LAST选项可以决定在排序操作中在non-null值之前还是之后。默认情况下，空值大于任何非空值；也就是说，DESC排序 默认是NULLS FIRST，否则为NULLS LAST。

注意，排序选项对于每个排序列是相对独立的。例如ORDER BY x， y DESC意思是说ORDER BY x ASC， y DESC， 不同于ORDER BY x DESC， y DESC.

一个sort_expression也可以是列标签或数 输出列，如：

```
SELECT a + b AS sum， c FROM table1 ORDER BY sum;
SELECT a， max(b) FROM table1 GROUP BY a ORDER BY 1;
```

都按照第一个字段进行排序。需要注意的是，输出字段名必须是独立的 (不允许作为排序表达式的一部分)。比如，下面的语句是not正确的。

```
SELECT a + b AS sum， c FROM table1 ORDER BY sum + c;          -- wrong
```

这样的限制主要是为了减少歧义。另外，如果某个ORDER BY排序表达式能够同时匹配输 出字段名和表表达式中的字段名，也会导致歧义(此时使用输出字段名)。当 然，这种情况仅在你使用了AS重命名输出字段并且恰好与其它 表的字段同名的时候才会发生。

ORDER BY可以应用于UNION， INTERSECT或者EXCEPT的计算结果，不过在这种情况下，只允许按照字段名或编号进行排序，而不允许按照表达式进行排序。

Notes:事实上，PostgreSQL使用默认的B-tree操作符类为表达式的数据类型确定ASC和DESC排序顺序。一般来说， 数据类型将被转换为适合于<和>操作符进行排序。但是对于用户自定义的数据类型可以不必如此。

##LIMIT和OFFSET##
LIMIT和OFFSET子句允许你只取出查询结果中的一部分数据行：

<pre>
SELECT select_list
    FROM table_expression
    [ ORDER BY ... ]
    [ LIMIT { number | ALL } ] [ OFFSET number ]
</pre>

如果给出了一个LIMIT计数，那么将返回不超过该数字的行(也可能更少些， 因为可能查询本身生成的总行数就比较少)。LIMIT ALL和省略LIMIT子句是一样的。

OFFSET 指明在开始返回行之前忽略多少行。OFFSET 0和省略OFFSET和LIMIT NULL子句是一样的。  
如果OFFSET和LIMIT都出现了，那么在计算OFFSET之前先忽略LIMIT指定的行数。

使用LIMIT的同时使用ORDER BY子句把结果行约束成一个唯一的顺序是一个好主意。 否则你就会得到一个不可预料的子集。你要的可能是第十到二十行，但以什么顺序的 十到二十？除非你声明了ORDER BY，否则顺序是未知的。

查询优化器在生成查询规划的时候会考虑LIMIT，因此如果你给LIMIT和OFFSET的值不同， 那么你很可能得到不同的规划(产生不同的行顺序)。因此，使用不同的LIMIT/OFFSET值选择不同的子集将w得到不一致的结果，除非你 用ORDER BY强制一个可预料的顺序。这可不是臭虫，而是一个很自然的结果， 因为SQL没有许诺把查询的结果按照任何特定的顺序发出， 除非用了ORDER BY来约束顺序。

OFFSET子句忽略的行仍然需要在服务器内部计算；因此，一个很大的OFFSET可能还是不够有效率。
##VALUES列表##
可以在查询中使用由VALUES生成的"常数表"，而无需在磁盘上实际创建这个表。语法如下：

<pre>
VALUES ( expression [， ...] ) [， ...]
</pre>

每个括号中的表达式列表生成表中的一行。每个列表中的项数(也就是字段数)必须相等，并且对应的数据类型必须兼容。 最终表中每个字段的数据类型将使用与UNION(参见Section 10.5)相同的规则确定。

例如:

```
VALUES (1， 'one')， (2， 'two')， (3， 'three');
```

将得到2列和3行的表。并且与下面的语句等价：

```
SELECT 1 AS column1， 'one' AS column2
UNION ALL
SELECT 2， 'two'
UNION ALL
SELECT 3， 'three';
```

PostgreSQL默认将VALUES所得到的表中各字段分别命名为column1，column2等等。SQL标准并未规定此种情况下的字段名命名规范，不同的数据库系统对此 的处理也各不相同，所以最好明确指定字段的名字。

语法上，带有表达式列表的VALUES和下面的语句等价：

<pre>
SELECT select_list FROM table_expression
</pre>

并且可以出现在任何SELECT可以出现的地方。例如，你可以把它用于UNION的一侧， 或者在其上附加一个sort_specification(ORDER BY，LIMIT和/或OFFSET)。VALUES通常用作INSERT命令的数据源或者子查询。

##WITH的查询(公用表表达式)##
WITH提供了一种在更大的SELECT查询中编写子查询的方式。 这个通常称为公共表表达式或CTEs的子查询可以认为是定义存在于查询中的临时表。 这个特性的一个应用是用于分解复杂查询为简单的部分。下面是一个例子：

```
WITH regional_sales AS (
        SELECT region， SUM(amount) AS total_sales
        FROM orders
        GROUP BY region
     )， top_regions AS (
        SELECT region
        FROM regional_sales
        WHERE total_sales > (SELECT SUM(total_sales)/10 FROM regional_sales)
     )
SELECT region，
       product，
       SUM(quantity) AS product_units，
       SUM(amount) AS product_sales
FROM orders
WHERE region IN (SELECT region FROM top_regions)
GROUP BY region， product;
```

它在唯一最好的销售区域显示每个产品的销售总额。该例可以不使用WITH来编写，但是我们必须需要两个隔离的SELECT嵌套语句。该方法比其它方法更容易理解。

可选的RECURSIVE修饰符从仅有的语法便利性到一个完成事情的特性的改变。 使用RECURSIVE，一个WITH查询可以引用它自己的输出。 一个简单的例子就是查询从1加到100的和：

```
WITH RECURSIVE t(n) AS (
    VALUES (1)
  UNION ALL
    SELECT n+1 FROM t WHERE n < 100
)
SELECT sum(n) FROM t;
```

一般形式的递归WITH语句总是一个non-recursive term，然后是UNION (或UNION ALL)，那么一个recursive term， 它们只可以包含参考查询的输出。这样的一个查询执行如下：

递归查询评估

评估无递归术语。使用UNION(并不是UNION ALL)，去除重复的行。包括在递归查询结果中所有剩余的行，并将它们放入临时的工作表。

只要工作表不为空，那么将重复这些步骤：

评价递归术语，为递归自我参照替换当前工作表内容。 用UNION(并不是UNION ALL)，去除重复的行和与以前 结果行重复的行。 包括所有在递归查询结果中剩余的行，并将它们放入一个临时的中间表。

以中间表的内容替换工作表的内容，然后清空中间表。

Note: 严格的说，该过程是迭代而不是递归，但是RECURSIVE是通过SQL标准委员会选择的术语。

在上面的例子中，在每一步中仅有一个工作表行，并且在后续的步骤中它的值将从1升至100。 在第100步，因为WHERE子句的原因没有任何输出， 因此查询终止。

递归查询通常用于处理分层或树状结构数据。一个有用的示例查询是查找所有直接 或间接的产品的附带部分，仅提供一个表来显示即时的包含：

```
WITH RECURSIVE included_parts(sub_part， part， quantity) AS (
    SELECT sub_part， part， quantity FROM parts WHERE part = 'our_product'
  UNION ALL
    SELECT p.sub_part， p.part， p.quantity
    FROM included_parts pr， parts p
    WHERE p.part = pr.sub_part
  )
SELECT sub_part， SUM(quantity) as total_quantity
FROM included_parts
GROUP BY sub_part
```

当使用递归查询的时候，确保查询的递归部分最终不会返回元组是很重要的，否则查询将会循环下去。 有时，通过使用UNION替代UNION ALL去除掉前面输出重复的行可以实现这个。 然而，通常一个周期不涉及那些完全复制的输出行：检查一个或几个字段来查看是否存在事先达成的 相同点可能是必要的。 处理这种情况的标准方式是计算一个访问队列。 例如，请考虑下面的查询，使用link字段搜索一个表graph：

```
WITH RECURSIVE search_graph(id， link， data， depth) AS (
        SELECT g.id， g.link， g.data， 1
        FROM graph g
      UNION ALL
        SELECT g.id， g.link， g.data， sg.depth + 1
        FROM graph g， search_graph sg
        WHERE g.id = sg.link
)
SELECT * FROM search_graph;
```

如果link关系包含循环那么这个查询将会循环。 因为我们需要一个"深度"输出，仅改变UNION ALL为UNION将不会消除循环。 相反，我们需要认识到我们当按照特定路径链接时是否再次得到了相同的行。 我们添加两列path和cycle到倾向循环的查询：

```
WITH RECURSIVE search_graph(id， link， data， depth， path， cycle) AS (
        SELECT g.id， g.link， g.data， 1，
          ARRAY[g.id]，
          false
        FROM graph g
      UNION ALL
        SELECT g.id， g.link， g.data， sg.depth + 1，
          path || g.id，
          g.id = ANY(path)
        FROM graph g， search_graph sg
        WHERE g.id = sg.link AND NOT cycle
)
SELECT * FROM search_graph;
```

除了防止循环，该数组值通常是有用的，在它的右边作为代表采取的得到任何特定行的"路径"。

在一般情况下，使用一个行数组多于一个字段需要检查到一个循环。 例如，如果我们需要对比字段f1和f2：

```
WITH RECURSIVE search_graph(id， link， data， depth， path， cycle) AS (
        SELECT g.id， g.link， g.data， 1，
          ARRAY[ROW(g.f1， g.f2)]，
          false
        FROM graph g
      UNION ALL
        SELECT g.id， g.link， g.data， sg.depth + 1，
          path || ROW(g.f1， g.f2)，
          ROW(g.f1， g.f2) = ANY(path)
        FROM graph g， search_graph sg
        WHERE g.id = sg.link AND NOT cycle
)
SELECT * FROM search_graph;
```

Tip: 在常见的情况下，当只有一个字段需要检查到循环的时候忽略ROW()语法。 这允许一个简单的数组而不是使用一个复杂类型的数组获得效率。

Tip: 递归查询评估算法产生以广度优先搜索顺序的输出。 你可以按照深度优先查询排序通过通过外部查询ORDER BY一个"path"列来显示结果。

当你不能确定它们在设置了一个LIMIT父查询后是否会循环的时候，这是一个 对于测试查询有用的技巧。 例如，这个循环将在没有LIMIT的情况下循环：

```
WITH RECURSIVE t(n) AS (
    SELECT 1
  UNION ALL
    SELECT n+1 FROM t
)
SELECT n FROM t LIMIT 100;
```

它能工作是因为PostgreSQL的实现评估只有当许多实际上是通过父 查询获取的WITH查询行。  
在实际的生产环境下不推荐使用该技巧，因为其它的系统可以以不同的方式工作。 同样，如果你使用外部查询将递归查询结果或将它们加入到别的表中分类，那么它通常是不工作的。

一个有用的WITH查询属性是每个父查询执行一次它们做一次评估，即使指定它们 不止一次地通过父查询或WITH查询。  
所以，复杂的需要在多个地方放置的计算可以通过设置WITH查询来避免冗余工作。 另一个可能的应用是防止不必要的多副作用函数的评估。 然而，另一方面，比起普通的子查询，优化器是不能够避开父查询拆分为一个WITH查询的限制。 通常将WITH查询评估如上，没有行限制的父查询可能丢失。（但是，正如上面所说， 如果查询参考查询数量有限的行，评估可能会很早终止。）
