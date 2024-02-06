void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

int cont;
void loop() { 
  char comando; 
  comando =Serial.read();
  if (comando=='0')
  {
    digitalWrite(13,LOW);
    Serial.println("LOW");
  }
  if (comando=='1')
    {
    digitalWrite(13,HIGH);
    Serial.println("HIGH");
  }
  
  Serial.println(cont);
  ++cont;
  delay(1000);
}
