#include <SoftwareSerial.h>
#include "WiFiEsp.h"
#include <PubSubClient.h>
SoftwareSerial ESP8266(10, 11);
// WiFi
const char *ssid = "emilio";
const char *password = "mafeking";

// MQTT Broker
const char *mqtt_broker = "192.168.43.48";
//const char *mqtt_broker = "172.17.5.14";
const char *invia = "mytopic/invia";
const char *ricevi = "mytopic/ricevi";
const char *mqtt_username = "";
const char *mqtt_password = "";
const int mqtt_port = 1883;

WiFiEspClient espClient;
PubSubClient client(espClient);

void setup() {

  Serial.begin(115200);
  ESP8266.begin(9600);
  WiFi.init(&ESP8266);
  Serial.println("Inizio");

  Serial.print("Connecting to WiFi..");
  int status = WiFi.begin(ssid, password);
  if (status == WL_CONNECTED) {
    Serial.println();
    Serial.println("Connected to WiFi network.");
  } else {
    WiFi.disconnect(); // remove the WiFi connection
    Serial.println();
    Serial.println("Connection to WiFi network failed.");
  }
  Serial.println("");
  Serial.println("Connected to the WiFi network");

  String client_id = "esp32-client-" ;//+ String(WiFi.macAddress());
  //Serial.printf("%s connecting to MQTT broker .." , client_id.c_str());
  client.setServer(mqtt_broker, mqtt_port);
  client.setCallback(callback);
  while (!client.connected()) {
    if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
      Serial.println("mqtt broker connected");
    } else {
      Serial.print("failed with state ");
      Serial.println(client.state());
      Serial.println("retrying");
      delay(2000);
    }
  }
  // publish and subscribe
  client.publish(invia, "Attivo");

  client.subscribe(ricevi);
}

void callback(char *topic, byte *payload, unsigned int length) {
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char) payload[i]);
  }
  Serial.println();
  Serial.println("-----------------------");
}
int n = 0;
void loop() {
  char s[20];
  n = n + 1;
  sprintf(s,"%d",n);
  client.publish(invia, s);
  delay(5000);
  client.loop();
}
