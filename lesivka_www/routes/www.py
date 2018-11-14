from flask import Blueprint, redirect, render_template, session, url_for

from lesivka_www.utils import check_mode, get_mode, get_template

www = Blueprint('www', __name__, template_folder='templates')


@www.route('/')
def root():
    mode = get_mode()
    return redirect(url_for('www.template_view', mode=mode))


@www.route('/<mode>', defaults=dict(name='index'))
@www.route('/<mode>/<path:name>')
def template_view(mode, name):
    check_mode(mode)
    if session.new:
        session.permanent = True
    session['mode'] = mode
    template = get_template(name)
    return render_template(template)
