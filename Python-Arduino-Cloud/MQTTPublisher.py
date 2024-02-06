import paho.mqtt.publish as publish
import time
TOPIC="emilio"
#BROKER="test.mosquitto.org"
BROKER="172.17.200.5"

# pubblica ad intervalli di 5 secondi un numero progressivo
i=0
while True:
    i=i+1
    msg=str(i)
    print(i)
    
    publish.single(TOPIC, msg, hostname=BROKER)
    
    time.sleep(5)