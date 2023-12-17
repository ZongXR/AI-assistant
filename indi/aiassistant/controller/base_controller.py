# -*- coding: utf-8 -*-
from flask import render_template
from flask_ssm.springframework.web.bind.annotation import RequestMapping, RequestMethod, ResponseBody
from flask_ssm.vo import CommonResult
from indi.aiassistant.service import base_service


@RequestMapping("/", method=RequestMethod.GET)
def index():
    return render_template('index.html')


@RequestMapping("/shutdown", method=RequestMethod.POST)
@ResponseBody
def shutdown(minutes):
    """
    关机\n
    :param minutes: 设定关机时间
    :return: 几秒后关机，负数表示设定失败
    """
    result = base_service.shutdown(minutes)
    return CommonResult.ok(data=result)


@RequestMapping("/cancel_shutdown", method=RequestMethod.POST)
@ResponseBody
def cancel_shutdown():
    """
    取消关机\n
    :return: 是否成功
    """
    result = base_service.cancel_shutdown()
    return CommonResult.ok(data=result)
