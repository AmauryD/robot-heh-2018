#include <SPI.h>
#include <RFID.h>

/*
    Module RFID -> Arduino
    SDA -> Pin 10
    SCK -> Pin 13
    MOSI -> Pin 11
    MISO -> Pin 12
    GND -> GND
    RST -> Pin 9
    VCC -> 3.3V
*/

RFID RFID(10,9);

void setup()
{
  Serial.begin(9600);
  SPI.begin();
  RFID.init();  
}

void loop()
{
    if (RFID.isCard()) {  
        Serial.print("1");
        RFID.halt();
    }else{
        Serial.print("0");
    }
    delay(200);    
}
