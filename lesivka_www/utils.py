from flask import abort, request, session


def check_mode(mode):
    if mode not in ('cyr', 'lat'):
        abort(404)


def get_mode():
    return session.get('mode', 'cyr')


def get_template(name):
    return '%s.html' % name


def get_text():
    keys = list(request.values.keys())
    return request.values.get('t', keys[0] if keys else '')
