import lesiwka
from flask import Blueprint

from lesiwka_www.utils import get_text

transcode = Blueprint("transcode", __name__)


@transcode.route("/encode", methods=["GET", "POST"])
def encode():
    text = get_text()
    return lesiwka.encode(text)


@transcode.route("/decode", methods=["GET", "POST"])
def decode():
    text = get_text()
    return lesiwka.decode(text)
