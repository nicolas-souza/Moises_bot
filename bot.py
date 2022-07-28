import telebot
import requests
import json

api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJOb21lIjoiTmljb2xhcyBKb3PDqSBkb3MgU2FudG9zIGRlIFNvdXphIiwiRW1haWwiOiJuaWNvbGFzLmouc291emFAZ21haWwuY29tIiwiTml2ZWxEZUFjZXNzbyI6ImFkbWluIn0.ik-Lhso2g97dbSfWfkSZebsPyOxX45wxPTN2TLQ9WeI"
url = "http://192.168.1.4:7070/api/Reservas/fechadura/" + api_key

url_fechadura = "http://192.168.1.16/"

bot = telebot.TeleBot("5354549922:AAHKidv2uPGtYqYiombTM5tgYvQUYDTG8Ag")

def get_acesso(senha_telegram):
    response = requests.get(url)
    response_json = json.loads(response.content)
    # # {'tituloReserva': 'Cálculo 2', 'senhaReserva': '123', 'inicioReserva': '2022-07-21T09:32:00', 'fimReserva': '2022-07-21T15:30:00'}
    # response_json['senhaReserva']
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

# {
#   'content_type': 'text',
#   'id': 14, 
#   'message_id': 14, 
#   'from_user': 
#       {
#           'id': 95659176, 
#           'is_bot': False, 
#           'first_name': 'Nicolas', 
#           'username': 'Nicolas_jsouza', 
#           'last_name': 'De Souza', 
#           'language_code': 'pt-br', 
#           'can_join_groups': None, 
#           'can_read_all_group_messages': None, 
#           'supports_inline_queries': None, 
#           'is_premium': None, 
#           'added_to_attachment_menu': None
#       }, 
#   'date': 1657049142, 
#   'chat': 
#       {
#           'id': 95659176, 
#           'type': 'private', 'title': None, 
#           'username': 'Nicolas_jsouza', 
#           'first_name': 'Nicolas', 
#           'last_name': 'De Souza', 
#           'photo': None, 
#           'bio': None, 
#           'join_to_send_messages': None,
#           'join_by_request': None,
#           'has_private_forwards': None,
#           'description': None,
#           'invite_link': None,
#           'pinned_message': None,
#           'permissions': None,
#           'slow_mode_delay': None,
#           'message_auto_delete_time': None,
#           'has_protected_content': None,
#           'sticker_set_name': None,
#           'can_set_sticker_set': None,
#           'linked_chat_id': None,
#           'location': None
#       },
#  'sender_chat': None,
#  'forward_from': None,
#  'forward_from_chat': None, 
#  'forward_from_message_id': None,
#  'forward_signature': None, 
#  'forward_sender_name': None,
#  'forward_date': None,
#  'is_automatic_forward': None,
#  'reply_to_message': None,
#  'via_bot': None, 'edit_date': None,
#  'has_protected_content': None,
#  'media_group_id': None,
#  'author_signature': None,
#  'text': '/start',
#  'entities': [<telebot.types.MessageEntity object at 0x7fcdf9f05180>],
#  'caption_entities': None,
#  'audio': None,
#  'document': None,
#  'photo': None, 
#  'sticker': None,
#  'video': None, 
#  'video_note': None,
#  'voice': None, 
#  'caption': None,
#  'contact': None,
#  'location': None, 
#  'venue': None,
#  'animation': None,
#  'dice': None,
#  'new_chat_member': None,
#  'new_chat_members': None,
#  'left_chat_member': None,
#  'new_chat_title': None, 
#  'new_chat_photo': None,
#  'delete_chat_photo': None, 
#  'group_chat_created': None,
#  'supergroup_chat_created': None,
#  'channel_chat_created': None,
#  'migrate_to_chat_id': None,
#  'migrate_from_chat_id': None,
#  'pinned_message': None,
#  'invoice': None,
#  'successful_payment': None,
#  'connected_website': None, 
#  'reply_markup': None, 
#  'json': 
#       {
#           'message_id': 14,
#           'from': 
#               {
#                   'id': 95659176,
#                   'is_bot': False,
#                   'first_name': 'Nicolas',
#                   'last_name': 'De Souza',
#                   'username': 'Nicolas_jsouza',
#                   'language_code': 'pt-br'
#               }, 
#           'chat': 
#               {
#                   'id': 95659176,
#                   'first_name': 'Nicolas',
#                   'last_name': 'De Souza',
#                   'username': 'Nicolas_jsouza',
#                   'type': 'private'
#                },
#           'date': 1657049142,
#           'text': '/start',
#           'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]
#       }
# }

