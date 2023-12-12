# -*- coding: utf-8 -*-
from flask import render_template
from flask_ssm.springframework.web.bind.annotation import RequestMapping, RequestMethod


@RequestMapping("/", method=RequestMethod.GET)
def index():
    return render_template('index.html')
