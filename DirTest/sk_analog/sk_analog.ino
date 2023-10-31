void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int lum=0;
  lum=analogRead(A4);
  Serial.println(lum);
  delay(500);
}
