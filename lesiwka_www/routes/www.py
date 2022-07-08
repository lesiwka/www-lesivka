from flask import Blueprint, g, redirect, render_template, url_for

from lesiwka_www.utils import get_template

www = Blueprint("www", __name__, template_folder="templates")

redirects = {
    "abc": "abetka",
    "examples": "prikladi",
    "apps": "zastosunki",
    "conv": "konverter",
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
    g.mode = mode

    if name in redirects:
        name = redirects[name]
        url = url_for("www.template_view", mode=mode, name=name)
        return redirect(url, code=301)

    template = get_template(name)
    return render_template(template)


@www.route("/konverter-popup", defaults=dict(mode="cyr"))
@www.route("/lat/konverter-popup", defaults=dict(mode="lat"))
def konverter_popup(mode):
    g.mode = mode
    template = get_template("konverter")
    return render_template(template, popup=True)
