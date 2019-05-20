from flask import Blueprint, g, render_template

from lesivka_www.utils import get_template

www = Blueprint('www', __name__, template_folder='templates')


@www.route('/', defaults=dict(mode='cyr', name='index'))
@www.route('/<path:name>', defaults=dict(mode='cyr'))
@www.route('/lat', defaults=dict(mode='lat', name='index'))
@www.route('/lat/<path:name>', defaults=dict(mode='lat'))
def template_view(mode, name):
    g.mode = mode
    template = get_template(name)
    return render_template(template)
