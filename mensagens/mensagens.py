from urllib.request import urlopen
from json import loads
import re
from classes.Frase import Frase
from logs.logs import historico


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


def get_palavra_chave_message(msg):
    text = msg.text
    user = msg.from_user.first_name
    if validaSeEcontrouPalavra('Tudo Bem', text) or \
            validaSeEcontrouPalavra('Tudo Bom', text):
        return 'Eu sou um bot, e estou funcionando bem obrigado\n E você como está?'

    elif validaSeEcontrouPalavra('Bom dia', text):
        return 'Bom dia, ' + user

    elif validaSeEcontrouPalavra('Boa tarde', text):
        return 'Boa Tarde, ' + user

    elif validaSeEcontrouPalavra('Boa noite', text):
        return 'Boa Noite, ' + user

    elif validaSeEcontrouPalavra('Sentido da vida', text):
        return 'A vida é desprovida de sentido. Você dá sentido a ela. '\
                'O sentido da vida é aquilo que você atribui a ela. Estar vivo é o sentido. \n\n' \
                'Sou apenas um bot não tenho conhecimento para te falar isso'

    return 'Não entendi o que quis dizer com: \n\n"' + text + '"'


def validaSeEcontrouPalavra(palavraOrFrase, texto):
    return re.search(palavraOrFrase, texto, re.IGNORECASE)


def get_historico_user(msg):
    user = msg.from_user.first_name
    result = historico(user)
    return 'Dias e horarios de mensagens \n\n' + result
