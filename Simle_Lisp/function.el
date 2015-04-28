(defun range (n m &optional (step 1))
    "生成某个范围内的列表"
	   (loop
		for x
	       from n
	       to m by step
	        collect x)
	   )
;例如(range 0 100 5)生成20个元素的列表
;而(range 0 100)生成100个元素的列表

(defun xrange(max)
  "生成0到最大数的列表"
  (loop for x below max collect x))

(defun srange(max)
  "生成0到最大数的列表"
  (let ((result nil))
    (dotimes (i max)
      (push i result))
    (nreverse result)))

(defun is-int (n)
    "判断1个函数是不是1个整数"
    (integerp n)
    )

(defun plot (fn min max step)
    "生成对应函数的图像"
    (loop for i from min to max by step do
        (loop repeat (funcall fn i) do (format t "*"))
         (format t "~%")))
;例如(plot #'exp 0 4 1)

(defun cube (x)
    "计算数字的立方"
    (* x x x))

(defun pow (x)
    "计算数字的平方"
    (* x x))

(defun fibon (k)
    "计算给定位数的斐波那契数"
    (do ((n 0 (1+ n))
           (cur 0 next)
           (next 1 (+ cur next)))
          ((= k n) cur))
)

(defun fibonacci (n)
    "计算给定位数的斐波那契数"
    (loop for i below (1- n)
            and a = 0 then b
            and b = 1 then (+ b a)
            finally (return a))
)

(defun TimeStamp ()
    """获取当前时间戳"""
  (- (get-universal-time) 2208988800)
)
;使用Python的datetime中date模块,使用1970.1.1日的ordinal减去1900年得到天数差

(defun chr (n)
  "根据数字返回字符"
  (if (integerp n)
    (code-char n)))
;例如 (chr 255)

(defun ord (n)
  "根据给定字符返回数字,支持Unicode编码"
  (if (characterp n)
    (char-code n)))
;例如 (ord #\LATIN_CAPITAL_LETTER_A_WITH_MACRON)

(defun first-line (filename)
    "读取指定文件第1行文字"
     (let ((in (open filename :if-does-not-exist nil)))
       (when in
         (format t "~a~%" (read-line in))
         (close in))))

(defun read-file (filename)
  "读取指定文件的内容"
  (let ((in (open filename :if-does-not-exist nil)))
    (when in
      (loop for line = (read-line in nil)
         while line do (format t "~a~%" line))
      (close in))))

(defun write-to-file (filename content)
  "将内容写入到指定文件中"
  (with-open-file (stream filename :direction :output)
    (format stream content)))

(defun basename (path)
  "获取指定文件的路径名"
  (pathname-directory (
    pathname path)))

(defun filetype (path)
  "获取文件类型"
  (pathname-type (
    pathname path)))

(defun filename (path)
  "获取文件名"
  (pathname-name (
    pathname path)))

(defun file-exists (filename)
  "检查指定文件是否存在,probe-file会返回文件的名称"
  (if (probe-file filename)
    T nil))

(defun get-file-length (filename)
  "获取文件的长度"
  (with-open-file (in filename :element-type '(unsigned-byte 8))
  (file-length in)))

(defun byte-xor (a b)
  "按位异或,lggand支持多个参数"
  (logior a b))

(defun byte-and (a b)
  "按位与操作"
  (logand a b))

(defun byte-shift (a b)
  "进位"
  (ash a b)
)