from flask import Blueprint, redirect, render_template, url_for

from utils import get_template

www = Blueprint("www", __name__, template_folder="templates")

redirects = {
    "abc": "abetka",
    "examples": "pryklady",
    "apps": "zastosunky",
    "conv": "konverter",
    "prikladi": "pryklady",
    "zastosunki": "zastosunky",
}


@www.route("/cyr", defaults=dict(name="index"))
@www.route("/cyr/<path:name>")
def redirect_cyr(name):
    url = url_for("www.template_view", mode="cyr", name=name)
    return redirect(url, code=301)


@www.route("/", defaults=dict(mode="cyr", name="index"))
@www.route("/<path:name>", defaults=dict(mode="cyr"))
@www.route("/lat", defaults=dict(mode="lat", name="index"))
@www.route("/lat/<path:name>", defaults=dict(mode="lat"))
def template_view(mode, name):
    if name in redirects:
        name = redirects[name]
        url = url_for("www.template_view", mode=mode, name=name)
        return redirect(url, code=301)

    template = get_template(name)
    return render_template(template, mode=mode)


@www.route("/konverter-popup", defaults=dict(mode="cyr"))
@www.route("/lat/konverter-popup", defaults=dict(mode="lat"))
def konverter_popup(mode):
    template = get_template("konverter")
    return render_template(template, mode=mode, popup=True)
