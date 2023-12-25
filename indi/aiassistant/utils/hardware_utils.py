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
