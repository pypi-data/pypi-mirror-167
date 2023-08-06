# encoding: utf-8
"""
@author: yizhao
@file: setup.py
@time: 2022/8/29 10:49
@desc:
"""
# encoding: utf-8
from setuptools import setup, find_packages, find_namespace_packages


# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='whale-nacos',
    version="0.4",
    author="Joey",
    author_email='yizhao@whale.im',
    description='whale nacos sdk',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=['whnacos'],
    include_package_data=True,
    install_requires=[
        "nacos-sdk-python",
        "grpcio"
    ],
    python_requires='>=3.5',
    dependency_links=[
        "https://pypi.doubanio.com/simple"
        ],
    package_dir={'whnacos': 'src'}

)
