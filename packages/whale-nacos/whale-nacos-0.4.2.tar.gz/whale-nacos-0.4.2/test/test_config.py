# encoding: utf-8
"""
@author: yizhao
@file: test_config.py
@time: 2022/8/29 10:02
@desc:
"""
import unittest
from src import config


class TestNacos(unittest.TestCase):
    def test_get_config(self):
        configs = config.get_config("aml-video-task")
        pg_configs = config.get_pg_config("aml-video-task")
        print(configs)
        print(pg_configs)