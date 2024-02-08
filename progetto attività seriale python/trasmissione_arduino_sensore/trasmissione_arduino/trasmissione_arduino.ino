struct pacchettoS1
{
 char id[2];
 char mittente[4];
 char destinatario[4];
 char tipo[2];
 char valoreSensore[4];
 char vuoto[16];
};

void setup() {
 Serial.begin(9600);
}

void loop() {  
 #define CARATTEREVUOTO "----------------"
 #define ID "aa"
 #define MITTENTE "0001"
 #define DESTINATARIO "0000"
 #define TIPO "S1"
 
 int x = analogRead(A0);
 char dato[5];
 sprintf(dato, "%04d", x);
 struct pacchettoS1 msg;
 memcpy(msg.vuoto, CARATTEREVUOTO, sizeof(msg.vuoto));
 memcpy(msg.valoreSensore, dato, sizeof(msg.valoreSensore));
 memcpy(msg.id, ID, sizeof(msg.id));
 memcpy(msg.mittente, MITTENTE, sizeof(msg.mittente));
 memcpy(msg.destinatario, DESTINATARIO,sizeof(msg.destinatario));
 memcpy(msg.tipo, TIPO, sizeof(msg.tipo));
 Serial.write((byte *)&msg, sizeof(msg));
 delay(1000);
} 
