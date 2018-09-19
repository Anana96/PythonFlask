#!/bin/env python3
# -*- coding: utf-8 -*-

from flask import request
import html as utils
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Response
from app import app
from flask_cors import CORS

CORS(app)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


def send_msg_from_site(name, email, message):
    pass


limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@app.route('/send', methods=['POST'])
def send_email():
    def strip_size(l, x):
        if len(x) > l:
            return x[:l]
        else:
            return x

    def escape_strip(l, x):
        text = str(request.form[x])
        if len(text) == 0:
            return ""
        return (utils.escape(strip_size(l, text))).strip()

    respons = ("""<html>
    <body>
        <p>Спасибо за Ваше письмо.</p>
        <strong>Наши специалисты ответят Вам в кратчайшие сроки.</strong>
        <p>С  искренним уважением,</p>
        <p>ООО &laquo;FooBar&raquo;</p>
    </body></html>""")

    name = escape_strip(1000, 'send-name')
    email = escape_strip(1000, 'send-email')
    message = escape_strip(10000, 'send-message')

    if len(name) == 0 or len(email) == 0 or len(message) == 0:
        return "Ошибка. Поля формы не заполнены."

    send_msg_from_site(name, email, message)
    return Response(respons, mimetype="text/html")


