# -*- coding: utf-8 -*-
from flask import Response, stream_with_context
from flask_ssm.springframework.web.bind.annotation import RequestMapping, RequestMethod, ResponseBody
from flask_ssm.vo import CommonResult
from indi.aiassistant.service import video_service


@RequestMapping("/server_camera", method=RequestMethod.GET)
def server_camera():
    """
    捕获远程摄像头画面\n
    :return: 远程摄像头画面
    """
    return Response(stream_with_context(video_service.jpg_from_camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@RequestMapping("/enable_server_camera", method=RequestMethod.POST)
@ResponseBody
def enable_server_camera(enable: bool):
    """
    开启或关闭远程摄像头
    :param enable: 开启或关闭
    :return: 修改前的状态
    """
    result = video_service.enable_server_camera
    video_service.enable_server_camera = enable
    return CommonResult.ok(message="OK", data=result)


@RequestMapping("/is_server_camera_enabled", method=RequestMethod.POST)
@ResponseBody
def is_server_camera_enabled():
    """
    查看远程摄像头是否开启\n
    :return: 是否开启
    """
    result = video_service.enable_server_camera
    return CommonResult.ok(data=result)
