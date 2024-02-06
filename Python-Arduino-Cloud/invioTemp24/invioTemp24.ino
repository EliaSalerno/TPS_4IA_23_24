/*
* https://howtomechatronics.com/tutorials/arduino/arduino-wireless-communication-nrf24l01-tutorial/
* https://github.com/nRF24/RF24
*/

#include <RF24.h>
#include <printf.h>
#include <math.h>
RF24 radio(7, 8); // CE, CSN

const byte address[6] = "00001";

double thermistor(int rawADC) {
  // Utilizes the Steinhart-Hart Thermistor Equation:
  // Temperature in Kelvin = 1 / {A + B[ln(R)] + C[ln(R)]^3}
  long resistance;  
  double temperature;  
  double logTemp;
  resistance=((10240000/rawADC) - 10000);  // Resistance = (1024 * BalanceResistor/ADC) - BalanceResistor
  logTemp = log(resistance);               
  temperature = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * logTemp * logTemp ))* logTemp );;
  temperature = temperature - 273.15;  // Convert Kelvin to Celsius   
  return(temperature);
  }
void setup() {
  Serial.begin(9600);
  printf_begin();
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
  radio.printDetails();
}

int temperatura;

void loop() {  
  //trasmette la temperatura
  temperatura=thermistor(analogRead(A7));
  Serial.println(temperatura);
  radio.write(&temperatura, sizeof(temperatura));
  delay(1000);
  
}
