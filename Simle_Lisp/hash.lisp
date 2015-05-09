(defun create-hash (hashname)
    "生成指定名称的哈希表"
    (defparameter hashname
        (make-hash-table))
)

(defun set-hash (hashname key value)
    "设置指定哈希表的值,例如(set-hash hash 'foo 'world)"
    (setf (gethash key hashname)  value))

(defun get-hash-value (hashname key)
    "获取哈希表指定键的值,(get-hash-value hash 'foo)"
    (gethash key hashname))

(defun clear-hash (hashname)
    "清空指定哈希表的所有值"
    (clrhash hashname))

(defun get-hash-info (hashname)
    "获取哈希表所有的键值"
   (maphash #'(lambda (k v)
              (format t "~a => ~a~%" k v))
          hashname))

(defun remove-hash-key (hash key)
    "删除哈希表中指定的键值"
    (remhash key hash))