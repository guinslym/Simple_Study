本地化.md
本章从管理员的角度描述可用的区域特性。PostgreSQL通过两种途径支持区域设施：  
利用操作系统库的区域(locale)特性，提供对集合顺序、数字格式、翻译信息和其它方面的支持。
提供多种定义在 PostgreSQL 服务器里的字符集，包括多字节字符集、多种语言的排序文本、客户端和服务器端之间的字符集转换。
##区域支持##
###概述###
区域支持是在使用initdb创建一个数据库集群的时候自动初始化的。缺省时，initdb将会按照它的执行环境的区域设置初始化数据库集群。  
因此如果你的系统已经设置为你的数据库集群想要的区域，那么你就没有什么可干的。如果你想使用其它的区域(或者你还不知道你的系统设置的区域是什么)，那么你可以用--locale 命令行选项告诉initdb 比如：

```
initdb --locale=sv_SE
```

这个例子是在Unix 系统上把区域设置为瑞典(sv)用瑞典语说话(SE)。  
其它的可能性是`en_US (美国英语)`和`fr_CA`(加拿大法语)。如果多于一种字符集用于区域，那么你可以从language_territory.codeset进行详细设置。例如:  
fr_BE.UTF-8代表 比利时人说的法语,将编码设置为UTF-8 。

你的系统里有哪些可用的区域设置,它们的名字是什么，这些信息都取决于你的操作系统提供商提供了什么以及你安装了什么东西。在大多数Unix系统上,命令locale -a 将提供所有可用区域的一个列表。Windows 使用冗长的 区域名称, 像`German_Germany`或者`Swedish_Sweden.1252`,但是基本原则是一样的。

有时候，把几种区域规则混合起来也很有用，比如，使用英语字符规则而用西班牙语信息。为了支持这些，我们有一套区域子范畴用于控制区域规则的某一方面：

<pre>
LC_COLLATE	字符串排序顺序
LC_CTYPE	字符分类(什么是字母?它是这个字母的等效大写?)
LC_MESSAGES	信息语言
LC_MONETARY	货币金额的格式
LC_NUMERIC	数字的格式
LC_TIME	    日期和时间的格式
</pre>

这些范畴名转换成initdb选项的名字以覆盖某个特定范畴的区域选择。比如，要把区域设置为加拿大法语，但使用美国的货币格式化规则，可以使用

```
initdb --locale=fr_CA --lc-monetary=en_US.
```

如果你想要你的系统表现得像没有区域支持一样，那么使用特殊的区域C或POSIX.

一些区域范畴的性质是它们的值必需在数据库集群的生命期内固定。也就是说，一旦运行了initdb之后，你就再也不能更改它们了。`LC_COLLATE`和`LC_CTYPE`就是这样的范畴。 它们影响索引的排序顺序，因此它们必需保持固定，否则在文本字段上的索引将会崩溃。

其它区域范畴可以在服务器启动的时候根据需要设置运行时配置变量来改变.initdb选择的缺省值实际上只是做为服务器启动缺省写入postgresql.conf配置文件。如果你在 postgresql.conf里面删除了这些缺省值，那么服务器将会继承来自运行环境的设置。

请注意服务器的区域行为是由它看到的环境变量决定的，而不是由客户端的环境变量影响的。因此，我们要在启动服务器之前认真地设置好这些变量。 这样带来的一种情况是如果客户端和服务器设置成不同的区域，那么消息可能以不同的语言呈现，实际情况取决于它们的源是什么。

Note: 在我们谈到从执行环境继承区域的时候，我们的意思是在大多数操作系统上的下列动作：对于一个给定的区域范畴，比如字符集，按照下面的顺序评估这些环境变量， 直到找到一个已设置的：`LC_ALL`,`LC_COLLATE`(变量对应相应的范畴),LANG。如果这些环境变量一个都没有设置，那么区域缺省为C.

一些信息区域化库也使用环境变量LANGUAGE它覆盖所有其它用于设置语言信息的区域设置。如果有问题，请参考你的操作系统文档，特别是gettext的文档获取更多信息。

要允许将信息翻译成用户选择的语言，编译时必需打开NLS选项(configure --enable-nls)。所有其它的本地化支持会在编译时自动提供。

###行为###
区域设置特别影响下面的SQL特性:  

- 使用 ORDER BY和区域的排序
- 使用 LIKE 子句的索引能力
- upper,lower,和initcap函数
- to_char函数族

PostgreSQL里使用非C或POSIX是速度。它降低了字符处理的速度并阻止了在LIKE类查询里面普通索引的使用。因此，只有在你实际上需要的时候才使用它。

为了允许 PostgreSQL在非C区域下的LIKE子句中使用索引，有好几个自定义的操作符类可以用。这些操作符类允许创建一个严格地比较每个字符的索引，而忽略区域比较规则。
###问题##
如果经过上面解释后区域支持仍然不能运转， 那你就要检查一下操作系统的区域支持是否正确配置。 要检查某个区域是否安装并且正常运转，你可以使用 locale -a 命令(如果你的系统提供了该命令)。

请检查核实PostgreSQL确实使用了你认为它该用的区域设置。`LC_COLLATE`和`LC_CTYPE`的设置都是在initdb时决定的，如果不重复initdb是不可能改变的。 其它的区域设置包括`LC_MESSAGES`和`LC_MONETARY`都是由服务器的启动环境决定的，但是可以在运行时修改。你可以用SHOW命令检查数据库正在使用的区域设置。

目录src/test/locale目录包含PostgreSQL的区域支持测试套件。

那些通过分析错误信息处理服务器端错误的客户端应用很明显会有问题，因为服务器信息可能会以不同的语言表示。我们建议这类应用的开发人员改用错误代码机制。
##字符集支持##
PostgreSQL 能够以各种字符集存储文本，比如 ISO-8859系列和EUC(扩展Unix编码)、UTF-8、Mule国际编码。  
所有字符集都可以在服务器上透明地使用。如果你使用了来自其它数据源的扩展函数，那么它取决于他们是否正确地书写了代码。  
缺省的字符集是在使用initdb初始化数据库集群的时候选择的。在你创建数据库的时候是可以覆盖这个缺省的。因此，你可以有多个数据库，每个都有不同的字符集。

一项重要的限制是每个数据库的字节设置必须被数据库的`LC_CTYPE`（字节分类）和`LC_COLLATE`（字符串存储命令）区域设置兼容。 对于C或者POSIX区域，任何字符设置都是被允许的，但是对于其它区域仅仅只可以设置一种字符才可以正常工作。(在windows操作系统，UTF-8编码可以在任何一个区域使用。)  

<pre>
SQL_ASCII设置与其它设置表现得相当不同。如果服务器字符集是SQL_ASCII, 服务器把字节值 0-127的数值根据ASCII标准解析而字节值128-255的则当作未解析的字符。 如果设置为SQL_ASCII.就不会有编码转换。  
因此，这个设置基本不用来声明所使用的编码，因为这个声明会忽略编码。在大多数情况下，如果你使用了任何非ASCII数据，那么使用SQL_ASCII设置都是不明智的，因为 PostgreSQL会无法帮助你转换或者校验非ASCII字符。
</pre>

###设定字符集###
initdb 为一个 PostgreSQL 集群定义缺省的字符集，比如：

```
initdb -E EUC_JP
```

把缺省字符集设置为EUC_JP(用于日文的扩展 Unix 编码).如果你喜欢用长选项声明的话,可以用--encoding代替-E 选项。如果没有给出-E或者--encoding选项 initdb将基于制定的区域或者缺省区域试图判断合适的编码。

在创建数据库的时候你可以指定一个非默认的编码，提供适合所选区域的编码：

```
createdb -E EUC_KR -T template0 --lc-collate=ko_KR.euckr --lc-ctype=ko_KR.euckr korean
```

创建一个叫做korean的数据库，使用字集`EUC_KR`和区域`ko_KR`，另外一种实现方法是使用SQL命令：

```
CREATE DATABASE korean WITH ENCODING 'EUC_KR' LC_COLLATE='ko_KR.euckr' LC_CTYPE='ko_KR.euckr' TEMPLATE=template0;
```

注意：以上的命令指定复制数据库template0。当复制别的数据库时，编码和别的区域化设置不能从源数据库内被改变，因为结果可能是错误的数据。

数据库的编码是存储在 pg_database系统表中的。你可以用 psql 的-l 选项或者 \l列出这些编码.

<pre>
$ psql -l
                                         List of databases
   Name    |  Owner   | Encoding  |  Collation  |    Ctype    |          Access Privileges          
-----------+----------+-----------+-------------+-------------+-------------------------------------
 clocaledb | hlinnaka | SQL_ASCII | C           | C           | 
 englishdb | hlinnaka | UTF8      | en_GB.UTF8  | en_GB.UTF8  | 
 japanese  | hlinnaka | UTF8      | ja_JP.UTF8  | ja_JP.UTF8  | 
 korean    | hlinnaka | EUC_KR    | ko_KR.euckr | ko_KR.euckr | 
 postgres  | hlinnaka | UTF8      | fi_FI.UTF8  | fi_FI.UTF8  | 
 template0 | hlinnaka | UTF8      | fi_FI.UTF8  | fi_FI.UTF8  | {=c/hlinnaka,hlinnaka=CTc/hlinnaka}
 template1 | hlinnaka | UTF8      | fi_FI.UTF8  | fi_FI.UTF8  | {=c/hlinnaka,hlinnaka=CTc/hlinnaka}
(7 rows)
</pre>

Important: 在大多数现代的操作系统中，PostgreSQL可以决定哪个字符集被LC_CTYPE设置，它会在匹配数据库编码时运行。  
在比较老的操作系统上，你的任务是保证你用到的编码是你选择的区域所预期的。这个区域的的一个错误可能会导致locale-dependent的错误行为。

PostgreSQL将会允许超级用户用`SQL_ASCII`编码创建数据库，即使`LC_CTYPE`不是C或POSIX。  
就像上面注意到的，SQL_ASCII不执行那些在数据库里有特别编码的数据存储，这个选择构成locale-dependent发生错误行为的风险。 使用这些组合的设置已经过时，或者某一天可能被禁止。
###服务器和客户端之间的自动字符集转换###
PostgreSQL 支持在服务器和前端之间的自动编码转换。转换信息在系统表pg_conversion中存储。PostgreSQL带着一些预定义的转换。 你可以使用 SQL命令CREATE CONVERSION创建一个新的转换。  

要想打开自动字符集转换功能，你必须告诉PostgreSQL你想在客户端使用的字符集(编码)。你可以用好几种方法实现这个目的。

用psql里的\encoding 命令\encoding允许你动态修改客户端编码。 比如，把编码改变为SJIS 键入：

```
\encoding SJIS
```

2. 使用libpq具有控制客户端编码的功能。
3. 使用 SET client_encoding TO. 设置客户端编码:
4. SET CLIENT_ENCODING TO 'value';

你还可以把SQL语法里的SET NAMES用于这个目的：

```
SET NAMES 'value';
```

查询当前客户端编码：

```
SHOW client_encoding;
```

返回缺省编码：

```
RESET client_encoding;
```

使用PGCLIENTENCODING.如果在客户端的环境里定义了PGCLIENTENCODING 环境变量，那么在与服务器进行连接时将自动选择客户端编码。这个编码随后可以用上面谈到的任何其它方法覆盖。

使用`client_encoding`配置变量。如果在`client_encoding`里设置了该变量， 那么在与服务器建立了连接之后，这个客户端编码将自动选定。这个设置随后可以被上面提到的其它方法覆盖。

假如无法进行特定的字符转换，比如，你选的服务器编码是EUC_JP而客户端是LATIN1那么有些日文字符不能转换成LATIN1,这时将报告错误。

如果客户端字符集定义成了`SQL_ASCII`,那么编码转换会被关闭，不管服务器的字符集是什么都一样。和服务器一样，除非你的工作环境全部是ASCII数据，否则使用 SQL_ASCII是不明智的。