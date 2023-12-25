# -*- coding: utf-8 -*-
import logging
from typing import Optional
from flask_ssm.utils.module_utils import try_to_import


def read_temperature(zone: int = 0) -> Optional[float]:
    """
    读取温度\n
    :param zone: 区域，默认CPU温度
    :return: 摄氏度
    """
    try:
        with open("/sys/class/thermal/thermal_zone%d/temp" % zone) as f:
            return int(f.read()) / 1000
    except FileNotFoundError as e:
        logging.exception(e)
        return None


def import_gpio(*packages):
    """
    导出gpio模块\n
    :param: 包名，按优先级降低从前往后写
    :return: gpio模块
    """
    for package in packages:
        result = try_to_import(package)
        if result is not None:
            return result
    return None
