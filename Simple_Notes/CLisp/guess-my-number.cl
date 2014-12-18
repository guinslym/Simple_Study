; SLIME 2014-08-01
CL-USER> (defparameter *small* 1)        ;定义全局变量small,当然还可以使用defvar定义,指示该函数定义的变量不能被修改。
*SMALL*
CL-USER> (defparameter *big* 100)        ;定义全局变量big
*BIG*
CL-USER> (defun guess-my-number ()       ;定义函数guess-my-number
	   (ash (+ *small* *big*) -1))   ;将变量small和变量big相加后,位左移1位后返回
GUESS-MY-NUMBER
CL-USER> (defun small()                  ;定义函数small
	   (setf *big* (1- (guess-my-number))) ;设置变量big的数值为1减函数guess-my-number返回的值
	   (guess-my-number))            ;执行函数guess-my-number
SMALL
CL-USER> (defun bigger()
	   (setf *small* (1+ (guess-my-number)))
	   (guess-my-number))
BIGGER
CL-USER> (defun start-over ()            ;定义函数start-over,用于重置函数guess-my-number的数值,即50
	   (defparameter *small* 1)
	   (defparameter *big* 100)
	   (guess-my-number))
START-OVER
CL-USER> (guess-my-number)
50
CL-USER> (small)
25
CL-USER> (bigger)
37
CL-USER> (bigger)
43
CL-USER> (bigger)
46
CL-USER> (bigger)
48
CL-USER> (bigger)
49
CL-USER> (bigger)
49
CL-USER> (start-over)
50
CL-USER> (bigger)
75
CL-USER> (small)
62
CL-USER> (bigger)
68
CL-USER> (bigger)
71
CL-USER> (bigger)
73
CL-USER> (bigger)
74
CL-USER> (bigger)
74
CL-USER> (small)
74
CL-USER> (small)
74
CL-USER> (start-over)
50
CL-USER> 