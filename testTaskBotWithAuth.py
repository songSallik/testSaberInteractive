import telebot
import calculate
import auth
import pymongo
from pymongo import MongoClient

AUTH_FAIL = "Wrong user or password"
AUTH_SUCSSEED = "User exist and password correct!"

bot = telebot.TeleBot('5374816114:AAHqjvn-dpgpq_WW-XmJvp-2Q85b-kSTwXs')
authMsg = "Hello, send UserName and Password. Example: \nDoomguy Welcome_to_hell"
startMsg = "Hello, I'm a calculator bot. I will be able to calculate equations with 2 and 3 operators. Example: \n2+2 \n2*9 \n2*6/8 \n100-2*10"
tryAgan = "Please send /start and try again"
isAuth = False


@bot.message_handler(commands=["start"])

def start(m, res=False):
    bot.send_message(m.chat.id, authMsg)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    global isAuth
    if isAuth == False:
        responceAuth = auth.auth(message)
        if responceAuth == AUTH_SUCSSEED:
            isAuth = True
            bot.send_message(message.chat.id, responceAuth)
            bot.send_message(message.chat.id, startMsg)
        elif responceAuth == AUTH_FAIL:
            bot.send_message(message.chat.id, responceAuth)
            bot.send_message(message.chat.id, tryAgan)
    else:
        bot.send_message(message.chat.id, calculate.runCalculate(message.text))     
        
bot.polling(none_stop=True, interval=0)