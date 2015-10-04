# coding=utf8
import sys
from urllib2 import urlopen, URLError
from json import loads
from sys import argv
reload(sys)
sys.setdefaultencoding("utf8")
urls = 'http://ipinfo.io/{}/json'


def locateip(ip):
    url = urls.format(ip)
    handle = ""
    try:
        handle = urlopen(url, timeout=5)
    except URLError:
        print('输入ip 出现问题')
        exit(1)
    reader = handle.read()
    handle.close()
    if not reader:
        print("获取数据失败，请检查连接状态")
        exit(1)
    return loads(reader)


def myip():
    __url = "http://ipinfo.io/json"
    handle = ""
    try:
        handle = urlopen(__url, timeout=5)
    except URLError:
        print('网络连接出现问题')
        exit(1)
    reader = handle.read()
    handle.close()
    if not reader:
        print("获取数据失败，请检查连接状态")
        exit(1)
    return loads(reader)


def help_():
    print ("""\ndeploy like below:\n\tiplocate ==> 获取本机外网ip地址\n\tiplocate 192.168.0.1 ==> 获取该ipv4地址信息\n\tiplocate fe80::a9e:1ff:fe8d:9197 ==> 获取该ipv6地址信息""")
    print ('')


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
    print('\n\033[01;32mIP Address \033[00m: \033[01;31m{}\033[00m\n'.format(data.get('ip', '无法获取目标')))
    data.pop('ip')
    for i in data:
        if data[i]:
            print ("{} >>>>> {}".format(i, data[i]))
    print('')


if __name__ == '__main__':
    main()


