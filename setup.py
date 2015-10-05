# coding=utf8
from setuptools import setup, find_packages
__author__ = 'hellflame'


setup(
    name='iplocate',
    version='1.0.4',
    keywords=('ip', 'ipv4', 'ipv6', 'location', 'ip2location', 'ip to location'),
    description="在终端获取本机或者指定ip地址",
    license="MIT",
    author='hellflame',
    author_email="hellflamedly@gmail.com",
    url="https://github.com/hellflame/iplocate",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    platforms="any",
    entry_points={
        'console_scripts': [
            'iplocate=iplocate.iplocate:main'
        ]
    }
)


