Mysql在Linux下的配置文件在/etc/Mysql目录下:

- debian.cnf,这个文件是系统自动生成的,不要手动修改。
- debian-start,每次/etc/init.d/mysql运行时都调用这个文件。
- my.cnf,这是Mysql的主配置文件。
- conf.d/,该目录下所有以.cnf结尾的文件都会被my.cnf读入。
- conf.d/old_passwords.cnf,该文件决定是否对旧格式的密码提供支持。

Apache2在Linux下的配置文件在/etc/apache2目录下:

- apache2.conf,全局配置文件,不要轻易修改它。
- conf.d/,该目录存放一些一般性的配置。
- envvars,存放环境变量,一般不需要修改。
- httpd.conf,用户配置文件。
- mods-available/,该目录下是已经安装的可用模块。
- mods-enabled/,该目录下是已经启动的模块。
- ports.conf,httpd服务的端口。
- sites-available/,该目录下是可用的虚拟主机。
- sites-enabled/,该目录下是已经启用的虚拟主机。

apache2.conf是Apache2的主配置文件,它会读取上面列出的所有目录和文件(sites-available目录除外,因为Apache不需要知道有哪些虚拟主机可用,它只需要加载那些已经启用的虚拟主机即可)。