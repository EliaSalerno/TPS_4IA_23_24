#!/usr/bin/env python


import logging
import serial
import time
import sys
import struct
import traceback

import pigpio
from nrf24 import *

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup
#-------------------------------------------------------------------------------

# costanti

#-------------------------------------------------------------------------------
TOKEN="2032071494:AAFy5kT4eEBOkt4q_r-FBtVpx6HLLIBjsls"
PROXY={'proxy_url': 'http://proxy:3128'}
PIGPIONAME='localhost'
PIGPIOPORT=8888
RCVADDRESS='00001'
SNDADDRESS='00002'
LENADDRESS=5
#-------------------------------------------------------------------------------
# ultima temperatura
#-------------------------------------------------------------------------------
temperatura=0
#-------------------------------------------------------------------------------
# funzioni per la gestione dei diversi messaggi e comandi
#-------------------------------------------------------------------------------
def start(aggiornamento, contesto):
    print('started')
    help(aggiornamento, contesto)

def help(aggiornamento, contesto):
    tastiera = [
        [
            KeyboardButton("/apri: apre la finestra"),
            KeyboardButton("/chiudi: chiude la finestra"),
        ],
        [   KeyboardButton("/temperatura: dimmi la temperatura"),
        ],
    ]

    tastiera_markup = ReplyKeyboardMarkup(tastiera)
    aggiornamento.message.reply_text('Scegli una funzione:', reply_markup=tastiera_markup)

def echo(aggiornamento, contesto):
    #aggiornamento.message.reply_text(aggiornamento.message.text)
    #print(aggiornamento.message.text)
    help(aggiornamento, contesto)

def temperatura(aggiornamento, contesto):
    aggiornamento.message.reply_text('La temperatura attuale è di '+str(temperatura)+' gradi')

def apri(aggiornamento, contesto):
    payload = struct.pack("c", '1'.encode('ascii'))
    for x in range(3):
        nrf.send(payload)
        nrf.wait_until_sent()
    print("on")
    aggiornamento.message.reply_text('Aperta')

def chiudi(aggiornamento, contesto):
    payload = struct.pack("c", '0'.encode('ascii'))
    for x in range(3):
        nrf.send(payload)
        nrf.wait_until_sent()
    print("off")
    aggiornamento.message.reply_text('Chiusa')

def error(aggiornamento, contesto):
    logger.warning("L'aggiornamento '%s' ha causato un errore  's'", aggiornamento, contesto.error)

#-------------------------------------------------------------------------------
# abilita il logging su console
#-------------------------------------------------------------------------------
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
#-------------------------------------------------------------------------------
# connessioni NRF24
#-------------------------------------------------------------------------------
# connessione a pigpiod
pi = pigpio.pi(PIGPIONAME, PIGPIOPORT)

if not pi.connected:
    print("Pigpiod non connesso. Lanciare: SUDO PIGPIOD")
    sys.exit()

# Create l'oggetto NRF24 
nrf = NRF24(pi, ce=17, payload_size=32, channel=76, data_rate=RF24_DATA_RATE.RATE_1MBPS, pa_level=RF24_PA.LOW)

# apre le pipe
nrf.set_address_bytes(LENADDRESS)
nrf.open_reading_pipe(RF24_RX_ADDR.P1, RCVADDRESS)
nrf.open_writing_pipe(SNDADDRESS)

# Visualizza i registri NRF24L01
nrf.show_registers()
#-------------------------------------------------------------------------------
# connessioni Telegram
#-------------------------------------------------------------------------------

# crea l'updater telegram passandogli la chiave ottenuta da Telegram in fase di registrazione del Bot
updater = Updater(TOKEN)
#updater = Updater(TOKEN, request_kwargs=PROXY)

# dispatcher per la registrazine delle funzioni di gestione messaggi telegram
dp = updater.dispatcher

# registrazione delle funzioni per la gestione messaggi telegram
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler('temperatura', temperatura))
dp.add_handler(CommandHandler('apri', apri))
dp.add_handler(CommandHandler('chiudi', chiudi))
dp.add_handler(MessageHandler(Filters.text, echo))
dp.add_error_handler(error)

# avvia l'attesa di messaggi telegram (asincrona)
try:
    updater.start_polling()
except:
    pass

#-------------------------------------------------------------------------------
# ciclo lettura da Arduino e attesa messaggi Telegram
#-------------------------------------------------------------------------------
time.sleep(0.1)
try:
    while True:
        while nrf.data_ready():
            payload = nrf.get_payload()   
            print(payload) 
            temperatura = (struct.unpack("h", payload[0:2]))[0]
            print(temperatura)
     
    # Sleep 100 ms.
    time.sleep(0.1)
except:
    traceback.print_exc()
    nrf.power_down()
    pi.stop()