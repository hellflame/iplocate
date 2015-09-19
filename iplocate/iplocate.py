#!/usr/bin/python
# coding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
from urllib2 import urlopen, URLError
from json import loads
from sys import argv
# cn_urls = "http://ip.taobao.com/service/getIpInfo.php?ip={}"
urls = 'http://ipinfo.io/{}/json'


def locateip(ip):
    url = urls.format(ip)
    handle = ""
    try:
        handle = urlopen(url)
    except URLError:
        print('网络连接 或 输入ip 出现问题')
        exit(1)
    reader = handle.read()
    handle.close()
    return loads(reader)


def myip():
    __url = "http://ipinfo.io/json"
    handle = ""
    try:
        handle = urlopen(__url)
    except URLError:
        print('网络连接出现问题')
        exit(1)
    reader = handle.read()
    handle.close()
    return loads(reader)


def help_():
    print """\ndeploy like below:\n\tiplocate ==> 获取本机外网ip地址\n\tiplocate 192.168.0.1 ==> 获取该ipv4地址信息\n\tiplocate fe80::a9e:1ff:fe8d:9197 ==> 获取该ipv6地址信息"""
    print


def main():
    if '-h' in argv or '--help' in argv:
        help_()
        exit(0)
    if argv.__len__() <= 1:
        raw = myip()
        target = raw['ip']
    else:
        target = sys.argv[1]
    data = locateip(target)
    for i in data:
        if data[i]:
            print "{} >>>>> {}".format(i, data[i])


if __name__ == '__main__':
    main()


