import os

import lesiwka
from flask import Blueprint, Response, request
from telebot import TeleBot
from telebot.types import Message, Update
from viberbot import Api, BotConfiguration
from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import ViberMessageRequest, ViberSubscribedRequest

bot = Blueprint("bot_hook", __name__)

token = os.environ["TELEGRAM_BOT_TOKEN"]
telebot = TeleBot(token)

viber_token = os.environ["VIBER_BOT_TOKEN"]
viber_conf = BotConfiguration(
    viber_token,
    "Lesiwka Bot",
    "https://lesiwka.com/static/icons/android-chrome-512x512.png",
)
viber = Api(viber_conf)

START_MSG = "Конвертер з кирилиці у лесівку\nПодробиці https://lesiwka.com"


def chat_type(*types):
    def f(message):
        return message.chat.type in types

    return f


@bot.route(f"/{token}", methods=["POST"])
def hook():
    update = Update.de_json(request.json)
    telebot.process_new_updates([update])
    return Response(status=200)


@bot.route(f"/{viber_token}", methods=["POST"])
def viber_hook():
    data = request.get_data()
    if not viber.verify_signature(
        data, request.headers.get("X-Viber-Content-Signature")
    ):
        return Response(status=403)

    viber_request = viber.parse_request(data)
    if isinstance(viber_request, ViberSubscribedRequest):
        message = TextMessage(text=START_MSG)
        viber.send_messages(viber_request.user.id, [message])
    elif isinstance(viber_request, ViberMessageRequest):
        message = TextMessage(text=lesiwka.encode(viber_request.message.text))
        viber.send_messages(viber_request.sender.id, [message])

    return Response(status=200)


@telebot.message_handler(commands=["start"], func=chat_type("private"))
def start(message: Message):
    telebot.send_message(message.chat.id, START_MSG)


@telebot.message_handler(
    commands=["lesiwka", "лесівка"],
    func=chat_type("group", "supergroup"),
)
def convert(message: Message):
    try:
        _, text = message.text.split(maxsplit=1)
    except ValueError:
        telebot.send_message(message.chat.id, START_MSG)
    else:
        telebot.reply_to(message, lesiwka.encode(text))


@telebot.message_handler(func=chat_type("private"))
def encode(message: Message):
    telebot.send_message(message.chat.id, lesiwka.encode(message.text))
