#!/usr/bin/python
# coding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
from urllib2 import urlopen, URLError
from json import loads
from sys import argv
cn_urls = "http://ip.taobao.com/service/getIpInfo.php?ip={}"
urls = 'http://ipinfo.io/{}/json'


def locateip(ip, cn=False):
    if cn:
        url = cn_urls.format(ip)
    else:
        url = urls.format(ip)
    handle = ""
    try:
        handle = urlopen(url)
    except URLError:
        print('网络连接出现问题')
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


def main():
    raw = None
    if argv.__len__() <= 1:
        raw = myip()
        target = raw['ip']
    else:
        target = sys.argv[1]
    if raw and raw['country'] == 'CN':
        cn = True
    else:
        cn = False
    data = locateip(target, cn)
    if cn:
        data = data['data']
    for i in data:
        if data[i]:
            print i + " >>>>> " + data[i]


if __name__ == '__main__':
    main()


