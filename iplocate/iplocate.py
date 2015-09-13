#!/usr/bin/python
#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
from urllib2 import urlopen, URLError
from json import JSONDecoder
# urls ="http://ip.taobao.com/service/getIpInfo.php?ip={}"
urls = 'http://ipinfo.io/{}/json'


def locateip(ip):
    url = urls.format(ip)
    handle = ""
    try:
        handle = urlopen(url)
    except URLError:
        print('网络连接出现问题')
        exit(1)
    reader = handle.read()
    handle.close()
    return JSONDecoder().decode(reader)


def myip():
    import re
    url = "http://pv.sohu.com/cityjson?id=utf-8"
    handle = ""
    try:
        handle = urlopen(url)
    except URLError:
        print('网络连接出现问题')
        exit(1)
    reader = handle.read()
    handle.close()
    regs = re.compile("""var returnCitySN = {"cip": "(.+?)",""", re.DOTALL)
    return regs.findall(reader)


def main():
    import sys
    if sys.argv.__len__() <= 1:
        target = myip()[0]
    else:
        target = sys.argv[1]
    data = locateip(target)
    for i in data:
        if data[i]:
            print i + " >>>>> " + data[i]


if __name__ == '__main__':
    main()


