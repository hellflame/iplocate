# coding=utf8
from setuptools import setup, find_packages
__author__ = 'hellflame'


setup(
    name='iplocate',
    version='2.0.0',
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
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Environment :: Console",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=[
        "paramSeeker"
    ],
    platforms="any",
    entry_points={
        'console_scripts': [
            'iplocate=iplocate.run:main'
        ]
    }
)


