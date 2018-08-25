import lesivka
from flask import Flask, request

app = Flask(__name__)


def get_text():
    keys = list(request.values.keys())
    return request.values.get('t', keys[0] if keys else '')


@app.route('/encode', methods=['GET', 'POST'])
def encode():
    return lesivka.encode(get_text())


@app.route('/decode', methods=['GET', 'POST'])
def decode():
    return lesivka.decode(get_text())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
