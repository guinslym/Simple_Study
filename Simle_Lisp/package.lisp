(defun get-package-name (symbol-name)
    "获取指定符号来自哪个包,例如(get-package-name 'gcd)"
    (package-name (symbol-package symbol-name)))

(defun get-inherit-from ()
    "获取特定实现中从哪些包继承了符号"
    (mapcar #'package-name (package-use-list :cl-user)))

(defpackage :email
    (:use :common-lisp))