#include <dht11.h>
#define DHT1PIN 2
void setup() {
  Serial.begin(9600);

}
 void loop() {
  Serial.println();
  int chk = DHT11.read(DHT11PIN);
  Serial.print("Humidity (%):");
  Serial.println((float) DHT11.humidity, 2 );
  Serial.print("Temperature (c):");
  Serial.println((float) DHT11.temperature, 2);
  delay(2000);
  
 }