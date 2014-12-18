读取和打印Lisp对象.md
打印和读取是转换Lisp对象到文本表和反之的操作。它们使用打印说明和阅读语法来描述Lisp数据类型。
本章主要描述用于读取和打印的Lisp函数。通常用流来描述,用于它获取的文本去向哪里和在哪里输入。  
##流的描述##
读取1个Lisp对象意味这解析1个文本Lisp表达式和生成1个一致的Lisp对象。这是Lisp程序如何进入包含Lisp代码的Lisp文件。我们称这个文本对象的读取语法。例如:文本`(a . 5)`是1个cons cell的CAR是`a`和CDR是数字5的读取语法。  
打印1个Lisp对象意味着当前对象生成的文本,转换对象为它的输出说明。打印上述cons cell生成的文本是`(a . 5)`.
读取和打印是或多或少的逆操作。另外,这2个操作不能彼此非常清楚的转换。这是3个另外的情况:

* 打印能生成那些不能被读取操作的文本。例如:buffers, windows, frames, subprocesses和markers能被打印称以`#`开头的文本。如果你尝试读取这些文本,将会得到1个错误。这就是那些不能被读取的数据类型。
* 1个对象能有多个文本说明。例如:`1`和`01`代表相同的整数,而`(a b)`和`(a . (b))`代表相同的列表.  读取能接受它们中的任何一个,但是打印只能选择它们中的1个。
* 注释能出现在对象中间的确定的位置读取序列而不影响读取的结果。

##输入流##
许多Lisp函数读取文本使用1个输入流作为参数。输入流指示哪里和如何取读取文本的字符。以下是可能的输入流:

BUFFER
     输入的字符点后直接开始字符从缓冲区进行读取。
MARKER
     输入的字符直接从缓冲区标记的字符进行读取。标记的位置就是字符读取位置。

STRING
     输入的字符来自字符串,开始于字符串的第1个字符。
FUNCTION
     输入的字符由函数生成,必须支持2种情况的调用:
        * 当调用时灭有参数,它可以返回下1个字符。
        * 当调用时只有1个参数(通常是1个字符),函数应该保存参数并安排在下1个调用时进行返回。这个调用称为"unreading"字符。它只发生在Lisp读取器读取太多的字符,并想将其放回到原先它的地方。在这种情况下,它与函数返回没有差别。
`t'
     `t' used as a stream means that the input is read from the
     minibuffer.  In fact, the minibuffer is invoked once and the text
     given by the user is made into a string that is then used as the
     input stream.  If Emacs is running in batch mode, standard input
     is used instead of the minibuffer.  For example,
          (message "%s" (read t))
     will read a Lisp expression from standard input and print the
     result to standard output.

`nil'
     `nil' supplied as an input stream means to use the value of
     `standard-input' instead; that value is the "default input
     stream", and must be a non-`nil' input stream.

SYMBOL
     1个输入流标记等于标记函数定义。下面是1个从缓冲区读取流的例子,显示了在前后点变化:

     ---------- Buffer: foo ----------
     This-!- is the contents of foo.
     ---------- Buffer: foo ----------

     (read (get-buffer "foo"))
          => is
     (read (get-buffer "foo"))
          => the

     ---------- Buffer: foo ----------
     This is the-!- contents of foo.
     ---------- Buffer: foo ----------
需要注意的是第1次读取会跳过空格。
Note that the first read skips a space.  Reading skips any amount of
whitespace preceding the significant text.

   Here is an example of reading from a stream that is a marker,
initially positioned at the beginning of the buffer shown.  The value
read is the symbol `This'.


     ---------- Buffer: foo ----------
     This is the contents of foo.
     ---------- Buffer: foo ----------

     (setq m (set-marker (make-marker) 1 (get-buffer "foo")))
          => #<marker at 1 in foo>
     (read m)
          => This
     m
          => #<marker at 5 in foo>   ;; Before the first space.

   Here we read from the contents of a string:

     (read "(When in) the course")
          => (When in)

   The following example reads from the minibuffer.  The prompt is:
`Lisp expression: '.  (That is always the prompt used when you read
from the stream `t'.)  The user's input is shown following the prompt.

     (read t)
          => 23
     ---------- Buffer: Minibuffer ----------
     Lisp expression: 23 <RET>
     ---------- Buffer: Minibuffer ----------

   Finally, here is an example of a stream that is a function, named
`useless-stream'.  Before we use the stream, we initialize the variable
`useless-list' to a list of characters.  Then each call to the function
`useless-stream' obtains the next character in the list or unreads a
character by adding it to the front of the list.

     (setq useless-list (append "XY()" nil))
          => (88 89 40 41)

     (defun useless-stream (&optional unread)
       (if unread
           (setq useless-list (cons unread useless-list))
         (prog1 (car useless-list)
                (setq useless-list (cdr useless-list)))))
          => useless-stream
现在我们读取流,例如结构:
Now we read using the stream thus constructed:

     (read 'useless-stream)
          => XY

     useless-list
          => (40 41)

Note that the open and close parentheses remain in the list.  The Lisp
reader encountered the open parenthesis, decided that it ended the
input, and unread it.  Another attempt to read from the stream at this
point would read `()' and return `nil'.

##输入函数##
##输出流##
##输出函数##
##输出变量##