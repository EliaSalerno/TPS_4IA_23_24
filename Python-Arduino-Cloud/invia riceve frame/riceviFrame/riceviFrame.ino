#define MIO_ID "EP"               // nome attribuito al pacchetto
#define MIO_TIPO "S1"             // tipo di pacchetto
#define MIO_INDIRIZZO "A328"      // nome attribuito all'attuatore
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

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available() >= sizeof(msg)) {                      // controlla che l'intero pacchetto
    Serial.readBytes((byte *) &msg, sizeof(msg));               // sia disponibile e lo legge
    //Serial.println((char *)&msg);
    if (strncmp(msg.id, MIO_ID, sizeof(msg.id)) == 0) {         // pacchetto presumibilmente corretto
      if (strncmp(msg.destinatario, MIO_INDIRIZZO, sizeof(msg.destinatario)) == 0) {   // è per me?
        Serial.print("Ricevuto ");
        Serial.write(msg.direzione, sizeof(msg.direzione));
        Serial.print(":");
        Serial.write(msg.velocita, sizeof(msg.velocita));
        Serial.println();
        digitalWrite(13, HIGH);
        delay(100);
        digitalWrite(13, LOW);

      }
    }
  }
}
