// Motor control pins
#include <Encoder.h>
#include "max6675.h"

#define ENA 4   // PWM control for motor A
#define IN1 2   // Motor A direction control
#define IN2 3  // Motor A direction control
int thermoSO1 = 8;
int thermoCS1 = 9;
int thermoSCK1 =10;
MAX6675 thermocouple1(thermoSCK1, thermoCS1, thermoSO1);
// Encoder pins
#define encoderPinA 6
#define encoderPinB 5
Encoder myEncoder(6, 5);
const unsigned long timePeriod = 1000;
unsigned long startTime;
int dacPin1 = 11; // Use an analog output pin
int dacPin2 = 12; // Use an analog output pin

// Variables
char op = '0';
//char vel[]={' ',' ',' '};
int v=250;
void setup() {
   startTime = millis();
  // Motor setup
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  Serial.begin(9600);
  // Encoder setup
  pinMode(encoderPinA, INPUT);
  pinMode(encoderPinB, INPUT);
  
}
long oldPosition = 0;
void loop() {
   float tempC1 = thermocouple1.readCelsius();
 
  // Convert temperature to a voltage (adjust as needed)
  float pulse1 = map(tempC1, 0, 100, 0, 255); // Assuming a 0-100°C range
 
  
  // Output the voltage to the DAC
analogWrite(dacPin1, pulse1);


  unsigned long now = millis();
  long newPosition = myEncoder.read();

if ( now - startTime >= timePeriod ) {
    // time to calculate average encoder speed
    float speed = (newPosition - oldPosition) / (float)( now - startTime );// or time period which is 1000ms

    Serial.println( speed, 4 );
    startTime = now;
    oldPosition = newPosition;

}
}
void serialEvent(){
  delay(20);
  op = Serial.read();
  
  while(Serial.available()>0){Serial.read();}
    
    if(op=='1'){
        digitalWrite(IN1,HIGH);
        digitalWrite(IN2,LOW);
        analogWrite(ENA,v);
        
  
    }
      else{
        analogWrite(ENA,0);
    
      }
    
}

  
 
