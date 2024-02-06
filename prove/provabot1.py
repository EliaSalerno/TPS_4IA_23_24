import telepot
import serial
import time


def on_chat_message(msg):
    #content_type, chat_type, chat_id = telepot.glance(msg)
    #if content_type == 'text':
        #print(msg['text'])
        #bot.sendMessage(chat_id, 'ciao, sono un bot molto stupido!')
    i=7
TOKEN = '2032071494:AAFy5kT4eEBOkt4q_r-FBtVpx6HLLIBjsls'

telepot.api.set_proxy('http://proxy:3128')
bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print('Listening ...')

while 1:
    time.sleep(10)