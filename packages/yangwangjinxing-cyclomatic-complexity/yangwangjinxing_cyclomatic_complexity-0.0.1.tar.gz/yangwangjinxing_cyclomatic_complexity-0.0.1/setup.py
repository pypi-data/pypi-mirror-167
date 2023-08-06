#!/usr/bin/env python
# encoding: utf-8


import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="cyclomatic-complexity",
    version="0.0.1",
    author="yangwangjinxing",
    author_email="yangwangjinxing@163.com",
    description="cyclomatic complexity.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yangwangjinxing/cyclomatic_complexity",
    packages=setuptools.find_packages(),
    install_requires=['lizard'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
