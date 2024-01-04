# -*- coding: utf-8 -*-
import socket
from flask import Flask
from werkzeug.serving import get_interface_ip
import pyttsx3
from indi.aiassistant import sp


app = Flask(sp.base_package.__package__)
sp.init_app(app)
app.tts_engine = pyttsx3.init(debug=app.config.get("DEBUG", False))
for config_key, config_value in app.config.items():
    if config_key.startswith("TTS_"):
        app.tts_engine.setProperty(config_key.lstrip("TTS_").lower(), config_value)
if "TTS_VOICE" not in app.config.keys():
    voices = app.tts_engine.getProperty('voices')
    if len(voices) > 0:
        app.tts_engine.setProperty('voice', voices[0].id)


if __name__ == '__main__':
    app.tts_engine.say("本机IP是" + get_interface_ip(socket.AF_INET).replace(".", "点"))
    app.tts_engine.runAndWait()
    app.run()
