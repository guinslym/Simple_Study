##Linux各版本操作的比较##

###Red Hat和Debian体系服务操作对比###

|  任务  |  Red Hat  |      Debian     |      Ubuntu(安装sysv-rc-conf和sysvconfig)    |
|--------|-----------|-----------------|----------------|
|启动服务|service httpd start|/etc/init.d/apache2 start|service apache2 start|
|停止服务|service httpd stop |/etc/init.d/apache2 stop|service apache2 stop|
|让服务随系统启动自动运行|chkconfig httpd on|update-rc.d apache2 defaults|sysv-rc.conf apache2 on|
|禁止服务随系统启动自动运行|chkconfig httpd off|update-rc.d apache2 purge|sysv-rc.conf apache2 off|


###Red Hat和Ubuntu软件包操作对比###

|    内容   |Red Hat         |       Ubuntu    |
|-----------|----------------|-----------------|
|软件包后缀|*.rpm           |*.deb            |
|软件源配置文件|/etc/yum.conf|/etc/apt/sources.list|
|更新软件包列表|每次运行yum时自动运行|apt-get update|
|从软件仓库安装软件|yum install package|apt-get install package|
|安装1个已下载的软件包|yum install pkg.rpm,rpm -i pkg.rpm|dpkg -i pkg.deb,dpkg --install pkg.deb|
|删除软件包|rpm -e package|apt-get remove package|
|软件包升级检查/测试|yum check-update|apt-get -s upgrade,apt-get -s dist-upgrade|
|升级软件包|yum update,rpm -Uvh [args]|apt-get upgrade|
|升级整个系统|yum upgrade|apt-get dist-upgrade|
|获取某个软件包的信息|yum search package|apt-cache show package|
|获取所有软件包的信息|yum list available|apt-cache dumpavail|
|显示所有已安装的软件|yum kust installed,rpm -qa|dpkg -l,dpkg --list|
|获取某个已安装软件包的信息|yum info package,rpm -qi package|dpkg --status package|
|列出某个已安装软件包所包含的文件列表|rpm -ql package|dpkg --listfile package|
|列出某个已安装软件包所包含的文档|rpm -qd package|无|
|列出某个已安装软件包所包含的配置文件|rpm -qc package|无|
|显示某个软件包所依赖的软件包列表|rpm -qR package|apt-cache depends package|
|显示某个软件包的反向依赖关系|rpm -q -whatrequires [args]|apt-cache rdepends package|
|获取某个软件包文件的信息|rpm -qpi pkg.rpm|dpkg --info pkg.deb|
|列出某个软件包文件所包含的文件列表|rpm -qpi pkg.rpm|dpkg --contents pkg.deb|
|列出某个软件包文件所包含的文档|rpm -qpd pkg.rpm|无|
|列出某个软件包文件所包含的配置文件|rpm -qpc pkg.rpm|无|
|软件包解压|rpm2cpio pkg.rpm |cpio -vid|dpkg -deb --extract pkg.deb|
|搜索某个文件是由哪个文件软件包安装的|rpm -qf filename|dpkg -S filename,dpkg --search filename|
|搜索所有提供某个文件的软件包|rpm provides filename|apt-file search filename|
|显示本地软件包缓存的状态|无|apt-cache stats|
|检验所有已安装的软件包|rmp -Va|debsums|
|删除本地缓存的所有软件包|yum clean package|apt-get clean|
|仅删除本地缓存中过时的软件包|无|apt-get autoclean|
|删除所有软件包信息(以便下次重新下载)|yum clean headers|apt-file purge|
