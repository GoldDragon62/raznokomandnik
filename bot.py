import random
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import asyncio
from config import token
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    text = 'привет! Я бот повторялка и я буду повторять всё, что ты скажешь.'
    await bot.reply_to(message, text)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help'])
async def send_help(message):
    text = 'у нас есть команды /start /help /coin'
    await bot.reply_to(message, text)

@bot.message_handler(commands=['coin'])
async def random_coin(message):
    text = random.choice(['орел','решка'])
    await bot.reply_to(message, text)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())