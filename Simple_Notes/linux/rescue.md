Linux下的救援模式.md
作为一名Linux爱好者,常常需要安装1台主机上安装双系统.有时候先安装linux，然后安装windows系统引起Linux系统无法被引导，我们可以重装grub,使用opensuse中的Rescue System,ubuntu中的救援模式来解决这个问题.

```
grub
find /boot/grub/stage1
root (hdx,y)
setup (hd0)
quit
```

下面是关于重装grub的命令详解:

|  命令  |            含义            |
|--------|-----------------------------|
|grub    |grub以root身份运行|
|find /boot/grub/stage1|查找硬盘上的Linux系统将/boot目录存放在哪个硬盘分区中.grub在安装的时候需要读取这个目录中的相关配置文件|
|root (hdx,y)|指示Linux内核文件所在的硬盘分区,也就是/boot目录所在的分区,将这里的(hdx,y)替换为上1行中查找的那个分区.注意这个括号内不能存在空格|
|setup (hd0)|在第一块硬盘上引导程序grub|
|quit    |退出grub程序|

Grub并不分IDE、SCSI还是SATA硬盘,所有的硬盘被表示为"(hd#)"的形式,其中"#"从0开始编号。hd0表示第1块硬盘,hd1表示第2块硬盘(对于多个硬盘可以考虑用RAID合并在一起)。随后,(hd#,4)表示逻辑分区,例如(hd0,1)表示第1块硬盘的第2个主分区。