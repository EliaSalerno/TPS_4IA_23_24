#define PACKETID "EP"
#define TIPO 0x01
#define MITTENTE 0x00000001
#define DESTINATARIO 0x00000002
/*********************************************************************
  struttura del pacchetto di 32 byte 
  il tipo specifica la struttura della parte dati
*********************************************************************/
struct packet {
  char packetID[2];
  unsigned long mittente;
  unsigned long destinatario;
  byte tipo;
  byte dati[21];
};
/*********************************************************************
  struttura del tipo 1: dati inviati dal sensore 
*********************************************************************/
struct dati1 {
  unsigned int valoreSensore;
  byte vuoto[19];
};
/*********************************************************************
  pacchetto
  
*********************************************************************/
struct packet myPacket;
struct dati1 myDati1;
void setup() {
  Serial.begin(9600);
}

void loop() {

  // legge il valore 
  unsigned int valoreSensore = analogRead(A7);

  // riempie la parte iniziale del pacchetto
  memcpy(myPacket.packetID, PACKETID, sizeof(myPacket.packetID));
  myPacket.tipo=TIPO;
  myPacket.mittente=MITTENTE;
  myPacket.destinatario=DESTINATARIO;
  
  // riempie la parte dati del pacchetto
  myDati1.valoreSensore=valoreSensore;
  for (int i = 0; i < sizeof(myDati1.vuoto); ++i)
    myDati1.vuoto[i] = 0;
  memcpy(myPacket.dati,(void *)&myDati1,sizeof(myDati1));

  Serial.write((byte *)&myPacket, sizeof(myPacket));
  //printBuffer((byte *)&myPacket,sizeof(myPacket));
  delay(5000);
}
void printBuffer(byte buffer[], int len) {
  for (int i = 0; i < len; i++) {
    Serial.print(buffer[i] < 16 ? "0" : "");
    Serial.print(buffer[i], HEX);
    Serial.print(" ");
  }
  Serial.println(" ");
}
