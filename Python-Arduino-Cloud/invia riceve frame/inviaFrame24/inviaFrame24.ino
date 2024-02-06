#define ID "EP"               // nome attribuito al pacchetto
#define TIPO "S1"             // tipo di pacchetto
#define MITTENTE "S730"       // nome attribuito al sensore
#define DESTINATARIO "P001"   // nome attribuito al Python ricevente
#define WRITINGPIPE "00001"   // pipe di invio 
/*********************************************************************
  struttura del pacchetto di 32 byte - tipo sensore S1
*********************************************************************/
struct pacchettoS1 {
  char id[2];
  char mittente[4];
  char destinatario[4];
  char tipo[2];
  char valoreSensore[4];
  char vuoto[16];
};

struct pacchettoS1 msg;

/*********************************************************************
  RF24
*********************************************************************/
#include <RF24.h>
RF24 radio(7, 8); // CE, CSN

void setup() {
  Serial.begin(9600);

  radio.begin();
  radio.setPALevel(RF24_PA_MIN);
  radio.openWritingPipe((byte *)WRITINGPIPE);
  radio.stopListening();
}

void loop() {
    

  // legge il valore e lo converte in stringa di 4 caratteri
  // con zeri a sinistra
  int valoreLetto = analogRead(A7);
  char valoreLettoStr[10];
  sprintf(valoreLettoStr, "%04d", valoreLetto);

  // riempie il pacchetto
  memcpy(msg.id, ID, sizeof(msg.id));
  memcpy(msg.mittente, MITTENTE, sizeof(msg.mittente));
  memcpy(msg.destinatario, DESTINATARIO, sizeof(msg.destinatario));
  memcpy(msg.tipo, TIPO, sizeof(msg.tipo));
  memcpy(msg.valoreSensore, valoreLettoStr, sizeof(msg.valoreSensore));
  
  // riempie di '.' la parte vuota
  for (int i = 0; i < sizeof(msg.vuoto); ++i)
    *((char *)&msg.vuoto + i) = '.';

  // scrive su seriale a scopo di debugging
  Serial.write((char *)&msg, sizeof(msg));
  Serial.println();

  // invia su RF24
  radio.write((char *)&msg, sizeof(msg));
  delay(5000);
}
