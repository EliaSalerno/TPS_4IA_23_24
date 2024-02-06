import paho.mqtt.client as client
TOPIC="prova1"
#BROKER="test.mosquitto.org"
BROKER="192.168.43.47"

# funzione di callback dopo la corretta connessione
def on_connect(subscriber, userdata, flags, rc):
    print("Connesso con return code "+str(rc))

    # sottoscrizione dopo che la connessione è avvenuta
    subscriber.subscribe(TOPIC)

# funzione di callback alla ricezione di messaggi
def on_message(subscriber, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

subscriber = client.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message

subscriber.connect(BROKER, 1883, 60)

# ciclo di attesa messaggi
subscriber.loop_forever()