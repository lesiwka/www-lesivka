import os

from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

from lesiwka_www.context import active, page, switch, text
from lesiwka_www.routes.bot import bot
from lesiwka_www.routes.transcode import transcode
from lesiwka_www.routes.www import www
from lesiwka_www.utils import encode, get_template

app = Flask(__name__)
app.register_blueprint(bot)
app.register_blueprint(www)
app.register_blueprint(transcode)


@app.context_processor
def template_injection():
    return dict(
        TRACKING_ID=os.environ["TRACKING_ID"],
        active=active,
        encode=encode,
        page=page,
        switch=switch,
        text=text,
    )


@app.errorhandler(404)
@app.errorhandler(TemplateNotFound)
def page_not_found(_):
    template = get_template('errors/404')
    return render_template(template), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
