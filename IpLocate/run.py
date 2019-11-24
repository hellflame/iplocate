# coding=utf8

import sys
import platform
from argparse import ArgumentParser

from IpLocate import IpLocate, __version__

if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding("utf8")


def parser():
    _parser = ArgumentParser(description="little tool to get location by the HOST or the IP")
    _parser.add_argument("ip", default=[], nargs="*", help="target ip or hostname")
    _parser.add_argument("-v", "--version", action="store_true", help="show version")
    return _parser.parse_args()


def disable_color():
    if platform.system().lower() == "windows":
        return True


def left_space(key, max_len):
    target_len = len(key)
    if max_len > target_len:
        return max_len - target_len
    else:
        return 0


def generate(target):
    iplocate = IpLocate()
    if not target:
        result = iplocate.my_locate()
    else:
        if ':' in target or target.split('.')[-1].isdigit():
            iplocate.ip = target
        else:
            iplocate.host = target
        result = iplocate.his_locate()

    ip = " " * 5 + result.pop("ip", "0.0.0.0")
    result.pop("readme", "")
    if not disable_color():
        ip = "\033[01;32m{}\033[00m".format(ip)
    title = "\n{}\n\n".format(ip)
    container = "\n".join(["{}{}{}".format(k.title(), " " * left_space(k, 20), v)
                           for k, v in sorted(result.items())])
    return title + container


def run():
    args = parser()
    if args.version:
        print("iplocate v{}".format(__version__))
        return

    if not args.ip:
        print(generate(None))
        return
    for target in args.ip:
        print(generate(target))
    return


def main():
    run()


if __name__ == '__main__':
    main()

