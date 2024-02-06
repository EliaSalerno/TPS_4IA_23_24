#define ID "EP"               // nome attribuito al pacchetto
#define TIPO "A1"             // tipo di pacchetto
#define MITTENTE "S730"       // nome attribuito al programma di test
#define DESTINATARIO "P438"   // nome attribuito all'attuatore
#define WRITINGPIPE "55555"   // pipe di invio 
/*********************************************************************
  struttura del pacchetto di 32 byte – tipo A1
*********************************************************************/
struct pacchettoA1 {
  char id[2];
  char mittente[4];
  char destinatario[4];
  char tipo[2];
  char direzione[1];
  char velocita[3];
  char vuoto[16];
};

struct pacchettoA1 msg;
int v = 100;
char d = 'A';
/*********************************************************************
  RF24
*********************************************************************/
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN

void setup() {
  Serial.begin(9600);

  radio.begin();

  radio.setPALevel(RF24_PA_MIN);
  radio.setPayloadSize(32);
  radio.setDataRate(RF24_2MBPS);
  radio.openWritingPipe((byte *)WRITINGPIPE);
  radio.stopListening();
  //pinMode(13, OUTPUT);
  if (radio.isChipConnected())
    Serial.println ("nRF24L01p ok");
  else
    Serial.println ("nRF24L01p non rilevato");

}

void loop() {

  // incrementa il contatore e lo converte in stringa di 3 caratteri
  // con zeri a sinistra
  v = v + 50;
  if (v > 250) {
    v = 100;
    if (d == 'A')
      d = 'I';
    else
      d = 'A';
  }
  char pStr[10];
  sprintf(pStr, "%03d", v);

  // riempie il pacchetto
  memcpy(msg.id, ID, sizeof(msg.id));
  memcpy(msg.mittente, MITTENTE, sizeof(msg.mittente));
  memcpy(msg.destinatario, DESTINATARIO, sizeof(msg.destinatario));
  memcpy(msg.tipo, TIPO, sizeof(msg.tipo));
  memcpy(msg.direzione, &d, sizeof(msg.direzione));
  memcpy(msg.velocita, pStr, sizeof(msg.velocita));

  // riempie di '.' la parte vuota
  for (int i = 0; i < sizeof(msg.vuoto); ++i)
    *((char *)&msg.vuoto + i) = '.';

  // scrive su seriale a scopo di debugging
  Serial.write((char *)&msg, sizeof(msg));

  Serial.println();

  // invia su RF24
  radio.write((char *)&msg, sizeof(msg));
  //digitalWrite(13, HIGH);
  delay(500);
  //digitalWrite(13, LOW);
  delay(5000);
}
