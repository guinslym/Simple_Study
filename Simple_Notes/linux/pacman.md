##同步与升级##
安装和升级软件包前，先让本地的包数据库和远程的软件仓库同步是个好习惯.

```
pacman -Syy
```

也可以使用一句命令同时进行同步软件库并更新系统到最新状态.

```
pacman -Syu
```

##安装软件包##
安装或者升级单个软件包，或者一列软件包（包含依赖包），使用如下命令：

```
pacman -S package_name1 package_name2
```

有时候在不同的软件仓库中，一个软件包有多个版本（比如extra和testing）。你可以选择一个来安装：

```
pacman -S extra/package_name 
pacman -S testing/package_name
```

你也可以在一个命令里同步包数据库并且安装一个软件包：

```
pacman -Sy package_name
```

##卸载软件包##
删除单个软件包，保留其全部已经安装的依赖关系 

```
pacman -R package_name
```

删除指定软件包，及其所有没有被其他已安装软件包使用的依赖关系： 

```
pacman -Rs package_name
```

##包数据库查询##
可以使用 -Q 标志搜索和查询本地包数据库。详情参见

```
pacman -Q --help
```

可以使用-S 标志搜索和查询远程同步的包数据库。详情参见

```
pacman -S --help
```

##其它##
下载包而不安装它： 

```
pacman -Sw package_name
```

安装一个本地包（不从源里）： 

```
pacman -U /path/to/package/package_name-version.pkg.tar.gz
```

完全清理包缓存(/var/cache/pacman/pkg)：

```
pacman -Scc
```

##配置##
###编辑###

Pacman的配置文件位于`/etc/pacman.conf`。关于配置文件的进一步信息可以用man pacman.conf查看。
###常用选项###
常用选项都在[options]段。阅读man手册或者查看缺省的pacman.conf可以获得有关信息和用途。
##软件仓库##
你可以在`/etc/pacman.conf`和`/etc/pacman.d/`里定义使用哪些仓库。它们可以直接在里面定义或者从其它文件里包含进来。下面例子中使用官方软件仓库，用`mirrorlist`设定镜像的一个范例。
所有官方软件仓库都使用同一个包含了'$repo' 的 /etc/pacman.d/mirrorlist文件，因此只需要维护一个列表。其中mirrorlist的修改与维护可参见Archlinux的官方wiki.