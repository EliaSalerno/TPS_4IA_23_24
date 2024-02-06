/*
* https://howtomechatronics.com/tutorials/arduino/arduino-wireless-communication-nrf24l01-tutorial/
* https://github.com/nRF24/RF24
*/

#include <SPI.h>
//#include <nRF24L01.h>
#include <RF24.h>
#include <printf.h>

RF24 radio(7, 8); // CE, CSN

const byte address[6] = "00002";

void setup() {
  Serial.begin(9600);
  printf_begin();
  
  radio.begin();
  
  radio.setPALevel(RF24_PA_MIN);
  //radio.enableDynamicPayloads();
  radio.setAutoAck(true);
  //radio.setDataRate(RF24_250KBPS);
  radio.openReadingPipe(0, address);
  radio.printDetails();
  radio.startListening();
  delay(2000);
  Serial.println("pronto...");
}

void loop() {
  if (radio.available()) {
    char stato = '0';
    radio.read(&stato, sizeof(stato));
    
    Serial.println(stato);
  }
}
