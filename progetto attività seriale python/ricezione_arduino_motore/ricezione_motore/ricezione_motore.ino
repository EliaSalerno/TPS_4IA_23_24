#define ID "aa"
#define DESTINATARIO "0000"

struct pacchettoA1
{
  char id[2];
  char mittente[4];
  char destinatario[4];
  char tipo[2];
  char direzione[1];
  char velocita[3];
  char vuoto[16];
};

void setup()
{
  Serial.begin(9600);
  pinMode(9, OUTPUT);
  pinMode(3, OUTPUT);
}

void loop()
{
  struct pacchettoA1 msg;
  if (Serial.available())
  {
    Serial.readBytes((byte*) &msg, sizeof(msg));
    int controlloId = memcmp(ID, msg.id, 2);
    int controlloDest = memcmp(DESTINATARIO, msg.destinatario, 4);
    char vel[4];
    if (controlloId == 0 && controlloDest == 0)
    {
      memcpy(vel,msg.velocita,sizeof(msg.velocita));
      vel[3] = '\0';
      int velocita = atoi(vel);
      if (memcmp("D",msg.direzione, 1) == 0)
      {
        digitalWrite(3, LOW);
        digitalWrite(9, HIGH);
        analogWrite(5, velocita);
      }

      if (memcmp("S",msg.direzione, 1) == 0)
      {
        digitalWrite(3, HIGH);
        digitalWrite(9, LOW);
        analogWrite(5, velocita);
      }
      if (memcmp("F",msg.direzione, 1) == 0)
      {
        digitalWrite(3, LOW);
        digitalWrite(9, LOW);
        analogWrite(5, velocita);
      }
    }
  }
}