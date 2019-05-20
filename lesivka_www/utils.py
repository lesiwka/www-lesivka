from flask import Markup, request

import lesivka


def encode(text):
    text = lesivka.encode(text).encode('ascii', 'xmlcharrefreplace').decode()
    return Markup(text)


def get_template(name):
    return '%s.html' % name


def get_text():
    keys = list(request.values.keys())
    return request.values.get('t', keys[0] if keys else '')
