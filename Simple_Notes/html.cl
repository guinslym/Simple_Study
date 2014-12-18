; SLIME 2014-08-01
CL-USER> (append '(mary had) '(a) '(little lamb))
(MARY HAD A LITTLE LAMB)
CL-USER> (apply #'append '((mary had)(a)(little lamb)))
(MARY HAD A LITTLE LAMB)
CL-USER> (find 'y '((5 x)(6 x)(7 z)) :key #'cadr)
; No value
CL-USER> (find 'y '((5 x)(6 x)(7 z)) :key #'cadr)
NIL
CL-USER> (find 'y '((5 x)(6 y)(7 z)) :key #'cadr)
(6 Y)
CL-USER> (push '(hello) '(Welcome,Jack))

; No value
CL-USER> (push '(hello) (list 'welcome))
; in: PUSH '(HELLO)
;     (FUNCALL #'(SETF LIST) #:NEW977 'WELCOME)
; ==>
;   (SB-C::%FUNCALL #'(SETF LIST) #:NEW977 'WELCOME)
; 
; caught WARNING:
;   The function (SETF LIST) is undefined, and its name is reserved by ANSI CL so
;   that even if it were defined later, the code doing so would not be portable.
; 
; compilation unit finished
;   Undefined function:
;     (SETF LIST)
;   caught 1 WARNING condition

; No value
CL-USER> (push 7 (list 1 2 3))

; in: PUSH 7
;     (FUNCALL #'(SETF LIST) #:NEW979 1 2 3)
; ==>
;   (SB-C::%FUNCALL #'(SETF LIST) #:NEW979 1 2 3)
; 
; caught WARNING:
;   The function (SETF LIST) is undefined, and its name is reserved by ANSI CL so
;   that even if it were defined later, the code doing so would not be portable.
; 
; compilation unit finished
;   Undefined function:
;     (SETF LIST)
;   caught 1 WARNING condition

; No value
CL-USER> (defparameter *foo* '(1 2 3))
*FOO*
CL-USER> (push 7 *foo*)
(7 1 2 3)
CL-USER> (push '(hello) *foo*)
((HELLO) 7 1 2 3)
CL-USER> *foo*
((HELLO) 7 1 2 3)
CL-USER> (mapcdr #'(lambda (x)(* x 2))'(2 4 6))

; in: MAPCDR #'(LAMBDA (X) (* X 2))
;     (MAPCDR #'(LAMBDA (X) (* X 2)) '(2 4 6))
; 
; caught STYLE-WARNING:
;   undefined function: MAPCDR
; 
; compilation unit finished
;   Undefined function:
;     MAPCDR
;   caught 1 STYLE-WARNING condition

; No value
CL-USER> (mapcar #'(lambda (x)(* x 5))
			   '(2 4 6))
(10 20 30)
CL-USER> (mapcar #'list
		 '(a b c)
		 '(1 2 3 4))
((A 1) (B 2) (C 3))
CL-USER> (maplist #'(lambda (x) x)
		  '(a b c))
((A B C) (B C) (C))
CL-USER> (nth 2 '(a b c d e f))
C
CL-USER> (nthcdr 2 '(a b c))
(C)
CL-USER> (last '(a b c d))
(D)
CL-USER> (eq (second '(a b c))
	     (nth 1 '(a b c)))
T
CL-USER> (caddr '(a b c d e f))
C
CL-USER> (car '(a b c d e f))
A
CL-USER> (car (cdr '(a b c d e f)))
B
CL-USER> (car (cdr (cdr '(a b c d e f))))
C
CL-USER> (cdr (cdr '(a b c d e f)))
(C D E F)
CL-USER> (cadr '(a b c d e f))
B
CL-USER> (caddddr '(a b c d e f g))

; in: CADDDDR '(A B C D E F G)
;     (CADDDDR '(A B C D E F G))
; 
; caught STYLE-WARNING:
;   undefined function: CADDDDR
; 
; compilation unit finished
;   Undefined function:
;     CADDDDR
;   caught 1 STYLE-WARNING condition
Help! 11 nested errors. SB-KERNEL:*MAXIMUM-ERROR-DEPTH* exceeded.
Backtrace for: #<SB-THREAD:THREAD "repl-thread" RUNNING {10035B0063}>
; Evaluation aborted on #<UNDEFINED-FUNCTION CADDDDR {1005695563}>.
; Evaluation aborted on #<UNDEFINED-FUNCTION CADDDDR {1005695563}>.
; Evaluation aborted on #<UNDEFINED-FUNCTION CADDDDR {1005695563}>.
; Evaluation aborted on #<UNDEFINED-FUNCTION CADDDDR {1005695563}>.
; Evaluation aborted on #<UNDEFINED-FUNCTION CADDDDR {1005695563}>.
; Evaluation aborted on #<UNDEFINED-FUNCTION CADDDDR {1005695563}>.
; Evaluation aborted on #<UNDEFINED-FUNCTION CADDDDR {1005695563}>.
CL-USER> 
CL-USER> 
CL-USER> 
CL-USER> 
CL-USER> 
CL-USER> 
CL-USER> (cadddr '(a b c d e f))
D
CL-USER> (member 'b '(a b c d e f))
(B C D E F)
CL-USER> (member 'b '(a c f))
NIL
CL-USER> (member 'b '(a b c d) :test #'eq)
(B C D)
CL-USER> (member '(b) '((a)(b)(c)(d)))
NIL
CL-USER> (member '(b) '((a)(b)(c)(d)) :test #'eq)
NIL
CL-USER> (member '(b) '((a)(b)(c)(d)) :test #'equal)
((B) (C) (D))
CL-USER> (member '(b) '((a)(b)) :test #'eql)
NIL
CL-USER> (member 'a '((a b)(c d)))
NIL
CL-USER> (member 'a '((a b)(c d)) :key #'car)
((A B) (C D))
CL-USER> (/ 1 0)
:abort
:ABORT
CL-USER> (defmacro as (tag content)
	   `(format t "<~(~A~)>~A</~(~A~)>"
		    ',tag,content',tag))
AS
CL-USER> (defmacro with (tag &rest body)
	   `(progn
	      (format t "~&<~(~A~)>~%"',tag)
	      ,@body
	      (format t "~&</~(~A~)>~%" ',tag)))
WITH
CL-USER> (defmacro brs (&optional (n 1))
	   (fresh-line)
	   (dotimes (i n)
	     (princ "<br>"))
	   (terpri))
BRS
CL-USER> 