(defun factorial (n)
    "计算给定数字的阶乘"
    (! n))

(defun get-cube (x)
    "计算1个函数的3次方"
    (expr x 3))

(defun get-pow-list (n)
    "获取平方和列表"
    (loop
        for i from 0 to n
        for j from 0 to n
        collect (* i j)))