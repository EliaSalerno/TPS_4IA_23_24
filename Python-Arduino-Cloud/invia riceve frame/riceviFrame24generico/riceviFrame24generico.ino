#define READINGPIPE "00001"       // pipe di ricezione 
/*********************************************************************
  struttura del pacchetto di 32 byte
*********************************************************************/
struct pacchetto {
  char id[2];
  char mittente[4];
  char destinatario[4];
  char tipo[2];
  char dati[20];
};

struct pacchetto msg;

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
  radio.openReadingPipe(0, (byte *) READINGPIPE);
  radio.startListening();

  //pinMode(13,OUTPUT);

  if (radio.isChipConnected())
    Serial.println ("nRF24L01p presente");
  else
    Serial.println ("nRF24L01p non rilevato");
}

void loop() {
  if (radio.available() ) {                       // controlla che ci siano dati
    radio.read((char *) &msg, sizeof(msg));       // legge il pacchetto
    char s[33];
    memcpy(s, (char *)&msg, sizeof(msg));
    s[32] = 0;
    Serial.println(s);
    //digitalWrite(13,HIGH);
    delay(300);
    //digitalWrite(13,LOW);
  }
}
