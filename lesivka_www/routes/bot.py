import os

import lesivka
from flask import Blueprint, Response, request
from telebot import TeleBot
from telebot.types import Message, Update

bot = Blueprint("bot_hook", __name__)

token = os.environ["TELEGRAM_BOT_TOKEN"]
telebot = TeleBot(token)

START_MSG = "Конвертер з кирилиці у лесівку. Подробиці https://lesivka.com"


def chat_type(*types):
    def f(message):
        return message.chat.type in types

    return f


@bot.route(f"/{token}", methods=["POST"])
def hook():
    update = Update.de_json(request.json)
    telebot.process_new_updates([update])
    return Response(status=200)


@telebot.message_handler(commands=["start"], func=chat_type("private"))
def start(message: Message):
    telebot.send_message(message.chat.id, START_MSG)


@telebot.message_handler(
    commands=["lesivka"],
    func=chat_type("group", "supergroup"),
)
def convert(message: Message):
    try:
        _, text = message.text.split(maxsplit=1)
    except ValueError:
        telebot.send_message(message.chat.id, START_MSG)
    else:
        telebot.reply_to(message, lesivka.encode(text))


@telebot.message_handler(func=chat_type("private"))
def encode(message: Message):
    telebot.send_message(message.chat.id, lesivka.encode(message.text))
