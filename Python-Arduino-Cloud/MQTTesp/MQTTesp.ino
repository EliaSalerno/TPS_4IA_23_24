#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// WiFi
const char *WIFI_SSID = "Greppi-2G";
const char *WIFI_PASSWORD = "withProxy";

// MQTT Broker
const char *MQTT_BROKER = "172.17.3.26";
const char *MQTT_USERNAME = "";
const char *MQTT_PASSWORD = "";
const int MQTT_PORT = 1883;

// topic
const char *INVIA = "miotopic/invia";
const char *RICEVI = "miotopic/ricevi";

// oggetti per wifi e mqtt
WiFiClient espClient;
PubSubClient client(espClient);

// setup
void setup() {

  Serial.begin(9600);
  Serial.println("Inizio");

  Serial.print("Connessione al WiFi..");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("Connesso");

  // assegna un nome q uesto client
  String client_id = "esp8266-client-" + String(WiFi.macAddress());
  Serial.printf("%s in connessione al MQTT .." , client_id.c_str());
  client.setServer(MQTT_BROKER, MQTT_PORT);
  client.setCallback(callback);
  while (!client.connected()) {
    if (client.connect(client_id.c_str(), MQTT_USERNAME, MQTT_PASSWORD)) {
      Serial.println("Connesso al broker mqtt");
    } else {
      Serial.print("Fallito con codice di errore: ");
      Serial.println(client.state());
      Serial.println("Ritento");
      delay(2000);
    }
  }
  // pubblicazione di un primo messaggio
  client.publish(INVIA, "Attivo");

  // sottoscrizione 
  client.subscribe(RICEVI);
}

// ciclo di invio messaggi
int n = 0;
void loop() {
  char s[20];
  n = n + 1;
  sprintf(s,"%d",n);
  client.publish(INVIA, s);
  delay(10000);
  client.loop();
}

// funzione di callback
void callback(char *topic, byte *payload, unsigned int length) {
  Serial.print("Arrivato un messaggio nel topic: ");
  Serial.println(topic);
  Serial.print("Messaggio:");
  for (int i = 0; i < length; i++) {
    Serial.print((char) payload[i]);
  }
  Serial.println();
  Serial.println("-----------------------");
}
