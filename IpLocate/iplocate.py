# coding=utf8
import sys
import json
import socket

if sys.version_info.major == 2:
    from urllib2 import urlopen, URLError
else:
    from urllib.request import urlopen, URLError


class IpLocate:
    def __init__(self, ip='', host=''):
        self.ip = ip
        self.host = host
        self.result = {}

    def retriever(self, urls):
        try:
            handle = urlopen(urls, timeout=2)
            result = json.loads(handle.read().decode('utf8'))
        except URLError:
            print("IP FORMAT WRONG")
            exit(1)
        except ValueError:
            print("FAILED TO RETRIEVE DATA")
            exit(2)
        except Exception as e:
            print(type(e))
            exit(3)
        else:
            self.result = result

    def my_locate(self):
        urls = "http://ipinfo.io/json"
        self.retriever(urls)
        return self.result

    def host_ip(self):
        try:
            socket.setdefaulttimeout(3)
            result = socket.gethostbyname(self.host)
            self.ip = result
            return result
        except socket.gaierror:
            print('HOST NAME ERROR')
            exit(1)
        except socket.timeout:
            print('NETWORK FAILED')
            exit(1)

    def his_locate(self):
        if self.ip:
            urls = 'http://ipinfo.io/{}/json'.format(self.ip)
            self.retriever(urls)
        elif self.host:
            self.host_ip()
            self.his_locate()
        else:
            pass
        return self.result


if __name__ == '__main__':
    test = IpLocate(host='www.baidu.cm')
    print(test.host_ip())
    print(test.my_locate())
    # print(test.result)

