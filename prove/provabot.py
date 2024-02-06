#!/usr/bin/env python

import logging
import serial
import time

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup

#-------------------------------------------------------------------------------
# funzione per la gestione dei diversi messaggi e comandi
#-------------------------------------------------------------------------------
def start(aggiornamento, contesto):
    help(aggiornamento, contesto)

def help(aggiornamento, contesto):
    tastiera = [
        [
            KeyboardButton("/on: Arduino ON"),
            KeyboardButton("/off: Arduino OFF"),
        ],
        [   KeyboardButton("/reg: Inviami i dati di temperatura"),
            KeyboardButton("/unreg: Non inviarmi i dati"),
        ],
    ]

    tastiera_markup = ReplyKeyboardMarkup(tastiera)
    aggiornamento.message.reply_text('Scegli una funzione:', reply_markup=tastiera_markup)

def echo(aggiornamento, contesto):
    #aggiornamento.message.reply_text(aggiornamento.message.text)
    #print(aggiornamento.message.text)
    help(aggiornamento, contesto)

def reg(aggiornamento, contesto):
    global utente_registrato_id,utente_registrato_contesto
    utente_registrato_id=aggiornamento.effective_chat.id
    utente_registrato_contesto=contesto
    aggiornamento.message.reply_text('Ora riceverai i dati di temperatura da Arduino')

def unreg(aggiornamento, contesto):
    global utente_registrato_id,utente_registrato_contesto
    utente_registrato_id=None
    utente_registrato_contesto=None
    aggiornamento.message.reply_text('Ora non riceverai più i dati da Arduino')

def on(aggiornamento, contesto):
    arduino.write(b"1")
    aggiornamento.message.reply_text('Arduino attivo')

def off(aggiornamento, contesto):
    arduino.write(b"0")
    aggiornamento.message.reply_text('Arduino inattivo')

def error(aggiornamento, contesto):
    logger.warning("L'aggiornamento '%s' ha causato un errore  's'", aggiornamento, contesto.error)

#-------------------------------------------------------------------------------
# abilita il logging su console
#-------------------------------------------------------------------------------

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
# utente registrato per ricevere dati
#-------------------------------------------------------------------------------
utente_registrato_id=None
utente_registrato_contesto=None

#-------------------------------------------------------------------------------
# costanti
#-------------------------------------------------------------------------------

TOKEN="2032071494:AAFy5kT4eEBOkt4q_r-FBtVpx6HLLIBjsls"
PROXY={'proxy_url': 'http://proxy:3128'}

# crear l'updater passandogli la chiave ottenuta da Telegram in fase di registrazione del Bot
updater = Updater(TOKEN)
#updater = Updater(TOKEN, request_kwargs=PROXY)

# dispatcher per la registrazine delle funzioni di gestione messaggi
dp = updater.dispatcher

# registrazione delle funzioni per la gestione messaggi
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler('reg', reg))
dp.add_handler(CommandHandler('unreg', unreg))
dp.add_handler(CommandHandler('on', on))
dp.add_handler(CommandHandler('off', off))
dp.add_handler(MessageHandler(Filters.text, echo))
dp.add_error_handler(error)

# avvia l'attesa di messaggi (asincrona)
updater.start_polling()
 
#-------------------------------------------------------------------------------
# apre la seriale per il colloquio con Arduino
#-------------------------------------------------------------------------------
arduino = serial.Serial('COM5', 9600, timeout=1)

#-------------------------------------------------------------------------------
# ciclo lettura da Arduino e attesa messaggi Telegram
#-------------------------------------------------------------------------------
while True:
    try:
        linea=arduino.readline()
        temperatura=int(linea.decode().strip())    
        if utente_registrato_id!=None:
            utente_registrato_contesto.bot.send_message(utente_registrato_id,text=str(temperatura))
    except:
        pass
        
    time.sleep(0.1)