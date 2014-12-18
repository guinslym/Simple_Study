数据类型.md
PostgreSQL有着丰富的内置数据类型可用。 用户还可以使用CREATE TYPE命令增加新的数据类型。

Table 8-1显示了所有内置的普通数据类型。 在"别名"列里列出的大多数可选名字都是因历史原因 PostgreSQL在内部使用的名字。 另外，还有一些内部使用的或者废弃的类型也可以使用，但没有在这里列出。

<h4>Table 8-1. 数据类型</h4>

|名字|别名|	描述|
|------|------|---------|
|bigint|	int8|	有符号8字节整数|
|bigserial|	serial8	|自增8字节整数|
|bit [ (n) ]	| 	|定长位串|
|bit varying [ (n) ]	|varbit	|变长位串|
|boolean	|bool	|逻辑布尔值（真/假）|
|box	| |	平面中的矩形|
|bytea|	| 	二进制数据（"字节数组"）|
|character varying [ (n) ]|	varchar [ (n) ]|	变长字符串|
|character [ (n) ]|	char [ (n) ]|	定长字符串|
|cidr|	| 	IPv4或IPv6网络地址|
|circle||	 	平面中的圆|
|date	 |	|日历日期（年，月，日）|
|double precision	|float8	(8 bytes)|双精度浮点数字（8字节）|
|inet	| |	IPv4或IPv6网络地址|
|integer|	int, int4	|有符号4字节整数|
|interval |[ fields ] [ (p) ]	 	|时间间隔|
|line	| |	平面中的无限长直线|
|lseg| |	平面中的线段|
|macaddr|	| 	MAC地址|
|money|	| 	货币金额|
|numeric [ (p, s) ]|	decimal [ (p, s) ]|	可选精度的准确数字|
|path	| |	平面中的几何路径|
|point|	 |	平面中的点|
|polygon|	| 	平面中的封闭几何路径|
|real|	float4(4 bytes)|单精度浮点数（4字节）|
|smallint	|int2	|有符号2字节整数|
|serial	|serial4	|自增4字节整数|
|text|	| 	变长字符串|
|time [ (p) ] [ without time zone ]|	| 	一天中的时间（没有时区）|
|time [ (p) ] with time zone	timetz||	一天里的时间，包括时区|
|timestamp [ (p) ] [ without time zone ]||	 	日期和时间（没有时区）|
|timestamp [ (p) ] with time zone|	timestamptz	|日期和时间，包括时区|
|tsquery|	 |	全文检索查询|
|tsvector	| |	全文检索文件|
|txid_snapshot|	 	|用户级事务ID快照|
|uuid	|| 	通用唯一标识符|
|xml|	| 	XML数据|

兼容性: 下列类型(或者那样拼写的)是SQL声明的： bigint，bit，bit varying，boolean，char，character varying， character，varchar，date，double precision，integer， interval，numeric，decimal，real，smallint，time (有时区和无时区)，timestamp(有时区和无时区)，xml。

每种数据类型都有一个由其输入和输出函数决定的外部表现形式。 许多内建的类型有明显的格式。  
不过，许多类型要么是PostgreSQL所特有的， 比如几何路径，要么是有几种可能的格式，比如日期和时间类型。
有些输入和输出函数是不可逆的。 也就是说，输出函数的输出结果和原始的输入比较的时候可能丢失精度。

##数值类型##
数值类型由2，4或8字节的整数以及4或8字节的浮点数和可选精度的小数组成。 Table 8-2列出了所有可用类型。

<h4>Table 8-2. 数值类型</h4>

|名字	|存储空间|	描述|	范围|
|--------|-------------|---------|--------|
|smallint|	2字节	|小范围整数	|-32768到+32768|
|integer|	4字节|	常用的整数|	-2147483648到+2147483647|
|bigint|	8字节|	大范围的整数|	-9223372036854775808到9223372036854775807|
|decimal|	变长|	用户声明精度，精确	|无限制|
|numeric|	变长|	用户声明精度，精确	|无限制|
|real|	4字节|	变精度，不精确	|6位十进制数字精度(单精度)|
|double precision|8字节|变精度，不精确|15位十进制数字精度(双精度)|
|serial	|4字节|	自增整数|	1到2147483647|
|bigserial|	8字节|	大范围的自增整数|	1到9223372036854775807|

数值类型常量的语法在Section 4.1.2里描述。 数值类型对应有一套完整的数学操作符和函数。

###整数类型###

smallint，integer，bigint类型存储各种范围的全部是数字的数， 也就是没有小数部分的数字。试图存储超出范围以外的数值将导致一个错误。

常用的类型是integer，因为它提供了在范围、存储空间、性能之间的最佳平衡。  
一般只有在磁盘空间紧张的时候才使用smallint。 而只有在integer的范围不够的时候才使用bigint，因为前者绝对快得多。

在很小的操作系统上，bigint类型可能无法正常工作，因为它依赖编译器对八字节整数的支持。  
在那些没有八字节整数支持的机器上， bigint的作用和integer一样(但是仍然占据八字节存储)。

SQL只声明了整数类型integer(或int)和smallint,bigint。 类型别名int2，int4，int8都是扩展，并且也在许多其它SQL数据库系统中使用。

###任意精度数值###

numeric类型可以存储最多1000位精度的数字并且准确地进行计算。 我们特别建议将它用于货币金额和其它要求精确计算的场合。
不过，numeric类型上的算术运算比整数类型或者我们下一节描述的浮点数类型要慢很多。

我们使用下述术语： 一个numeric类型的标度(scale)是小数部分的位数，精度(precision)是全部数据位的数目， 也就是小数点两边的位数总和。因此数字23.5141的精度为6而标度为4。你可以认为整数的标度为零。

numeric字段的最大精度和最大标度都是可以配置的。 要声明一个字段的类型为numeric，你可以用下面的语法：

```
NUMERIC(precision, scale)
```

精度必须为正数，标度可以为零或者正数。另外，

```
NUMERIC(precision)
```

选择了标度为0.具体说明：

NUMERIC
则创建一个可以存储一个直到实现精度上限的任意精度和标度的数值， 一个这样类型的字段将不会把输入数值转化成任何特定的标度， 而带有标度声明的numeric字段将把输入值转化为该标度。  
SQL标准要求缺省的标度是 0(也就是转化成整数精度)。 我们觉得这样做有点没用。如果你关心移植性，那你最好总是明确声明精度和标度。

如果一个要存储的数值的标度比字段声明的标度高， 那么系统将尝试圆整(四舍五入)该数值到指定的小数位。  
然后，如果小数点左边的数据位数超过了声明的精度减去声明的标度，那么将抛出一个错误。

numeric类型的数据值在物理上是不带任何前导或者后缀零的形式存储的。 因此，字段上声明的精度和标度都是最大值，而不是固定分配的。  
在这个方面，numeric类型更类似于varchar(n) 而不是char(n)。实际存储是每四个十进制位两个字节， 然后在整个数据上加上八个字节的额外开销。

除了普通的数字值之外，numeric类型允许用特殊值NaN 表示"不是一个数字"。任何在NaN上面的操作都生成另外一个NaN。
如果在 SQL 命令里把这些值当作一个常量写，你必须在其周围放上单引号， 比如U`PDATE table SET x = 'NaN'`。在输入时，字符串NaN是大小写无关的。

Note: 在大多数"not-a-number"概念中，不认为NaN等于其他数值类型（包括NaN）。  
为了能够存储numeric类型的值，并且使用Tree索引， PostgreSQL认为NaN相等，并且大于所有非NaN值。

类型decimal和numeric是等效的。 两种类型都是SQL标准。

###浮点数类型###

数据类型real和double precision是不精确的、变精度的数字类型。  
实际上，这些类型是IEEE754标准二进制浮点数算术(分别对应单和双精度)的一般实现， 外加下层处理器、操作系统和编译器对它的支持。

不精确意味着一些数值不能精确地转换成内部格式并且是以近似值存储的， 因此存储后再把数据打印出来可能有一些差异。  
处理这些错误以及这些错误是如何在计算中传播的属于数学和计算机科学的一个完整的分支：

- 如果你要求精确的计算(比如计算货币金额)，应使用numeric类型。
- 如果你想用这些类型做任何重要的复杂计算， 尤其是那些你对范围情况(无穷/下溢)严重依赖的事情，那你应该仔细评诂你的实现。
- 拿两个浮点数值进行相等性比较可能不像你想像那样运转。

在大多数平台上，real类型的范围是至少1E-37到1E+37， 精度至少是6位小数。  
double precision的范围通常是1E-307到1E+308， 精度是至少15位数字。太大或者太小的数值都会导致错误。  
如果输入数据的精度太高，那么将会发生圆整。太接近零的数字， 如果无法与零值的表现形式相区分就会产生下溢错误。

除了普通的数字值之外，浮点类型还有几个特殊值：

- Infinity
- Infinity
- NaN

这些值分别表示IEEE 754特殊值"正无穷大"、"负无穷大"、 "不是一个数字"。  
在不遵循IEEE 754浮点算术的机器上， 这些值的含义可能不是预期的。  
如果在SQL命令里把这些数值当作常量写， 你必须在它们周围放上单引号，像这样`UPDATE table SET x = 'Infinity'`。 输入时，这些值是以大小写无关的方式识别的。  
Note: IEEE754声明NaN不应该等于任何其他浮点值（包括NaN）。 为了能存储浮点值，并且使用Tree索引，PostgreSQL认为NaN相等，并且大于所有非NaN值。

PostgreSQL还支持SQL标准表示法float和float(p)用于声明非精确的数值类型。  
其中的p声明以二进制位表示的最低可接受二进制精度。 在选取real类型的时候， PostgreSQL接受float(1)到float(24)， 在选取double precision的时候， 接受float(25) 到float(53)。  
在允许范围之外的p值将导致一个错误。 没有声明精度的float将被当作double precision。

Note: PostgreSQL7.4以前， 在float(p)里面 的精度会被当作是这么多位小数的十进制位。 到7.4已经被修改成与SQL标准匹配，标准声明这个精度是以二进制位度量的。  
假设real和double precision分别有24和53个二进制位的位数对 IEEE 标准的浮点实现来说是正确的。  
在非IEEE平台上， 这个数值可能略有偏差，但是为了简化，我们在所有平台上都用了同样的p值范围。

###序列号类型###

serial和bigserial类型不是真正的类型， 只是为在表中设置唯一标识做的概念上的便利。 类似其它一些数据库中的AUTO_INCREMENT属性。 在目前的实现中，下面一个语句：

```
CREATE TABLE tablename (
    colname SERIAL
);
```

等价于声明下面几个语句：

```
CREATE SEQUENCE tablename_colname_seq;
CREATE TABLE tablename (
    colname integer NOT NULL DEFAULT nextval('tablename_colname_seq')
);
ALTER SEQUENCE tablename_colname_seq OWNED BY tablename.colname;
```

因此，我们就创建了一个整数字段并且把它的缺省数值安排为从一个序列发生器读取。应用了一个NOT NULL约束以确保NULL不会被插入。  
在大多数情况下你可能还希望附加一个UNIQUE或PRIMARY KEY约束避免意外地插入重复的数值， 但这个不是自动的。  
最后，将序列发生器"从属于"那个字段， 这样当该字段或表被删除的时候也一并删除它。

Note: PostgreSQL7.3以前， serial隐含UNIQUE。 但现在不再如此。如果你希望一个序列字段有一个唯一约束或者一个主键， 那么你现在必须声明，就像其它数据类型一样。

要在serial字段中插入序列中的下一个数值， 主要是要注意serial字段应该赋予缺省值。 我们可以通过在INSERT语句中把该字段排除在字段列表之外来实现， 也可以通过使用DEFAULT关键字来实现。

类型名serial和serial4是等效的： 两者都创建integer字段。 类型名bigserial和serial8也一样， 只不过它创建一个bigint字段。 如果你预计在表的生存期中使用的标识数目可能超过231个， 那么你应该使用bigserial。

一个serial类型创建的序列在所属的字段被删除的时候自动删除。 你可以只删除序列而不删除字段，不过这将删除该字段的缺省值表达式。

##货币类型##
money类型存储带有固定小数精度的货币金额。 小数精度由lc_monetary的设置来决定。  
可以以任意格式输入，包括整型，浮点型，或者典型的货币格式，如`$1,000.00`。 根据区域字符集，输出一般是最后一种形式。  
通过将整数值转换成text类型，再转换成money类型的方式， 将不带引号的数值转换成money类型。

```
SELECT 1234::text::money;
```

在缺少区域语言支持的条件下，反向将money值转换成数值类型是很麻烦的。 如果知道货币符号和千位分隔符，你可以使用regexp_replace()：

```
SELECT regexp_replace('52093.89'::money::text, '[$,]', '', 'g')::numeric;
```

由于输出的数据类型对语言环境要求很细，因此，lc_monetary设置的不同可能会造成 无法将money数据输入到数据库中。  
为了避免这种问题的发生，在向一个新数据库进行转储之前，确保lc_monetary与原数据库相同，或具有等价值。

Table 8-3. 货币类型

|名字|	存储容量|	描述|	范围|
|-------|---------------|---------|-------|
|货币|	8字节	|货币金额	|-92233720368547758.08到+92233720368547758.07|

##字符类型##
Table 8-4. 字符类型

|名字|	描述|
|-------|---------|
|character varying(n), varchar(n)	|变长，有长度限制|
|character(n), char(n)	|定长，不足补空白|
|text	|变长，无长度限制|

Table 8-4显示了在PostgreSQL里可用于一般用途的字符类型。

SQL定义了两种基本的字符类型： character varying(n)和character(n)， 这里的n是一个正整数。  
两种类型都可以存储最多n个字符的字符串（没有字节）。 试图存储更长的字符串到这些类型的字段里会产生一个错误， 除非超出长度的字符都是空白，这种情况下该字符串将被截断为最大长度。  
这个看上去有点怪异的例外是SQL标准要求的。 如果要存储的字符串比声明的长度短， 类型为character的数值将会用空白填满； 而类型为character varying的数值将只是存储短些的字符串。

如果我们明确地把一个数值转换成character varying(n)或character(n)， 那么超长的数值将被截断成n个字符，且不会抛出错误。 这也是SQL标准的要求。

varchar(n)和char(n)分别是character varying(n)和character(n)的别名， 没有声明长度的character等于character(1)； 如果不带长度说明词使用character varying， 那么该类型接受任何长度的字符串。后者是PostgreSQL的扩展。

另外，PostgreSQL提供text类型， 它可以存储任何长度的字符串。尽管类型text不是SQL标准， 但是许多其它SQL数据库系统也有它。

character类型的数值物理上都用空白填充到指定的长度n并且以这种方式存储和显示。 不过，填充的空白在是无语意的。  
在比较两个character值的时候， 填充的空白都不会被关注，在转换成其它字符串类型的时候，character值里面的空白会被删除。 请注意，在character varying和text数值里， 结尾的空白是有语意的。

在一个简短的字符串（最多126个字节）的存储要求是1个字节加上实际的字符串， 其中包括空格填充的character。 更长的字符串有4个字节的开销，而不是1。    长的字符串将会自动被系统压缩，因此在磁盘上的物理需求可能会更少些。 更长的数值也会存储在后台表里面，这样它们就不会干扰对短字段值的快速访问。  
不管怎样，允许存储的最长字符串大概是1GB 。 允许在数据类型声明中出现的n的最大值比这还小。  
修改这个行为没有什么意义，因为在多字节编码下字符和字节的数目可能差别很大。  
如果你想存储没有特定上限的长字符串，那么使用text或没有长度声明词的character varying，而不要选择一个任意长度限制。

Tip: 这三种类型之间没有性能差别，除了当使用填充空白类型时的增加存储空间， 和当存储长度约束的列时一些检查存入时长度的额外的CPU周期。  
虽然在某些其它的数据库系统里，character(n)有一定的性能优势， 但在PostgreSQL里没有。  
事实上，character(n)通常是这三个中最慢的，因为额外存储成本。 在大多数情况下，应该使用text或character varying 。

 数据库的字符集决定用于存储文本值的字符集。

Example 8-1. 使用字符类型

```
CREATE TABLE test1 (a character(4));
INSERT INTO test1 VALUES ('ok');
SELECT a, char_length(a) FROM test1; -- (1)
```

<pre>
  a   | char_length
------+-------------
 ok   |           2
</pre>

```
CREATE TABLE test2 (b varchar(5));
INSERT INTO test2 VALUES ('ok');
INSERT INTO test2 VALUES ('good      ');
INSERT INTO test2 VALUES ('too long');
ERROR:  value too long for type character varying(5)
INSERT INTO test2 VALUES ('too long'::varchar(5)); -- explicit truncation
SELECT b, char_length(b) FROM test2;
```

<pre>
   b   | char_length
-------+-------------
 ok    |           2
 good  |           5
 too l |           5
(1)
</pre>

在PostgreSQL里另外还有两种定长字符类型， 在Table 8-5里显示。 name类型只用于在内部系统表中存储标 识符并且不是给一般用户使用的。该类型长度当前定为64字节(63可用字符加结束符) 但应该在C的源代码中使用常量NAMEDATALEN引用。  
这个长度是在编译的时候设置的，因而可以为特殊用途调整， 缺省的最大长度在以后的版本可能会改变。  
类型"char" (注意引号)和char(1)是不一样的， 它只用了一个字节的存储空间。它在系统内部用于系统表当做穷人的枚举类型用

Table 8-5. 特殊字符类型

|名字|	存储空间|	描述|
|-------|---------------|-------|
|"char"|	1字节|	单字节内部类型|
|name|	64字节|	用于对象名的内部类型|

##二进制数据类型##
bytea数据类型允许存储二进制字符串。

Table 8-6. 二进制数据类型

|名字|	存储空间|	描述|
|------|-----|-------|
|bytea|1或4字节加上实际的二进制字符串|变长的二进制字符串|

二进制字符串是一个字节序列。二进制字符串和普通字符字符串的区别有两个：
首先，二进制字符串完全可以存储字节零值以及其它"non-printable"字节 (定义在32到126范围之外的字节)。  
字符串不允许字节零值， 并且也不允许那些不附合选定的字符集编码的非法字节值或者字节序列。
第二，对二进制字符串的处理实际上就是处理字节，而对字符串的处理则取决于区域设置 。  
简单说，二进制字符串适用于存储那些程序员认为是"raw bytes"的数据， 而字符串适合存储文本。

bytea类型支持两种输入输出的外部格式： "hex"格式和PostgreSQL的历史"escape"格式。  
这两种格式通常在输入中使用，输出格式由bytea_output配置参数决定，默认是hex。 （需要注意的是hex格式是在PostgreSQL9.0中引入的， 早期版本和一些工具中不识别）

SQL 标准定义了一个不同的二进制字符串格式， 称为BLOB或BINARY LARGE OBJECT。 输入格式与bytea不同，但提供的函数和操作符基本一致。

###bytea十六进制格式###

"hex"格式将二进制数据编码为每字节2位十六进制数字， 最重要的四位（半字节）放在开始。  
整条字符串以\x开始（与逃逸格式相区别）。 在某些情况下，最初的反斜杠需要再写一次，以逃逸， 有时，在逃逸格式中，反斜杠需要写两个，下面会详细介绍。

- 十六进制数字可以大写也可以小写，并且数字对之间允许有空格（但不能是在一个数对， 也不能是在\x起始序列）。
-  十六进制格式能够与许多的外部应用程序和协议兼容，并且转换往往比逃逸快，因此更倾向于这种用法。

例子:

```
SELECT E'\\xDEADBEEF';
```

###bytea逃逸格式###

对于bytea格式来说， "escape"格式是一种传统的PostgreSQL格式。 它采用以ASCII字符序列来表示二进制串的方法， 同时将那些无法表示成ASCII字符的二进制串转换成特殊的逃逸序列。
从应用的角度看，如果代表字节的字符有意义，那么这种表示方法会很方便。  
但实际上，这样做会模糊二进制字符串和字符字符串之间的关系，从而造成困扰，同时筛选出的逃逸机制 会显得很臃肿。因此对一些新应用应该恰当的避免这种格式。

当以逃逸格式录入bytea值时，某些值的八位字节必须被逃逸， 同时所有的八位字节值可以被逃逸。  
一般情况下，逃逸一个八位字节时，将它转换成 反斜杠+三位八进制值的形式（或两个反斜杠，如果用逃逸字符穿语法将值写成文本形式）。  
另外，反斜杠本身（字节值92）可以用双反斜杠表示。 Table 8-7给出了必须逃逸的字符串，和替代的逃逸序列（如适用）。

Table 8-7. bytea八进制文本逃逸

|十进制数值|	描述|	输入逃逸形式|	例子|	输出形式|
|----|---|---|---|---|
|0	|八进制的零|	E'\\000'|	SELECT E'\\000'::bytea;	|\000|
|39	|单引号|	''''或E'\\047'|	SELECT E'\''::bytea;	|'|
|92|	反斜杠|	E'\\\\' or E'\\134'|	SELECT E'\\\\'::bytea;|	\\|
|0 到 31 和 127 到255|	"不可打印"字节|	E'\\xxx' (八进制值)|	SELECT E'\\001'::bytea;|	\001|

逃逸不可打印字节的要求因区域设置而异。 在某些场合下，你可以不逃逸它们。 请注意Table 8-7里的每个例子都是刚好一个字节长， 虽然字节零和反斜杠输出形式比一个字符要长。

你必须写这么多反斜杠的原因，如Table 8-7所示， 是因为一个写成字符串文本的输入字符串必须通过PostgreSQL服务器里的两个分析阶段。
每一对反斜杠中的第一个会被字符串文本分析器 理解成一个逃逸字符而消耗掉，于是剩下的第二个反斜杠被bytea输入函数当作 一个三位八进制值或者是逃逸另外一个反斜杠的开始。  
比如，一个传递给服务器的字符串文本E'\\001'在通过 字符串分析器之后会当作\001发送给 bytea输入函数，在这里它被转换成一个十进制值为 1 的单个字节。  
请注意，单引号字符(')不会被bytea特殊对待， 它遵循字符串文本的普通规则。

Bytea字节也在输出中逃逸。 通常，每个"不可打印"的字节值都 转化成对应的前导反斜杠的三位八进制数值。  
大多数"可打印"字节值是以客户端字符集的标准表现形式出现的。 十进制值为 92(反斜杠)的字节在输出形式增加一倍。

Table 8-8. bytea输出逃逸序列

|字节的十进制	|描述|	逃逸的输出形式	|例子|	输出结果|
|---|---|---|---|---|
|92	|反斜杠|	\\	|SELECT E'\\134'::bytea;|	\\|
|0 to 31 and 127 to 255|	"不可打印"八进制字符|	\xxx (八进制值)	|SELECT E'\\001'::bytea;	|\001|
|32 to 126|	"可打印"八进制字符|	客户端字符集表现形式|	SELECT E'\\176'::bytea;	|~|

根据你使用的前端不同，在是否逃逸bytea字符串的问题上你可能有一些额外的工作要做。 比如，如果你的接口自动转换换行和回车，那你可能还要逃逸它们。

##日期/时间类型##
Table 8-9显示了PostgreSQL支持的SQL中所有日期和时间类型。

Table 8-9. 日期/时间类型

|名字|	存储空间|	描述|	最低值|	最高值|	分辨率|
|-----|---|---|---|---|---|
|timestamp [ (p) ] [ without time zone ]|	8字节	|日期和时间（无时区）|	4713 BC	|294276 AD|	1毫秒/14位|
|timestamp [ (p) ] with time zone	|8字节	|日期和时间，带时区	|4713 BC	|294276 AD|	1毫秒/14位|
|date	|4字节|	只用于日期	|4713 BC	|5874897 AD	|1天|
|time [ (p) ] [ without time zone ]	|8字节	|只用于时间|	00:00:00	|24:00:00	|1毫秒/14位|
|time [ (p) ] with time zone|	12字节	|只用于一日内时间，带时区|	00:00:00+1459|	24:00:00-1459	|1毫秒/14位|
|interval [ fields ] [ (p) ]	|12字节	|时间间隔|	-178000000年|	178000000年|	1毫秒/14位|

Note: SQL标准要求仅仅将timestamp类型等于timestamp without time zone类型，（7.3之前的版本将其看做timestamp with time zone）

time，timestamp和interval 接受一个可选的精度值p以指明秒域中小数部分的位数。  
没有明确的缺省精度， p的范围对timestamp 和interval类型是从0到大约6。

Note: 如果timestamp数值是以双精度浮点数(目前的缺省)的方式存储的， 微秒的精度是可以通过全方位的价值观。当timestamp值存储为双精度浮点数（1过时的编译时间选项），那么有效精度会小于6。  
timestamp值是以2000-01-01午夜之前或之后的秒数存储的， 而微秒的精度是为那些在2000-01-01前后几年的日期实现的，对于那些远一些的日子，精度会下降。  
但当timestamp值是使用浮点实现数字，日期内取得几微秒精度。
请注意，在以浮点数存储的时候，随着时间间隔的增加，timestamp数值的精度会降低。 如上图所示：从公元前4713年至5874897 AD。

相同的编译时间选项也决定是否time和interval值存储为 浮点数或8字节的整数。在浮点运算的情况下，大interval值降低 精密的间隔增加的大小。

对于time类型，如果使用了八字节的整数存储， 那么p允许的范围是从0到6， 如果使用的是浮点数存储，那么这个范围是0到10。

interval类型有一个额外的选项，用于通过写这些词组之一，限制存储领域；

- YEAR
- MONTH
- DAY
- HOUR
- MINUTE
- SECOND
- YEAR TO MONTH
- DAY TO HOUR
- DAY TO MINUTE
- DAY TO SECOND
- HOUR TO MINUTE
- HOUR TO SECOND
- MINUTE TO SECOND

需要注意的是，如果同时声明了fields和p， fields必须包括SECOND，因为精度只适用于秒。

time with time zone类型是SQL标准定义的， 但是完整定义的有些方面会导致有问题的用法。  
在大多数情况下，date，time，timestamp without time zone和timestamp with time zone的组合就应该 能提供一切应用需要的日期/时间的完整功能。

abstime和reltime类型是低分辨率类型， 它们被用于系统内部。我们反对你使用这些类型， 因为这些旧类型的部分或全部可能会在未来的版本里消失。

###日期/时间输入###

日期和时间的输入几乎可以是任何合理的格式， 包括 ISO-8601 格式、SQL-兼容格式、传统POSTGRES格式、其它的形式。  
对于一些格式，日期输入里的月和日可能会让人迷惑， 因此系统支持自定义这些字段的顺序。  
把DateStyle参数设置为MDY就按照"月-日-年"解析， 设置为DMY就按照"日-月-年"解析，设置为YMD就按照"年-月-日"解析。

PostgreSQL在处理日期/时间输入上 比SQL标准要求的更灵活。 参阅Appendix B获取关于日期/时间输入的 准确分析规则和可识别文本字段，包括月份、星期几、时区。

请记住任何日期或者时间的文本输入需要由单引号包围， 就像一个文本字符串一样。 SQL要求使用下面的语法：

<pre>
type [ (p) ] 'value'
</pre>

可选精度声明中的p是一个整数， 表示在秒域中小数部分的位数，我们可以对 time,timestamp,和interval类型声明精度。  
允许的精度在上面已经说明。如果在常量声明中没有声明精度，缺省是文本值的精度。

###日期###

Table 8-10显示了date类型可能的输入方式。

Table 8-10. 日期输入

|例子|	描述|
|------|--------|
|1999-01-08	|ISO 8601格式(建议格式)，任何方式下都是1999年1月8号|
|January 8, 1999|	在任何datestyle输入模式下都无歧义|
|1/8/1999	|在MDY下是一月八号；在DMY模式下是八月一日|
|1/18/1999|	MDY 模式下是一月十八日，其它模式下被拒绝|
|01/02/03|	MDY模式下的2003年1月2日；DMY模式下的2003年2月1日；YMD模式下的2001年2月3日|
|1999-Jan-08|	任何模式下都是1月8日|
|Jan-08-1999|	任何模式下都是1月8日|
|08-Jan-1999|	任何模式下都是1月8日|
|99-Jan-08|	YMD模式下是1月8日，否则错误|
|08-Jan-99|	一月八日，除了在YMD模式下是错误的之外|
|Jan-08-99|	一月八日，除了在YMD模式下是错误的之外|
|19990108|	ISO 8601；任何模式下都是1999年1月8日|
|990108|	ISO 8601；任何模式下都是1999年1月8日|
|1999.008	|年和年里的第几天|
|J2451187	|儒略日|
|January 8, 99 BC	|公元前99年|

###时间###

当日时间类型是time [ (p) ] without time zone和 time [ (p) ] with time zone。 只写time等效于time without time zone。

这些类型的有效输入由当日时间后面跟着可选的时区组成( 参阅Table 8-11和Table 8-12)。  
 如果在time without time zone类型的输入中声明了时区， 那么它会被悄悄地忽略。  
 同样指定的日期也会被忽略， 除非使用了一个包括夏令时规则的时区名，比如 America/New_York，在这种情况下， 必须指定日期以确定这个时间是标准时间还是夏令时。 时区偏移将记录在time with time zone中。

Table 8-11. 时间输入

|例子|	描述|
|------|--------|
|04:05:06.789|	ISO 8601|
|04:05:06|	ISO 8601|
|04:05	|ISO 860|
|040506|	ISO 8601|
|04:05 AM	|与04:05一样；AM不影响数值|
|04:05 PM	|与16:05一样；输入小时数必须<=12|
|04:05:06.789-8|	ISO 8601|
|04:05:06-08:00	|ISO 8601|
|04:05-08:00|	ISO 8601|
|040506-08|	ISO 8601|
|04:05:06 PST	|缩写的时区|
|2003-04-12 04:05:06 America/New_York	|用名字声明的时区|

Table 8-12. 时区输入

|例子	|描述|
|--------|------|
|PST	|太平洋标准时间(Pacific Standard Time)|
|America/New_York	|完整时区名称|
|PST8PDT|	POSIX风格的时区|
|-8:00	|ISO-8601与PST的偏移|
|-800	|ISO-8601与PST的偏移|
|-8|	ISO-8601与PST的偏移|
|zulu	|军方对UTC的缩写|
|z	|zulu的缩写|

###时间戳###

时间戳类型的有效输入由一个日期和时间的连接组成， 后面跟着一个可选的时区，一个可选的AD或BC。 另外，AD/BC可以出现在时区前面， 但这个顺序并非最佳的。因此

`1999-01-08 04:05:06`和`1999-01-08 04:05:06 -8:00`都是有效的数值，它是兼容 ISO-8601的。另外，也支持下面这种使用广泛的格式;`January 8 04:05:06 1999 PST`被支持。

SQL标准通过"+"或者"-"是否存在来区分timestamp without time zone和timestamp with time zone文本。因此，根据标准，

`TIMESTAMP '2004-10-19 10:23:54'是一个timestamp without time zone，而`TIMESTAMP '2004-10-19 10:23:54+02`是一个timestamp with time zone。  
PostgreSQL从来不会 在确定文本的类型之前检查文本内容， 因此会把上面两个都看做是timestamp without time zone。 因此要保证把上面的第二个当作timestamp without time zone看待， 就要给它明确的类型：

`TIMESTAMP WITH TIME ZONE '2004-10-19 10:23:54+02'，如果一个文本已被确定是timestamp without time zone, PostgreSQL将悄悄忽略任何文本中指出的时区。 因此，生成的日期/时间值是从输入值的日期/时间字段衍生出来的，并且没有就时区进行调整。

对于timestamp with time zone，内部存储的数值总是UTC(全球统一时间，以前也叫格林威治时间 GMT)。 如果一个输入值有明确的时区声明，那么它将用该时区合适的偏移量转换成 UTC 。  
如果在输入字符串里没有时区声明， 那么它就假设是在系统的timezone参数里的那个时区，然后使用这个timezone时区转换成UTC。

如果输出一个timestamp with time zone，那么它总是从UTC转换成当前的timezone时区， 并且显示为该时区的本地时间。要看其它时区的该时间， 要么修改timezone， 要么使用AT TIME ZONE构造 (参阅Section 9.9.3)。

在timestamp without time zone和timestamp with time zone之间的 转换通常假设timestamp without time zone数值应该以timezone本地时间的形式接受或者写出。 其它的时区引用可以用AT TIME ZONE的方式为转换声明。

###特殊值###

PostgreSQL为方便起见支持在 Table 8-13里面显示的几个特殊输入值。 值infinity 和 -infinity是特别在系统内部表示的， 并且将按照同样的方式显示；  
但是其它的都只是符号缩写， 在读取的时候将被转换成普通的日期/时间值。 特别是now和相关的字符串在读取的时候就被转换成对应的数值。  
 所有这些值在 SQL 命令里当作普通常量对待时，都需要写在单引号里面。

Table 8-13. 特殊日期/时间输入

|输入字符串|	适用类型|	描述|
|--|---|---|
|epoch|	date, timestamp|	1970-01-01 00:00:00+00 (UNIX系统零时)|
|infinity|	date, timestamp	|比任何其它时间戳都晚|
|-infinity|	date, timestamp|	比任何其它时间戳都早|
|now|	date, time, timestamp|	当前事务的开始时间|
|today|	date, timestamp	|今日午夜|
|tomorrow|	date, timestamp|	明日午夜|
|yesterday|	date, timestamp	|昨日午夜|
|allballs|	time	|00:00:00.00 UTC|

下列SQL兼容函数也可以用于获取对应数据类型的当前时间值： `CURRENT_DATE`,`CURRENT_TIME`,`CURRENT_TIMESTAMP`, LOCALTIME,LOCALTIMESTAMP。 后四个接受一个可选的精度声明(Section 9.9.4)。不过， 请注意这些SQL函数不是被当作数据输入字符串识别的。

###日期/时间输入###

日期/时间类型的输出格式设成 ISO 8601(默认)、SQL(Ingres)、 传统的POSTGRES(Unix date 格式)、German四种风格之一。 SQL标准要求使用ISO 8601格式。"SQL"输出格式的名字是历史偶然。 Table 8-14显示了每种输出风格的例子。 date和time类型的输出当然只是给出的例子里面的日期和时间部分。

Table 8-14. 日期/时间输入

|风格	|描述	|例子|
|--------|--------|-------|
|ISO	|ISO 8601/SQL标准|	1997-12-17 07:37:16-08|
|SQL	|传统风格|	12/17/1997 07:37:16.00 PST|
|POSTGRES|	原始风格|	Wed Dec 17 07:37:16 1997 PST|
|German	|地区风格	|17.12.1997 07:37:16.00 PST|

如果声明了DMY顺序，那么在SQL和POSTGRES风格里， 日期在月份之前出现，否则月份出现在日期之前(参阅Section 8.5.1看看这个设置如何影响对输入值的解释)。Table 8-15里有一个例子。

Table 8-15. 日期顺序习惯

|datestyle设置|	输入顺序|	输入样例|
|------|-----|-----|-----|
|SQL, DMY	|日/月/年|	17/12/1997 15:37:16.00 CET|
|SQL, MDY	|月/日/年|	12/17/1997 07:37:16.00 PST|
|Postgres, DMY|	day日/month月/year年	|Wed 17 Dec 07:37:16 1997 PST|

用户可以用SET datestyle命令选取日期/时间的风格， 也可以在配置文件postgresql.conf中的DateStyle参数中设置， 或者在服务器或客户端的PGDATESTYLE环境变量中设置。 我们也可以用格式化函数to_char(参见Section 9.8)来更灵活地控制时间/日期地输出。

<h3>时区</h3>

时区和时区习惯不仅仅受地球几何形状的影响，还受到政治决定的影响。
到了19世纪，全球的时区变得稍微标准化了些，但是还是易于遭受随意的修改 ，部分是因为夏时制规则。  
PostgreSQL使用广泛 使用的zoneinfo时区信息数据库有关历史的时区规则。在未来，假设是已知的对于一个给定的时区的最新规则会被继续无限期的遵守。

PostgreSQL在典型应用中尽可能与SQL的定义相兼容。 但SQL标准在日期/时间类型和功能上有一些奇怪的混淆。 两个显而易见的问题是：

- date类型与时区没有联系，而time类型却有或可以有。
- 然而，现实世界的时区只有在与时间和日期都关联时才有意义， 因为时间偏移量(时差)可能因为实行类似夏时制这样的制度而在一年里有所变化。

缺省的时区用一个数字常量表示与UTC的偏移(时差)。 因此，当跨DST(夏时制)界限做日期/时间算术时， 我们根本不可能把夏时制这样的因素计算进去。

为了克服这些困难，我们建议在使用时区的时候，使用那些同时包含日期和时间的日期/时间类型。  
我们建议不使用time with time zone类型( 尽管PostgreSQL出于合理应用以及为了与其它RDBMS兼容的考虑支持这个类型)。  
PostgreSQL假设你用于任何类型的本地时区都只包含日期或时间(而不包含时区)。

在系统内部，所有日期和时间都用全球统一时间UTC格式存储， 时间在发给客户前端前由数据库服务器根据timezone配置参数声明的时区转换成本地时间。

PostgreSQL允许使用三种方法指定时区：

完整的时区名，例如America/New_York.所有可以识别的时区名在pg_timezone_names视图中列出 (参见Section 45.60)。  
PostgreSQL使用广泛使用的zoneinfo时区数据， 所以这些时区名在其它软件里也能被轻松的识别。

时区缩写。例如PST。 这种缩写名通常只是定义了相对于UTC的偏移量， 而前一种完整的时区名可能还隐含着一组夏时制转换规则。 所有可以识别的时区缩写在`pg_timezone_abbrevs`视图中列出(参见Section 45.59)。  
你不能使用时区缩写来设置timezone或log_timezone配置参数， 但是你可以在日期/时间输入值中结合AT TIME ZONE操作符使用时区缩写。

除完整的时区名及其缩写之外，PostgreSQL还接受POSIX风格的STDoffset 或 STDoffsetDST格式的时区， 其中的STD是时区缩写、offset是一个相对于UTC的小时偏移量、 DST是一个可选的夏时制时区缩写(假定相对于给定的偏移量提前一小时)。  
例如，如果EST5EDT不是一个已识别的时区名，那么它将等同于美国东部时间。
如果存在夏时制时区名是当前时区名， 根据zoneinfo时区数据库的posixrules条目中相同的夏时制事务规则，可以考虑使用这个特性。  
在一个PostgreSQL标准安装中， posixrules与US/Eastern相同，因此POSIX格式的时区声明遵循USA夏时制规则。 如果需要，可以通过替换posixrules文件来调整该习惯。

总之，完整的时区名与时区缩写在理论与实践之间存在差异：  
时区缩写总是代表一个相对于UTC的固定偏移量， 然而大多数完整的时区名隐含着一个本地夏令时规则， 因此就有可能有两个相对于UTC的不同偏移量。

需要警惕的是，由于没有合理的时区缩写检查，POSIX格式的时区特点能导致静默的伪输入。 例如，使用SET TIMEZONE TO FOOBAR0时，实际上系统使用的是一个很特别的UTC缩写。
另一个需要注意的是，在POSIX时区名中，积极的偏移用于west格林尼治位置。 在其他地方，PostgreSQL遵循ISO-8601规定，即积极的时区偏移east格林威治。

总体而言，PostgreSQL8.2版本以后时区名在所有情况下 都是大小写无关的。而之前的版本在某些情况下是大小写敏感的。

无论是完整的时区名还是时区缩写都不是硬连接进服务器的， 它们都是从安装目录下的.../share/timezone/和.../share/timezonesets/配置文件中获取的(参见Section B.3)

可以在postgresql.conf文件里设置timezone配置参数， 或者用任何其它在Chapter 18描述的标准方法。除此之外， 还有好几种特殊方法可以设置它：

- 如果既没有在postgresql.conf里也没有在命令行开关 上声明timezone，那么服务器将试图使用服务器主机上的TZ环境变量作为服务器的缺省时区。 - 如果TZ没有定义或者是PostgreSQL不认识的时区名， 那么服务器将试图通过检查C库函数localtime()的行为来判断操作系统的缺省时区.
- 缺省时区是按照最接近PostgreSQL的已知时区的原则来选择的. (如果没有指定，这些规则也可以用来选择默认值log_timezone)。

使用SQL命令SET TIME ZONE为会话设置时区， 这是SET TIMEZONE TO的一个可选的拼写方式， 更加兼容标准。

如果在客户端设置了PGTZ环境变量， 那么libpq在连接时将使用 这个环境变量给后端发送一个SET TIME ZONE命令。

<h3>间隔输入</h3>

interval类型值可以用下面的详细语法写：

<pre>
[@] quantity unit [quantity unit...] [direction]
</pre>

这里quantity是一个数字（可能已标记）； unit可以是microsecond，millisecond，second， minute，hour，day，week， month，year，decade，century，millennium或这些单位的缩写或复数。 direction可以是ago或为空。@标记是可选的。ago否定所有。  
如果IntervalStyle设置为postgres_verbose，那么这个语法同样用于间隔输入。

可以在没有明确单位标记的情况下声明天，小时，分钟和秒。 例如，'1 12:59:10'等同于'1 day 12 hours 59 min 10 sec'。  
同样，可以用一个破折号来声明一个年和月的组合，例如'200-10'等同于'200 years 10 months'.（事实上，SQL标准值允许短的格式，并且当 IntervalStyle设置为sql_standard时,用于输出）。

要么使用ISO 8601标准4.4.3.2的"format with designators"，要么使用4.4.3.3的"alternative format"，间隔值可以写为ISO 8601的时间间隔。 格式如下：

<pre>
P quantity unit [ quantity unit ...] [ T [ quantity unit ...]]
</pre>

字符串必须以P开始，并且可以含有一个T用以指明一天中时间的格式。 可用单位的缩写在Table 8-16有说明。 可以忽略单位，也可以以任意顺序声明，但单位小于一天时必须在T之后。 尤其M的含义依赖于它在T之前或之后。

Table 8-16. ISO8601间隔单位的缩写

|缩写|	含义|
|-----|-----|
|Y	|年|
|M|	月（日期部分）|
|W|周|
|D|	日|
|H|	小时|
|M|	分钟（时间部分）|
|S|	秒|

以缩写格式：

<pre>
P [ years-months-days ] [ T hours:minutes:seconds ]
</pre>

一个字符串必须以P开始，然后以T隔开日期和时间。 给出的值是如同ISO 8601日期的数字。

当用fields规范写一个时间间隔常熟，或将一个字符串标记为用fields规范定义的一个间隔柱时， 未标记单位的解释由fields解释。  
如INTERVAL '1' YEAR读作1年，然而INTERVAL '1'代表1秒。  
同样，fields规范中最低有效字段值规定会被静默的忽略。如，INTERVAL '1 day 2:03:04' HOUR TO MINUTE会导致删除 秒字段，而不是天字段。

根据SQL标准，间隔值的所有字段必须有相同的符号，因此前导负号可以用于所有字段； 如'-1 2:03:04'中负号同时应用于天和小时/分钟/秒。  
PostgreSQL允许字段有不同的标记，并且传统上，文本表述中的每个字段会被认为是独立标记的， 因此在这个例子中的小时/分钟/秒被认为是允许的。  
如果IntervalStyle被设置为sql_standard，那么前导标记被认为是应用于所有字段的 （当然前提是没有再出现其他标记），否则会使用传统的PostgreSQL解释。为了避免这种奇异，建议为每个字段附上一个明确的标记。

PostgreSQL内部，interval值被存储为月，日，秒的格式，这是因为月中包含天，并且如果进行了夏令时调整，那么一天可以有23或25小时。  
当秒字段可以存储分数时，月和天字段可以是整数型。  
由于时间间隔通常是由常量字符串或timestamp减法来定义的， 这种存储方法在大多数情况下很有效。justify_days和justify_hours函数可用于调整溢出正常范围值的天和小时。

在详细的输出格式，以及更紧凑的输入格式中，字段值可以有小数部分，例如'1.5 week'或'01:02:03.45'。  
这种输入被转换成恰当的月，天和秒来存储。  
由于这样会产生小数的月或天，因此在低阶字段中引入了分数，用以1 month = 30 days 和 1 day = 24 hours的转换。 例如，'1.5 month'即1个月15天。输出中，只有秒可以写成分数形式。

Table 8-17中有一些有效的interval输入的例子。

Table 8-17. 间隔输入

|示例	|说明|
|--------|------|
|1-2	|SQL标准格式：一年两个月|
|3 4:05:06	|SQL标准格式：3天4小时5分6秒|
|1 year 2 months 3 days 4 hours 5 minutes 6 seconds	|传统Postgres格式: 1年2个月3天4小时5分钟6秒|
|P1Y2M3DT4H5M6S	ISO 8601 |"带标识符格式":与上面相同含义|
|P0001-02-03T04:05:06	ISO 8601| "缩写格式":与上面相同含义|

<h3>间隔输出</h3>

间隔类型的输出格式可以用命令SET intervalstyle设置为下面四种类型：`sql_standard`，postgres，`postgres_verbose`或iso_8601. 默认是postgres格式，Table 8-18中有每种格式的示例。

sql_standard格式产生的输出结果符合SQL的区间字符串标准， 如果间隔值满足标准的限制（无论年-月，或只有天-时间，没有积极和消极的构成的混合）。  
否则类似一个标准年-月文本字符串后跟有一个天-时间文本字符串的输出，带有添加明确标记的消除歧义混合信号的时间间隔。

postgres格式的输出与PostgreSQL8.4（此时DateStyle参数设置为ISO）之前的输出是一致的。

postgres格式的输出与PostgreSQL8.4（此时DateStyle参数设置为非ISO输出）之前的输出是一致的

iso_8601格式的输出与ISO 8601标准4.4.3.2节中的"format with designators"一致。

Table 8-18. 间隔输出格式示例

|格式|	年-月区间|	天-时间区间|	混合区间|
|-----|----|----|----|
|sql_standard|	1-2|	3 4:05:06|	-1-2 +3 -4:05:06|
|postgres	|1年2个月|	3天04:05:06|	-1年-2个月+3天-04:05:06|
|postgres_verbose|	@1年2个月|	@3天4小时5分6秒|	@1年2个月-3天4小时5分6秒以前|
|iso_8601|	P1Y2M|	P3DT4H5M6S|	P-1Y-2M3DT-4H-5M-6S|

<h3>内部</h3>

PostgreSQL 使用儒略历法计算所有日期/时间， 假设一年的长度是365.2425天。这个方法可以很精确地预计/计算从公元前4713年到很久的未来的任意一天的日期。

19世纪以前的日期传统(历法)只是对一些趣味读物有意义， 而在我们这里好像没有充分的理由把它们编码入日期/时间控制器里面去。

##布尔类型##
PostgreSQL支持SQL标 准的boolean数据类型。查阅Table 8-19。 boolean只能有"true"(真)或"false"(假)两个状态之一， 第三种"unknown"(未知)状态，用NULL表示。

Table 8-19. 布尔数据类型

|名称|	存储格式|	描述|
|------|----|----|
|boolean|	1字节|	真/假|

"真"值的有效文本值是：

<pre>
TRUE
't'
'true'
'y'
'yes'
'on'
'1'
</pre>

对于"假"，你可以使用下面这些：

<pre>
FALSE
'f'
'false'
'n'
'no'
'off'
'0'
</pre>

前导或尾随空白将被忽略，大小写无关紧要。 使用TRUE和FALSE这样的字眼比较好(也是SQL兼容的用法)。
Example 8-2显示了用字母t和f输出boolean值的例子。

Example 8-2. 使用boolean类型

```
CREATE TABLE test1 (a boolean, b text);
INSERT INTO test1 VALUES (TRUE, 'sic est');
INSERT INTO test1 VALUES (FALSE, 'non est');
SELECT * FROM test1;
```

<pre>
 a |    b
---+---------
 t | sic est
 f | non est
</pre>

```
SELECT * FROM test1 WHERE a;
```

<pre>
 a |    b
---+---------
 t | sic est
 </pre>

##枚举类型##
枚举类型是一个包含静态和值的有序集合的数据类型。 等于某些编程语言中的enum类型。 一个枚举类型可以是一周中的天，或者一块数据的状态值的集合。

8.7.1. 枚举类型的声明

用CREATE TYPE创建枚举类型，如：

```
CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');
```

就像其他类型一样，一旦创建，枚举类型可以用于表和函数定义。

```
CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');
CREATE TABLE person (
    name text,
    current_mood mood
);
INSERT INTO person VALUES ('Moe', 'happy');
SELECT * FROM person WHERE current_mood = 'happy';
```

<pre>
 name | current_mood
------+--------------
 Moe  | happy
(1 row)
</pre>

<h3>排序</h3>

枚举类型中，值的顺序是创建枚举类型是定义的顺序。 所有的比较标准运算符及其相关的聚集函数都可支持枚举类型，例如：

```
INSERT INTO person VALUES ('Larry', 'sad');
INSERT INTO person VALUES ('Curly', 'ok');
SELECT * FROM person WHERE current_mood > 'sad';
```

<pre>
 name  | current_mood
-------+--------------
 Moe   | happy
 Curly | ok
(2 rows)
</pre>

```
SELECT * FROM person WHERE current_mood > 'sad' ORDER BY current_mood;
```

<pre>
 name  | current_mood
-------+--------------
 Curly | ok
 Moe   | happy
(2 rows)
</pre>

```
SELECT name
FROM person
WHERE current_mood = (SELECT MIN(current_mood) FROM person);
```
<pre>
 name  
-------
 Larry
(1 row)
</pre>

<h3>类型安全</h3>

每个枚举类型都是独立的，不能与其他枚举类型结合，如：

```
CREATE TYPE happiness AS ENUM ('happy', 'very happy', 'ecstatic');
CREATE TABLE holidays (
    num_weeks integer,
    happiness happiness
);
INSERT INTO holidays(num_weeks,happiness) VALUES (4, 'happy');
INSERT INTO holidays(num_weeks,happiness) VALUES (6, 'very happy');
INSERT INTO holidays(num_weeks,happiness) VALUES (8, 'ecstatic');
INSERT INTO holidays(num_weeks,happiness) VALUES (2, 'sad');
ERROR:  invalid input value for enum happiness: "sad"
SELECT person.name, holidays.num_weeks FROM person, holidays
  WHERE person.current_mood = holidays.happiness;
ERROR:  operator does not exist: mood = happiness
```

如果真的需要那么做，可以要么自定义运算符，要么为查询添加显式转换：

```
SELECT person.name, holidays.num_weeks FROM person, holidays
  WHERE person.current_mood::text = holidays.happiness::text;
```

<pre>
 name | num_weeks
------+-----------
 Moe  |         4
(1 row)
</pre>

<h3>实施细则</h3>

一个枚举值在磁盘上占4字节。 一个枚举值的文本标签长度由NAMEDATALEN设置并编译到PostgreSQL中， 以标准编译方式进行，也就意味着至少是63字节。

枚举标签对大小写是敏感的，因此'happy'不等于'HAPPY'。 标签中的空格也是一样。

从内部枚举值到文本标签的翻译是保存在系统目录pg_enum中。 可以直接查询这个目录。

##几何类型##
几何数据类型表示二维的平面物体。Table 8-20显 示了PostgreSQL里面可用的几何类型。 最基本的类型：点，是其它类型的基础。

Table 8-20. 几何类型

|名字|	存储空间|	说明|	表现形式|
|------|-----|----|----|----|
|point|	16字节|	平面中的点|	(x,y)|
|line|	32字节|	(无穷)直线(未完全实现)|	((x1,y1),(x2,y2))|
|lseg	|32字节|	(有限)线段|	((x1,y1),(x2,y2))|
|box|	32字节|	矩形|	((x1,y1),(x2,y2))|
|path|	16+16n字节|	闭合路径(与多边形类似|	((x1,y1),...)|
|path|	16+16n字节|	开放路径|	[(x1,y1),...]|
|polygon|	40+16n字节|	多边形(与闭合路径相似）|	((x1,y1),...)|
|circle|	24字节|	圆	|<(x,y),r> (圆心和半径)|

我们有一系列丰富的函数和操作符可用来进行各种几何计算， 如拉伸、转换、旋转、计算相交等。它们在Section 9.11里有解释。

<h3>点</h3>

点是几何类型的基本二维构造单位。使用下面任一语法描述point的数值：

```
( x , y )
  x , y
```

这里的x和y是用浮点数表示的点的坐标。

点输出使用第一种语法。

<h3>线段</h3>

线段(lseg)是用一对点来代表的。lseg的值用下面语法声明：

```
[ ( x1 , y1 ) , ( x2 , y2 ) ]
( ( x1 , y1 ) , ( x2 , y2 ) )
  ( x1 , y1 ) , ( x2 , y2 )
    x1 , y1   ,   x2 , y2
```

这里的(x1,y1)和 (x2,y2)是线段的端点。

线段输出使用第一种语法。

<h3>矩形</h3>

矩形是用一对对角点来表示的。box的值用下面语法声明：

```
( ( x1 , y1 ) , ( x2 , y2 ) )
  ( x1 , y1 ) , ( x2 , y2 )
    x1 , y1   ,   x2 , y2
```

这里的(x1,y1)和(x2,y2)是矩形的一对对角点。

通过第二种语法输出矩形。

任何两个对角都可以出现在输入中，但按照那样的顺序，右上角和左下角的值会被重新排序以存储。

<h3>路径</h3>

路径由一系列连接的点组成。路径可能是开放的，也就是认为列表 中第一个点和最后一个点没有连接，也可能是闭合的， 这时认为第一个和最后一个点连接起来。

path的数值用下面语法声明：

```
[ ( x1 , y1 ) , ... , ( xn , yn ) ]
( ( x1 , y1 ) , ... , ( xn , yn ) )
  ( x1 , y1 ) , ... , ( xn , yn )
  ( x1 , y1   , ... ,   xn , yn )
    x1 , y1   , ... ,   xn , yn
```

这里的点是组成路径的线段的端点。方括弧([])表明一个开放的路径 ，圆括弧(())表明一个闭合的路径。当最外层的括号被省略，如 在第三至第五语法，会假定一个封闭的路径。

路径的输出使用第一种或第二种语法输出，在适当的时候。

<h3>多边形</h3>

多边形由一系列点代表(多边形的顶点)。多边形可以认为与闭合路径一样， 但是存储方式不一样而且有自己的一套支持函数。

polygon的数值用下列任一语法声明：

```
( ( x1 , y1 ) , ... , ( xn , yn ) )
  ( x1 , y1 ) , ... , ( xn , yn )
  ( x1 , y1   , ... ,   xn , yn )
    x1 , y1   , ... ,   xn , yn
```

这里的点是多边形的端点。

多边形输出使用第一种语法。

<h3>圆</h3>

圆由一个圆心和一个半径标识。circle的数值用任一下面语法表示：

```
< ( x , y ) , r >
( ( x , y ) , r )
  ( x , y ) , r
    x , y   , r
```

这里的(x,y)是圆心，r是半径。

圆的输出用第一种格式。
##网络地址类型##
PostgreSQL提供用于存储 IPv4、IPv6、MAC地址的数据类型， 在Table 8-21里显示。 用这些数据类型存储网络地址比用纯文本类型好， 因为这些类型提供输入错误检查和好些种特殊的操作和功能(见Section 9.12)。

Table 8-21. 网络地址类型

|名字|	存储空间|	描述|
|---|---|----|
|cidr|	7或19字节|	IPv4或IPv6网络|
|inet	|7或19字节|	IPv4 或 IPv6 网络和主机|
|macaddr|	6字节	|MAC 地址|

在对inet或cidr数据类型进行排序的时候， IPv4地址总是排在IPv6地址前面，包括那些封装或者是映射在IPv6地址里 的IPv4地址，比如::10.2.3.4或::ffff::10.4.3.2

<h3>inet</h3>

inet在一个数据域里保存主机的IPv4或IPv6地址， 以及一个可选的等效子网。  
子网的等效是通过计算主机地址中有多少位表示网络地 址的方法来表示的("子网掩码")。  
如果子网掩码是32并且地址是IPv4， 那么不表示任何子网，只是一台主机。在IPv6里，地址长度是128位， 因此128位表明一个唯一的主机地址。请注意如果你想只接受网络地址， 你应该使用cidr类型而不是inet类型。

该类型的输入格式是address/y， 这里的address是IPv4或者IPv6地址， y是子网掩码的二进制位数。 如果/y部分未填， 则子网掩码对IPv4而言是32，对IPv6而言是128， 所以该值表示只有一台主机。显示时，如果该值表示只有一台主机， /y将不会显示。

<h3>cidr</h3>

cidr保存一个IPv4或IPv6网络地址。 其输入和输出遵循无类别的互联网域路由习惯。
声明一个网络的格式是address/y， 这里的address是IPv4或者IPv6地址， y是子网掩码的二进制位数。  
如果省略y， 那么掩码部分用旧的有类别的网络编号系统进行计算， 但要求输入的数据已经包括了确定掩码所需的所有字节。 声明一个指定掩码的网络地址是错误的。

Table 8-22是些例子。

Table 8-22. cidr类型输入举例

|cidr输入|	cidr输出|	abbrev(cidr)|
|---|----|----|
|192.168.100.128/25|	192.168.100.128/25|	192.168.100.128/25|
|192.168/24	|192.168.0.0/24|	192.168.0/24|
|192.168/25	|192.168.0.0/25|	192.168.0.0/25|
|192.168.1|	192.168.1.0/24	|192.168.1/24|
|192.168|	192.168.0.0/24	|192.168.0/24|
|128.1|	128.1.0.0/16|	128.1/16|
|128|	128.0.0.0/16|	128.0/16|
|128.1.2|	128.1.2.0/24|	128.1.2/24|
|10.1.2	|10.1.2.0/24|	10.1.2/24|
|10.1|	10.1.0.0/16	|10.1/16|
|10|	10.0.0.0/8|	10/8|
|10.1.2.3/32|	10.1.2.3/32	|10.1.2.3/32|
|2001:4f8:3:ba::/64	|2001:4f8:3:ba::/64|	2001:4f8:3:ba::/64|
|2001:4f8:3:ba:2e0:81ff:fe22:d1f1/128|	2001:4f8:3:ba:2e0:81ff:fe22:d1f1/128|	2001:4f8:3:ba:2e0:81ff:fe22:d1f1|
|::ffff:1.2.3.0/120	|::ffff:1.2.3.0/120|	::ffff:1.2.3/120|
|::ffff:1.2.3.0/128	|::ffff:1.2.3.0/128|	::ffff:1.2.3.0/128|

<h3>inet与cidr对比</h3>

inet和cidr类型之间的基本区别是inet接受子网掩码， 而cidr不接受。

Tip: 如果你不喜欢inet或cidr值的输出格式， 请试一下host，text和abbrev函数。

<h3>macaddr</h3>

macaddr类型存储MAC地址，也就是以太网卡硬件地址 (尽管 MAC 地址还用于其它用途)。可以接受多种自定义的格式，包括

```
'08:00:2b:01:02:03'
'08-00-2b-01-02-03'
'08002b:010203'
'08002b-010203'
'0800.2b01.0203'
'08002b010203'
```

它们声明的都是同一个地址。对于数据位a到f，大小写都行。 输出总是我们上面给出的最后一种形式。
IEEE标准802-2001指定第二种形式（带连字符）为MAC地址的标准格式， 并指定的第一种形式（用冒号）为位反转符号，因此08-00-2b-01-02-03=01:00:4D:08:04:0C。 这个条约现在已很少使用，它至于过时的网络协议（如令牌环）有关。 PostgreSQL对位反转没有规定，并且所有接受的格式使用LSB协议顺序。

其余四个输入格式不是任何标准的一部分。
##为串类型##
位串就是一串1和0的字符串。它们可以用于存储和直观化位掩码。 我们有两种SQL位类型：bit(n)和bit varying(n)，这里的n是一个正整数。

bit类型的数据必须准确匹配长度n， 试图存储短些或者长一些的数据都是错误的。 bit varying类型数据是最长n的变长类型； 更长的串会被拒绝。写一个没有长度的bit 等效于bit(1)，没有长度的vbit varying意思是没有长度限制。

Note: 如果我们明确地把一个位串值转换成bit(n)， 那么它的右边将被截断或者在右边补齐零， 直到刚好n位，而不会抛出任何错误。类似地， 如果我们明确地把一个位串数值转换成bit varying(n)， 如果它超过了n位，那么它的右边将被截断。

请参考Section 4.1.2.5获取有关位串常量的语法信息。 还有一些位逻辑操作符和位处理函数可用；参见Section 9.6。

Example 8-3. 使用位串类型

```
CREATE TABLE test (a BIT(3), b BIT VARYING(5));
INSERT INTO test VALUES (B'101', B'00');
INSERT INTO test VALUES (B'10', B'101');
ERROR:  bit string length 2 does not match type bit(3)
INSERT INTO test VALUES (B'10'::bit(3), B'101');
SELECT * FROM test;
```

<pre>
  a  |  b
-----+-----
 101 | 00
 100 | 101
 </pre>

位字符串值需要1字节，每组8位，增加5或8字节的开销取决于字符串的长度（Section 8.3中有相关解释）。
##文本搜索类型##
PostgreSQL提供了两种数据类型用于支持全文检索， 即通过自然语言documents的集合来找到那些匹配一个query的检索。 tsvector类型产生一个文档（以优化了全文检索的形式），tsquery类型用于代表查询。 Chapter 12中说明了这两个类型，同时Section 9.13总结了相关的函数和操作符。

<h3>tsvector</h3>

tsvector的值时一个无重复值的lexemes排序列表， 即一些归并为同一个词的不同变种的词（可参阅 Chapter 12）。 在输入的同时会自动排序和消除重复，如：

```
SELECT 'a fat cat sat on a mat and ate a fat rat'::tsvector;
```

<pre>
                      tsvector
----------------------------------------------------
 'a' 'and' 'ate' 'cat' 'fat' 'mat' 'on' 'rat' 'sat'
 </pre>

为了包含空格或标点符号，可以用引号标记：

```
SELECT $$the lexeme '    ' contains spaces$$::tsvector;
```

<pre>
                 tsvector
-------------------------------------------
 '    ' 'contains' 'lexeme' 'spaces' 'the'
 </pre>

（在这个例子中，我们使用了双引号美元字符串文本呢，下一个例子是为了避免文本中双引号的混淆） 枚举的引号和反斜杠必须双倍：

```
SELECT $$the lexeme 'Joe''s' contains a quote$$::tsvector;
```

<pre>
                    tsvector
------------------------------------------------
 'Joe''s' 'a' 'contains' 'lexeme' 'quote' 'the'
 </pre>

可选的，整型positions也可以放到词汇中：

```
SELECT 'a:1 fat:2 cat:3 sat:4 on:5 a:6 mat:7 and:8 ate:9 a:10 fat:11 rat:12'::tsvector;
```

<pre>
                                  tsvector
-------------------------------------------------------------------------------
 'a':1,6,10 'and':8 'ate':9 'cat':3 'fat':2,11 'mat':7 'on':5 'rat':12 'sat':4
 </pre>

位置通常表示文档中的源字的位置。位置信息可以用于proximity ranking。 位置值可以使从1到16383，最大值默认是16383. 相同词的重复位会被忽略掉。

拥有位置的词汇甚至可以用一个权来标记，这个权可以是A，B，C或D。 默认的是D，因此输出中不会出现：

```
SELECT 'a:1A fat:2B,4C cat:5D'::tsvector;
```

<pre>
          tsvector
----------------------------
 'a':1A 'cat':5 'fat':2B,4C
 </pre>

权可以用来反映文档结构，如：标记标题以与主体相区别。全文检索排序函数可以为不同的权标记来分配不同的优先级。

充分理解tsvector类型不能自己标准化这一点是很重要的，它假设传递给它的单词对应用程序来说是恰当的标准化了的，如：

```
select 'The Fat Rats'::tsvector;
```

<pre>
      tsvector
--------------------
 'Fat' 'Rats' 'The'
 </pre>

对大多数的英文全文检索应用来说，上面的单词会被认为非规范化的，但tsvector并不关心这些。 原始文件中的文字应该通过to_tsvector来为检索恰当的规范化这些单词。

```
SELECT to_tsvector('english', 'The Fat Rats');
   to_tsvector
-----------------
 'fat':2 'rat':3
```

详细信息可参阅Chapter 12。

<h3>tsquery</h3>

tsquery存储用于检索的词汇，并且使用布尔操作符& (AND)，| (OR)和! (NOT)来组合它们。 括号用来强调操作符的分组：

```
SELECT 'fat & rat'::tsquery;
```

<pre>
    tsquery
---------------
 'fat' & 'rat'
</pre>

```
SELECT 'fat & (rat | cat)'::tsquery;
```

<pre>
          tsquery
---------------------------
 'fat' & ( 'rat' | 'cat' )
</pre>

```
SELECT 'fat & rat & ! cat'::tsquery;
```

<pre>
        tsquery
------------------------
 'fat' & 'rat' & !'cat'
 </pre>

在没有括号的情况下，! (NOT)结合的最紧密，而& (AND)结合的比| (OR)紧密。

可选的，tsquery中的词汇可以被一个或多个权字母来标记，这些权字母用来限制它们只能与带有匹配权的tsvector词汇进行匹配。

```
SELECT 'fat:ab & cat'::tsquery;
```

<pre>
    tsquery
------------------
 'fat':AB & 'cat'
 </pre>

同样，tsquery中的词汇可以用*进行标记来指定前缀匹配：

```
SELECT 'super:*'::tsquery;
```

<pre>
  tsquery  
-----------
 'super':*
 </pre>

这个查询可以匹配tsvector中以"super"开始的任意单词。

词汇的引用规则与之前tsvector中词汇的描述一样；并且，与tsvector，任何单词必须在转换为tsvector类型前规范化。 to_tsquery函数可以方便的用来执行规范化。

```
SELECT to_tsquery('Fat:ab & Cats');
```

<pre>
    to_tsquery
------------------
 'fat':AB & 'cat'
 </pre>

##UUID类型##
uuid数据类型用来存储RFC 4122，ISO/IEF 9834-8:2005以及相关标准定义的通用唯一标识符。 （一些系统认为这个数据类型为全球唯一标识符）。 这个标识符是一个由特选的语法产生的128标识符。因此，对分布式系统而言，这种标识符比序列能更好的提供唯一性保证， 因为序列只能在单一数据库中保证唯一。

UUID被写成一个小写十六进制数字的序列，由分字符分成几组，特别是一组8位数字+3组4位数字+一组12位数字，总共32个数字代表128位， 一个这种标准的UUID例子如下：

```
a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11
```

PostgreSQL同样支持以其他方式输入： 大写数字，由括号包围的标准格式，省略部分或所有连字符，在任意一组四位数字之后加一个连字符。如：

```
A0EEBC99-9C0B-4EF8-BB6D-6BB9BD380A11
{a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11}
a0eebc999c0b4ef8bb6d6bb9bd380a11
a0ee-bc99-9c0b-4ef8-bb6d-6bb9-bd38-0a11
{a0eebc99-9c0b4ef8-bb6d6bb9-bd380a11}
```

一般是以标准格式输出。

PostgreSQL为UUID提供了存储和比较函数，但核心数据库不包括能生成UUID的函数， 因为没有单一的算法非常适合于每一个应用程序。  
contrib模块contrib/uuid-ossp提供了实施几个标准算法的函数。 另外，UUID可以由客户端应用或通过服务器端函数库调用而生成。

##XML类型##
xml数据类型可以用于存储XML数据。相比较将XML数据存到text类型中，xml数据类型的优势在于 它能够为XML的编排良好性来检查输入值，并且还支持函数对其进行类型安全性检查，可参阅Section 9.14。 要使用这个数据类型，编译时必须使用configure --with-libxml。

xml可以存储由XML标准定义的格式良好的"文档"，以及由XML标准中的XMLDecl? content定义的"内容"片段， 大致上，这意味着内容片段可以有多个顶级元素或字符节点。xmlvalue IS DOCUMENT表达式可以用来	 判断一个特定的XML值是一个完整的文件还是内容片段。

<h3>创建XML值</h3>

使用函数xmlparse:来从字符数据产生xml类型的值：

<pre>
XMLPARSE ( { DOCUMENT | CONTENT } value)
</pre>

Examples:

```
XMLPARSE (DOCUMENT '<?xml version="1.0"?><book><title>Manual</title><chapter>...</chapter></book>')
XMLPARSE (CONTENT 'abc<foo>bar</foo><bar>foo</bar>')
```

然而根据SQL标准，这是唯一的用于将字串转换成XML值得方式，PostgreSQL特有的语法是：

```
xml '<foo>bar</foo>'
'<foo>bar</foo>'::xml
```

xml类型对一个文档类型声明（DTD）不会验证输入值，即使输入值声明了一个DTD。 目前没有内置支持用于对其他XML架构语言（如XML Schema）验证。

使用函数xmlserialize:来从xml产生一个字串。

```
XMLSERIALIZE ( { DOCUMENT | CONTENT } value AS type )
```

type可以是character，character varying或text (或其中某个的变种)。 同时，根据SQL标准，这是xml和字符类型之间的唯一的转换方式，但PostgreSQL仍支持简单的值转换。

当一个字符串值在没有通过XMLPARSE或XMLSERIALIZE的情况下，与xml类型进行转换时，分别的， 选择DOCUMENT与CONTENT是由"XML option"决定。 会话配置参数，可以由标准命令来设置：

<pre>
SET XML OPTION { DOCUMENT | CONTENT };
</pre>

或更多类似的PostgreSQL语法：

<pre>
SET xmloption TO { DOCUMENT | CONTENT };
</pre>

默认是CONTENT，因此所有的XML数据格式都能支持。

Note: 随着默认XML选项的设置，如果字符串中包含一个文档类型声明，那么你不能直接将其转换成xml类型， 因为XML内容片断的定义不支持。如果非得需要这么做，要么使用XMLPARSE，要么更改XML选项。

<h3>编码处理</h3>

在对客户端和服务器端进行多字符编码，以及在通过它们传递XML数据时需要格外注意。  
当使用文本模式（正常模式）在服务器端和客户端之间传递查询和查询结果时，PostgreSQL在各自终端对所有传递的字符数据和字符编码进行相互转换，参阅Section 22.2。  
这包括XML值得字符串表示形式，如上面的例子。这通常意味着XML数据中的编码声明，在客户端和服务器之间传递时，可以成为无效字符数据转换为其他编码。  
这是因为枚举编码声明没有改变。为了应对该问题，提交输入到xml类型的字符串中的编码声明会被ignored， 同时，内容会被认为是在当前服务器编码中。所以，对正确的处理来说，XML数据的字符串必须从在当前客户端编码中的客户端发送。  
客户端有责任，要么将文档转换成当前客户端编码，在传递到服务器之前，要么适当的调整客户端编码。  
输出时，xml类型的值不会有编码声明，同时客户端会认为所有的数据都是在当前客户端编码之中的。

当使用二进制模式在服务器和客户端之间传递查询参数和查询结果，没有执行字符集转换， 因此解决方法是不同的。  
在这种情况下，将会遵守XML数据中的编码声明，并且如果不存在， 数据会被假定为UTF-8格式(如同XML标准要求那样，但需要注意的是PostgreSQL不支持UTF-16).  
输出时，会对数据进行编码声明以声明客户端编码，除非客户端编码格式是UTF-8。

不用说，如果XML数据编码格式，客户端编码格式，以及服务器编码格式都一样，那么用PostgreSQL处理XML数据将会减少错误，并且效率会很高。 在国内，XML数据是用UTF-8编码格式处理的，因此，如果服务器端编码也是UTF-8时，计算性能会很高。

Caution
当服务器编码非UTF-8格式时，一些相关的XML函数可能完全不支持非ASCII数据，特别是xpath()函数。

<h3>连接XML值</h3>

xml数据类型有些特殊，因为它不提供比较运算符。 这是因为对XML数据，没有很好的定义和通用的比较运算符。  
这样做的一个后果是，不能通过xml与检索值的比较来检索行。 因此XML值必须带有一个单独的关键值，如一个ID。  
另一个解决比较XML值得方法是，先将它们转换成字符串，但需要注意的是字符串比较与一个有用的XML比较方法无关。

因为没有针对xml数据类型的比较运算符，因此不能在这种类型的字段上直接创建索引。  
如果需要对XML数据进行快速搜索，可能得解决方法包括将表达式转换成一个字符串类型，然后对它进行索引，或索引一个XPath表达式。  
当然，实际查询是将不得不进行调整，以使用一个索引表达式进行检索。

PostgreSQL中的文本检索功能也可用于加快XML数据的全文搜索。但必要的预处理支持在PostgreSQL中还不能获得。

##数组##
PostgreSQL允许将字段定义成定长或变长的一维或多维数组。 数组类型可以是任何基本类型或用户定义类型,枚举类型或者组合类型。 不支持复合类型和域的数组。

<h3>数组类型的声明</h3>

为说明这些用法，我们先创建一个由基本类型数组构成的表：

```
CREATE TABLE sal_emp (
    name            text,
    pay_by_quarter  integer[],
    schedule        text[][]
);
```

如上所示，一个数组类型是通过在数组元素类型名后面附加方括弧([])来命名的 上面的命令将创建一个叫sal_emp的表， 表示雇员名字的name字段是一个text类型字符串， 表示雇员季度薪水的`pay_by_quarter`字段是一个一维integer数组， 表示雇员周计划的schedule字段是一个两维text数组。

CREATE TABLE的语法允许声明数组的确切大小，比如：

```
CREATE TABLE tictactoe (
    squares   integer[3][3]
);
```

不过，目前的实现并不强制数组尺寸限制(等价于未声明长度的数组)。

实际上，目前的实现也不强制数组维数。 特定元素类型的数组都被认为是相同的类型，不管他们的大小或者维数。 因此，在CREATE TABLE里定义数字或者维数都不影响运行时的行为。

另外还有一种语法，它遵循SQL标准，运用主键ARRAY，可以用于声明一维数组。 `pay_by_quarter`可以定义为：

```
    pay_by_quarter  integer ARRAY[4],
```

或者，如果没有指定数组大小：

```
    pay_by_quarter  integer ARRAY,
```

不过，如前所述，PostgreSQL并不强制这个尺寸限制。

<h3>数组值输入</h3>

将数组写成文本的时候， 用花括弧把数组元素括起来并且用逗号将它们分开(如果你懂C，那么这与初始化一个结构很像)。 你可以在数组元素值周围放置双引号，但如果这个值包含逗号或者花括弧， 那么就必须加上双引号(下面有更多细节)。因此，一个数组常量的常见格式如下：

```
'{ val1 delim val2 delim ... }'
```

这里的delim是该类型的分隔符， 就是在该类型的pg_type记录中指定的那个。 在PostgreSQL发布提供的标准数据类型里，除了box类型使用分号(;)之外， 其它所有类型都使用逗号(,)。每个val要么是一个数组元素类型的常量， 要么是一个子数组。一个数组常量的例子如下：

```
'{{1,2,3},{4,5,6},{7,8,9}}'
```

这个常量是一个3乘3的两维数组，由三个整数子数组组成。

要将一个数组元素的值设为NULL，直接写上NULL即可(大小写无关)。 要将一个数组元素的值设为字符串"NULL"，那么你必须加上双引号。

这种数组常量实际上只是我们在Section 4.1.2.7里 讨论过的一般类型常量的一种特例。 常量最初是当作字符串看待并且传递给数组输入转换器的， 可能需要使用明确的类型声明。

现在我们可以展示一些INSERT语句:

```
INSERT INTO sal_emp
    VALUES ('Bill',
    '{10000, 10000, 10000, 10000}',
    '{{"meeting", "lunch"}, {"training", "presentation"}}');

INSERT INTO sal_emp
    VALUES ('Carol',
    '{20000, 25000, 25000, 25000}',
    '{{"breakfast", "consulting"}, {"meeting", "lunch"}}');
```

前面的两个插入的结果看起来像这样：

```
SELECT * FROM sal_emp;
```

<pre>
 name  |      pay_by_quarter       |                 schedule
-------+---------------------------+-------------------------------------------
 Bill  | {10000,10000,10000,10000} | {{meeting,lunch},{training,presentation}}
 Carol | {20000,25000,25000,25000} | {{breakfast,consulting},{meeting,lunch}}
(2 rows)
</pre>

多维数组必须匹配每个维的元素数。如果不匹配将导致错误,如：

```
INSERT INTO sal_emp
    VALUES ('Bill',
    '{10000, 10000, 10000, 10000}',
    '{{"meeting", "lunch"}, {"meeting"}}');
ERROR:  multidimensional arrays must have array expressions with matching dimensions
```

我们还可以使用ARRAY构造器语法:

```
INSERT INTO sal_emp
    VALUES ('Bill',
    ARRAY[10000, 10000, 10000, 10000],
    ARRAY[['meeting', 'lunch'], ['training', 'presentation']]);

INSERT INTO sal_emp
    VALUES ('Carol',
    ARRAY[20000, 25000, 25000, 25000],
    ARRAY[['breakfast', 'consulting'], ['meeting', 'lunch']]);
```

请注意数组元素是普通的SQL常量或者表达式； 比如，字符串文本是用单引号包围的，而不是像数组文本那样用双引号。 ARRAY构造器语法在Section 4.2.11里有更详细的讨论。

<h3>访问数组</h3>

现在我们可以在这个表上运行一些查询。 首先，我们演示如何一次访问数组的一个元素。 这个查询检索在第二季度薪水变化的雇员名:

```
SELECT name FROM sal_emp WHERE pay_by_quarter[1] <> pay_by_quarter[2];
```

<pre>
 name
-------
 Carol
(1 row)
</pre>

数组的下标数字是写在方括弧内的。 PostgreSQL缺省使用以1为基的数组习惯， 也就是说，一个n元素的数组从array[1]开始，到array[n]结束。

这个查询检索所有雇员第三季度的薪水:

```
SELECT pay_by_quarter[3] FROM sal_emp;
```

<pre>
 pay_by_quarter
----------------
          10000
          25000
(2 rows)
</pre>

我们还可以访问一个数组的任意矩形片段，或称子数组。 对于一维或更多维数组，可以用(lower-bound(下标下界)): (upper-bound(上界上标)) 表示一个数组的某个片段。 比如，下面查询检索Bill该周前两天的计划中的第一件事情：

```
SELECT schedule[1:2][1:1] FROM sal_emp WHERE name = 'Bill';
```

<pre>
        schedule
------------------------
 {{meeting},{training}}
(1 row)
</pre>

如果任意维数写成片段，即包含一个冒号，那么所有的维数都可以看成片段。 对于没有冒号且仅有单一数字的任意维数，可以看成是从1到该指定数字。 例如，[2]可以看成[1:2]，正如在这样的例子中：

```
SELECT schedule[1:2][2] FROM sal_emp WHERE name = 'Bill';
```

<pre>
                 schedule
-------------------------------------------
 {{meeting,lunch},{training,presentation}}
(1 row)
</pre>

为了避免和非片段实例混淆，最好对所有维数使用片段语法，例如，`[1:2][1:1]`，而不是`[2][1:1]`。

如果数组本身或者任何一个下标表达式是NULL，那么，该数组的下标表达式会返回NULL。同样的， 从一个数组的当前范围之外抓取数据时，不会产生错误，而是也返回一个NULL。 比如，如果schedule目前的维是`[1:3][1:2]`， 那么，当我们抓取`schedule[3][3]`时会生成NULL 。 类似的还有，引用一个下标错误的数组时也会生成 NULL，而不是错误。

如果数组本身或任何一个下标表达式是NULL，那么，该数组的片段表达式也将生成NULL 。 但在其它其它情况下，比如当完全在数组的当前范围之外抓取一个数组片断时， 将生成一个空数组(零维)而不是NULL 。 (这与非片段形式不匹配，并且有这样做的历史原因。) 如果抓取的片断部分覆盖数组的范围，那么它会自动缩减为抓取覆盖的范围,而不是NULL。

可以通过array_dims函数来检索任何一个数组的当前维数：

```
SELECT array_dims(schedule) FROM sal_emp WHERE name = 'Carol';
```

<pre>
 array_dims
------------
 [1:2][1:2]
(1 row)
</pre>

array_dims函数返回一个text类型的结果，从而便于人们阅读和理解。 同样的，我们也可以用`array_upper`和`array_lower`函数来 分别返回一个特定维的上界和下界：

```
SELECT array_upper(schedule, 1) FROM sal_emp WHERE name = 'Carol';
```

<pre>
 array_upper
-------------
           2
(1 row)
</pre>

而array_length可以用来查看指定维的长度：

```
SELECT array_length(schedule, 1) FROM sal_emp WHERE name = 'Carol';
```

<pre>
 array_length
--------------
            2
(1 row)
</pre>

<h3>修改数组</h3>

数组值是可以完全被代替的，如：

```
UPDATE sal_emp SET pay_by_quarter = '{25000,25000,27000,27000}'
    WHERE name = 'Carol';
```

或者使用ARRAY构造器语法：

```
UPDATE sal_emp SET pay_by_quarter = ARRAY[25000,25000,27000,27000]
    WHERE name = 'Carol';
```

同样，也可以只更新某一个元素：

```
UPDATE sal_emp SET pay_by_quarter[4] = 15000
    WHERE name = 'Bill';
```

或者更新某个片断

```
UPDATE sal_emp SET pay_by_quarter[1:2] = '{27000,27000}'
    WHERE name = 'Carol';
```

可以通过给尚不存在的数组元素赋值的办法来扩大数组， 所有位于原数组最后一个元素和这个新元素之间的未赋值元素都将设为NULL。 例如，如果myarray数组当前有4个元素，在对myarray[6]赋值之后它将拥有6个元素， 其中myarray[5]的值将为NULL。 目前，只允许对一维数组使用这种方法扩大，而不是多维数组。

下标赋值允许创建下标不从1开始的数组。 比如，我们可以通过给myarray[-2:7]赋值，来创建一个下标值在-2到7之间的数组。

新的数组值也可以用连接操作符||构造。

```
SELECT ARRAY[1,2] || ARRAY[3,4];
```

<pre>
 ?column?
-----------
 {1,2,3,4}
(1 row)
</pre>

```
SELECT ARRAY[5,6] || ARRAY[[1,2],[3,4]];
```

<pre>
      ?column?
---------------------
 {{5,6},{1,2},{3,4}}
(1 row)
</pre>

连接操作符允许把一个元素压入一维数组的开头或者结尾，当然，也接受两个N维的数组， 或者一个N维和一个N+1维的数组。

当向一维数组的头部或尾部压入单独一个元素后，数组的下标下界保持不变。 比如：

<pre>
SELECT array_dims(1 || '[0:1]={2,3}'::int[]);
 array_dims
------------
 [0:2]
(1 row)

SELECT array_dims(ARRAY[1,2] || 3);
 array_dims
------------
 [1:3]
(1 row)
</pre>

如果将两个相同维数的数组连接在一起，结果数组将保留左操作数的外层维数的下标下界值，即 结果会是这样一个数组：包含左操作数的每个元素，后面跟着右操作数的每个元素。比如：

<pre>
SELECT array_dims(ARRAY[1,2] || ARRAY[3,4,5]);
 array_dims
------------
 [1:5]
(1 row)

SELECT array_dims(ARRAY[[1,2],[3,4]] || ARRAY[[5,6],[7,8],[9,0]]);
 array_dims
------------
 [1:5][1:2]
(1 row)
</pre>

如果将一个N维的数组压到一个N+1维数组的开头或者结尾，结果和上面数组元素的情况类似。 每个N维子数组实际上都是N+1维数组的最外层元素。比如：

<pre>
SELECT array_dims(ARRAY[1,2] || ARRAY[[3,4],[5,6]]);
 array_dims
------------
 [1:3][1:2]
(1 row)
</pre>

也可以用 array_prepend, array_append, array_cat函数来构造函数。 前两个只支持一维数组，而array_cat支持多维数组。 需要注意的是使用连接操作符要比直接使用这些函数好。实际上，这些函数主要是用于实现连接操作符。 不过，在创建用户定义函数时，直接使用这些函数可能会更直接有效。比如：

<pre>
SELECT array_prepend(1, ARRAY[2,3]);
 array_prepend
---------------
 {1,2,3}
(1 row)

SELECT array_append(ARRAY[1,2], 3);
 array_append
--------------
 {1,2,3}
(1 row)

SELECT array_cat(ARRAY[1,2], ARRAY[3,4]);
 array_cat
-----------
 {1,2,3,4}
(1 row)

SELECT array_cat(ARRAY[[1,2],[3,4]], ARRAY[5,6]);
      array_cat
---------------------
 {{1,2},{3,4},{5,6}}
(1 row)

SELECT array_cat(ARRAY[5,6], ARRAY[[1,2],[3,4]]);
      array_cat
---------------------
 {{5,6},{1,2},{3,4}}
 </pre>

<h3>在数组中检索</h3>

为了查找一个数组中的某个数值，必须检查该数组的每一个值。 而如果你知道这个数组的尺寸，那么你完全可以进行手工处理。比如：

```
SELECT * FROM sal_emp WHERE pay_by_quarter[1] = 10000 OR
                            pay_by_quarter[2] = 10000 OR
                            pay_by_quarter[3] = 10000 OR
                            pay_by_quarter[4] = 10000;
```

不过，对于大数组而言，这个方法会让人觉得很无聊，并且，如果你不知道数组的尺寸，也是没什么用的。 在Section 9.21里为大家描述了另外一个方法。 上面的查询可以用下面的代替：

```
SELECT * FROM sal_emp WHERE 10000 = ANY (pay_by_quarter);
此外，你可以找到数组的中所有等于10000的值的行：

SELECT * FROM sal_emp WHERE 10000 = ALL (pay_by_quarter);
另外，也可以使用generate_subscripts函数，如：

SELECT * FROM
   (SELECT pay_by_quarter,
           generate_subscripts(pay_by_quarter, 1) AS s
      FROM sal_emp) AS foo
 WHERE pay_by_quarter[s] = 10000;
```

Table 9-46中有对该函数的说明。

Tip: 数组不是集合；搜索数组中的特定元素通常表明你的数据库设计有问题。 数组字段通常是可以分裂成独立的表。 很明显表要容易搜索得多，并且在元素数目非常庞大的时候也可以更好地伸展。

<h3>数组的输入和输出语法</h3>

一个数组值的外部表现形式由一些根据该数组元素类型的I/O转换规则分析的项组成， 再加上一些标明该数组结构的修饰 这些修饰由围绕在数组值周围的花括弧({ and })加上相邻项之间的分隔字符组成。
分隔字符通常是一个逗号(,)，但也可以是其它的东西：它由该数组元素类型的typdelim设置决定。  
在PostgreSQL提供的标准数据类型里，除了box类型使用分号(;)外,所有其它类型都使用逗号。  
在多维数组里，每个维都有自己级别的花括弧，并且在同级相邻的花括弧项之间必须写上分隔符。

如果数组元素值是空字符串或者包含花括弧、分隔符、双引号、反斜杠、空白， 或者匹配NULL关键字，那么数组输出过程将在这些值周围包围双引号。  
在元素值里包含的双引号和反斜杠将被反斜杠逃逸。 对于数值类型，你可以安全地假设数值没有双引号包围， 但是对于文本类型，我们就需要准备好面对有双引号包围和没有双引号包围两种情况了。

缺省时，一个数组维数的下标索引设置为1。 如果一个数组维数下标不等于1，那么就会在数组结构修饰域里面放置一个实际的维数。 这个修饰由方括弧(([])围绕在每个数组维的下界和上界索引，中间有一个冒号(:)分隔的字符串组成。数组维数修饰后面跟着一个等号操作符(=)。比如：

```
SELECT f1[1][-2][3] AS e1, f1[1][-1][5] AS e2
 FROM (SELECT '[1:1][-2:-1][3:5]={{{1,2,3},{4,5,6}}}'::int[] AS f1) AS ss;
```

<pre>
 e1 | e2
----+----
  1 |  6
(1 row)
</pre>

仅当一个或多个下界不等于1时，数组输出程序才在结果中包含明确的尺寸。

如果一个数组元素的值写成NULL(不区分大小写)，那么该元素的值就是NULL。 而引号和反斜杠可以表示输入文本字符串"NULL"值。 另外，为了兼容8.2之前的版本， 可以将array_nulls配置参数设为off以禁止将NULL识别为NULL。

如前所示，当书写一个数组值的时候，可以在任何元素值周围加上双引号。  
当元素值可能让数组值解析器产生歧义时，就必须在元素周围加上双引号，例如：元素值包含花括号、逗号(或者是其它分割符)、双引号、反斜杠、在开头/结尾处有空白符、匹配NULL的字符串。  
要在元素值中包含双引号或反斜杠，可以加一个前导反斜杠。 当然，你也可以使用反斜杠逃逸来保护任何可能引起语法混淆的字符。

你可以在左花括弧前面或者右花括弧后面写空白，也可以在任意独立的项字符串前面或者后面写空白。 所有这些情况下，空白都会被忽略。 不过，在双引号包围的元素里面的空白，或者是元素里被两边非空白字符包围的空白，不会被忽略。

Note: 请记住你在SQL命令里写的任何东西都将首先解释成一个字符串文本，然后才是一个数组。 这样就造成你所需要的反斜杠数量翻了翻。 比如，要插入一个包含反斜杠和双引号的text数组，你需要这么写:

```
INSERT ... VALUES (E'{"\\\\","\\""}');
```

字符串文本处理器去掉第一层反斜杠，然后省下的东西到了数组数值分析器的时候将变成{"\\","\""}。 接着，该字符串传递给text数据类型的输入过程，分别变成\和"。 如果我们使用的数据类型对反斜杠也有特殊待遇，比如bytea， 那么我们可能需要在命令里放多达八个反斜杠才能在存储态的数组元素中得到一个反斜杠。 也可以用美元符界定(参阅Section 4.1.2.4)来避免双份的反斜杠。

Tip: ARRAY构造器语法(参阅xref linkend="sql-syntax-array-constructors">) 通常比数组文本语法好用些，尤其是在SQL命令里写数组值的时候。 在ARRAY里，独立的元素值的写法和数组里没有元素时的写法一样。

##复合类型##
复合类型描述一行或者一条记录的结构；它实际上只是一个字段名和它们的数据类型的列表。 PostgreSQL允许像简单数据类型那样使用复合类型。比如，一个表的某个字段可以声明为一个复合类型。

8.15.1. 声明复合类型

下面是两个定义复合类型的简单例子：

```
CREATE TYPE complex AS (
    r       double precision,
    i       double precision
);

CREATE TYPE inventory_item AS (
    name            text,
    supplier_id     integer,
    price           numeric
);
```

语法类似于CREATE TABLE，只是这里只可以声明字段名字和类型；目前不能声明约束 (比如NOT NULL)。请注意AS关键字是很重要的；没有它， 系统会认为这是完全不同的CREATE TYPE命令，因此你会看到奇怪的语法错误。

定义了类型，我们就可以用它创建表：

```
CREATE TABLE on_hand (
    item      inventory_item,
    count     integer
);

INSERT INTO on_hand VALUES (ROW('fuzzy dice', 42, 1.99), 1000);
```

或者函数：

```
CREATE FUNCTION price_extension(inventory_item, integer) RETURNS numeric
AS 'SELECT $1.price * $2' LANGUAGE SQL;

SELECT price_extension(item, 10) FROM on_hand;
```

在你创建表的时候，也会自动创建一个复合类型，名字与表名字相同，表示该表的复合类型。比如，如果我们说过：

```
CREATE TABLE inventory_item (
    name            text,
    supplier_id     integer REFERENCES suppliers,
    price           numeric CHECK (price > 0)
);
```

那么，和前面相同的inventory_item复合类型也会作为副产品创建， 并且可以和上面一样使用。不过，需要注意一个重要限制： 因为现在还没有对复合类型实现约束，所以在表定义中显示的约束并不适用 于表之外的复合类型。一个部分绕开的办法是使用域类型作为复合类型的成员。

<h3>复合类型值输入</h3>

要以文本常量书写复合类型值，在圆括弧里包围字段值并且用逗号分隔他们。 你可以在任何字段值周围放上双引号，如果值本身包含逗号或者圆括弧， 你必须用双引号括起(更多细节见下面)。因此，复合类型常量的一般格式如下：

```
'( val1 , val2 , ... )'
```

一个例子是：

```
'("fuzzy dice",42,1.99)'
```

如果inventory_item类型在前面已经定义了， 那么这是一个合法的数值。要让一个字段值是NULL，那么在列表里它的位置上不要写任何字符。 比如，下面这个常量在第三个字段声明一个NULL：

```
'("fuzzy dice",42,)'
```

如果你想要一个空字符串，而不是NULL，写一对双引号：

```
'("",42,)'
```

这里的第一个字段是一个非NULL的空字符串，第三个字段是NULL。

这些常量实际上只是我们在Section 4.1.2.7 讨论的一般类型常量的一个特殊例子。这些常量一开始只是当作字符串， 然后传递给复合类型输入转换器。一个明确的类型声明可能是必须的。

我们也可以用ROW表达式语法来构造复合类型值。在大多数场合下， 这种方法都比用字符串文本的语法更简单，因为你不用操心多重引号。我们已经在上面使用了这种方法了：

```
ROW('fuzzy dice', 42, 1.99)
ROW('', 42, NULL)
```

只要你在表达式里有超过一个字段，那么关键字ROW就实际上是可选的，所以可以简化为

```
('fuzzy dice', 42, 1.99)
('', 42, NULL)
```

ROW表达式语法在Section 4.2.12里有更详细的讨论。

<h3>访问复合类型</h3>

要访问复合类型字段的一个域，我们写出一个点以及域的名字， 非常类似从一个表名字里选出一个字段。实际上，因为实在太像从表名字中选取字段， 所以我们经常需要用圆括弧来避免分析器混淆。比如，你可能需要从on_hand例子表中选取一些子域，像下面这样：

```
SELECT item.name FROM on_hand WHERE item.price > 9.99;
```

这样将不能工作，因为item是被当做一个表名字选取的， 而不是on_hand的字段名。你必须像下面这样写：

```
SELECT (item).name FROM on_hand WHERE (item).price > 9.99;
```

或者如果你也需要使用表名字(比如，在一个多表查询里)，那么这么写：

```
SELECT (on_hand.item).name FROM on_hand WHERE (on_hand.item).price > 9.99;
```

现在圆括弧对象正确地解析为一个指向item字段的引用，然后就可以从中选取子域。

类似的语法问题适用于在任何地点从一个复合类型值中查询一个域。 比如，要从一个返回复合类型值的函数中只选取一个字段，你需要写像下面这样的东西：

```
SELECT (my_func(...)).field FROM ...
```

如果没有额外的圆括弧，会产生一个语法错误。

<h3>修改复合类型</h3>

下面是一些插入和更新复合类型字段的正确语法。首先，插入或者更新整个字段：

```
INSERT INTO mytab (complex_col) VALUES((1.1,2.2));
UPDATE mytab SET complex_col = ROW(1.1,2.2) WHERE ...;
```

第一个例子省略了ROW，第二个使用它；两种方法都行。

我们可以更新一个复合字段的独立子域：

```
UPDATE mytab SET complex_col.r = (complex_col).r + 1 WHERE ...;
```

请注意，这里我们不需要(实际上是不能)在SET后面出现的字段名周围放上圆括弧， 但是我们在等号右边的表达式里引用同一个字段的时候却需要圆括弧。

我们也可以声明子域是INSERT的目标：

```
INSERT INTO mytab (complex_col.r, complex_col.i) VALUES(1.1, 2.2);
```

如果我们没有为字段的所有子域提供数值，那么剩下的子域将用NULL填充。

<h3>复合类型输入和输出语法</h3>

一个复合类型的文本表现形式包含那些根据独立的子域类型各自I/O转换规则解析的项， 加上一些表明这是复合结构的修饰。这些修饰由整个数值周围的圆括弧((和)) 加上相邻域之间的逗号(,)组成。圆括弧外面的空白被忽略， 但是在圆括弧里面，它被当作子域数值的一部分，根据该子域的数据类型，这些空白可能有用，也可能没用。比如，在

```
'(  42)'
```

里，如果子域类型是整数，那么空白将被忽略，但是如果是文本，那么就不会忽略。

如前面显示的那样，在给一个复合类型写数值的时候，你可以在独立的子域数值周围用双引号包围。  
如果子域数值会导致复合数值分析器产生歧义，那么你必须这么做。特别是子域包含圆括弧、逗号、双引号、反斜杠的场合。  
要想在双引号括起来的子域数值里面放双引号，那么你需要在它前面放一个反斜杠。  
同样，在一个双引号括起的子域数值里面的一对双引号表示一个双引号字符，就像SQL字符串文本的单引号规则一样。  
另外，你可以用反斜杠逃逸，而不必用引号的方法保护所有可能会当作复合类型语法的数据字符。

一个完全空的子域数值(在逗号或者逗号与圆括弧之间没有字符)表示一个NULL。 要写一个空字符串，而不是一个NULL，写""。

假如子域数值是空字符串或者包含圆括弧、逗号、双引号、反斜杠、空白， 复合类型输出程序会在子域数值周围放上双引号。这么处理空白不是必须的， 但是可以增强易读性。在一个子域数值里面嵌入的双引号和反斜杠将会写成两份。

Note: 请注意你写的任何SQL命令都首先被当作字符串文本解析，然后才当作复合类型。 这就加倍了你需要的反斜杠数目。比如，要插入一个包含双引号和一个反斜杠的text子域到一个复合类型数值里，你需要写

```
INSERT ... VALUES (E'("\\"\\\\")');
```

字符串文本处理器先吃掉一层反斜杠，这样到达复合类型分析器的东西将变成("\"\\")。 接着，该字符串传递给text数据类型的输入过程，变成"\。  
如果我们使用的数据类型对反斜杠也有特殊待遇，比如 bytea ， 那么我们可能需要在命令里放多达八个反斜杠以获取在存储的复合类型子域中有一个反斜杠。 美元符界定(参阅Section 4.1.2.4)可以用于避免双份反斜杠的问题。

Tip: 在SQL命令里写复合类型值的时候，ROW构造器通常比复合文本语法更容易使用。 在ROW里，独立的子域数值的写法和并非作为复合类型的成员书写的方法一样。

##对象标识符类型##
PostgreSQL在内部使用对象标识符(OID)作为各种系统表的主键。 同时，系统不会给用户创建的表增加一个 OID 系统字段(除非在建表时声明了WITH OIDS或者配置参数default_with_oids 设置为开启)。  
oid类型代表一个对象标识符。 除此以外oid还有几个别名：regproc，regprocedure， regoper，regoperator，regclass，regtype， regconfig和regdictionary。

目前oid类型用一个四字节的无符号整数实现。 因此，它不够提供大数据库范围内的唯一性保证，甚至在单个的大表中也不行。 因此，我们不鼓励在用户创建的表中使用OID字段做主键。OID最好只是用于系统表。

oid类型本身除了比较之外还有几个操作。 不过，它可以转换为整数，然后用标准的整数操作符操作。 如果你这么干，请注意可能的有符号和无符号之间的混淆。

OID别名类型除了输入和输出过程之外没有自己的操作。 这些过程可以为系统对象接受和显示符号名，而不仅仅是类型oid将要使用的行数值。 别名类型允许我们简化为对象查找OID值的过程。 比如，检查和一个表mytable相关的pg_attribute行， 我们可以这样写：

```
SELECT * FROM pg_attribute WHERE attrelid = 'mytable'::regclass;
```

而不是：

```
SELECT * FROM pg_attribute
  WHERE attrelid = (SELECT oid FROM pg_class WHERE relname = 'mytable');
```

虽然看上去不坏，但是这个例子还是简化了好多， 如果在不同的模式里有好多叫mytable的表， 那么我们需要写一个更复杂的子查询。regclass的输入转换器处理根据模式路径设置的表检索工作， 所以它自动干了"正确的事情"。类似的还有， 把一个表的OID转换成regclass是查找一个OID对应的符号名称的最简单方法。

Table 8-23. 对象标识符类型

|名字|	引用|	描述|	数值例子|
|------|------|----|-----|
|oid|	任意|	数字化的对象标识符	|564182|
|regproc|	pg_proc	|函数名字|	sum|
|regprocedure	|pg_proc|	带参数类型的函数|	sum(int4)|
|regoper|	pg_operator|	操作符名|	+|
|regoperator|	pg_operator	|带参数类型的操作符|	*(integer,integer) or -(NONE,integer)|
|regclass	|pg_class	|关系名	pg_type|
|regtype|	pg_type	|数据类型名	integer|
|regconfig	|pg_ts_config	|全文检索配置	|english|
|regdictionary|	pg_ts_dict	|全文检索路径	|simple|

所有OID别名类型都接受有模式修饰的名字， 并且如果在当前搜索路径中不增加修饰无法找到该对象的话， 那么在输出时将显示有模式修饰的名字。 regproc和regoper别名类型将只接受唯一的输入名字(不能重载)， 因此它们的用途有限。  
对于大多数应用，regprocedure或regoperator更合适。 对于regoperator，单目操作符是通过在 那些未用的操作数上写NONE来标识的。

OID别名类型的一个额外的属性是依赖关系的创建。如果这些类型之一的常量 出现在一个存储的表达式里(比如字段缺省表达式或者视图)， 它在被引用的对象上创建一个依赖性。  
比如，如果一个字段有缺省的 nextval('my_seq'::regclass)表达式， PostgreSQL理解缺省表达式依赖于 序列my_seq；系统将不允许在删除缺省的表达式之前删除该序列。

系统使用的另外一个标识符类型是事务(缩写xact)标识符xid。 它是系统字段xmin和xmax的数据类型。 事务标识符是32位的量。

系统需要的第三种标识符类型是命令标识符cid。 是系统字段cmin和cmax的数据类型。 命令标识符也是32位的量。

系统使用的最后一个标识符类型是行标识符tid。 它是系统表字段ctid的数据类型。 行ID是一对数值(块号，块内的行索引)，它标识该行在其所在表内的物理位置。

##伪类型##
PostgreSQL类型系统包含一系列特殊用途的条目， 它们按照类别来说叫做伪类型。伪类型不能作为字段的数据类型， 但是它可以用于声明一个函数的参数或者结果类型。 伪类型在一个函数不只是简单地接受并返回某种SQL数据类型的情况下很有用。

Table 8-24. 伪类型

|名字	|描述|
|-----|----|
|any|	表示一个函数接受任何输入数据类型|
|anyarray|	表示一个函数接受任意数组数据类型 （参阅Section 35.2.5）|
|anyelement	|表示一个函数接受任何数据类型 （参阅Section 35.2.5）|
|anyenum|	表示一个函数接受任意枚举数据类型 (参阅Section 35.2.5 and Section 8.7).|
|anynonarray|	表示一个函数接受任意非数组数据类型 (参阅Section 35.2.5).|
|cstring	|表示一个函数接受或者返回一个空结尾的C字符串|
|internal	|表示一个函数接受或者返回一种服务器内部的数据类型|
|language_handler	|一个过程语言调用处理器声明为返回 language_handler.|
|record	|标识一个函数返回一个未声明的行类型|
|trigger	|一个触发器函数声明为返回trigger.|
|void	|表示一个函数不返回数值|
|opaque	|一个已经过时的类型，以前用于所有上面这些用途|

用C编写的函数(不管是内置的还是动态装载的)都可以声明为接受或者返回这样的伪数据类型。 在把伪类型用做函数参数类型的时候，保证函数行为正常就是函数作者的任务了。

用过程语言编写的函数只能根据它们的实现语言是否可以使用伪类型而使用它。 目前，过程语言都不允许使用伪类型作为参数类型， 并且只允许使用void和record作为结果类型 (如果函数用做触发器，那么加上trigger)。 一些多态的函数还支持使用anyarray， anyelement，anyenum和anynonarray类型。

伪类型internal用于声明那种只能在数据库系统内部调用的函数， 它们不能直接在SQL查询里调用。 如果函数至少有一个internal类型的参数， 那么我们就不能从SQL里调用它。 为了保留这个限制的类型安全，我们一定要遵循这样的编码规则： 不要创建任何声明为返回internal的函数，除非它至少有一个internal参数。
