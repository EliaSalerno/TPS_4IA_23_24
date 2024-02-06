import os, time
import logging
import sys
import struct
import traceback

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
# invio comandi
#-------------------------------------------------------------------------------
def apri():
    payload = struct.pack("c", '1'.encode('ascii'))
    #for x in range(5):
    nrf.send(payload)
    nrf.wait_until_sent()
    
def chiudi():
    payload = struct.pack("c", '0'.encode('ascii'))
    #for x in range(5):
    nrf.send(payload)
    nrf.wait_until_sent()

while True:
    if input()=="a":
        apri()
    if input()=="c":
        chiudi()