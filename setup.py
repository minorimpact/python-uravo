#!/usr/bin/env python3

from setuptools import find_packages, setup

with open("./README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name='uravo',
    author='Patrick Gillan',
    author_email = 'pgillan@minorimpact.com',
    description='Python interface to the Uravo monitoring system',
    install_requires=['PyMySQL'],
    license='GPLv3',
    long_description = readme,
    packages=find_packages(include=['uravo']),
    setup_requires=[],
    tests_require=[],
    url = 'https://github.com/minorimpact/python-uravo',
    version='0.0.2',
)
