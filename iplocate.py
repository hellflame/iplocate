#!/usr/bin/python
#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
from urllib2 import urlopen, URLError
from json import JSONDecoder

urls ="http://ip.taobao.com/service/getIpInfo.php?ip={}"
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
  regs = re.compile("""var returnCitySN = {"cip": "(.+?)",""",re.DOTALL)
  return regs.findall(reader)

if __name__ == "__main__":
  import sys
  if sys.argv.__len__() <= 1:
    target = myip()[0]
  else:
    target = sys.argv[1]
  data = locateip(target)
  if data["code"] == 0:
    datu = data["data"]
    for i in datu:
      print i + " >>>>> " + datu[i]
