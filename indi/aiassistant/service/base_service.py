# -*- coding: utf-8 -*-
import os
from flask import current_app


def shutdown(minutes: int = 0) -> int:
    """
    关机，需要su权限\n
    :param minutes: 等待的分钟
    :return: 几秒后关机，负数表示设定失败
    """
    command = "sudo shutdown -P %d" % minutes
    result = os.system(command)
    if result == 0:
        return minutes * 60
    else:
        current_app.logger.error("Error in command 'sudo shutdown -P %d'" % minutes)
        return -1


def cancel_shutdown() -> int:
    """
    取消关机，需要su权限\n
    :return: 是否执行成功
    """
    command = "sudo shutdown -c"
    result = os.system(command)
    if result == 0:
        return 0
    else:
        return -1
