# coding=utf8
import sys
from urllib2 import urlopen, URLError
from json import loads
from sys import argv
from os import popen
from instantDB.controller import Controller
reload(sys)
sys.setdefaultencoding("utf8")
urls = 'http://ipinfo.io/{}/json'
db_path = "{}/.iplocate".format(popen("echo $HOME").read().strip())
# Mac OS 中 popen("echo -n $HOME").read() 返回值错误 为 "-n /home/home_name"
# 顾此处统一使用现有方法获取家目录 popen("echo $HOME").read().strip()
# test env db path
# db_path = "../tempDB"


def locateip(ip):
    url = urls.format(ip)
    reader = ""
    controller = Controller(data_dir=db_path)
    try:
        result = controller.search(ip)
        if result:
            return result
        handle = urlopen(url, timeout=5)
        content = handle.read()
        reader = loads(content)
        controller.insert(ip, content)
        handle.close()
    except URLError:
        print('输入ip 出现问题')
        exit(1)
    except ValueError:
        print("获取数据失败，请检查连接状态")
        exit(1)
    return reader


def myip():
    __url = "http://ipinfo.io/json"
    reader = ''
    try:
        controller = Controller(db_path)
        handle = urlopen(__url, timeout=5)
        content = handle.read()
        reader = loads(content)
        result = controller.search(reader['ip'])
        if not result:
            controller.insert(reader['ip'], content)
        handle.close()
    except URLError:
        print('网络连接出现问题')
        exit(1)
    except ValueError:
        print("获取数据失败，请检查连接状态")
        exit(1)
    return reader


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


