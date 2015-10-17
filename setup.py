# coding=utf8
from setuptools import setup, find_packages
__author__ = 'hellflame'


setup(
    name='iplocate',
    version='1.1.0',
    keywords=('ip', 'ipv4', 'ipv6', 'location', 'ip2location', 'ip to location'),
    description="在终端获取本机或者指定ip地址",
    license="MIT",
    author='hellflame',
    author_email="hellflamedly@gmail.com",
    url="https://github.com/hellflame/iplocate",
    packages=[
        'iplocate'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=[
        "instantDB>=0.0.9"
    ],
    platforms="any",
    entry_points={
        'console_scripts': [
            'iplocate=iplocate.iplocate:main'
        ]
    }
)


