'''
Alexa Custom Skill per leggere la temperatura e aprire/chiudere la finestra 
 con Raspberry Pi e flask-ask
 
Alexa, apri greppi finestra
        dimmi la temperatura
        apri la finestra
        chiudi la finestra

'''
from flask import Flask, render_template
from flask_ask import Ask, statement, question, request, session, convert_errors
import os, time
import logging
import sys
import struct
import traceback
import threading

import pigpio
from nrf24 import *

#-------------------------------------------------------------------------------
# costanti
#-------------------------------------------------------------------------------
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
# inizializzazione
#-------------------------------------------------------------------------------
app = Flask(__name__)
ask = Ask(app, '/')

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
# funzione gestione intenti
#-------------------------------------------------------------------------------
@ask.launch
def start_skill():
    welcome_message = render_template('benvenuto')
    return question(welcome_message)

@ask.intent('AMAZON.HelpIntent')
def help():
    return start_skill()

@ask.intent('AMAZON.FallbackIntent')
def fallback():
    fallback_message = render_template('errore')
    return statement(fallback_message)

@ask.intent('AMAZON.StopIntent')
def stop():
    text = render_template('arrivederci')
    return statement(text).simple_card('Status', text)

@ask.session_ended
def session_ended():
    return "{}", 200

@ask.intent('ApriIntent')
def apri():
    payload = struct.pack("c", '1'.encode('ascii'))
    for x in range(3):
        nrf.send(payload)
        nrf.wait_until_sent()
    print("aperta")
    text = render_template('apri')
    return question(text)
    
@ask.intent('ChiudiIntent')
def chiudi():
    payload = struct.pack("c", '0'.encode('ascii'))
    for x in range(3):
        nrf.send(payload)
        nrf.wait_until_sent()
    print("chiusa")
    text = render_template('chiudi')
    return question(text)

@ask.intent('TempIntent')
def temp():
    global temperatura
    print ("inviata temperatura: "+str(temperatura))
    text = render_template('temp1')+' '+str(temperatura)+' '+render_template('temp2')
    return question(text)

def threadTemp():
    global temperatura
    while True:
        while nrf.data_ready():
            time.sleep(0.5)
            payload = nrf.get_payload()   
            #print(payload) 
            dato = (struct.unpack("h", payload[0:2]))[0]
            if dato!=0:
                temperatura=dato
                print(temperatura)
    time.sleep(1)
if __name__ == '__main__':
    t = threading.Thread(target=threadTemp, args=())
    t.start()
    app.run(debug=True)
    
