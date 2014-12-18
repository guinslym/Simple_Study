哈希表.md
哈希表是1个非常快的查找表类型,有点像alist。  
Emacs Lisp提供了1个通用目的的哈希表类型,并且提供了一系列的函数来操作它。  
哈希表有1个特殊的书写说明,由`#s`跟1个列表属性和内容组成。  
Obarry也是哈希表的1种,不过它们是不同的对象类型,并且只能用于保存interned符号。
##创建哈希表##
第1个创建哈希表的函数是`make-hash-table`.

 -- Function: make-hash-table &rest keyword-args
该函数根据特定的参数创建1个新的哈希表。这些函数必须由交替的关键字组成,其值与之相对应。

     Several keywords make sense in `make-hash-table', but the only two
     that you really need to know about are `:test' and `:weakness'.

`:test TEST'
    这个特殊的键值方法用于查找哈希表。默认是`eql'; `eq`和`equal`是其他交互的。

`eql'
               Keys which are numbers are "the same" if they are
               `equal', that is, if they are equal in value and either
               both are integers or both are floating point numbers;
               otherwise, two distinct objects are never "the same".

`eq'
               Any two distinct Lisp objects are "different" as keys.

 `equal'
 2个Lisp对象是键值相等的。


  你可以使用`define-hash-table-test`定义额外可能的用于测试。

`:weakness WEAK'

  The weakness of a hash table specifies whether the presence
  of a key or value in the hash table preserves it from garbage
  collection.

  WEAK的值必须是`nil', `key', `value',`key-or-value', `key-and-value',或`t'(`key-and-value'的别名)中的1其中1个。
  如果WEAK是键值,那么哈希表不会阻止它的键值被垃圾回收(如果它没有被指引)。如果1个特定的键值没有被收集,其关联性将被哈希表给移除。

  If WEAK is `key-and-value' or `t', both the key and the value
  must be live in order to preserve the association.  Thus, the
  hash table does not protect either keys or values from garbage
  collection; if either one is collected as garbage, that
  removes the association.

  If WEAK is `key-or-value', either the key or the value can
  preserve the association.  Thus, associations are removed
  from the hash table when both their key and value would be
  collected as garbage (if not for references from weak hash
  tables).

  The default for WEAK is `nil', so that all keys and values
  referenced in the hash table are preserved from garbage
  collection.

`:size SIZE'
  This specifies a hint for how many associations you plan to
  store in the hash table.  If you know the approximate number,
  you can make things a little more efficient by specifying it
  this way.  If you specify too small a size, the hash table
  will grow automatically when necessary, but doing that takes
  some extra time.

  默认值大小是65.

`:rehash-size REHASH-SIZE'
  When you add an association to a hash table and the table is
  "full", it grows automatically.  This value specifies how to
  make the hash table larger, at that time.

  If REHASH-SIZE is an integer, it should be positive, and the
  hash table grows by adding that much to the nominal size.  If
  REHASH-SIZE is a floating point number, it had better be
  greater than 1, and the hash table grows by multiplying the
  old size by that number.

 默认值是1.5.

`:rehash-threshold THRESHOLD'
  This specifies the criterion for when the hash table is
  "full" (so it should be made larger).  The value, THRESHOLD,
  should be a positive floating point number, no greater than
  1.  The hash table is "full" whenever the actual number of
  entries exceeds this fraction of the nominal size.  The
  default for THRESHOLD is 0.8.

-- Function: makehash &optional test
等价于`make-hash-table`,不过有1个不同风格的参数列表。参数TEST用于特殊的键名查找。这个函数被废弃了,使用`make-hash-table`替代.
你可以使用输出说明来创建1个新的哈希表。Lisp读取器读取输出说明,提供每个元素特殊的合法的读取哈希表语法。例如,紧接的新的哈希表包括1个 `key1`和`key2`键并分别与符号`val1`(1个符号)和`300`(a number)关联。

```
#s(hash-table size 30 data (key1 val1 key2 300))
```

The printed representation for a hash table consists of `#s' followed
by a list beginning with `hash-table'.  The rest of the list should
consist of zero or more property-value pairs specifying the hash
table's properties and initial contents.  The properties and values are
read literally.  Valid property names are `size', `test', `weakness',
`rehash-size', `rehash-threshold', and `data'.  The `data' property
should be a list of key-value pairs for the initial contents; the other
properties have the same meanings as the matching `make-hash-table'
keywords (`:size', `:test', etc.), described above.

Note that you cannot specify a hash table whose initial contents
include objects that have no read syntax, such as buffers and frames.
Such objects may be added to the hash table after it is created.
##访问哈希##
This section describes the functions for accessing and storing
associations in a hash table.  In general, any Lisp object can be used
as a hash key, unless the comparison method imposes limits.  Any Lisp
object can also be used as the value.

-- Function: gethash key table &optional default
This function looks up KEY in TABLE, and returns its associated
VALUE--or DEFAULT, if KEY has no association in TABLE.

-- Function: puthash key value table
This function enters an association for KEY in TABLE, with value
VALUE.  If KEY already has an association in TABLE, VALUE replaces
the old associated value.

-- Function: remhash key table
This function removes the association for KEY from TABLE, if there
is one.  If KEY has no association, `remhash' does nothing.

Common Lisp note: In Common Lisp, `remhash' returns non-`nil' if
it actually removed an association and `nil' otherwise.  In Emacs
Lisp, `remhash' always returns `nil'.

-- Function: clrhash table
This function removes all the associations from hash table TABLE,
so that it becomes empty.  This is also called "clearing" the hash
table.

Common Lisp note: In Common Lisp, `clrhash' returns the empty
TABLE.  In Emacs Lisp, it returns `nil'.

-- Function: maphash function table
This function calls FUNCTION once for each of the associations in
TABLE.  The function FUNCTION should accept two arguments--a KEY
listed in TABLE, and its associated VALUE.  `maphash' returns
`nil'.
##定义哈希##
你可以定义1个新的键名方法查找所谓的`define-hash-table-test`. 为了使用这个特性,你需要明白哈希表的运行和哈希码的意思。

You can think of a hash table conceptually as a large array of many
slots, each capable of holding one association.  To look up a key,
`gethash' first computes an integer, the hash code, from the key.  It
reduces this integer modulo the length of the array, to produce an
index in the array.  Then it looks in that slot, and if necessary in
other nearby slots, to see if it has found the key being sought.

Thus, to define a new method of key lookup, you need to specify both
a function to compute the hash code from a key, and a function to
compare two keys directly.

-- Function: define-hash-table-test name test-fn hash-fn
This function defines a new hash table test, named NAME.

After defining NAME in this way, you can use it as the TEST
argument in `make-hash-table'.  When you do that, the hash table
will use TEST-FN to compare key values, and HASH-FN to compute a
"hash code" from a key value.
函数TEST-FN必须接受2个参数,2个键名,并返回非nil在它们认为相同时。
函数HASH-FN需要接受1个参数,1个键名,并返回键名哈希值的整数。为了能得到更好的结果,函数最好使用整个整数范围的值用于哈希值,包括负整数。

The specified functions are stored in the property list of NAME
under the property `hash-table-test'; the property value's form is
`(TEST-FN HASH-FN)'.

-- Function: sxhash obj
This function returns a hash code for Lisp object OBJ.  This is an
integer which reflects the contents of OBJ and the other Lisp
objects it points to.
如果2个对象OBJ1和OBJ2相等,那么`(sxhash OBJ1)`和`(sxhash OBJ2)`是相同的整数.

If the two objects are not equal, the values returned by `sxhash'
are usually different, but not always; once in a rare while, by
luck, you will encounter two distinct-looking objects that give
the same result from `sxhash'.

This example creates a hash table whose keys are strings that are
compared case-insensitively.

(defun case-fold-string= (a b)
(eq t (compare-strings a nil nil b nil nil t)))
(defun case-fold-string-hash (a)
(sxhash (upcase a)))

(define-hash-table-test 'case-fold
'case-fold-string= 'case-fold-string-hash)

(make-hash-table :test 'case-fold)

Here is how you could define a hash table test equivalent to the
predefined test value `equal'.  The keys can be any Lisp object, and
equal-looking objects are considered the same key.

(define-hash-table-test 'contents-hash 'equal 'sxhash)

(make-hash-table :test 'contents-hash)
##其他哈希##
下面是其他一些用于哈希表的函数。

-- Function: hash-table-p table
如果对象是1个哈希表对象则返回非nil。

-- Function: copy-hash-table table
这个函数创建并返回1个复制的表。只有表自身被复制,键名和键值是共享的。

-- Function: hash-table-count table
这个函数返回表中实际数量的实体。

-- Function: hash-table-test table
This returns the TEST value that was given when TABLE was created,
to specify how to hash and compare keys.  See `make-hash-table'
(*note Creating Hash::).

-- Function: hash-table-weakness table
This function returns the WEAK value that was specified for hash
table TABLE.

-- Function: hash-table-rehash-size table
This returns the rehash size of TABLE.

-- Function: hash-table-rehash-threshold table
This returns the rehash threshold of TABLE.

-- Function: hash-table-size table
This returns the current nominal size of TABLE.


