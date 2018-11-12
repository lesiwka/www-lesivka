import lesivka
from flask import request, url_for

from .utils import get_mode


def active(classes='', **checks):
    for key, value in checks.items():
        if request.view_args.get(key) != value:
            return classes
    return ' '.join([classes, 'active'])


def page(name=None):
    mode = get_mode()
    return url_for('www.template_view', mode=mode, name=name)


def switch(mode):
    endpoint = request.endpoint
    args = request.view_args.copy()
    args['mode'] = mode
    return url_for(endpoint, **args)


def text(t):
    return lesivka.encode(t) if get_mode() == 'lat' else t
