#define ID "EP"               // nome attribuito al pacchetto
#define TIPO "S1"             // tipo di pacchetto
#define MITTENTE "S730"       // nome attribuito al sensore
#define DESTINATARIO "P001"   // nome attribuito al Python ricevente
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

void setup() {
  Serial.begin(9600);
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
    
  // scrive su seriale
  Serial.write((byte *)&msg, sizeof(msg));
  delay(5000);
}
