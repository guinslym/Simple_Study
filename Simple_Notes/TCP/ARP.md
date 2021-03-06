地址解析协议(ARP).md
在IP协议能够把1个分组从源地址交付到目的主机之前,它首先要知道的是如何将这个分组交付给下一跳。
1个IP分组可以通过咨询路由表找出下一跳的IP地址。但是,既然IP使用的是数据链路层的服务,它就需要知道下一跳的物理地址。
##地址映射##
在网络这一级,主机和路由器是通过它们的逻辑地址来识别的。逻辑地址就是互联网地址。在TCP/IP协议族中,逻辑地址也称为IP地址,它的长度是32位。
但是,分组必须通过物理地址才能到达主机和路由器。在物理这1级,主机和路由器是用它们的物理地址来识别的。
物理地址是1个本地地址,它的管辖范围是本地网络的。物理地址和逻辑地址是2种不同的标识符,这2个地址我们都需要,因为1个物理网络(如以太网)可以同时为使用2种不同的协议的网络层提供服务。
这就意味着把1个分组交付到主机或路由器需要用到两级地址:逻辑地址和物理地址。我们要把逻辑地址映射为相应的物理地址。这样的映射可以通过静态映射或动态映射来完成。
###静态映射###
静态映射(static mapping)就是说要创建1张表,把逻辑地址与物理地址关联起来。这张表存储在网络中的每1台机器上。
###动态映射###
动态映射(dynamic mapping)时,每次只要机器知道另1台机器的逻辑地址,就可以使用协议找出相应的物理地址。已经设计出的实现了动态映射的协议有2个:地址解析协议(ARP)和逆地址解析协议(RARP)。
##ARP协议##
ARP接受来自IP协议的逻辑地址,将其映射为相应的物理地址,然后再把这个物理地址递交给数据链路层。
任何时候,当主机或路由器需要找出这个网络上的另1个主机或路由器的物理地址时,它就可以发送1个ARP查询分组。这个分组包括了发送方的物理地址和IP地址以及接收方的IP地址。因为发送方不知道接收方的物理地址,所以这个查询会在网络上进行广播。
网络上的每1台主机或路由器都会接受并处理这个ARP查询分组,但是只有期待的接收方才能认出是自己的IP地址,并返回1个ARP响应分组。这个响应分组包含有接收方的IP地址和物理地址,这个分组利用收到的查询分组中的物理地址以单播方式直接发送给查询者。
###封装###
ARP分组直接封装在数据链路帧中。
###操作###
ARP处理过程需要以下7个步骤:

1. 发送方知道目标的IP地址。
2. IP请求ARP创建1个ARP请求报文,填入发送方的物理地址、发送方的IP地址以及目标IP地址。对于目的物理地址字段则全部填入0。
3. 这个报文被提交给数据链路层。在这一层它被封装称帧,并以发送方的物理地址作为源地址,以物理广播地址作为目的地址。
4. 每1个主机或路由器都会收到这个帧,因为这个帧包含的是广播目的的地址。所有站点都会取走这个这个报文并把它交给ARP。除了目的机器之外,其他所有机器都会丢弃这个分组。目的机器认识这个IP地址。
5. 目标机器用ARP回答报文进行回答。回答报文中包含了它的物理地址，这个报文使用的是单播方式。
6. 发送方收到这个回答报文，现在发送方就知道目标机器的物理地址了。
7. 携带有给目标机器的IP数据报现在可以封装称帧,并用单播方式发送到终点。