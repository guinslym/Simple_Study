(defun is-directory (pathname)
    "判断文件夹是否存在且为1个文件夹"
    (ext:probe-directory pathname))

(defun list-directory (&optional (pathname "~"))
    "列出当前文件夹下的内容"
    (directory (concatenate 'string pathname  "/*") :full :circle))

(defun getcwd ()
    "获取当前目录"
    (cd))

(defun get-directory-name (pathname)
    "获取给定名称的目录名"
    (dir pathname))

(defun file-exists (filename)
    "判断文件是否存在"
    (if (probe-file filename) T nil)))