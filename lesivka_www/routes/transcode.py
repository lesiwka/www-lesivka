import lesivka
from flask import Blueprint

from lesivka_www.utils import get_text

transcode = Blueprint('transcode', __name__)


@transcode.route('/encode', methods=['GET', 'POST'])
def encode():
    text = get_text()
    return lesivka.encode(text)


@transcode.route('/decode', methods=['GET', 'POST'])
def decode():
    text = get_text()
    return lesivka.decode(text)
