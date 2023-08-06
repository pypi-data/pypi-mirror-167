#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Mail: mage@woodcol.com
# Created Time:  2018-1-23 19:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name = "Vlt-comm",
    version = "0.0.8",
    keywords = ("pip", "vlt", "drive control"),
    description = "FcBus library for Vlt drives",
    long_description = "FcBus library for Vlt drives",
    license = "MIT Licence",

    url = "",
    author = "tangfei",
    author_email = "fei.tang@danfoss.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)