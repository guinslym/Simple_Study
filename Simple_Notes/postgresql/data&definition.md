数据定义.md
##表的基本概念##
关系型数据库中的表非常类似纸面上的一张表：它由行和列组成。字段的数目是固定的，每个字段都有一个名字。  
行的数目是变化的(它反映了任意时刻存储的数据量)。 SQL 对行的顺序没有任何承诺(除非你明确地要求排序)。  
另外，SQL 并不给行赋予唯一的标识，因此我们很可能在一个表中有好几个完全相同的行。 这是作为 SQL 基础的下层数学模型的必然结果，但是这通常是我们不愿意看到的。

每个字段都有一个数据类型。数据类型控制着一个字段所有可能值的集合，并且控制着字段中数据的语义，这样它就可以用于计算。  
比如，一个声明为数值类型的字段不会接受任意文本字符串，而存储在这种字段里的数据可以用于数学计算。  
相比之下，一个声明为字符串类型的字段接受几乎任意类型的数据，但是它们不能进行数学计算(不过可以进行像字符串连接之类的操作)。

PostgreSQL 包含一套可剪裁的内置数据类型，这些类型 可以适用于许多应用。  
用户也可以定义它们自己的数据类型。大多数内置的数据类型有 显而易见的名字和语义。  
常用的数据类型有：用于整数的integer、用于可能为分数的numeric 、 用于字符串的text、用于日期的date 、用于时间的time 、 用于时间戳的timestamp 。

要创建一个表，可用使用CREATE TABLE命令。 在这个命令里，你至少要为新表声明 一个名字，还有各字段的名字以及其数据类型。比如：

```
CREATE TABLE my_first_table (
    first_column text,
    second_column integer
);
```

这样就创建了一个有两个字段的名为my_first_table的表。 第一个字段的名字是first_column，数据类型为text； 第二个字段的名字遵循Section 4.1.1里面解释的标识符语法。 类型名通常也是标识符(但是有一些例外)。 请注意字段 列表是逗号分隔的，并且用圆括弧包围。

当然，前面只是一个非常虚构的例子。通常，你会给表和字段取一个有意义的名字， 所以还是让我们给一个比较现实的例子：

```
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric
);
```

numeric 类型可以存储分数部分，金额很可能有这样的分数部分。

Tip: 如果你创建了许多相互关联的表，那么最好为表和字段选择一致的命名模式。 比如，表名字可以统一选择单数或者复数，两种选择都有这样那样的理论家支持。

一个表能包含的字段数目是有限制的。根据字段类型的不同，这个数目可能在250 到1600 之间。不过，不管是哪一端的数字，如果你设计的表包含那么多 的字段好像都很不可能发生，否则是设计上有问题的表现。

如果你不再需要一个表，那么可以用DROP TABLE命令删除它。像这样：

```
DROP TABLE my_first_table;
DROP TABLE products;
```

试图删除一个不存在的表是一个错误。不过，在 SQL 脚本文件里，我们通常在创建表 之前无条件删除它并忽略错误信息。（当然你还可以使用DROP TABLE IF EXISTS 来避免警告信息，不过这并不符合 SQL 标准。）

使用到目前为止讨论的工具我们可以创建功能完整的表。本章剩下的部分是有关向表定义中增加特性、保证数据完整性、安全性或便利性的内容。如果 你急于给表填充数据，那么你可以忽略余下的部分直接到Chapter 6， 然后在稍后的时候再回来阅读本章。

##缺省值##
一个字段可以赋予缺省值。如果新创建了一个数据行，而有些字段的数值没有声明， 那么这些字段将被填充为它们各自的缺省值。一条数据修改命令也可以明确地要求 把一个字段设置为它的缺省值，而不用事先知道这个缺省值是什么。

如果没有明确声明缺省值，那么缺省值是 NULL。这么做通常是合理的，因为NULL表示"未知"。

在一个表定义里，缺省值是在字段数据类型后面列出的。比如：

```
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric DEFAULT 9.99
);
```

缺省值可以是一个表达式，它会在插入缺省值的时候计算(不是 在创建表的时候)。一个常见的例子是一个timestamp字段可能有缺省值 CURRENT_TIMESTAMP ，它表示插入行的时刻。另外一个常见的例子是为 每一行生成一个""serial number""。在PostgreSQL里， 通常是用类似下面这样的方法生成的：

```
CREATE TABLE products (
    product_no integer DEFAULT nextval('products_product_no_seq'),
    ...
);
```

这里的nextval()从一个序列对象(参阅Section 9.15)提供后继的数值。这种做法非常普遍， 以至于我们有一个专门的缩写用于此目的：

```
CREATE TABLE products (
    product_no SERIAL,
    ...
);
```

##约束##
数据类型是限制我们可以在表里存储什么数据的一种方法。不过，对于许多应用 来说，这种限制实在是太粗糙了。比如，一个包含产品价格的字段应该只接受正数。
但是没有哪种标准数据类型只接受正数。另外一个问题是你可能需要根据其它字段或者其它行的数据来约束字段数据。比如，在一个包含产品信息的表中，每个产品 编号都应该只有一行。

对于这些问题，SQL允许你在字段和表上定义约束。约束允许你对数据施加任意控制。 如果用户企图在字段里存储违反约束的数据，那么就会抛出一个错误。这种情况同时 也适用于数值来自缺省值的情况。

###检查约束###

检查约束是最常见的约束类型。它允许你声明在某个字段里的数值必须使一个布尔表达式为真。比如，要强制一个正数的产品价格，你可以用：

```
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric CHECK (price > 0)
);
```

如你所见，约束定义在数据类型之后，就好像缺省值定义一样。缺省值和 约束可以按任意顺序排列。一个检查约束由一个关键字CHECK 后面跟一个放在圆括弧里的表达式组成。检查约束表达式应该包含受约束的字段， 否则这个约束就没什么意义了。

你还可以给这个约束取一个独立的名字。这样就可以令错误信息更清晰，并且 在你需要修改它的时候引用这个名字。语法是：

```
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric CONSTRAINT positive_price CHECK (price > 0)
);
```

因此，要声明一个命名约束，使用关键字 CONSTRAINT 后面跟一个标识符(作为名字)，然后再跟约束定义。如果你不用这个方法声明约束，那么系统会自动 为你选择一个名字。

一个检查约束也可以引用多个字段。假设你存储一个正常价格和一个折扣价， 并且你想保证折扣价比正常价低。

```
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric CHECK (price > 0),
    discounted_price numeric CHECK (discounted_price > 0),
    CHECK (price > discounted_price)
);
```

头两个约束看上去很面熟。第三个使用了一个新的语法。它没有附着在某个字段上，而是在逗号分隔的字段列表中以一个独立行的形式出现。 字段定义和约束定义可以按照任意顺序列出。

我们称头两个约束是"字段约束"，而第三个约束是"表约束"(和字段定义分开写)。 字段约束也可以写成表约束，而反过来很可能不行，因为系统假设字段约束只 引用它所从属的字段。  
PostgreSQL 并不强制这条规则， 但是如果你希望自己的表定义可以和其它数据库系统兼容，那么你最好还是遵循这条 规则。上面的例子也可以这么写：

```
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric,
    CHECK (price > 0),
    discounted_price numeric,
    CHECK (discounted_price > 0),
    CHECK (price > discounted_price)
);
```

或者是

```
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric CHECK (price > 0),
    discounted_price numeric,
    CHECK (discounted_price > 0 AND price > discounted_price)
);
```

这只是风格的不同。

和字段约束一样，我们也可以给表约束赋予名称，方法也相同：

```
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric,
    CHECK (price > 0),
    discounted_price numeric,
    CHECK (discounted_price > 0),
    CONSTRAINT valid_discount CHECK (price > discounted_price)
);
```

我们还要注意的是，当约束表达式计算结果为 NULL 的时候，检查约束会被认为是满足条件的。因为大多数表达式在含有 NULL 操作数的时候结果都是 NULL ，所以这些约束不能阻止字段值为NULL 。要确保一个字段值不为NULL ，可以使用下一节 介绍的非空约束。

###非空约束###

非空约束只是简单地声明一个字段必须不能是 NULL 。下面是一个例子：

```
CREATE TABLE products (
    product_no integer NOT NULL,
    name text NOT NULL,
    price numeric
);
```

一个非空约束总是写成一个字段约束。非空约束在功能上等效于创建一个检查 约束 CHECK (column_name IS NOT NULL) ，但在PostgreSQL里， 创建一个明确的非空约束效率更高。缺点是你不能给它一个明确的名字。

当然，一个字段可以有多个约束。只要一个接着一个写就可以了：

```
CREATE TABLE products (
    product_no integer NOT NULL,
    name text NOT NULL,
    price numeric NOT NULL CHECK (price > 0)
);
```

它们的顺序无所谓。顺序并不影响约束检查的顺序。

NOT NULL 约束有个相反的约束：NULL 约束。它并不意味着该字段必须是空，因为这样的字段也没用。它只是定义了该字段 可以为空的这个缺省行为。  
在 SQL 标准里没有定义NULL约束， 因此不应该在可移植的应用中使用它。在PostgreSQL 里面增加这个约束只是为了和其它数据库系统兼容。  
不过，有些用户喜欢它，因为 这个约束可以让他们很容易在脚本文件里切换约束。比如，你可以从下面这样开始：

```
CREATE TABLE products (
    product_no integer NULL,
    name text NULL,
    price numeric NULL
);
```

然后在需要的时候插入 NOT 关键字。

Tip: 在大多数数据库设计里，主要的字段都应该标记为非空。

### 唯一约束###

唯一约束保证在一个字段或者一组字段里的数据与表中其它行的数据相比是唯一的。 它的语法是：

```
CREATE TABLE products (
    product_no integer UNIQUE,
    name text,
    price numeric
);
```

上面是写成字段约束，下面这个则写成表约束：

```
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric,
    UNIQUE (product_no)
);
```

如果一个唯一约束引用一组字段，那么这些字段用逗号分隔列出：

```
CREATE TABLE example (
    a integer,
    b integer,
    c integer,
    UNIQUE (a, c)
);
```

这样就声明了特定字段值的组合在整个表范围内是唯一的。但是这些字段中的某个单独值可以不必是(并且通常也确实不是)唯一的。

你也可以给唯一约束赋予一个自己定义的名字，方法与前面相同：

```
CREATE TABLE products (
    product_no integer CONSTRAINT must_be_different UNIQUE,
    name text,
    price numeric
);
```

添加一个唯一约束会在一个字段或者一组字段里自动创建一个唯一btree索引，以供在约束里运用。

通常，如果包含在唯一约束中的那几个字段在表中有多个相同的行，就违反了唯一约束。
但是在这种比较中，NULL 被认为是不相等的。这就意味着，在多字段唯一约束的情况下， 如果在至少一个字段上出现 NULL ，那么我们还是可以存储同样的这种数据行。  
这种行 为遵循 SQL 标准，但是我们听说其它 SQL 数据库可能不遵循这个标准。因此如果你要开发可移植的程序，那么最好仔细些。

###主键###

从技术上讲，主键约束只是唯一约束和非空约束的组合。所以，下面两个表定义是等价的：

```
CREATE TABLE products (
    product_no integer UNIQUE NOT NULL,
    name text,
    price numeric
);
CREATE TABLE products (
    product_no integer PRIMARY KEY,
    name text,
    price numeric
);
```

主键也可以约束多于一个字段；其语法类似于唯一约束：

```
CREATE TABLE example (
    a integer,
    b integer,
    c integer,
    PRIMARY KEY (a, c)
);
```

主键表示一个或多个字段的组合可以用于唯一标识表中的数据行。这是定义 一个主键的直接结果。  
请注意：一个唯一约束实际上并不能提供一个唯一标识， 因为它不排除NULL。  
这个功能对文档目的和客户应用都很有用。比如,一个 可以修改行数值的GUI应用可能需要知道一个表的主键才能唯一地标识每一行。

添加一个主键会在主key运用的一字段或一组字段里自动创建一个唯一btree索引。

一个表最多可以有一个主键(但是它可以有多个唯一和非空约束)。关系型数据库 理论告诉我们，每个表都必须有一个主键。PostgreSQL并不强制这个规则，但 我们最好还是遵循它。

###外键###

外键约束声明一个字段(或者一组字段)的数值必须匹配另外一个表中出现的数值。 我们把这个行为称为两个相关表之间的参照完整性。

假设你有个产品表，我们可能使用了好几次：

```
CREATE TABLE products (
    product_no integer PRIMARY KEY,
    name text,
    price numeric
);
```

假设你有一个存储这些产品的订单的表。我们想保证订单表只包含实际存在的产品。因此我们在订单表中定义一个外键约束引用产品表：

```
CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_no integer REFERENCES products (product_no),
    quantity integer
);
```

现在，我们不能创建任何其product_no没有在产品表中出现的订单。

在这种情况下我们把订单表叫做引用表， 而产品表叫做被引用表。 同样，也有引用字段和被引用字段。

你也可以把上面的命令简写成：

```
CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_no integer REFERENCES products,
    quantity integer
);
```

因为如果缺少字段列表的话，就会引用被引用表的主键。

一个外键也可以约束和引用一组字段。同样，也需要写成表约束的形式。 下面是一个捏造出来的语法例子：

```
CREATE TABLE t1 (
  a integer PRIMARY KEY,
  b integer,
  c integer,
  FOREIGN KEY (b, c) REFERENCES other_table (c1, c2)
);
```

当然，被约束的字段数目和类型需要和被引用字段数目和类型一致。

和平常一样，你也可以给外键约束赋予自定义的名字。

一个表可以包含多于一个外键约束。这个特性用于实现表之间的多对多关系。 比如你有关于产品和订单的表，但现在你想允许一个订单可以包含多种产品 (上面那个结构是不允许这么做的)，你可以使用这样的结构：

```
CREATE TABLE products (
    product_no integer PRIMARY KEY,
    name text,
    price numeric
);

CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    shipping_address text,
    ...
);

CREATE TABLE order_items (
    product_no integer REFERENCES products,
    order_id integer REFERENCES orders,
    quantity integer,
    PRIMARY KEY (product_no, order_id)
);
```

注意最后的表的主键和外键是重叠的。

我们知道外键不允许创建和任何产品都无关的订单。但是如果一个订单 创建之后其引用的产品被删除了怎么办？SQL 也允许你处理这个问题。 简单说，我们有几种选择：

- 不允许删除一个被引用的产品
- 同时也删除订单
- 其它的？

为了说明这个问题，我们对上面的多对多关系制定下面的策略：如果有人想 删除一种仍然被某个订单引用的产品(通过order_items)，那么就不允许这么做。 如果有人删除了一个订单，那么订单项也被删除。

```
CREATE TABLE products (
    product_no integer PRIMARY KEY,
    name text,
    price numeric
);

CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    shipping_address text,
    ...
);

CREATE TABLE order_items (
    product_no integer REFERENCES products ON DELETE RESTRICT,
    order_id integer REFERENCES orders ON DELETE CASCADE,
    quantity integer,
    PRIMARY KEY (product_no, order_id)
);
```

限制和级联删除是两种最常见的选项。RESTRICT禁止删除被引用的行。 NO ACTION的意思是如果在检查约束的时候 还存在任何引用行，则抛出错误；  
如果你不声明任何东西，那么它就是缺省的行为。 这两个选择的实际区别是：NO ACTION允许约束检查推迟到事务的 晚些时候，而 RESTRICT不行。  
CASCADE声明在删除 一个被引用的行的时候，所有引用它的行也会被自动删除掉。在外键字段上的动作还有两个选项： SET NULL和SET DEFAULT ， 它们导致在被引用行删除的时候，将引用它们的字段分别设置为NULL和缺省值。
请注意这些选项并不能让你逃脱被观察和约束的境地。比如，如果一个动作声明 SET DEFAULT，但是缺省值并不能满足外键，那么该动作就会失败。

与ON DELETE类似的还有ON UPDATE选项， 它是在被引用字段修改(更新)的时候调用的，可用的动作是一样的。

从一个引用表中的DELETE一行或者从引用字段中UPDATE一列都需要扫描一次引用表以便从行中匹配老的数值，给引用列建索引一直是一个好主意。  
因为这不总是被需要，而且怎么去建立索引还有许多其它的选择，外键的约束声明不能在引用字段里自动生成索引。

最后，我们应该说明的是，一个外键必须要么引用一个主键，要么引用一个唯一约束。 如果外键引用了一个唯一约束，那么在如何匹配 NULL 这个问题上还有一些其它的可能性。 这些东西都在CREATE TABLE 中解释。

###排除约束###

排除约束保证如果任何两行被在声明的字段里比较或者用声明的操作表达， 至少有一个操作比较会返回错误或空值。 句法是：

```
CREATE TABLE circles (
    c circle,
    EXCLUDE USING gist (c WITH &&)
);
```

更多细节也请参考CREATE TABLE ... CONSTRAINT ... EXCLUDE。

添加一个排除约束会在约束声明里自动创建一个声明类型的索引。
##系统字段##
每个表都有几个系统字段 ，这些字段是由系统隐含定义的。 因此，这些名字不能用于用户定义的字段名。请注意这些限制与这个名字是否关 键字无关，把名字用引号括起来并不能让你逃离这些限制。你实际上不需要注意 这些字段，只要知道它们存在就可以了。

- oid
行对象标识符(对象ID)。这个字段只有在创建表的时候使用了WITH OIDS 或者是配置参数default_with_oids的值为真时出现。 这个字段的类型是oid(和字段同名)。
- tableoid
包含本行的表的OID。这个字段对那些从继承层次中选取的查询特别有用 (参阅节Section 5.8)，因为如果没有它的话，我们就很难 说明一行来自哪个独立的表。tableoid可以 和pg_class的oid 字段连接起来获取表名字。
- xmin
插入该行版本的事务标识(事务ID)。注意：在这个环境里，一个行版本是一行的 一个状态；一行的每次更新都为同一个逻辑行创建一个新的行版本。
- cmin
在插入事务内部的命令标识(从零开始)。
- xmax
删除事务的标识(事务ID)，如果不是被删除的行版本，那么是零。在一个可见行版本里， 这个字段有可能是非零。这通常意味着删除事务还没有提交，或者是一个删除的企图被回滚掉了。
- cmax
删除事务内部的命令标识符，或者是零。
- ctid
一个行版本在它所处的表内的物理位置。请注意，尽管ctid 可以用于非常快速地定位行版本，但每次VACUUM FULL之后， 一个行的ctid都会被更新或者移动。因此ctid是不能作为长期的行标识符的。应该使用 OID ， 或者更好是用户定义的序列号，来标识一个逻辑行。

OID是32位的量，是在同一个集群内通用的计数器上赋值的。对于一个大型或者 长时间使用的数据库，这个计数器是有可能重叠的。因此，假定OID唯一是非常错误的， 除非你自己采取了措施来保证它们是唯一的。如果你需要标识表中的行，我们强烈建议 使用序列号生成器。不过，也可以使用OID，只要采取几个注意事项即可

在使用OID标识行的每个表的OID字段创建一个唯一约束。在唯一约束(或者唯一索引) 存在的时候，系统会注意不去生成一个和现有行相同的OID。  
当然，只有在表中的数据行 少于232(40亿)行的时候才是可能的，而实际上表中的行最好远比这个小，要不性能就会 受影响了。

绝对不要假设OIDs是跨表唯一的；如果你需要全数据库范围内的标识，请使用 tableoid和行的OID的组合。

需要OID的表应该带着WITH OIDS创建。 从PostgreSQL开始，WITHOUT OIDS是缺省的。

事务标识符也是32位的量。在长时间运转的数据库里，它也可能会重叠。只要我们采取 一些合适的维护步骤，这并不是很要命的问题；不过，在长时间运行的环境里(超过十亿次事务)依赖事务ID的唯一性并非明智的做法。

命令标识符也是32位的量。这样就在一个事务里有 232(四十亿)条SQL命令的硬限制。 在现实里这个限制应该不是什么问题，需要注意的是这个限制是SQL命令的条数， 而不是处理的行版本的条数。
##修改表##
如果你创建了一个表后发现自己犯了一个错误，或者是应用的需求发生了变化， 那么你可以删除这个表然后重新创建它。  
但是如果这个表已经填充了许多数据， 或者该表已经被其它数据库对象引用(比如一个外键约束)，那这可不是一个方 便的方法。  
因此PostgreSQL提供了一族命令用于修改现有表。请注意它在概 念上和修改一个表中包含的数据是不一样的：这里我们感兴趣的是修改一个表 的定义，或者说结构。

你可以:

- 增加字段
- 删除字段
- 增加约束
- 删除约束
- 改变缺省值
- 修改字段数据类型
- 重命名字段
- 重命名表

所有这些动作都是用 ALTER TABLE 命令执行的。

###增加字段###

要增加一个字段，使用下面这样的命令：

```
ALTER TABLE products ADD COLUMN description text;
```

新增的字段对于表中已经存在的行而言最初将先填充所给出的缺省值 (如果你没有声明DEFAULT子句，那么缺省是NULL)。

你也可以同时在该字段上定义约束，使用通常的语法：

```
ALTER TABLE products ADD COLUMN description text CHECK(description <> '');
```

实际上，所有在CREATE TABLE里描述的可以应用于字段的选项 都可以在这里使用。  
不过，我们要注意的是缺省值必须满足给出的约束，否则ADD将会失败。另外，你可以在正确填充了新字段的数值之后再增加约束(见下文)。

Tip: 添加一个字段并填充缺省值将会导致更新表中的所有行(为了存储新字段的值)， 但如果没有声明缺省值，PostgreSQL就可以 避免物理更新。  
所以如果你将要在新字段中填充的值大多数都不等于缺省值， 那么最好添加一个没有缺省值的字段，然后再使用UPDATE更新数据， 最后使用下面的方法添加缺省值。

###删除字段###

要删除一个字段，使用下面这样的命令：

```
ALTER TABLE products DROP COLUMN description;
```

不管字段里有啥数据，都会消失，和这个字段相关的约束也会被删除。不过， 如果这个字段被另一个表的外键所引用，PostgreSQL 则不会隐含地删除该约束。你可以通过使用CASCADE指明删除任何依 赖该字段的东西：

```
ALTER TABLE products DROP COLUMN description CASCADE;
```

###增加约束###

要增加一个约束，必须使用表约束语法。比如：

```
ALTER TABLE products ADD CHECK (name <> '');
ALTER TABLE products ADD CONSTRAINT some_name UNIQUE (product_no);
ALTER TABLE products ADD FOREIGN KEY (product_group_id) REFERENCES product_groups;
```

要增加一个不能写成表约束的非空约束，使用下面的语法：

```
ALTER TABLE products ALTER COLUMN product_no SET NOT NULL;
```

这个约束将立即进行检查，所以表在添加约束之前必须符合约束条件。

###删除约束###

要删除一个约束，你需要知道它的名字。如果你曾经给了它取了名字，那么事情 就很简单。否则你就需要找出系统自动分配的名字。psql的命令 \d tablename可以这个帮忙；其它接口 可能也提供了检查表的细节的方法。然后就是这条命令：

```
ALTER TABLE products DROP CONSTRAINT some_name;
```

如果你在处理一个生成的约束名，比如`$2`， 别忘了你需要给它添加双引号，让它成为一个有效的标识符。

和删除字段一样，如果你想删除被依赖的约束，你需要用CASCADE。 一个例子是某个外键约束依赖被引用字段上的唯一约束或者主键约束。

除了非空约束外，所有约束类型都这么用。要删除非空约束，可以这样：

```
ALTER TABLE products ALTER COLUMN product_no DROP NOT NULL;
```

要记得非空约束没有名字。

### 改变字段的缺省值###

要给一个字段设置缺省值，可以使用一个像下面这样的命令：

```
ALTER TABLE products ALTER COLUMN price SET DEFAULT 7.77;
```

请注意这么做不会影响任何表中现有的数据行，它只是为将来的INSERT 命令改变缺省值

要删除缺省值，可以用

```
ALTER TABLE products ALTER COLUMN price DROP DEFAULT;
```

这样实际上相当于把缺省设置为空。结果是，如果我们删除一个还没有 定义的缺省值不算错误，因为缺省隐含就是NULL

###修改字段的数据类型###

把一个字段转换成另外一种数据类型，使用下面的命令：

```
ALTER TABLE products ALTER COLUMN price TYPE numeric(10,2);
```

只有在字段里现有的每个项都可以隐含的转换成新类型时才可能成功。 如果需要更复杂的转换，你可以增加一个USING子句， 它声明如何从旧值里计算新值。

PostgreSQL将试图把字段的缺省值(如果存在)转换成新的类型， 还有涉及该字段的任何约束。但是这些转换可能失败，或者可能生成奇怪的结果。 在修改某字段类型之前，你最好删除那些约束，然后再把合适的约束添加上去。

###重命名字段###

重命名一个字段：

```
ALTER TABLE products RENAME COLUMN product_no TO product_number;
```

###重命名表###

重命名一个表：

```
ALTER TABLE products RENAME TO items;
```

##权限
如果你创建了一个数据库对象，那么你就成为它的所有者。缺省时， 只有对象的所有者可以在对象上做任何事情。为了允许其它用户使用它 ，我们必须赋予他们权限。不过超级 用户总是可以操作任何对象。）

有好多种不同的权限：SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE. 适用于特定对象的权限因对象类型(表/函数等)不同而不同。  
有关 PostgreSQL 所支持的不同类型的权限的完整信息， 请参考GRANT的手册页。下面的章节将为你展示如何利 用这些权限。

修改或者删除一个对象的权限永远是所有者独有的权限。

Note: 要改变一个表、索引、序列、或者视图的所有者，使用ALTER TABLE命令， 以及对应其它对象类型的ALTER命令。

使用GRANT命令赋予权限。因此，如果joe 是一个已经存在的用户，而accounts是一个已经存在的表， 更新表的权限可以用下面的命令赋予：

```
GRANT UPDATE ON accounts TO joe;
```

在权限的位置写上ALL则赋予所有与该对象类型相关的权限。

名为PUBLIC的特殊""user""可以用于将权限 赋予系统中的所有用户。另外，还可以使用""group""角色来帮助管理一群 用户的权限，细节可参见Chapter 20。

可以使用REVOKE命令撤销权限：

```
REVOKE ALL ON accounts FROM PUBLIC;
```

对象所有者的特殊权限(也就是，DROP，GRANT， REVOKE，等权限)总是隐含地属于所有者，并且不能赋予或者撤销。 但是对象所有者可以选择撤销自己的普通权限，比如把一个表做成对自己和别人都是只读的。

最初，只有对象所有者(或者超级用户)可以赋予或者撤销对象的权限。 但是，我们可以赋予一个""with grant option""权限，这样 就允许接受权限的人将该权限转授他人。如果授权选项后来被撤销， 那么所有那些从这个接受者接受了权限的用户(直接或间级)都将失去该权限. 细节详见GRANT和REVOKE手册页。
##模式##
一个PostgreSQL数据库集群包含一个或多个已命名数据库。用户和用户组在整个集群范围内是共享的，但是其它数据并不共享。 任何与服务器连接的客户都只能访问那个在连接请求里声明的数据库。

Note: 集群中的用户并不一定要有访问集群内所有数据库的权限。共享用户名的意思是 不能有重名用户。假定同一个集群里有两个数据库和一个joe用户， 系统可以配置成只允许joe访问其中的一个数据库

一个数据库包含一个或多个已命名的schemas，模式又包含表。 模式还可以包含其它对象，包括数据类型、函数、操作符等。同一个对象名 可以在不同的模式里使用而不会导致冲突；比如，schema1和 myschema都可以包含一个名为mytable的表。 和数据库不同，模式不是严格分离的：只要有权限，一个用户可以访问他所 连接的数据库中的任意模式中的对象。

我们需要模式的原因有好多：

- 允许多个用户使用一个数据库而不会干扰其它用户。
- 把数据库对象组织成逻辑组，让它们更便于管理。
- 第三方的应用可以放在不同的模式中，这样它们就不会和其它对象的名字冲突。
- 模式类似于操作系统层次的目录，只不过模式不能嵌套。

###创建模式###

要创建一个模式，使用CREATE SCHEMA命令。给出你选择的模式名字。比如：

```
CREATE SCHEMA myschema;
```

要创建或者访问在模式中的对象，写出一个受修饰的名字， 这个名字包含模式名以及表名，它们之间用一个句点分开：

- schema.table

这个方式在任何需要表名字的地方都可用，包括后面章节讨论的表修改命令 和数据访问命令。出于简化，我们将只讨论表，这个概念适用于所有其它已 命名对象类型，比如数据类型和函数。

实际上，更一般的语法是

- database.schema.table

这个语法也可以使用，但目前它只是为了和SQL标准形式上上兼容。 如果你写了一个数据库名，那么它必须和你当前连接的数据库同名。

要在新模式里创建一个表，用

```
CREATE TABLE myschema.mytable (
 ...
);
```

如果一个模式是空的(所有它里面的对象都已经删除)，那么删除一个模式的命令如下：

```
DROP SCHEMA myschema;
```

要删除一个模式及其包含的所有对象，可以使用：

```
DROP SCHEMA myschema CASCADE;
```

参阅Section 5.11获取对隐藏在这些动作背后的东西的一般机制的描述。

通常你想创建一个他人拥有的模式(因为这是一种限制用户在定义良好的模式中的活动的方法)。 其语法如下：

```
CREATE SCHEMA schemaname AUTHORIZATION username;
```

你甚至可以省略模式名字，这时模式名将和用户名同名。参阅 Section 5.7.6获取这种情况的适用场合。

以pg_开头的模式名是保留给系统使用的，用户不能创建这样的名字。

###模式###

在前面的小节里，我们没有声明任何模式名字就创建了表。缺省时，这样的表 (以及其它对象)都自动放到一个叫做""public""的模式中去了。 每个新数据库都包含一个这样的模式。因此，下面的命令是等效的：

```
CREATE TABLE products ( ... );
和
CREATE TABLE public.products ( ... );
```

###模式搜索路径###

全称的名字写起来非常费劲，并且我们最好不要在应用里直接写上特定的模式名。 因此，表通常都是用未修饰的名字引用的，这样的名字里只有表名字。
系统通过查找一个搜索路径来判断一个表究竟是哪个表，这个路径是一个需要查找的模式名列表。  
在搜索路径里找到的第一个表将被使用。如果在搜索路径中没有找到表，那么就报告一个错误 (即使在数据库里的其它模式中存在此表也如此)。

在搜索路径中的第一个模式叫做"当前模式"。除了是搜索的第一个模式之外，它还是在CREATE TABLE没有声明模式名的时候，新建表的默认所在地。

要显示当前搜索路径，使用下面的命令：

```
SHOW search_path;
```

在缺省的设置中，返回下面的东西：

<pre>
 search_path
--------------
 "$user",public
</pre>

第一个元素声明搜索和当前用户同名的模式。因为还没有这样的模式存在，所以这条记录被忽略。第二个元素指向我们已经看过的公共模式。

搜索路径中第一个存在的模式是创建新对象的缺省位置。这就是为什么缺省的对象都会创建在 public 模式里的原因。  
如果在其它环境中引用对象且没有模式修饰，那么系统会遍历搜索路径，直到找到一个匹配的对象。因此，在缺省的配置里，任何未修饰的访问只能引用 public 模式。

要设置模式的搜索路径，可以用(省略了$user是因为并不立即需要它)

```
SET search_path TO myschema,public;
```

然后我们就可以不使用模式修饰来访问表了：

```
DROP TABLE mytable;
```

同样，因为myschema是路径中的第一个元素，新对象缺省时将创建在这里。

我们也可以写成:

```
SET search_path TO myschema;
```

然后我们如果不明确修饰的话，就不能再访问public模式了。public模式没有任何特殊之处，只不过它缺省时就存在。我们也可以删除它。

搜索路径对于数据类型名、函数名、操作符名的运作方式和表名完全相同。数据类型和函数名可以像表名一样加以修饰。 如果你需要在表达式里写一个有模式修饰的操作符，你必须这么写：

```
OPERATOR(schema.operator)
```

这样是为了避免语法歧义。下面是一个例子：

```
SELECT 3 OPERATOR(pg_catalog.+) 4;
```

实践中我们通常依赖搜索路径寻找操作符，这样就不用写这么难看的东西了。

###模式和权限###

缺省时，用户无法访问模式中不属于他们所有的对象。为了让他们能够访问， 模式的所有者需要在模式上赋予他们USAGE权限。 为了让用户使用模式中的对象，我们可能需要赋予适合该对象的额外权限。

用户也可以在别人的模式里创建对象。要允许这么做， 需要被赋予在该模式上的CREATE权限。请注意，缺省时每个人都在public。模式上有CREATE和USAGE权限。 这样就允许所有可以连接到声明数据库上的用户在这里创建对象。如果你不打算这么做，可以撤销这个权限：

```
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
```

第一个"public"是模式，第二个"public"意思是 "every user"。第一句里它是个标识符， 而第二句里是个关键字，所以有不同的大小写。 记住我们在Section 4.1.1里面说过的原则。

###系统表模式###

除了public和用户创建的模式之外，每个数据库都包含一个pg_catalog模式， 它包含系统表和所有内置数据类型、函数、操作符。  
pg_catalog总是搜索路径中的一部分。 如果它没有明确出现在路径中，那么它隐含地在所有路径之前搜索。这样就保证了内置名字总是可以被搜索。  
不过，你可以明确地把pg_catalog放在搜索路径之后，如果你想使用用户自定义的名字覆盖内置的名字的话。

在PostgreSQL版本 7.3 之前，以pg_开头的表名字是保留的。这个规则现在不正确了：如果必要， 你可以创建这样的表名字，只要是在非系统模式里。  
不过，我们最好还是不要使用这样的名字，以保证自己将来不会和新版本冲突：

- 那些版本也许会定义一些和你的表同名的表(在缺省搜索路径中，一个对你的表的无修饰引用将解析为系统表)。  
- 系统表将继续遵循以pg_开头的传统，因此，只要你的表不是以pg_开头，就不会和无修饰的用户表名字冲突。

###使用方式###

模式可以用多种方式组织数据。下面是一些建议使用的模式，它们也很容易在缺省配置中得到支持：

如果没有创建任何模式，那么所有用户隐含都访问public模式。这样就模拟了没有模式的时候的情景。这种设置建议主要用在只有一个用户或者数据库里只有几个可信用户的情形。这样的设置也允许我们平滑地从无模式的环境过渡。

你可以为每个用户创建一个模式，名字和用户相同。要记得缺省的搜索路径从`$user`开始， 它会解析为用户名。因此，如果每个用户都有一个独立的模式，那么他们缺省时访问他们自己的模式。

如果你使用了这样的设置， 那么你可能还想撤销对public模式的访问(或者删除它)，这样，用户就真的限制于他们自己的模式了。

要安装共享的应用(被所有人使用的表、第三方提供的额外函数等等)，我们可以把它们放到独立的模式中。只要记得给需要访问它们的用户赋予合适的权限就可以了。然后用户就可以通过用一个模式名修饰来使用这些额外的对象，或者他们可以把额外的模式放到他们的搜索路径中。

###移植性###

在SQL标准里，在同一个模式里的对象被不同的用户所有的概念是不存在的。而且， 有些实现不允许你创建和它们的所有者不同名的模式。实际上，模式和用户的概念在 那些只实现了标准中规定的基本模式支持的数据库系统里几乎是一样的。因此，许多用户考虑对名字加以修饰， 使它们真正由username.tablename组成。如果你为每个用户都创建了一个模式，这实际上就是PostgreSQL的行为。

同样，在SQL标准里也没有public模式的概念。为了最大限度地遵循标准， 你不应该使用(可能甚至是应该删除)public模式。

当然，有些数据库系统可能根本没有模式，或者是通过允许跨数据库访问来提供模式的功能。如果你需要在这些系统上干活，那么为了最大限度的移植性，应该根本不使用模式。
##继承##
PostgreSQL实现了表继承，这个特性对数据库设计人员来说是一个很有效的工具。 SQL99及以后的标准定义了类型继承特性，和我们在这里描述的很多特性有区别。

让我们从一个例子开始：假设我们试图制作一个城市数据模型。每个州都有许多城市，但是只有一个首府。 我们希望能够迅速检索任何州的首府。这个任务可以通过创建两个表来实现，一个是州府表，一个是非州府表。 不过，如果我们不管什么城市都想查该怎么办?继承的特性可以帮助我们解决这个问题。 我们定义capitals 表，它继承自cities表：

```
CREATE TABLE cities (
    name            text,
    population      float,
    altitude        int     -- in feet
);

CREATE TABLE capitals (
    state           char(2)
) INHERITS (cities);
```

在这种情况下，capitals表继承它的父表cities中的所有属性。州首府有一个额外的state属性显示其所在的州。

在PostgreSQL里，一个表可以从零个或多个其它表中继承属性，而且一个查询既可以引用一个表中的所有行， 也可以引用一个表及其所有后代表的行(后面这个是缺省行为)。比如，下面的查询查找所有海拔500英尺以上的城市名，包括州首府：

```
SELECT name, altitude
    FROM cities
    WHERE altitude > 500;
```

使用PostgreSQL教程里面的数据(参阅Section 2.1)，它返回：

<pre>
   name    | altitude
-----------+----------
 Las Vegas |     2174
 Mariposa  |     1953
 Madison   |      845
</pre>
另一方面，如果要找出不包括州首府的所有海拔超过500英尺的城市，查询应该是这样的：

```
SELECT name, altitude
    FROM ONLY cities
    WHERE altitude > 500;
```

<pre>
   name    | altitude
-----------+----------
 Las Vegas |     2174
 Mariposa  |     1953
</pre>

cities前面的ONLY表明该查询应该只针对cities而不包括其后代。许多我们已经讨论过的命令— SELECT， UPDATE，DELETE —都支持ONLY关键字。

有时候你可能想知道某个行版本来自哪个表。在每个表里我们都有一个 tableoid系统属性可以告诉你源表是谁：

```
SELECT c.tableoid, c.name, c.altitude
FROM cities c
WHERE c.altitude > 500;
```

结果如下(你可能会得到不同的 OID)：

<pre>
tableoid | name | altitude
 ----------+-----------+----------
 139793 | Las Vegas | 2174
 139793 | Mariposa | 1953
 139798 | Madison | 845

 tableoid | name | altitude
 ----------+-----------+----------
 139793 | Las Vegas | 2174
 139793 | Mariposa | 1953
 139798 | Madison | 845
 </pre>

 通过和pg_class做一个连接，就可以看到实际的表名字:

```
SELECT p.relname, c.name, c.altitude
FROM cities c, pg_class p
WHERE c.altitude > 500 AND c.tableoid = p.oid;
```

它返回:

<pre>
     relname  |   name    | altitude
    ----------+-----------+----------
     cities   | Las Vegas |     2174
     cities   | Mariposa  |     1953
     capitals | Madison   |      845
</pre>

对于INSERT或COPY，继承并不自动影响其后代表。在我们的例子里，下面的INSERT语句将会失败：

```
INSERT INTO cities (name, population, altitude, state)
 VALUES ('New York', NULL, NULL, 'NY');
```

我们可能希望数据被传递到capitals表里面去，但这是不会发生的：INSERT总是插入明确声明的那个表。  
在某些情况下，我们可以使用规则进行重定向插入(参阅Chapter 37)。不过它不能对上面的例子有什么帮助， 因为cities表并不包含state字段，因此命令在规则施加之前就会被拒绝掉。

所有父表的检查约束和非空约束都会自动被所有子表继承。不过其它类型的约束(唯一、主键、外键)不会被继承。

一个子表可以从多个父表继承，这种情况下它将拥有所有父表字段的总和，并且子表中定义的字段也会加入其中。  
如果同一个字段名出现在多个父表中，或者同时出现在父表和子表的定义里，那么这些字段就会被"融合"， 这样在子表里就只有一个这样的字段。  
要想融合，字段的数据类型必须相同，否则就会抛出一个错误。融合的字段将会拥有其父字段的所有检查约束， 并且如果某个父字段存在非空约束，那么融合后的字段也必须是非空的。

表继承通常使用带INHERITS子句的CREATE TABLE语句定义。另外，一个已经用此方法定义的子表 可以使用带INHERIT的ALTER TABLE命令添加一个新父表。  
注意：该子表必须已经包含新父表的所有字段且类型一致，此外新父表的每个约束的名字及其表达式都必须包含在此子表中。  
同样，一个继承链可以使用带NO INHERIT的ALTER TABLE命令从子表上删除。 允许动态添加和删除继承链对基于继承关系的表分区很有用。

创建一个将要作为子表的新表的便利途径是使用带LIKE子句的CREATE TABLE命令。它将创建一个与源表字段相同的新表。  
如果源表中存在约束，那么应该声明LIKE的INCLUDING CONSTRAINTS选项， 因为子表必须包含源表中的CHECK约束。

任何存在子表的父表都不能被删除，同样,子表中任何从父表继承的字段也不能被删除或修改。如果你想删除一个表及其所有后代， 最简单的办法是使用CASCADE选项。

ALTER TABLE会把所有数据定义和检查约束传播到后代里面去。另外，只有在使用CASCADE选项的情况下，才能删除父表的字段或者约束。
ALTER TABLE在重复字段融合和拒绝方面和CREATE TABLE的规则相同。

注意表的访问权限是如何处理的。查询父表可以自动访问子表的数据而不用进一步检查访问权限。 这个保留数据（也）在父表中的外貌。然而，直接访问子表不会自动被允许，而且需要要求被授予进一步的权限。

###注意事项###

注意，不是所有的SQL命令可以在所有的继承层次上正常工作。  
数据查询，数据修改，模式修改的命令（比如，SELECT，UPDATE，DELETE， ALTER TABLE的大多数变型, 但不是INSERT和ALTER TABLE ...RENAME） 典型的默认包括子表和支持ONLY符号来排除它们。  
为数据库维护和调优的命令（例如，REINDEX，VACUUM）通常只对个别工作， 物理表格不支持递归超过继承层次结构。每个命令的各自行为都被记录在参考部分(Reference I, SQL命令)。

继承的一个严重局限性是索引(包括唯一约束)和外键约束只能用于单个表，而不能包括它们的子表 (不管对引用表还是被引用表都是如此)，因此，在上面的例子里：  
即使我们声明cities.name为UNIQUE或PRIMARY KEY也不会阻止capitals表拥有重复名字的cities数据行。  
并且这些重复的行在查询cities表的时候会显示出来。实际上，缺省时capitals将完全没有唯一约束， 因此可能包含带有同名的多个行。  
你应该给capitals增加唯一约束，但即使这样做也不能避免与cities的重复。

类似的，即使我们声明cities.name参照REFERENCES某些其它的表，这个约束也不会自动传播到capitals表。在这种条件下， 你可以通过手工给capitals表增加同样的REFERENCES约束来做到这点。

声明一个其它表的字段为REFERENCES cities(name)将允许其它表包含城市名，但是不包含首府名。这种情况下没有很好的绕开办法。

这些缺点很可能在将来的版本中修补，但同时你也需要考虑一下，继承是否对你的问题真正有用。

已废弃: 在7.1以前的PostgreSQL版本里，缺省的行为是不在查询里包含子表。后来发现这么做很容易出错并且也违反了SQL标柱。 你可以通过关闭sql_inheritance配置选项来兼容以前的行为。
##分区##
PostgreSQL支持基本的表分区功能。本节描述为什么需要表分区以及如何在数据库设计中使用表分区。

###概述###

分区的意思是把逻辑上的一个大表分割成物理上的几块。分区可以提供若干好处：

某些类型的查询性能可以得到极大提升。特别是表中访问率较高的行位于一个单独分区或少数几个分区上的情况下。  
分区可以减少索引体积从而可以将高使用率部分的索引存放在内存中。如果索引不能全部放在内存中，那么在索引上的读和写都会产生更多的磁盘访问。

当查询或更新一个分区的大部分记录时，连续扫描那个分区而不是使用索引离散的访问整个表可以获得巨大的性能提升。

如果需要大量加载或者删除的记录位于单独的分区上，那么可以通过直接读取或删除那个分区以获得巨大的性能提升，因为ALTER TABLE比操作大量的数据要快的多。它同时还可以避免由于大量DELETE导致的VACUUM超载。

很少用的数据可以移动到便宜一些的慢速存储介质上。

这种好处通常只有在表可能会变得非常大的情况下才有价值。到底多大的表会从分区中收益取决于具体的应用， 不过有个基本的拇指规则就是表的大小超过了数据库服务器的物理内存大小。

目前，PostgreSQL支持通过表继承进行分区。每个分区必须做为单独一个父表的子表进行创建。父表自身通常是空的，它的存在只是为了代表整个数据集。你在试图实现分区之前，应该先熟悉继承(参阅Section 5.8)。

PostgreSQL可以实现下面形式的分区：

- 范围分区
表被一个或者多个关键字段分区成"范围"，这些范围在不同的分区里没有重叠。比如，我们可以为特定的商业对象根据数据范围分区，或者根据标识符范围分区。
- 列表分区
表通过明确地列出每个分区里应该出现那些关键字值实现。

###实现分区###

要设置一个分区的表，做下面的步骤：

1. 创建"主表"，所有分区都从它继承。
这个表中没有数据，不要在这个表上定义任何检查约束，除非你希望约束同样也适用于所有分区。同样，在其上定义任何索引或者唯一约束也没有意义。
2. 创建几个"子表"，每个都从主表上继承。通常，这些表不会增加任何字段。我们将把子表称作分区，尽管它们就是普通的PostgreSQL表。
3. 给分区表增加约束，定义每个分区允许的健值。

典型的例子是：

```
CHECK ( x = 1 )
CHECK ( county IN ( 'Oxfordshire', 'Buckinghamshire', 'Warwickshire' ))
CHECK ( outletID >= 100 AND outletID < 200 )
```

确保这些约束能够保证在不同的分区里不会有重叠的键值。一个常见的错误是设置下面这样的范围：

```
CHECK ( outletID BETWEEN 100 AND 200 )
CHECK ( outletID BETWEEN 200 AND 300 )
```

请注意在范围和列表分区的语法方面没有什么区别；这些术语只是用于描述的。

对于每个分区，在关键字字段上创建一个索引，以及其它你想创建的索引。关键字字段索引并非严格必需的，但是在大多数情况下它是很有帮助的。  
如果你希望关键字值是唯一的，那么你应该总是给每个分区创建一个唯一或者主键约束。

另外，定义一个规则或者触发器，把对主表的数据插入重定向到合适的分区表。

确保constraint_exclusion里的配置参数postgresql.conf是打开的。没有这个参数，查询不会按照需要进行优化。

比如，假设我们为一个巨大的冰激凌公司构造数据库。该公司每天都测量最高温度，以及每个地区的冰激凌销售。概念上，我们需要一个这样的表：

```
CREATE TABLE measurement (
    city_id         int not null,
    logdate         date not null,
    peaktemp        int,
    unitsales       int
);
```

我们知道大多数查询都只会访问最后一周，最后一个月或者最后一个季度的数据，因为这个表的主要用途是为管理准备在线报告。为了减少需要存储的旧数据，我们决定只保留最近三年的有用数据。在每个月的开头，我们都会删除最旧的一个月的数据。

在这种情况下，我们可以使用分区来帮助实现所有对表的不同需求。下面的步骤描述了上面的需求，分区可以这样设置：

主表是measurement表，就像上面那样声明。

然后我们为每个月创建一个分区：

```
CREATE TABLE measurement_y2006m02 ( ) INHERITS (measurement);
CREATE TABLE measurement_y2006m03 ( ) INHERITS (measurement);
...
CREATE TABLE measurement_y2007m11 ( ) INHERITS (measurement);
CREATE TABLE measurement_y2007m12 ( ) INHERITS (measurement);
CREATE TABLE measurement_y2008m01 ( ) INHERITS (measurement);
```

每个分区都是拥有自己内容的完整的表，只是它们从measurement表继承定义。

这样就解决了我们的一个问题：删除旧数据。每个月，我们需要做的只是在最旧的子表上执行一个DROP TABLE，然后为新月份创建一个新的子表。

我们必须证明非重叠的表约束。而不是像上面一样只是创建分区表，建表脚本就变成：

```
CREATE TABLE measurement_y2006m02 (
    CHECK ( logdate >= DATE '2006-02-01' AND logdate < DATE '2006-03-01' )
) INHERITS (measurement);
CREATE TABLE measurement_y2006m03 (
    CHECK ( logdate >= DATE '2006-03-01' AND logdate < DATE '2006-04-01' )
) INHERITS (measurement);
...
CREATE TABLE measurement_y2007m11 (
    CHECK ( logdate >= DATE '2007-11-01' AND logdate < DATE '2007-12-01' )
) INHERITS (measurement);
CREATE TABLE measurement_y2007m12 (
    CHECK ( logdate >= DATE '2007-12-01' AND logdate < DATE '2008-01-01' )
) INHERITS (measurement);
CREATE TABLE measurement_y2008m01 (
    CHECK ( logdate >= DATE '2008-01-01' AND logdate < DATE '2008-02-01' )
) INHERITS (measurement);
```

我们可能还需要在关键字字段上有索引：

```
CREATE INDEX measurement_y2006m02_logdate ON measurement_y2006m02 (logdate);
CREATE INDEX measurement_y2006m03_logdate ON measurement_y2006m03 (logdate);
...
CREATE INDEX measurement_y2007m11_logdate ON measurement_y2007m11 (logdate);
CREATE INDEX measurement_y2007m12_logdate ON measurement_y2007m12 (logdate);
CREATE INDEX measurement_y2008m01_logdate ON measurement_y2008m01 (logdate);
```

我们选择先不建立更多的索引。

我们想让我们的应用可以说INSERT INTO measurement ...数据被重定向到相应的分区表。 我们可以安排给主表附上一个合适的触发器。 如果数据只进入最新的分区，我们可以使用一个非常简单的触发器： 创建函数后，我们将创建一个触发器调用触发功能：

```
CREATE TRIGGER insert_measurement_trigger
    BEFORE INSERT ON measurement
    FOR EACH ROW EXECUTE PROCEDURE measurement_insert_trigger();
```

我们必须每月重新定义触发器，以便指向当前分区。然而，触发定义不需要更新。

我们可能想插入数据并且想让服务器自动定位应该向哪个分区插入数据。我们可以用下面这个复杂的触发器来实现这个目标，比如：

```
CREATE OR REPLACE FUNCTION measurement_insert_trigger()
RETURNS TRIGGER AS $$
BEGIN
    IF ( NEW.logdate >= DATE '2006-02-01' AND
         NEW.logdate < DATE '2006-03-01' ) THEN

        INSERT INTO measurement_y2006m02 VALUES (NEW.*);

    ELSIF ( NEW.logdate >= DATE '2006-03-01' AND
            NEW.logdate < DATE '2006-04-01' ) THEN

        INSERT INTO measurement_y2006m03 VALUES (NEW.*);
    ...

    ELSIF ( NEW.logdate >= DATE '2008-01-01' AND
            NEW.logdate < DATE '2008-02-01' ) THEN

        INSERT INTO measurement_y2008m01 VALUES (NEW.*);
    ELSE
        RAISE EXCEPTION 'Date out of range.  Fix the measurement_insert_trigger() function!';
    END IF;
    RETURN NULL;
END;
$$
LANGUAGE plpgsql;
```

每一个触发器跟以前一样。注意，每一个IF测试必须匹配其分区的CHECK约束。

当这个函数比单月的情况更复杂时，它不需要经常的更新，因为分支可以在需要之前被添加。

Note: 在实践中，如果大部分插入该分区，它可能是最好首先检查好最新分区的。 为简单起见，我们已经表明触发器在同一命令的测试，在这个例子中的其他部分。

我们可以看出，一个复杂的分区方案可能要求相当多的DDL语句。在上面的例子里我们需要每个月创建一次新分区，因此写一个脚本自动生成需要的DDL是明智的。

###管理分区###

通常分区集在定义表的时候就已经确定了，但我们常常需要周期性的删除旧分区并添加新分区。分区最重要的好处是它能恰到好处的适应这个需求：以极快的速度操作分区的结构，而不是痛苦的物理移动大量数据。

删除旧数据最简单的方法是删除不再需要的分区：

```
DROP TABLE measurement_y2006m02;
```

这个命令可以迅速删除数包含数百万条记录的分区，因为它不需要单独删除每一条记录。

还可以在删除分区的同时保留其作为一个表访问的能力：

```
ALTER TABLE measurement_y2006m02 NO INHERIT measurement;
```

这将允许将来对这些数据执行其它的操作(比如使用COPY,pg_dump之类的工具进行备份)。并且此时也是执行其它数据操(数据聚集或运行报表等)的有利时机。

同样，我们可以像前面创建最初的分区一样，创建一个新的空分区来处理新数据。

```
CREATE TABLE measurement_y2008m02 (
    CHECK ( logdate >= DATE '2008-02-01' AND logdate < DATE '2008-03-01' )
) INHERITS (measurement);
```

有时在分区结构之外创建新表并在一段时间之后将其变为分区更为方便。因为这将允许在该表变为分区之前对其中的数据进行加载、检查、转换之类的操作。

```
CREATE TABLE measurement_y2008m02
  (LIKE measurement INCLUDING DEFAULTS INCLUDING CONSTRAINTS);
ALTER TABLE measurement_y2008m02 ADD CONSTRAINT y2008m02
   CHECK ( logdate >= DATE '2008-02-01' AND logdate < DATE '2008-03-01' );
\copy measurement_y2008m02 from 'measurement_y2008m02'
-- 其它可能的数据准备工作
ALTER TABLE measurement_y2008m02 INHERIT measurement;
```

###分区和约束排除###

约束排除是一种查询优化技巧，它改进了用上述方法定义的表分区的性能。比如：

```
SET constraint_exclusion = on;
SELECT count(*) FROM measurement WHERE logdate >= DATE '2008-01-01';
```

如果没有约束排除，上面的查询会扫描measurement表中的每一个分区。打开了约束排除之后，规划器将检查每个分区的约束然后试图证明该分区不需要被扫描(因为它不能包含任何符合WHERE子句条件的数据行)。如果规划器可以证明这个，它就把该分区从查询规划里排除出去。

你可以使用EXPLAIN命令显示一个规划在constraint_exclusion打开和关闭情况下的不同。用上面方法设置的表的典型的未优化规划是：

```
SET constraint_exclusion = off;
EXPLAIN SELECT count(*) FROM measurement WHERE logdate >= DATE '2008-01-01';
```

<pre>
                                          QUERY PLAN
-----------------------------------------------------------------------------------------------
 Aggregate  (cost=158.66..158.68 rows=1 width=0)
   ->  Append  (cost=0.00..151.88 rows=2715 width=0)
         ->  Seq Scan on measurement  (cost=0.00..30.38 rows=543 width=0)
               Filter: (logdate >= '2008-01-01'::date)
         ->  Seq Scan on measurement_y2006m02 measurement  (cost=0.00..30.38 rows=543 width=0)
               Filter: (logdate >= '2008-01-01'::date)
         ->  Seq Scan on measurement_y2006m03 measurement  (cost=0.00..30.38 rows=543 width=0)
               Filter: (logdate >= '2008-01-01'::date)
...
         ->  Seq Scan on measurement_y2007m12 measurement  (cost=0.00..30.38 rows=543 width=0)
               Filter: (logdate >= '2008-01-01'::date)
         ->  Seq Scan on measurement_y2008m01 measurement  (cost=0.00..30.38 rows=543 width=0)
               Filter: (logdate >= '2008-01-01'::date)
</pre>

部分或者全部分区可能会使用索引扫描而不是全表扫描，不过这里要表达的意思是没有必要扫描旧分区就可以回答这个查询。在打开约束排除之后，我们可以得到生成同样回答的明显简化的规划：

```
SET constraint_exclusion = on;
EXPLAIN SELECT count(*) FROM measurement WHERE logdate >= DATE '2008-01-01';
```

<pre>
                                          QUERY PLAN
-----------------------------------------------------------------------------------------------
 Aggregate  (cost=63.47..63.48 rows=1 width=0)
   ->  Append  (cost=0.00..60.75 rows=1086 width=0)
         ->  Seq Scan on measurement  (cost=0.00..30.38 rows=543 width=0)
               Filter: (logdate >= '2008-01-01'::date)
         ->  Seq Scan on measurement_y2008m01 measurement  (cost=0.00..30.38 rows=543 width=0)
               Filter: (logdate >= '2008-01-01'::date)
</pre>

请注意，约束排除只由CHECK约束驱动，而不会由索引驱动。因此，在关键字字段上定义索引是没有必要的。在给出的分区上是否需要建立索引取决于那些扫描该分区的查询通常是扫描该分区的一大部分还是只是一小部分。对于后者，索引通常都有帮助，对于前者则没有什么好处。

constraint_exclusion缺省（和建议）设置事实上不是on也不是off， 但是中间设置调用partition，导致很可能要工作在分区表上的技术只适用于查询。  
on设置导致计划在所有的查询里检查CHECK限制，即使是不可能受益，最简单的限制。

###替代分区方法###

用一个不同的途径去重新定向插入适当的分区表，这个途径是在主表中建立规则，代替触发器， 例如：

```
CREATE RULE measurement_insert_y2006m02 AS
ON INSERT TO measurement WHERE
    ( logdate >= DATE '2006-02-01' AND logdate < DATE '2006-03-01' )
DO INSTEAD
    INSERT INTO measurement_y2006m02 VALUES (NEW.*);
...
CREATE RULE measurement_insert_y2008m01 AS
ON INSERT TO measurement WHERE
    ( logdate >= DATE '2008-01-01' AND logdate < DATE '2008-02-01' )
DO INSTEAD
    INSERT INTO measurement_y2008m01 VALUES (NEW.*);
```

规则比触发器有显著的开销，但是这个开销是每检查一次支付一次而不是每行支付一次， 所以这种方法可能在批量插入的情况下有优势。然而在更多的情况下，触发器的方法更好。

请注意COPY会忽略规则。如果你想用COPY插入数据，你将需要复制 分区表而不是主表。COPY触发触发器，如果你用触发器的方法就可以正常使用。

另一个规则方法缺点是如果规则设置没有覆盖插入数据，那么没有简单的路径强制错误，数据将会悄悄代替主表中的数据。

安排分区也可以用UNION ALL视图，代替表继承。例如，

```
CREATE VIEW measurement AS
          SELECT * FROM measurement_y2006m02
UNION ALL SELECT * FROM measurement_y2006m03
...
UNION ALL SELECT * FROM measurement_y2007m11
UNION ALL SELECT * FROM measurement_y2007m12
UNION ALL SELECT * FROM measurement_y2008m01;
```

然而，增加和删除各个分区的数据集，需要重新创建视图，增加额外的步骤。在实际中 这个方法建议它跟使用继承相比较。

###警告###

下面的注意事项适合于已分区的表：

当前没有自动的办法验证所有CHECK约束是互斥的。 比每条用手写产生分区和创建、修改关联对象更安全。

计划显示假设分区内一行的主字段不变，或者至少不变足够要求它移到另一个分区。 UPDATE尝试去做那些由于CHECK的约束将会失败。如果你需要处理这些事情， 你可以在分区表内适度更新触发器，但是它使管理结构更加复杂。

如果你正在使用VACUUM手册或者ANALYZE命令，不要忘记 你需要在每个分区上分别运行他们，就像这样的命令：

```
ANALYZE measurement;
```

将只会处理主表。

下面的注意事项适合于约束排除：

约束排除只是在WHERE子句包含约束的时候才生效。一个参数化的查询不会被优化，因为在运行时规划器不知道该参数会选择哪个分区。 由于某些原因，像CURRENT_DATE这样"稳定的"函数必须避免。

保持分区约束的简单性，策划者可能不能证明分区不需要被访问。为列表分区使用简单平等的约束， 或为范围分区使用简单的范围测试，就像前面的例子说明。一个好的thumb规则是分区约束可以包含 分区字段的唯一比较常量使用的B-树索引的操作。

主表所有分区的所有约束在约束排除中被审查，所以大量的分区将大大增加查询规划时间。 分区使用这些技术或许可以将分区提升到一百个且能很好的工作；不要尝试使用数千分区。
##依赖性跟踪##
如果你创建了一个包含许多表，并且带有外键约束、视图、触发器、函数等复杂的数据库结构。那么你就会在对象之间隐含地创建了一个依赖性的网络。比如，一个带有外键约束的表依赖于它所引用的表。

为了保证整个数据库结构的完整性，PostgreSQL保证你无法删除那些还被其它对象依赖的对象。比如，试图删除在Section 5.3.5里被订单表所依赖的产品表是不能成功的，会有类似下面的错误信息出现：

<pre>
DROP TABLE products;

NOTICE:  constraint orders_product_no_fkey on table orders depends on table products
ERROR:  cannot drop table products because other objects depend on it
HINT:  Use DROP ... CASCADE to drop the dependent objects too.
</pre>

这个错误信息包含一个有用的提示：如果你不想麻烦的分别删除所有依赖对象，你可以运行

```
DROP TABLE products CASCADE;
```

然后所有被依赖的对象都将被删除(并不删除订单表，只是删除外键约束)。如果你想检查DROP ... CASCADE会干什么，运行不带CASCADE的DROP然后阅读NOTICE信息。

PostgreSQL里的所有删除命令都支持声明CASCADE。当然，具体的依赖性实体取决于对象的类型。 你也可以写RESTRICT而不是CASCADE以获取缺省的行为(仅限于删除那些其它对象所依赖的对象)。

Note: 根据SQL标准，要求至少声明RESTRICT或CASCADE中的一个。实际上没有哪种数据库系统强制这一点，但是缺省的行为是RESTRICT还是CASCADE则因系统而异。

Note: 在PostgreSQL7.3之前的外键约束依赖性和序列字段依赖性在升级过程中都不会得到维护或者创建。所有其它的依赖性类型 在从7.3版本以前的数据库升级过程中都将得到恰当的创建。
