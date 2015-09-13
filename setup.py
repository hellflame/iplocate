# coding=utf8
__author__ = 'hellflame'

from setuptools import setup, find_packages

setup(
    name='iplocate',
    version='0.9.2',
    keywords=('ip', 'ipv4', 'location', 'ip2location', 'ip to location'),
    description="在终端获取本机或者指定ip地址",
    license="MIT",
    author='hellflame',
    author_email="hellflamedly@gmail.com",
    url="https://github.com/hellflame/iplocate",
    packages=find_packages(),
    platforms="unix like",
    entry_points={
        'console_scripts': [
            'iplocate=iplocate.iplocate:main'
        ]
    }
)


