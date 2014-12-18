窗口函数通过在某种程度上关系到当前行的表行执行一组计算。 这相当于可以做一个聚合函数的计算类型。  
但不同于常规的聚合函数，使用的窗口函数不会 导致行成为分组到一个单一的输出行；行保留其独立的身份。在后台，窗口函数能够访问不止查询 结果的当前行。

这里是一个例子，说明如何比较每个员工的工资和在他或她的部门的平均工资：

```
SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;
```
<pre>
  depname  | empno | salary |          avg
-----------+-------+--------+-----------------------
 develop   |    11 |   5200 | 5020.0000000000000000
 develop   |     7 |   4200 | 5020.0000000000000000
 develop   |     9 |   4500 | 5020.0000000000000000
 develop   |     8 |   6000 | 5020.0000000000000000
 develop   |    10 |   5200 | 5020.0000000000000000
 personnel |     5 |   3500 | 3700.0000000000000000
 personnel |     2 |   3900 | 3700.0000000000000000
 sales     |     3 |   4800 | 4866.6666666666666667
 sales     |     1 |   5000 | 4866.6666666666666667
 sales     |     4 |   4800 | 4866.6666666666666667
(10 rows)
</pre>

前三输出列直接来自表empsalary，并有一个表中的每一行的输出行。 第四列将代表所有含有相同的depname值的表行的平均值作为当前值。 （这实际上是标准avg聚合函数功能，但是OVER条款使其 视为一个窗口函数和整个一套合适的计算行。）

窗口函数的调用总是包含一个OVER子句，即窗口函数的名称和参数. 该语法区别于普通函数或聚合功能。  
OVER子句决定究竟将查询的行如何通过窗口函数拆分处理。OVER子句内的PARTITION BY分区指定行划分成组，或分区，共享相同的PARTITION BY值。 对于每一行，窗口函数通过同一个分区作为当前行的行进行计算。

虽然无论什么样的顺序的行avg将产生相同的结果，但并这不是对于所有的窗口函数。当需要时，你可以使用OVER内的ORDER BY控制顺序。下面是一个例子：

```
SELECT depname, empno, salary, rank() OVER (PARTITION BY depname ORDER BY salary DESC) FROM empsalary;
```
<pre>
depname  | empno | salary | rank
---------------+-------+--------+------
 develop   |     8 |   6000 |    1
 develop   |    10 |   5200 |    2
 develop   |    11 |   5200 |    2
 develop   |     9 |   4500 |    4
 develop   |     7 |   4200 |    5
 personnel |     2 |   3900 |    1
 personnel |     5 |   3500 |    2
 sales     |     1 |   5000 |    1
 sales     |     4 |   4800 |    2
 sales     |     3 |   4800 |    2
(10 rows)
</pre>

如下所示，在由ORDER BY定义子句的顺序中，rank功能在每个不同ORDER BY值的当前行分区产生一个数值排名。 rank需要没有明确的参数，因为它完全取决于OVER子句。

窗口函数的行是通过查询FROM子句"virtual table"产生的，如果有的话，过滤WHERE, GROUP BY和HAVING子句。  
例如，行删除，因为它不符合没有任何窗口函数WHERE条件。查询可以包含多个窗口的功能，通过不同的OVER子句不同的方式分割数据，但是 他们所有的行动在这个虚拟表中定义的同一行的集合。

我们已经看到了，如果行排序并不重要，ORDER BY可以省略。 在一个分区包含所有行的情况下，也可以省略PARTITION BY。

还有一个重要的与窗口功能相关的概念： 对于每一行，是有其分区范围内的行集,又称为它的window frame。  
许多（但不是全部）窗口功能，只作用于窗框行上，而不是整个分区。 默认情况下，如果使用ORDER BY，那么这个frame包含从分区开始到当前的所有行， 以及那些当前行后面的，根据ORDER BY规则等于当前行的所有行， 如果不使用ORDER BY，那么，frame默认包含分区中的所有行。 [1] 下面是一个使用sum的例子：

```
SELECT salary, sum(salary) OVER () FROM empsalary;
```
<pre>
 salary |  sum
--------+-------
   5200 | 47100
   5000 | 47100
   3500 | 47100
   4800 | 47100
   3900 | 47100
   4200 | 47100
   4500 | 47100
   4800 | 47100
   6000 | 47100
   5200 | 47100
(10 rows)
</pre>

如上，因为在OVER子句没有使用ORDER BY，因此， 窗框与分区(不使用PARTITION BY时即整个表)相同;
换句话说，每一次sum求和都是使用表中所有的salary，所以我们得到了每个输出 行的相同结果。 但是，如果我们添加ORDER BY子句，我们会得到不同的结果：

```
SELECT salary, sum(salary) OVER (ORDER BY salary) FROM empsalary;
```

<pre>
 salary |  sum
----------+-------
   3500 |  3500
   3900 |  7400
   4200 | 11600
   4500 | 16100
   4800 | 25700
   4800 | 25700
   5000 | 30700
   5200 | 41100
   5200 | 41100
   6000 | 47100
(10 rows)
</pre>

这里的总和是通过从第一个（最低）工资到当前一个，包括任何当前重复的（注意 重复薪金结果）。

窗函数仅允许在SELECT和ORDER BY语句中使用。 在其他地方禁止使用，比如GROUP BY, HAVING 和WHERE子句，这是因为它们处理这些子句之后是逻辑 执行。  
此外，标准聚合函数后，执行窗口函数功能。 这意味在执行一个窗口函数时，发出一个标准聚合函数的请求是有效的，但反过来不行。

执行窗口计算后，如果有必要进行过滤或组行，你可以使用子选择。例如：

```
SELECT depname, empno, salary, enroll_date
FROM
  (SELECT depname, empno, salary, enroll_date,
          rank() OVER (PARTITION BY depname ORDER BY salary DESC, empno) AS pos
     FROM empsalary
  ) AS ss
WHERE pos < 3;
```

上面的查询只显示内部查询rank小于3的行。

当查询涉及多个窗口函数功能，可以将每一个查询结果通过单独的OVER子句输出， 但是，如果同一窗口行为需要多种功能，就会产生重复，并且容易出错。 相反，每个窗口的操作可以在WINDOW子句中进行命名，然后再被OVER引用。 例如：

```
SELECT sum(salary) OVER w, avg(salary) OVER w
  FROM empsalary
  WINDOW w AS (PARTITION BY depname ORDER BY salary DESC);
```
