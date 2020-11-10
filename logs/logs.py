from datetime import datetime
import os

data_e_hora_atuais = datetime.now()
data_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')


def atualizaLog(texto, user):
  localLogs = os.getcwd()
  localLogs = localLogs + '/logs/'
  arquivoPath = localLogs + user + ".txt" 
  arquivo = open(arquivoPath, "a")
  arquivo.writelines(data_em_texto + ' - ' + texto + '\n')
  arquivo.close()
  return True

def historico(user):
  localLogs = os.getcwd()
  localLogs = localLogs + '/logs/'
  arquivoPath = localLogs + user + ".txt" 
  arquivo = open(arquivoPath, "r")
  historico = arquivo.read()
  arquivo.close()
  return historico