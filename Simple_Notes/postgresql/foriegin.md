 考虑下面的问题： 你想确保没有人可以在weather表里插入一条 在cities表里没有匹配记录的数据行. 这就叫维护表的参照完整性。在简单的数据库系统里，实现(如果也叫实现)这个特性的方法通常是先看看 cities表里是否有匹配的记录， 然后插入或者拒绝新的weather记录。 这个方法有许多问题，而且非常不便，因此PostgreSQL 可以为你做这些。

新的表声明看起来会像下面这样：

```
CREATE TABLE cities (
        city     varchar(80) primary key,
        location point
);

CREATE TABLE weather (
        city      varchar(80) references cities(city),
        temp_lo   int,
        temp_hi   int,
        prcp      real,
        date      date
);
```

然后我们试图插入一条非法的记录：

```
INSERT INTO weather VALUES ('Berkeley', 45, 53, 0.0, '1994-11-28');
ERROR:  insert or update on table "weather" violates foreign key constraint "weather_city_fkey"
DETAIL:  Key (city)=(Berkeley) is not present in table "cities".
```
但是我们可以使用以下方式插入数据:

```
insert into cities values('Berkeley','(120,11)');
INSERT INTO weather VALUES ('Berkeley', 45, 53, 0.0, '1994-11-28');
```

查看表的结构:

<pre>
\d weather;

           Table "public.weather"
 Column  |         Type          | Modifiers
---------+-----------------------+-----------
 city    | character varying(80) |
 temp_lo | integer               |
 temp_hi | integer               |
 prcp    | real                  |
 date    | date                  |
Foreign-key constraints:
    "weather_city_fkey" FOREIGN KEY (city) REFERENCES cities(city)

\d cities;

            Table "public.cities"
  Column  |         Type          | Modifiers
----------+-----------------------+-----------
 city     | character varying(80) | not null
 location | point                 |
Indexes:
    "cities_pkey" PRIMARY KEY, btree (city)
</pre>
