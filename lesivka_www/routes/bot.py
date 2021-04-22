import os

import lesivka
from flask import Blueprint, Response, request
from telebot import TeleBot
from telebot.types import Message, Update

bot = Blueprint("bot_hook", __name__)

token = os.environ["TELEGRAM_BOT_TOKEN"]
telebot = TeleBot(token)


@bot.route(f"/{token}", methods=["POST"])
def hook():
    update = Update.de_json(request.json)
    telebot.process_new_updates([update])
    return Response(status=200)


@telebot.message_handler(commands=["start"])
def start(message: Message):
    telebot.send_message(
        message.chat.id,
        "Конвертер з кирилиці у лесівку. Подробиці https://lesivka.com",
    )


@telebot.message_handler(func=lambda m: True)
def encode(message: Message):
    telebot.reply_to(message, lesivka.encode(message.text))
