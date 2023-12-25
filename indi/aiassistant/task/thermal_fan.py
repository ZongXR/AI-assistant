# -*- coding: utf-8 -*-
from flask import current_app
from flask_ssm.utils.module_utils import try_to_import
from indi.aiassistant.utils.hardware_utils import read_temperature


gpio = try_to_import("ASUS.GPIO", "RPi.GPIO")
if gpio is not None:
    gpio.cleanup()
    gpio.setwarnings(True)
    gpio.setmode(gpio.BOARD)


FUNC = "change_status" if gpio else None          # 生效的函数名
TRIGGER = "interval"                              # 触发条件，interval表示定时间间隔触发
SECONDS = 60                                      # 触发时间间隔设定60秒
REPLACE_EXISTING = False                          # 重启替换持久化


def change_status():
    """
    每分钟执行一次，检查温度。\n
    低于低温阈值，关闭风扇\n
    高于高温阈值，全速开启风扇\n
    两个阈值之间，按温度比例调节转速\n
    :return: 空
    """
    gpio.setup(current_app.config.get("FAN_GPIO"), gpio.OUT)
    pwm = gpio.PWM(current_app.config.get("FAN_GPIO"), 50)
    temperature = read_temperature()
    current_app.logger.info("当前温度: %f" % temperature)
    if temperature < current_app.config.get("MIN_TEMP"):
        pwm.stop()
        gpio.output(current_app.config.get("FAN_GPIO"), gpio.LOW)
        current_app.logger.info("小于低温阈值，关闭风扇")
    elif temperature > current_app.config.get("MAX_TEMP"):
        pwm.start(100)
        gpio.output(current_app.config.get("FAN_GPIO"), gpio.HIGH)
        current_app.logger.info("大于低温阈值，打开风扇")
    else:
        speed = 100 * (temperature - current_app.config.get("MIN_TEMP")) / (current_app.config.get("MAX_TEMP") - current_app.config.get("MIN_TEMP"))
        pwm.start(int(speed))
        current_app.logger.info("低温阈值与高温阈值之间，调节转速: %.2f%%" % speed)
