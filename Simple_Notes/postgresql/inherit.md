继承是面向对象的数据库的概念。它开启了数据库设计新的有趣的可能性大门。

首先，创建两个表：一个cities表和一个capitals表。 自然，首府capitals也属于城市 cities，因此在列出所有城市时需要通过某种方式来隐含地显示出首府。 如果您对PostgreSQL数据库足够熟悉，您也可以像下面那样自定义一些模式：

```
CREATE TABLE capitals (
  name       text,
  population real,
  altitude   int,    -- (单位是英尺)
  state      char(2)
);

CREATE TABLE non_capitals (
  name       text,
  population real,
  altitude   int     -- (单位是英尺)
);

CREATE VIEW cities AS
  SELECT name, population, altitude FROM capitals
    UNION
  SELECT name, population, altitude FROM non_capitals;
```

如果只是查询，那么这个方法会很实用，而如果要进行更新，那么不推荐使用这个方法。

一种更好的方法是：

```
CREATE TABLE cities (
  name       text,
  population real,
  altitude   int     -- (in ft)
);

CREATE TABLE capitals (
  state      char(2)
) INHERITS (cities);
```

在这个例子里， 子表(capitals)继承(inherits) 其父表(parent)的所有字段(name,population, altitude)。 这些字段(name)的类型文本（text）类型(一种PostgreSQL用于变长字符串的固有类型)。 首府会有一个额外的字段，state，用以显示其所处的州。 在PostgreSQL里，一个表可以从零个或者多个其它表中继承过来。

比如，下面的查询找出的是所有海拔超过500英尺的城市的名字，包括州首府：

```
SELECT name, altitude
  FROM cities
  WHERE altitude > 500;
```

返回如下：

<pre>
   name    | altitude
-----------+----------
 Las Vegas |     2174
 Mariposa  |     1953
 Madison   |      845
(3 rows)
</pre>

另一方面，下面的查询找出的是所有海拔大于或等于500英尺的并且不是州首府的城市的名字：

```
SELECT name, altitude
    FROM ONLY cities
    WHERE altitude > 500;
```

<pre>
     name    | altitude
---------------+----------
 Las Vegas |     2174
 Mariposa  |     1953
(2 rows)
</pre>

该插叙语句中cities前面的ONLY表明只对cities表运行查询，而不包括继承级别中低于cities的表。许多我们已经讨论过的命令，如SELECT, UPDATE, DELETE都支持ONLY的使用。

Note: 尽管继承经常使用，但由于还没有集成唯一性约束或者外键， 因此制约了其实用性。
