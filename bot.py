import telebot
import requests
import json

api_key = "API_KEY_MOISES_API"
url = "URL_API_MOISES" + api_key

url_fechadura = "ENDPOINT_ESP32"

bot = telebot.TeleBot("")

def get_acesso(senha_telegram):
    response = requests.get(url)
    response_json = json.loads(response.content)

    if (response_json['senhaReserva'] == senha_telegram):
        requests.get(url_fechadura+'abrir')
        return True
    else:
        requests.get(url_fechadura+'fechar')
        return False

@bot.message_handler(commands=['start', 'help'], )
def send_welcome(message):
    bot.reply_to(message, "Olá, eu sou o Bot Moisés e serei o seu ajudante de acesso! 😎 \n \n" +
                          "1. Se você possui uma senha de acesso, basta enviá-la e nosso sitema se encarregará do resto \n"+
                          "2. Se você precisa reservar uma sala procure pelo responsável do sistema para que possa te auxiliar \n"+
                          "3. Este sistema é apenas um protótipo então tenha paciência comigo! 😪\n")


@bot.message_handler(commands=['senha'])
def acesso_password(message):
    bot.reply_to(message, "Muito bom, então você possui uma senha! \nVamos ver se é a certa? Só me enviar que eu já te conto!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if(get_acesso(message.text)):
        bot.reply_to(message, "🥳 \nDeu certo! Faça bom uso do nosso espaço, até mais!")
    else:        
        bot.reply_to(message, "Sinto muito, mas você não irá acessar com essa senha! 👀 \n\nPeça um /help se estiver precisando de uma mãozinha")
    

bot.infinity_polling()