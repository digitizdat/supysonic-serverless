#!/usr/bin/env python
# coding: utf-8
#

from flask import Flask
from supysonic.api import api
app = Flask(__name__)
app.register_blueprint(api)

