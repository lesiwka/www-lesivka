import re

import jinja2
from flask import Markup, request, url_for

from utils import encode


def active(classes='', **checks):
    for key, value in checks.items():
        arg = request.view_args.get(key)
        if not (isinstance(value, tuple) and arg in value or arg == value):
            return classes
    return ' '.join([classes, 'active'])


@jinja2.pass_context
def page(context, name=None):
    mode = context.get("mode")
    return url_for("www.template_view", mode=mode, name=name)


@jinja2.pass_context
def switch(context):
    mode = context.get("mode")
    endpoint = request.endpoint
    args = request.view_args.copy()
    args["mode"] = "cyr" if mode == "lat" else "lat"
    return url_for(endpoint, **args)


@jinja2.pass_context
def text(context, t):
    if context.get("mode") == "lat":
        t = re.sub("\u0301", "", t)
        t = encode(t)

    return Markup(t)
