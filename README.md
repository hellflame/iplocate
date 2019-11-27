# iplocate

查询目标IP或本机IP所记载的物理位置信息

[API](http://ipinfo.io)

> Golang 版本: [https://github.com/hellflame/ipinfo](https://github.com/hellflame/ipinfo)

整个项目基本都是依赖API，ip信息貌似会有更新，变动可能还比较大，所以就没有本地存储了

个人主要用来查看攻击者大概的来源

### Install

```bash
	$ sudo pip install iplocate --upgrade
```

### Usage

#### Command

> 终端调用方式

```bash
 $ iplocate
 $ iplocate 127.0.0.1
 $ iplocate -h # 显示帮助信息
```

1. 默认直接输入`iplocate`将会查询本机ip对应的物理地址
2. `iplocate`后跟ipv4或ipv6地址，将会尝试获取该地址对应记录的物理地址
3. `iplocate`后跟域名，本机将会尝试连接目标服务器，确定ip地址，然后尝试获取该ip对应的物理地址

原本目标域名有可能是绑定的ipv6地址，不过现在暂时没有尝试连接ipv6，这并不是API的问题，只是作者暂时用不到而已，，，，

#### Import

> my location

```python
	from IpLocate import IpLocate
	iplocate = IpLocate()
	my_loc = iplocate.my_locate()
	
```

> target ip location

```python
	iplocate = IpLocate(ip='127.0.0.1')
	his_location = iplocate.his_locate()
```

> target host location

```python
	iplocate = IpLocate(host="www.google.com")
	his_location = iplocate.his_locate()
```

### [API REF](http://ipinfo.io/)


### History

+ 0.9.7 => 添加简单帮助菜单,创建历史版本记录, 更新使用平台描述
+ 0.9.8 => 取消国内区域ip使用淘宝地址库(内容粗略无用)
+ 0.9.9 => 输出微调
+ 1.0.0 => 添加获取时间限制
+ 1.0.1 => 添加License文件
+ 1.0.2 => 添加获取json时的异常处理
+ 1.0.3 => 更正异常处理方式
+ 1.0.4 => 网络连接验证机制导致返回数据被强制重定向问题判断
+ 1.1.0 => 添加本地数据库
+ 1.1.2 => 修复mac os中本地数据库初始化失败
+ 2.0.0 => 使用paramseeker开始重写
+ 2.1.0 => socket替换ping
+ 2.2.0 => py3 support
+ 2.2.3 => py2 encoding setting
+ 2.3.0 => replace paramseeker with argparse
