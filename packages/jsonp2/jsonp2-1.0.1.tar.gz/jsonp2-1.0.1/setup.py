# -*- coding:utf-8 -*-
import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonp2",
    version="1.0.1",
    author="spider_jiang",
    author_email="author@example.com",
    description="jsonp to json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiang1243754883/jsonp2/tree/master",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[]
)
