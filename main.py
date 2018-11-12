from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

from lesivka_www.context import active, page, switch, text
from lesivka_www.routes.www import www
from lesivka_www.routes.transcode import transcode
from lesivka_www.utils import get_template

app = Flask(__name__)
app.register_blueprint(www)
app.register_blueprint(transcode)
app.secret_key = 'super secret key'


@app.context_processor
def template_injection():
    return dict(active=active, page=page, switch=switch, text=text)


@app.errorhandler(404)
@app.errorhandler(TemplateNotFound)
def page_not_found(_):
    template = get_template('404')
    return render_template(template), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
