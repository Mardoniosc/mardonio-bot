# coding=utf-8
import os
from telebot import TeleBot

from mensagens.mensagens import *
from logs.logs import atualizaLog

bot = TeleBot(os.environ["BOT_TOKEN_DONIOSC"])


@bot.message_handler(commands=["start", "help"])
def send_start_message(message):
    atualizaLog(message.text, message.from_user.first_name)
    bot.reply_to(
        message,
        "Olá " + message.from_user.first_name + ", eu sou o Foster "
        "\nAbaixo a lista de comandos que eu respondo"
        "\nDigite algum para eu lhe ajudar!"
        "\n\n/olá, /oi, /oii, /eae para um comprimento amigavel"
        "\n\n/frase para mostrar uma frase"
        "\n\n/start ou /help para mostrar os comandos novamente"
        "\n\n /info para informações sobre bot e seu desenvolvedor"
        "\n\n /teste /test para teste de resposta",
    )


# opções escolhida do menu acima
@bot.message_handler(commands=["frase"])
def send_frase(message):
    atualizaLog(message.text, message.from_user.first_name)
    frase = get_frase_random()
    bot.reply_to(message, frase)


@bot.message_handler(commands=["info", "donio"])
def send_people(message):
    atualizaLog(message.text, message.from_user.first_name)
    bot.reply_to(
        message,
        get_info_boot_donio(message),
    )


@bot.message_handler(commands=["oi", "olá", "oii", "eae"])
def send_cumprimento(message):
    atualizaLog(message.text, message.from_user.first_name)
    bot.reply_to(message, get_cumprimento_message(message))


@bot.message_handler(commands=["teste", "test", "tt"])
def send_cumprimento(message):
    atualizaLog(message.text, message.from_user.first_name)
    bot.reply_to(message, get_teste_message(message))


@bot.message_handler()
def send_cumprimento(message):
    atualizaLog(message.text, message.from_user.first_name)
    bot.reply_to(message, get_contexto_frase(message))
