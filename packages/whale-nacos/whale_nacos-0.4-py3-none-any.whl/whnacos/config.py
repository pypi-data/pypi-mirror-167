# encoding: utf-8
"""
@author: yizhao
@file: whnacos.py
@time: 2022/8/29 09:53
@desc:
"""
import json
import nacos
from . import nacos_client as client
from . import frame_client
from . import DEFAULT_GROUP


def get_config(service_name: str, group=DEFAULT_GROUP):
    """
    get nacos config by register service name
    :param service_name: service name
    :param group: group name
    :return:
    """
    conf = client.get_config(service_name, group)
    if conf is None:
        raise Exception('failed to get pg configs')

    return json.loads(conf)


def get_pg_config(service_name="", group=DEFAULT_GROUP):
    """
    get postgres configs via frameworks
    :param service_name:
    :param group:
    :return:
    """
    framework_config = get_framework_pg_config()
    if service_name == "":
        return framework_config

    pg_conf = client.get_config(f"{service_name}.pg-config", group)

    if pg_conf is None:
        raise Exception('failed to get pg configs')
    pg_conf = json.loads(pg_conf)
    return {**framework_config, **pg_conf}


def get_framework_pg_config():

    framework_conf = frame_client.get_config(f"pg-config", DEFAULT_GROUP)
    if framework_conf is None:
        raise Exception("failed to get frameworks configs")
    return json.loads(framework_conf)


