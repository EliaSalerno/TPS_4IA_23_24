import time
import sys

import pigpio
from nrf24 import *
import struct
#-------------------------------------------------------------------------------
# costanti
#-------------------------------------------------------------------------------
PIGPIONAME='localhost'
PIGPIOPORT=8888
WRITINGPIPE='00001'
ID=b"EP"
MITTENTE=b"P001"
DESTINATARIO=b"A328"
TIPO=b"A1"
VUOTO=("."*16).encode()

#-------------------------------------------------------------------------------
# connessioni NRF24
#-------------------------------------------------------------------------------

# connessione a pigpiod
pi = pigpio.pi(PIGPIONAME, PIGPIOPORT)
if not pi.connected:
    print("Pigpiod non connesso. Lanciare: SUDO PIGPIOD")
    sys.exit()

# Crea l'oggetto NRF24 
nrf = NRF24(pi, ce=17, payload_size=32, channel=76, data_rate=RF24_DATA_RATE.RATE_1MBPS, pa_level=RF24_PA.LOW)

# apre le pipe
nrf.set_address_bytes(5)
nrf.open_writing_pipe(WRITINGPIPE)
#-------------------------------------------------------------------------------
# invio dato (invia numeri in progressione)
#-------------------------------------------------------------------------------
i=0
while True:
    direzione=b"A"
    velocita=str(i).zfill(3).encode()
    msg=struct.pack("2s 4s 4s 2s 1s 3s 16s",ID,MITTENTE,DESTINATARIO,TIPO,direzione,velocita,VUOTO)
    nrf.send(msg)
    print(msg)
    i+=1
    time.sleep(1
    )