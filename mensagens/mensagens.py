from urllib.request import urlopen
from json import loads
import re
from classes.Frase import Frase

def get_frase_random():
    req = "https://allugofrases.herokuapp.com/frases/random"
    response = urlopen(req)
    obj = loads(response.read())
    MSG = Frase(obj['frase'], obj['livro'], obj['autor'])
    return MSG.mensagemCompleta()

def get_cumprimento_message(msg):
    return "Olá " + msg.from_user.first_name + ", Legal poder falar com você"

def get_info_boot_donio(msg):
  return ("Olá meu nome é Bot Donio\n"
        "Fui criado por Mardonio S Costa com BotFather"
        "\nUltima atualização: 10/11/2020"
        "\nPara mais informações pode entrar em contato com @Mardoniosc no telegram")

def get_teste_message(msg):
    return "Olá " + msg.from_user.first_name + "\nEstou funcionando bem"


def get_contexto_frase(msg):
    text = msg.text
    if re.search("tudo bem", text, re.IGNORECASE) or re.search(
        "tudo bom", text, re.IGNORECASE
    ):
        return "Eu sou um bot, e estou funcionando bem obrigado\n E você como está?"
    elif re.search("estou bem", text, re.IGNORECASE):
        return (
            "Que bom!! em que posso lhe ajudar??"
            "\n escolha a opção /start caso tenha duvida do que posso fazer"
        )

    return 'Não entendi o que quis dizer com: \n\n"' + text + '"'
