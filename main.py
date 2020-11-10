# coding=utf-8
from menus.menuPrincipal import bot
import traceback
import os, time

def telegram_polling():
    try:
        bot.polling(none_stop=True, timeout=123) #constantly get messages from Telegram
    except:
        localLogs = os.getcwd()
        localLogs = localLogs + '/logs/'
        arquivoPath = localLogs + "Error.log" 
        traceback_error_string=traceback.format_exc()
        with open(arquivoPath, "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime("%c")+"\r\n<<ERROR polling>>\r\n"+ traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(3)
        telegram_polling()

if __name__ == '__main__':
    telegram_polling()