# coding=utf8
import urllib2
import json
import socket


class IpLocate:
    def __init__(self, ip='', host=''):
        self.ip = ip
        self.host = host
        self.result = {}

    def retriever(self, urls):
        try:
            handle = urllib2.urlopen(urls, timeout=2)
            result = json.loads(handle.read())
        except urllib2.URLError:
            print("IP FORMAT WRONG")
        except ValueError:
            print("FAILED TO RETRIEVE DATA")
        except Exception as e:
            print(type(e))
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
    # print(test.result)

