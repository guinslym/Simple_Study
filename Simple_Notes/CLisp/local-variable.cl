; SLIME 2014-08-01
CL-USER> (let ((a 5)  ;使用let绑定本地变量
	       (b 6))
	   (+ a b))
11
;定义1个本地变量,使用命令let,1个let是类似下面的结构:
(let (variable declarations)
     ...body...)

;定义1个本地函数使用flet命令,flet命令是类似如下结构:
(flet ((function-name (arguments)
      ...function body...))
...body...)

CL-USER> (flet ((f (n)
		  (+ n 10)))
	   (f 5))
15
CL-USER> (flet ((f (n)
		  (+ n 10))
		(g (n)
		  (- n 3)))
	   (g (f 5)))  ;将函数f传入5后的结果再作为参数传给g函数
12
;如果想让函数名能在函数中使用,我们能使用labels命令。
;它的结构与flet一致。
;该方法主要用于后面的函数调用前面的函数。
CL-USER> (labels ((a (n)
		    (+ n 5))
		  (b (n)
		    (+ (a n) 6)))
	   (b 10))
21