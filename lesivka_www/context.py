import re

from flask import Markup, request, url_for

from .utils import encode, get_mode


_clauses = {
    '': lambda a, b: a == b,
    'startswith': lambda a, b: a.startswith(b),
}

_clean_pat = re.compile('\u0301')


def active(classes='', **checks):
    for key, value in checks.items():
        arg, _, clause = key.partition('__')
        check = _clauses[clause]
        if not check(request.view_args.get(arg, ''), value):
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
    if get_mode() == 'lat':
        t = _clean_pat.sub('', t)
        t = encode(t)

    return Markup(t)
