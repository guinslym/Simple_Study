##优化SQL语句的一般情况##
当面对1个有SQL性能问题的数据库时,我们可以通过以下步骤快速定位问题SQL并尽快解决问题.  
###通过show status命令了解各种SQL的执行频率###
Mysql客户端连接成功后,通过show [session|global] status命令可以提供服务器状态信息,也可以在操作系统上使用mysqladmin extended-status命令获得这些消息。show [session|global] status可以根据需要加上参数session或global来显示session级(当前连接)的统计结果和global级(自数据库上次启动至今)的统计结果。如果不写,默认使用参数是session。  
下面的命令显示了了当前session中所有统计参数的值。

```
show status like 'Com_%';
```

Com_xxx表示每个xxx语句的执行的次数,我们通常比较关心的是以下几个统计参数。

- Com_select：执行select操作的次数,1次查询只累计1。
- Com_insert:执行insert操作的次数,对于批量插入的insert操作,只累加1次。
- Com_update:执行update操作的次数。
- Com_delete:执行delete操作的次数。

上面这些参数对于所有存储引擎的表操作都会进行累计。下面这几个参数只是针对Innodb存储引擎的,累加的算法也略有不同。

- Innodb_rows_read:select查询返回的行数。
- Innodb_rows_inserted:执行insert操作插入的行数。
- Innodb_rows_updated:执行update操作更新的行数。
- Innodb_rows_deleted:执行delete操作删除的行数。

对于事务型的应用,通过Com_commit和Com_rollback可以了解事务提交和回滚的情况,对于回滚操作非常频繁的数据库,可能意味着应用编写存在问题。

- Connections:试图连接Mysql服务器的次数。
- Uptime:服务器工作时间。
- Slow_queries:慢查询的次数。

###定位执行效率较低的SQL语句###

- 通过慢查询日志定位那些执行效率较低的SQL语句,用--log-slow-queries[=file_name]选项启动时,mysqld写1个包含所有执行时间超过`long_query_time`秒的SQL语句的日志文件。
- 使用show processlist命令查看当前Mysql在进行的线程,包括线程的状态、是否锁表等,可以实时地查看SQL的执行情况,同时对一些锁表操作进行优化。

###通过explain分析低效SQL的执行计划###
通过以上步骤查询到效率低的SQL语句后,通过explain或者desc命令获取Mysql如何执行select语句的信息,包括在select语句执行过程表如何连接和连接的的顺序。  
每个列的简单解释如下:

- select_type：表示select类型,常见的取值有simple(简单表,即不使用表连接或者子查询)、primary(主查询,即外层的查询)、union(union中的第2个或者后面的查询语句)、subquery(子查询中的第1个select)等。
- table:输出结果集的表
- type:表示表的连接类型,性能由好到差的连接类型为system、const、`eq_ref`、`ref_or_null`、`index_merge`、`unique_subquery`、`index_subquery`、range、index、all.
- possible_key:表示查询时,可能使用的索引。
- key:表示实际使用的索引。
- key_len:索引字段的长度。
- rows:描述行的数量。
- Extra:执行情况的说明和描述。

以下是表的连接类型说明:

- system,表中仅有1行,即常量表。
- const,单表中最多有1个匹配行,例如primary key或者unique index
- `eq_ref`,对于前面的每1行,此表中只查询1条记录,简单来说,就是多表连接中使用primary key或者unique index。
- ref,与`eq_ref`类似,区别在于不是使用primary key或者unique index,而是使用普通的索引。
- `ref_or_null`,与ref类似,区别在于条件中包含对NULL的查询。
- `index_merge`,索引合并优化。
- `unique_subquery`(in的后面是1个查询主键字段的子查询)
- `index_subquery`,与unique_subquery类似,区别在于in的后面是查询非唯一索引字段的子查询。
- range,单表中的范围查询。
- index,对于前面的每1行,都通过查询索引来得到数据
- all,对于前面的每1行,都通过全表扫描来得到数据。

##索引问题##
###索引的存储分类###
MyISAMBR存储引擎的表的数据和索引是自动分开存储的,各自是独立的1个文件:Innodb存储引擎的表的数据和索引存储在同1个表空间里面,但可以有多个文件组成。  
Mysql中索引的存储类型目前只有2种,BTREE和HASH,具体和表的存储引擎有关,MyISAM和Innodb存储引擎都只支持BTREE索引,MEMORY/HEAP存储引擎可以支持HASH和BTREE索引。  
Mysqlm目前不支持函数索引,但是能对列的前面某一部分进索引,例如name字段,可以只取name的前4个字符进行索引,这个特性可以大大缩小索引文件的大小。
###Mysql如果使用索引###
索引用于快速找出在某个列中有1个特定值的行,对相关列使用索引是提高select操作性能的最佳途径。  
查询要使用索引最主要的条件是查询条件中需要使用索引关键字,如果是多列索引,那么只有查询条件使用了多列关键字最左边的前缀时,才可以使用索引,否则将不能使用索引。  
####使用索引####
在Mysql中,下列几种情况下有可能使用到索引:

1. 对于创建的多列索引,只要查询的条件中用到了最左边的列,索引一般就会被使用。把"%"放在第一位就不能用到索引,而后者没有使用第1位就使用了索引。另外,如果like后面跟着的是1个列的名字,那么索引也不会被使用。P241
2. 如果对大的文本进行搜索,使用全文索引而不用使用立刻'%...%'.
3. 如果列表是索引,使用`column_name is null`将使用索引。
4. 对于使用like的查询,后面如果是常量并且只有%号不在第1个字符,索引才可能会被使用。

####存在索引但不使用索引####
在下列情况下,虽然存在索引,但是Mysql并不会使用相应的索引:

1. 如果Mysql估计使用索引比全表扫描更慢,则不使用索引。例如,如果列均匀分步在1和100之间,使用索引就不是很好。
2. 如果使用MEMORY/HEAP表并且where条件中不使用"="进行索引列,那么不会用到索引。
3. 用or分割开的条件,如果or前的条件中的列有索引,而后面的列没有索引,那么涉及的索引将不会被用到。
4. 如果like是以%开始的。
5. 如果列类型是字符串,那么一定记得在where条件中把字符串常量值用引号引起来,否则的话即便这个列上有索引,Mysql也不会用到的。

###使用索引使用情况###
如果索引正在工作,`Handler_read_key`的值将很高,这个值代表了1个行被索引值读的次数,很低的值表明增加索引得到的性能改善不高,因为索引并不经常使用。  
`Handler_read_rnd_next`的值高则意味着查询运行低效,并且应该建立索引补救。这个值的含义是在数据文件中读下1行的请求数。如果正进行大量的表扫描,`Handler_read_rnd_next`的值较高,则通常说明表索引不正确或写入的查询没有利用索引。
##两个简单实用的优化方法##
###定期分析表和检查表###
分析表的语法如下:

<pre>analyze [local|no_write_to_binlog] table table_name,[,table_name]...</pre>

本语句用于分析和存储表的关键字分步,分析的结果将使的系统得到准确的统计信息,使得SQL能够生成正确的执行计划。在分析期间,使用1个读取锁定对表进行锁定,这对于MyISAM、BDB和Innodb表有作用。对于MyISAM表,本语句与使用myismchk -a相当。  

检查表的语法如下:

<pre>check table table_name [,table_name]...[option]...option={quick|fast|medium|extended|changed}</pre>

检查表的作用是检查1个或多个表是否有错误,check table对MyISAM和Innodb表有作用。对于MyISAM表,关键字统计数据被更新。  
check table也可以检查视图是否有错误,比如在视图定义中被引用的表已不存在。
###定期优化表###
优化表的语法如下:

<pre>optimize [local|no_write_to_binlog] table table_name [,table_name]...</pre>

如果已经删除了表的1大部分,或者如果已经对含有可变长度行的表(含有varchar、blob或text列的表)进行了很多更改,则使用optimize table命令来进行表优化。这个命令可以将表中的空间碎片进行合并,并且可以消除由于删除或者恒心造成的空间浪费,但optimize table命令只对MyISAM、BDB和Innodb表起作用。
##常用SQL优化##
###大批量插入数据###
当用load命令导入数据的时候,适当的设置可以提高导入的速度。对于MyISAM存储引擎的表,可以通过以下方式快速的导入大量的数据。

<pre>alter table table_name disable key;
loading the data
alter table table_name enable keys;
</pre>

diable keys和enable keys用来打开或者关闭MyISAM表非唯一索引的更新。在导入大量的数据到1个非空的MyISAM表时,通过设置这2个命令,可以提高导入的效率。对于导入大量数据到1个空的MyISAM表,默认是先导入数据然后才创建索引的,所以不用进行设置。  
对于Innodb类型的表,是按照铸件的顺序保持的,所以导入的数据按照主键的顺序排序,可以有效地提高导入数据的效率。  
在导入数据前执行`set unique_check=0`,关闭唯一性检验,在导入结束后执行`set unique_check=1`,恢复唯一性校验,可以提高导入的效率。  
如果应用使用自动提交的方式,建议在导入前执行`set autocommit=0`,关闭自动提交,导入结束后再执行`set autocommit=1`，打开自动提交,也可以提高导入的效率。
###优化insert语句###
当进行数据insert的时候,可以考虑采用如下几种优化方式:

1. 如果同时从同一客户插入很多行,尽量使用多个值表的insert语句,这种方式将大大缩减客户端与数据库之间的连接、关闭等消耗,使得效率比分开执行的单个insert语句快。
2. 从不同客户插入很多行,能通过使用insert delayed语句得到更快的速度。delayed的含义是让insert语句马上执行,其实数据都被放在内存的队列中,并没有真正写入磁盘。
3. 将索引文件和数据文件分在不同的磁盘上存放,利用建表中的选项。
4. 如果进行批量插入,可以增加`bulk_insert_buffer_size`变量值的方法来提高速度,但是只对MyISAM表使用。
5. 当从1个文件文件装载1个表时,使用load data infile,比使用很多insert语句快20倍。

###优化group by语句###
默认情况下,Mysql对所有的group by 列1,列2...的字段进行排序,这与在查询中指定order by 列1,列2...类似。因此,如果显式包括1个包含相同的列的order by子句,则对Mysql的实际执行性能没有任何影响。  
如果查询包括group by但用户想要避免排序结果的消耗,则可以指定order by null禁止排序。

###优化order by语句###
在某些情况下,Mysql可以使用1个索引来满足order by子句,而不需要额外的排序。where条件和order by使用相同的索引,并且order by的顺序与索引顺序相同,并且order by的字段都是升序或者都是降序。

###MySQL优化or条件###
对于含有or的查询子句,如果要利用索引,则or之间的每个条件列都必须用到索引:如果没有索引,则应该考虑增加索引。

###使用SQL提示###
下面是一些在Mysql中常用的SQL提示:

####use index####
在查询语句中表名的后面,添加use index来提供希望Mysql去参考的索引列表,就可以让Mysql不再考虑其他可用的索引。
####ignore index####
如果用户只是想单纯地让Mysql忽略1个或者多个索引,则可以使用ignore index作为HINT。
####force index####
为强制Mysql使用1个特定的索引,可在查询中使用force index作为HINT。