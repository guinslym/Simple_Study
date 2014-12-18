加载.md
加载Lisp代码的1个文件意味着将它的内容放入在Lisp表对象的Lisp环境。Emacs发现并打开文件,读取文本,运算每个表然后关闭文件。如此1个文件页称为"Lisp库"。  
load函数运算文件中的所有的表达式,就像`eval-buffer`函数运行在缓冲区运行所有的表达式。不同之处在于load函数读取和运行硬盘上文件中文本,而不是Emacs缓冲区的文本。  
导入的文件必须包含Lisp表达式,既可以是源代码页可以是字节码。每个文件的表被称为顶级表(top-level).导入的文件中的表没有任何特殊的格式。文件中的任何表能直接导入到缓冲区和运行它们。更多的是,表都市函数定义或变量定义。
##程序是如何运行导入##
Emacs Lisp has several interfaces for loading.  For example, `autoload'
creates a placeholder object for a function defined in a file; trying
to call the autoloading function loads the file to get the function's
real definition (*note Autoload::).  `require' loads a file if it isn't
already loaded (*note Named Features::).  Ultimately, all these
facilities call the `load' function to do the work.

-- Function: load filename &optional missing-ok nomessage nosuffix must-suffix
这个函数用于寻找和开启Lisp代码文件,运行所有的表和关闭文件。

To find the file, `load' first looks for a file named
`FILENAME.elc', that is, for a file whose name is FILENAME with
the extension `.elc' appended.  If such a file exists, it is
loaded.  If there is no file by that name, then `load' looks for a
file named `FILENAME.el'.  If that file exists, it is loaded.
Finally, if neither of those names is found, `load' looks for a
file named FILENAME with nothing appended, and loads it if it
exists.  (The `load' function is not clever about looking at
FILENAME.  In the perverse case of a file named `foo.el.el',
evaluation of `(load "foo.el")' will indeed find it.)

If Auto Compression mode is enabled, as it is by default, then if
`load' can not find a file, it searches for a compressed version
of the file before trying other file names.  It decompresses and
loads it if it exists.  It looks for compressed versions by
appending each of the suffixes in `jka-compr-load-suffixes' to the
file name.  The value of this variable must be a list of strings.
Its standard value is `(".gz")'.

If the optional argument NOSUFFIX is non-`nil', then `load' does
not try the suffixes `.elc' and `.el'.  In this case, you must
specify the precise file name you want, except that, if Auto
Compression mode is enabled, `load' will still use
`jka-compr-load-suffixes' to find compressed versions.  By
specifying the precise file name and using `t' for NOSUFFIX, you
can prevent file names like `foo.el.el' from being tried.

If the optional argument MUST-SUFFIX is non-`nil', then `load'
insists that the file name used must end in either `.el' or `.elc'
(possibly extended with a compression suffix), unless it contains
an explicit directory name.

If FILENAME is a relative file name, such as `foo' or
`baz/foo.bar', `load' searches for the file using the variable
`load-path'.  It appends FILENAME to each of the directories
listed in `load-path', and loads the first file it finds whose name
matches.  The current default directory is tried only if it is
specified in `load-path', where `nil' stands for the default
directory.  `load' tries all three possible suffixes in the first
directory in `load-path', then all three suffixes in the second
directory, and so on.  *Note Library Search::.

Whatever the name under which the file is eventually found, and the
directory where Emacs found it, Emacs sets the value of the
variable `load-file-name' to that file's name.
如果你得到1个警告说`foo.elc`老于`foo.el`,这意味着你需要重新编译`foo.el`. 

When loading a source file (not compiled), `load' performs
character set translation just as Emacs would do when visiting the
file.  

When loading an uncompiled file, Emacs tries to expand any macros
that the file contains (*note Macros::).  We refer to this as
"eager macro expansion".  Doing this (rather than deferring the
expansion until the relevant code runs) can significantly speed up
the execution of uncompiled code.  Sometimes, this macro expansion
cannot be done, owing to a cyclic dependency.  In the simplest
example of this, the file you are loading refers to a macro defined
in another file, and that file in turn requires the file you are
loading.  This is generally harmless.  Emacs prints a warning
(`Eager macro-expansion skipped due to cycle...') giving details
of the problem, but it still loads the file, just leaving the
macro unexpanded for now.  You may wish to restructure your code
so that this does not happen.  Loading a compiled file does not
cause macroexpansion, because this should already have happened
during compilation.  *Note Compiling Macros::.

Messages like `Loading foo...' and `Loading foo...done' appear in
the echo area during loading unless NOMESSAGE is non-`nil'.

Any unhandled errors while loading a file terminate loading.  If
the load was done for the sake of `autoload', any function
definitions made during the loading are undone.

If `load' can't find the file to load, then normally it signals the
error `file-error' (with `Cannot open load file FILENAME').  But
if MISSING-OK is non-`nil', then `load' just returns `nil'.

You can use the variable `load-read-function' to specify a function
for `load' to use instead of `read' for reading expressions.  See
below.

`load' returns `t' if the file loads successfully.

-- Command: load-file filename
This command loads the file FILENAME.  If FILENAME is a relative
file name, then the current default directory is assumed.  This
command does not use `load-path', and does not append suffixes.
However, it does look for compressed versions (if Auto Compression
Mode is enabled).  Use this command if you wish to specify
precisely the file name to load.

-- Command: load-library library
This command loads the library named LIBRARY.  It is equivalent to
`load', except for the way it reads its argument interactively.
*Note Lisp Libraries: (emacs)Lisp Libraries.

-- Variable: load-in-progress
This variable is non-`nil' if Emacs is in the process of loading a
file, and it is `nil' otherwise.

-- Variable: load-file-name
When Emacs is in the process of loading a file, this variable's
value is the name of that file, as Emacs found it during the search
described earlier in this section.

-- Variable: load-read-function
这个变量用于交互的进行读取表达式函数
This variable specifies an alternate expression-reading function
for `load`和`eval-region`用于`read`.  The
function should accept one argument, just as `read' does.
正常情况下,这个变量的值是`nil`,这意味这那些函数应该使用读取。

Instead of using this variable, it is cleaner to use another, newer
feature: to pass the function as the READ-FUNCTION argument to
`eval-region'.  *Note Eval: Definition of eval-region.
