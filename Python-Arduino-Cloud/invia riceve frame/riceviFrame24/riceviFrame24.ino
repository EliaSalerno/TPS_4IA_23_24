#define MIO_ID "AB"               // nome attribuito al pacchetto
#define MIO_TIPO "S1"             // tipo di pacchetto
#define MIO_INDIRIZZO "A328"      // nome attribuito all'attuatore
#define READINGPIPE "00001"       // pipe di ricezione 
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

/*********************************************************************
  RF24
*********************************************************************/
#include <RF24.h>
RF24 radio(7, 8); // CE, CSN

void setup() {
  Serial.begin(9600);

  radio.begin();
  radio.setPALevel(RF24_PA_MIN);
  radio.openReadingPipe(0, (byte *) READINGPIPE);
  radio.startListening();
}

void loop() {
  if (radio.available() ) {                       // controlla che ci siano dati
    radio.read((char *) &msg, sizeof(msg));       // legge il pacchetto
    Serial.println((char *)&msg);
    if (strncmp(msg.id, MIO_ID, sizeof(msg.id)) == 0) {         // pacchetto presumibilmente corretto
      if (strncmp(msg.destinatario, MIO_INDIRIZZO, sizeof(msg.destinatario)) == 0) {   // è per me?
        Serial.print("Ricevuto ");
        Serial.write(msg.direzione, sizeof(msg.direzione));
        Serial.print(":");
        Serial.write(msg.velocita, sizeof(msg.velocita));
        Serial.println();
        
      }
    }
  }
}
