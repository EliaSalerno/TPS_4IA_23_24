const unsigned int MAX_LMSG=1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(1200);
}

void loop() {
  // put your main code here, to run repeatedly:
  char tmsg=0;
  unsigned int val=0;
  static unsigned int MSG_POS=0;
  static char msg[MAX_LMSG+1];
  while(Serial.available()>0){
    tmsg=Serial.read();
    if(tmsg!='\n' && MSG_POS<MAX_LMSG){
      msg[MSG_POS++]=tmsg;
    }
    else
    {
      msg[MSG_POS]='\0';
      MSG_POS=0;
    }
  }
  val=atoi(msg);
  Serial.println(val);
  delay(1000);
}
