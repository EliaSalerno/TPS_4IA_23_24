#include <SoftwareSerial.h>

SoftwareSerial ESP8266(10, 11);  //RX,TX


//  Connect GND from the Arduino to GND on the ESP8266
//  Pull ESP8266 CH_PD HIGH

// When a command is entered in to the serial monitor on the computer
// the Arduino will relay it to the ESP8266


void setup()
{

  Serial.begin(9600);     
  ESP8266.begin(9600);
  //AT+UART=9600,8,1,0,0

  Serial.println("");
  Serial.println("Remember to to set Both NL & CR in the serial monitor.");
  Serial.println("Ready");
  Serial.println("");
}

void loop()
{
  // listen for communication from the ESP8266 and then write it to the serial monitor
  if ( ESP8266.available() )   {
    Serial.write( ESP8266.read() );
  }

  // listen for user input and send it to the ESP8266
  if ( Serial.available() )       {
    ESP8266.write( Serial.read() );
  }
}
