; SLIME 2014-08-01
CL-USER> (if nil 
	     'I-am-true
	     'I-am-false)
I-AM-FALSE
CL-USER> (if '()
	     'I-am-true
	     'I-am-false)
I-AM-FALSE
CL-USER> (if '(0)
	     'I-am-true
	     'I-am-false)
I-AM-TRUE
CL-USER> (if '(nil)
	     'I-am-true
	     'I-am-false)
I-AM-TRUE
CL-USER> (defun my-length (list)
	   (if list
	       (1+ (my-length (cdr list)))
	       0))
MY-LENGTH
CL-USER> (my-length '(list with five symbols OK))
5 
CL-USER> (if 'nil
	     'I-am-true
	     'I-am-false)
I-AM-FALSE
CL-USER> (if ()
	     'I-am-true
	     'I-am-false)
I-AM-FALSE
CL-USER> (if (oddp 5)
	     'odd-number
	     (/ 1 0))
ODD-NUMBER
CL-USER> (defvar *number-was-odd* nil)
*NUMBER-WAS-ODD*
CL-USER> (if (oddp 5)
	     (progn (setf *number-was-odd* t)
		    'odd-number)
	     'even-number)
ODD-NUMBER
CL-USER> *number-was-odd*
T
CL-USER> (defvar *arch-enemy* nil)
*ARCH-ENEMY*
CL-USER> (defun pudding-eater (person)
	   (cond ((eq person 'henry)(setf *arch-enemy* 'stupid-lisp-alien)
		                    '(curse you lisp alien - you ate my pudding))
		 ((eq person 'johnny)(setf *arch-enemy* 'useless-old-johnny)
		                    '(i hope you choked on my pudding johnny))
		 (t '(why you eat my pudding stranger ?))))
PUDDING-EATER
CL-USER> (pudding-eater 'johny)
(WHY YOU EAT MY PUDDING STRANGER ?)
CL-USER> *arch-enemy*
NIL
CL-USER> (pudding-eater 'henry)
(CURSE YOU LISP ALIEN - YOU ATE MY PUDDING)
CL-USER> (pudding-eater 'george-clooney)
(WHY YOU EAT MY PUDDING STRANGER ?)
CL-USER> (defvar *arch-enemy* nil)
*ARCH-ENEMY*
CL-USER> (defun pudding-eater (person)
	   (case person
	     ((henry) (setf *arch-enemy* 'stupid-lisp-alien)
	              '(curse you lisp alien - you ate my pudding))
	     ((johnny)(setf *arch-enemy* 'useless-old-johnny)
	              '(i hope you choked on my pudding johnny))
	     (otherwise '(why you eat my pudding stranger ?))))
PUDDING-EATER

