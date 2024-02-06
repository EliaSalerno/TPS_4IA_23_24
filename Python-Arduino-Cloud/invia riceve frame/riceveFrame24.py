import time
import sys
import struct

import pigpio
from nrf24 import *

#-------------------------------------------------------------------------------
# costanti
#-------------------------------------------------------------------------------
PIGPIONAME='localhost'
PIGPIOPORT=8888
ADDRESS='00001'

MIO_ID=b"EP"
MIO_INDIRIZZO=b"P001"
MIO_TIPO=b"S1"
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
nrf.set_address_bytes(5)
nrf.open_reading_pipe(RF24_RX_ADDR.P1, ADDRESS)

#-------------------------------------------------------------------------------
# lettura dato
#-------------------------------------------------------------------------------
while True:
    if nrf.data_ready():
        msg=(struct.unpack("2s 4s 4s 2s 4s 16s",nrf.get_payload()))
        print(msg)
        id=msg[0]
        if id==MIO_ID:
            mittente=msg[1]
            destinatario=msg[2]
            if destinatario==MIO_INDIRIZZO:
               tipo=msg[3]
               if tipo==MIO_TIPO:                  
                  valoreSensore=int(msg[4])
                  print(valoreSensore)
               else:
                  print("Errore - ricevuto tipo "+tipo)