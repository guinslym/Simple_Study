  General
  \copyright             show PostgreSQL usage and distribution terms,显示PostgreSQL的使用和发行许可条款
  \g [FILE] or ;         execute query (and send results to file or |pipe)，执行查询(将结果发送到文件或unix系统的管道中)
  \gset [PREFIX]         execute query and store results in psql variables，执行查询并将结果保存在psql变量中
  \h [NAME]              help on syntax of SQL commands, * for all commands，SQL命令语法上的说明,*表示所有的命令
  \q                     quit psql，退出psql
  \watch [SEC]           execute query every SEC seconds,每隔SEC秒执行1次查询

Query Buffer(查询缓冲区)
  \e [FILE] [LINE]       edit the query buffer (or file) with external editor,使用外部的编辑器查询缓存区或文件
  \ef [FUNCNAME [LINE]]  edit function definition with external editor，使用外部的编辑器编辑函数的定义
  \p                     show the contents of the query buffer，显示查询缓冲区的内容
  \r                     reset (clear) the query buffer，清除查询缓冲区
  \s [FILE]              display history or save it to file，显示历史记录或写入到文件中
  \w FILE                write query buffer to file，将查询缓冲区的内容写入到文件中

Input/Output(输入/输出)
  \copy ...              perform SQL COPY with data stream to the client host，执行SQL COPY语句,并将数据流发送到客户端主机
  \echo [STRING]         write string to standard output，将字符串写入到标准输出流
  \i FILE                execute commands from file，执行文件中的命令
  \ir FILE               as \i, but relative to location of current script，与\i类似，但是是相对于当前脚本的位置而言
  \o [FILE]              send all query results to file or |pipe，发送所有的查询结果到文件或管道中
  \qecho [STRING]        write string to query output stream (see \o)，将字符串写入到查询输出流中(参考\o)

Informational
  (options: S = show system objects, + = additional detail),选项:S表示显示系统对象，+表示额外的详细信息
  \d[S+]                 list tables, views, and sequences，列出当前数据库中的所有表、视图和序列
  \d[S+]  NAME           describe table, view, sequence, or index，描述给定表、视图、序列或索引的信息
  \da[S]  [PATTERN]      list aggregates，列出所有的聚合函数

  \db[+]  [PATTERN]      list tablespaces，列出所有的表空间
  \dc[S+] [PATTERN]      list conversions，列出所有的表转换
  \dC[+]  [PATTERN]      list casts，列出类型强制转换
  \dd[S]  [PATTERN]      show object descriptions not displayed elsewhere，列出没有在其他地方显示的对象的描述信息
  \ddp    [PATTERN]      list default privileges，列出缺省的权限
  \dD[S+] [PATTERN]      list domains，列出值域
  \det[+] [PATTERN]      list foreign tables，列出外键的表
  \des[+] [PATTERN]      list foreign servers，列出外部服务器
  \deu[+] [PATTERN]      list user mappings，列出用户的映射
  \dew[+] [PATTERN]      list foreign-data wrappers，列出外部数据的封装器
  \df[antw][S+] [PATRN]  list [only agg/normal/trigger/window] functions，列出(聚合、常规、触发器、窗口)函数
  \dF[+]  [PATTERN]      list text search configurations，列出文本搜索的配置
  \dFd[+] [PATTERN]      list text search dictionaries，列出文本搜索的字典
  \dFp[+] [PATTERN]      list text search parsers，列出文本搜索的解析器
  \dFt[+] [PATTERN]      list text search templates，列出文本搜索的模板
  \dg[+]  [PATTERN]      list roles，列出所有的角色
  \di[S+] [PATTERN]      list indexes，列出所有的索引
  \dl                    list large objects, same as \lo_list，列出所有的大对象，功能与\lo_list相同
  \dL[S+] [PATTERN]      list procedural languages，列出所有的过程化语言
  \dm[S+] [PATTERN]      list materialized views，列出所有的物化视图
  \dn[S+] [PATTERN]      list schemas，列出所有的模式
  \do[S]  [PATTERN]      list operators，列出所有的运算符
  \dO[S+] [PATTERN]      list collations，列出所有的校对规则
  \dp     [PATTERN]      list table, view, and sequence access privileges，列出表、视图和序列的访问权限
  \drds [PATRN1 [PATRN2]] list per-database role settings，列出每隔数据库的角色配置
  \ds[S+] [PATTERN]      list sequences，列出所有的序列
  \dt[S+] [PATTERN]      list tables，列出所有的数据表
  \dT[S+] [PATTERN]      list data types，列出所有的数据类型
  \du[+]  [PATTERN]      list roles，列出所有的角色
  \dv[S+] [PATTERN]      list views，列出所有的视图
  \dE[S+] [PATTERN]      list foreign tables，列出所有的引用表
  \dx[+]  [PATTERN]      list extensions，列出所有的扩展
  \dy     [PATTERN]      list event triggers，列出所有事件触发器
  \l[+]   [PATTERN]      list databases，列出所有的数据库
  \sf[+] FUNCNAME        show a function's definition，显示1个函数的定义
  \z      [PATTERN]      same as \dp，功能与\dp相同

Formatting(格式化)
  \a                     toggle between unaligned and aligned output mode，在非对齐与对齐输出模式进之间行切换
  \C [STRING]            set table title, or unset if none，设置表的标题，如果没有的标题则取消该操作
  \f [STRING]            show or set field separator for unaligned query output，显示或设置非对齐模式下查询输出的字段分隔符
  \H                     toggle HTML output mode (currently off)，切换到HTML输出模式，当前是关闭状态
  \pset NAME [VALUE]     set table output option，设置织表的输出选项
                         (NAME := {format|border|expanded|fieldsep|fieldsep_zero|footer|null|
                         numericlocale|recordsep|recordsep_zero|tuples_only|title|tableattr|pager})
  \t [on|off]            show only rows (currently off)，只显示记录(当前是关闭状态)
  \T [STRING]            set HTML <table> tag attributes, or unset if none，设置HTML表格标签属性，如果没有该标签的取消本次操作
  \x [on|off|auto]       toggle expanded output (currently off)，切换到扩展输出模式，当前是关闭模式

Connection(连接)
  \c[onnect] [DBNAME|- USER|- HOST|- PORT|-]
                         connect to new database (currently "tim")，连接新的数据库，当前是数据库tim
  \encoding [ENCODING]   show or set client encoding,显示或设置客户端的编码
  \password [USERNAME]   securely change the password for a user，安全的修改用户口令
  \conninfo              display information about current connection，显示当前连接的相关信息

Operating System(操作系统)
  \cd [DIR]              change the current working directory，改变当前工作的目录
  \setenv NAME [VALUE]   set or unset environment variable，设置或清空环境变量
  \timing [on|off]       toggle timing of commands (currently off)，切换到即时命令
  \! [COMMAND]           execute command in shell or start interactive shell，在shell下执行命令或开始交互模式

Variables(变量)
  \prompt [TEXT] NAME    prompt user to set internal variable，提示用户设定内部变量
  \set [NAME [VALUE]]    set internal variable, or list all if no parameters，设定内部变量，如果参数则列出所有变量
  \unset NAME            unset (delete) internal variable，删除或清空内部变量

Large Objects(大对象)
  \lo_export LOBOID FILE
  \lo_import FILE [COMMENT]
  \lo_list
  \lo_unlink LOBOID      large object operations(大对象运算)
