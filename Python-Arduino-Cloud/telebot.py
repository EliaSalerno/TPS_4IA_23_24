from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup
#-------------------------------------------------------------------------------
# costanti
#-------------------------------------------------------------------------------
TOKEN="5075804894:AAFmIxez9lHSBtqUBztflMgurtDKKn2_vgo"
PROXY={'proxy_url': 'http://proxy:3128'}
#-------------------------------------------------------------------------------
# funzioni per la gestione dei diversi messaggi e comandi
#-------------------------------------------------------------------------------
# messaggio /start
def start(aggiornamento, contesto):
    help(aggiornamento, contesto)

# messaggio /help
def help(aggiornamento, contesto):
    tastiera = [
        [
            KeyboardButton("/saluta: manda un saluto"),
            KeyboardButton("/insulta: manda un insulto"),
        ]
    ]
    tastiera_markup = ReplyKeyboardMarkup(tastiera)
    aggiornamento.message.reply_text('Scegli una funzione:', reply_markup=tastiera_markup)

# messaggio senza /
def echo(aggiornamento, contesto):
    help(aggiornamento, contesto)

# messaggio /saluta
def saluta(aggiornamento, contesto):
    aggiornamento.message.reply_text('Ciao!')

# messaggio /insulta
def insulta(aggiornamento, contesto):
    aggiornamento.message.reply_text('Babbeo!')

# errore
def error(aggiornamento, contesto):
    print(contesto.error)
    
#-------------------------------------------------------------------------------
# connessioni Telegram
#-------------------------------------------------------------------------------

# crea l'updater telegram passandogli la chiave ottenuta da Telegram in fase di registrazione del Bot 
# senza Proxy
updater = Updater(TOKEN)
# con il Proxy
#updater = Updater(TOKEN, request_kwargs=PROXY)

# dispatcher per la registrazione delle funzioni di gestione messaggi telegram
dp = updater.dispatcher

# registrazione delle funzioni per la gestione messaggi telegram
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler('saluta', saluta))
dp.add_handler(CommandHandler('insulta', insulta))
dp.add_handler(MessageHandler(Filters.text, echo))
dp.add_error_handler(error)

# avvia l'attesa di messaggi telegram e attende
updater.start_polling()
updater.idle()
