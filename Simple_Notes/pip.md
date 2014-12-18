pip手册.md
##常见操作##
本文是对官方文件的翻译,版本是1.5.6
首先是安装pip,然后安装PyPI中的1个包:

```
$ pip install 包的名字
[...]
Successfully installed SomePackage（成功安装某个包）
```

显示已经安装的文件:

```
$ pip show --files SomePackage
Name: SomePackage
Version: 1.0
Location: /my/env/lib/pythonx.x/site-packages
Files:
../somepackage/__init__.py
[...]
```

列出哪些包已经过时:

```
$ pip list --outdated
SomePackage (Current: 1.0 Latest: 2.0)
```

升级1个包:

```
$ pip install --upgrade SomePackage
[...]
Found existing installation: SomePackage 1.0
Uninstalling SomePackage:
Successfully uninstalled SomePackage
Running setup.py install for SomePackage
Successfully installed SomePackage
```

卸载某个包:

```
$ pip uninstall SomePackage
Uninstalling SomePackage:
/my/env/lib/pythonx.x/site-packages/somepackage
Proceed (y/n)? y
Successfully uninstalled SomePackage
```

##安装pip##
安装或更新pip,下载文件[get-pip.py](https://bootstrap.pypa.io/get-pip.py)。  
然后运行如下命令，可能或需要管理员权限:

```
python get-pip.py
```

如果[setuptools](https://pypi.python.org/pypi/setuptools)或[distribute](https://pypi.python.org/pypi/distribute)没有被安装，那么该文件将安装setuptools。  
升级1个存在的setuptools或distribute,运行:

```
pip install -U setuptools
```

为了能够在命令行上使用pip,需要确保你的python脚本是在系统环境变量(PATH)中。
##更新pip##
在Linux或OS X上:

```
pip install -U pip
```

在Windows上:

```
python -m pip install -U pip
```

##使用包管理工具##
在Linux系统上,pip能够使用系统包管理工具进行安装。在Debian和Ubuntu系统上:

```
sudo apt-get install python-pip
```

在Fedora系统上:

```
sudo yum install python-pip
```

<h2>安装包</h2>
pip支持安装PyPI中的包，版本控制，本地项目和直接安装对应版本。  

```
$ pip install SomePackage               # latest version（最新版本）
$ pip install SomePackage==1.0.4        # specific version（特殊版本）
$ pip install ’SomePackage>=1.0.4’      # minimum version（最小的版本）
```

<h2>请求文件</h2>
请求文件是包含1系列将在pip中被安装的文件目录。  

```
pip install -r requirements.txt
```

关于文件的格式细节见如下:

```
<requirement specifier>
<archive url/path>
[-e] <local project path>
[-e] <vcs project url>
```

在实际操作中,有几种常见的使用请求文件的方法:

1. 希望请求文件中包进行冻结。
```
pip freeze > requirements.txt
pip install -r requirements.txt
```

2. 请求文件用于覆盖本地已经存在的版本控制文件。
```
git+https://myvcs.com/some_dependency@sometag#egg=SomeDependency
```
3. 请求文件用于项目中各种pip版本之间的独立性。
```
pkg1
pkg2
pkg3>=1.0,<=2.0
```
4. 请求文件为了关联性版本的独立性，例如请求文件中的项目A依赖于项目B，但是最新版本有bug,你可以安装早起版本:
```
ProjectA
ProjectB<1.3
```

##从Wheel进行安装##
Wheel是1个已经压缩的格式,因此可以高速下载后解压安装。  
pip默认会尝试从Wheel进行安装,禁止它可以使用参数--no-use-wheel。  
直接从wheel版本进行安装:

```
pip install SomePackage-1.0-py2.py3-none-any.whl
```

搭建wheels用于你的请求文件和它们存储在1个本地目录:

```
pip install wheel
pip wheel --wheel-dir=/local/wheels -r requirements.txt
```

然后直接使用wheel来安装请求文件：

```
pip install --no-index --find-links=/local/wheels -r requirements.txt
```

<h2>删除包</h2>

```
pip uninstall SomePackage
```

<h2>列出包</h2>
列出已经安装的包:

```
pip list
```

列出过时的包和最新版本可用的版本:

```
$ pip list --outdated
```

显示要安装包的详细信息:

```
$ pip show sphinx
```

<h2>搜索包</h2>
pip能搜索PyPI上的包通过使用pip search命令:

```
$ pip search "query"
```

<h2>配置</h2>
<h3>配置文件</h3>
pip允许你设置所有的命令行参数在1个配置文件中。  
其名字和地址取决于平台的不同：

- 在Unix和Mac OS X上是:$HOME/.pip/pip.conf
- 在Windows系统配置文件是:%HOME%\pip\pip.ini

你可以设置1个自定义路径通过使用环境变量`PIP_CONFIG_FILE`。
<h3>环境变量</h3>
pip命令选项可以设置成环境变量通过格式`PIP_<UPPER_LONG_NAME>`。破折号(-,dashes)必须用下划线(_,underscores)取代。例如,设置默认超时（timeout):

```
export PIP_DEFAULT_TIMEOUT=60
```

这与直接传递给pip参数是一样的:

```
pip --default-timeout=60 [...]
```

如果是1次设置多个选项在1个命令行中,只需在2个值中添加1个空格:

```
export PIP_FIND_LINKS="http://mirror1.example.com http://mirror2.example.com"
pip install --find-links=http://mirror1.example.com --find-links=http://mirror2.example.com
```

<h3>配置优先顺序</h3>
命令行参数优先于环境变量，也优先于配置文件。在配置文件中，特殊部分命令优先于global部分。例如:  

+ --host=foo覆盖PIP_HOST=foo
+ PIP_HOST=foo覆盖带有[global]host=foo的配置文件
+ 配置文件中1个特殊部分命令[<command>]host=bar覆盖带有同名属性的[global]部分

<h3>完成命令</h3>
pip支持bash和zsh中的命令完成。

```
$ pip completion --bash >> ~/.profile
$ pip completion --zsh >> ~/.zprofile
```

<h2>快速和本地安装</h2>
你可以安装本地的压缩包，首先你需要下载所有你需要的压缩包文件:

```
$ pip install --download <DIR> -r requirements.txt
```

然后，使用-find-links和-no-index进行安装:

```
$ pip install --no-index --find-links=[file://]<DIR> -r requirements.txt
```

##无递归的升级##
pip install --upgrade现在使用递归的进行升级，例如:

- SomePackage-1.0 requires AnotherPackage>=1.0，需要另1个包版版本大于等于1.0
- SomePackage-2.0 requires AnotherPackage>=1.0 and OneMorePoject==1.0
- SomePackage-1.0 and AnotherPackage-1.0 are currently installed
- SomePackage-2.0 and AnotherPackage-2.0 are the latest versions available on PyPI.

运行pip install --upgrade SomePackage将升级SomePackage和AnotherPackage依赖于AnotherPackage已经满足条件。如果你想使用无递归的升级，只需做到以下两步:

```
pip install --upgrade --no-deps SomePackage
pip install SomePackage
```

##用户安装##
Python 2.6安装时实行用户模式(user scheme)，这意味着所有的Python版本支持1个用户多个安装地址。默认的安装地址在每个系统中使用Python官方手册中的`site.USER_BASE`变量。这种模式可以表示为pip install中的-user选项。  
更多的，用户模式能通过环境变量PYTHONUSERBASE进行自定义设置，它将对site.USER_BASE进行更新。  
例如,通过换将变量安装SomePackage到/myappenv中:

```
export PYTHONUSERBASE=/myappenv
pip install --user SomePaackge
```

pip install --user遵循以下4个规则:

1. 如果在python路径全局安装指定的包文件，而它们与安装请求有冲突，它们将被忽视并不安装。
2. 如果在python路径全局安装指定的包文件，它们满足安装的要求，pip将表示满足需求。（与virtualenv中安装1个--system-site-packages一样）
3. pip不会执行1个--user在1个--no-site-packages的virtualenv中，原因是python路径中不包含用户site。
4. 在1个--system-site-packages的virtualenv中，pip不会安装1个与virtualenv中site-packages中冲突的包。