#include <Adafruit_AHTX0.h>
 Adafruit_AHTX0 aht;

//Constants
const int siolMoistureS = A0; //Soilmoisture sensor at analog pin A0
const int pResistor = A1; // Photoresistor at Arduino analog pin A1
const int ledPin = 9;       // Led pin at Arduino pin 9


const int nightLight=50;      //threshold for sunlight after sunset
const int waterValue = 265;  //value from sensor in water
const int airValue = 627;   //value from a dry sensor in the air
const int moisturizedSoil = 230;  // threshold for moisturized soil
const int drySoil = 470;           //threshold for dry soil

const int drySoilPercent = map(drySoil, airValue, waterValue, 0, 100);
const int moisturizedSoilPercent = map(moisturizedSoil, airValue, waterValue, 0, 100);

//Variables
int sunlightValue;          // Store value from photoresistor 
int soilMoistureValue = 0;  // Store value from siolMoisture sensor
int soilMoisturePercent=0;  //soil moisture converted to percentages

void setup() {
//  Serial.begin(38400); // open serial port   
  pinMode(ledPin, OUTPUT);  // Set lepPin - 9 pin as an output
  pinMode(pResistor, INPUT);// Set pResistor - A1 pin as an input 
  Serial.begin(9600); // open the serial port at 9600 bps:

//  if (! aht.begin()) {
//    Serial.println("Could not find AHT? Check wiring");
//    while (1) delay(10);
//    }
//    Serial.println("AHT10 or AHT20 found"); 
//  
}
void loop() {
  soilMoistureValue = analogRead(siolMoistureS);  // read soilMoisture value 
  soilMoisturePercent = map(soilMoistureValue, airValue, waterValue, 0, 100);
  sunlightValue = analogRead(pResistor);          // read light value from photoresistor
  Serial.print("light: ");
  Serial.println(sunlightValue);
  Serial.print("soil_moisture: ");
  Serial.println(soilMoisturePercent );
   
  delay(1500);
  
//  sensors_event_t humidity, temp;
//  aht.getEvent(&humidity, &temp);// populate temp and humidity objects with fresh data
  
//  Serial.print("Temperature: "); 
//  Serial.print(temp.temperature); 
//  Serial.println(" degrees C");
//  Serial.print("Humidity: "); 
//  Serial.print(humidity.relative_humidity); 
//  Serial.println("% rH");
  

  if (sunlightValue > nightLight){
      digitalWrite(ledPin, LOW);  //Turn led off
  }
  else{
    if(soilMoisturePercent < drySoilPercent){
      digitalWrite(ledPin, HIGH); //Turn led on
    }
    else if (soilMoisturePercent > moisturizedSoilPercent){
      digitalWrite(ledPin, LOW);  //Turn led off
    }
  }
}
