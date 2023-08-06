# encoding: utf-8
"""
@author: yizhao
@file: __init__.py.py
@time: 2022/8/29 10:03
@desc:
"""
import os
import json
import nacos

SERVER_ENDPOINT = "nacos.meetwhale.com"
DEFAULT_GROUP = "DEFAULT"

nacos_config = os.getenv("NACOS_CONFIG")
if nacos_config is None:
    raise Exception("Please set the env variable of NACOS_CONFIG")
nacos_config = json.loads(nacos_config)
namespace = nacos_config.get('client_conf').get('NamespaceId')

nacos_client = nacos.NacosClient(SERVER_ENDPOINT, namespace=namespace)
frame_client = nacos.NacosClient(SERVER_ENDPOINT, namespace=f'frameworks-{namespace}')
