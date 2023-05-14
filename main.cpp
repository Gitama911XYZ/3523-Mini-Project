#include <Servo.h>
#include <string.h>
#include <Arduino.h>
Servo myServo;
int servoPin = 9;
String servoPos;
int pos;
int green=2;
int red=4;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
myServo.attach(servoPin);
myServo.write(90);
pinMode(green,OUTPUT);
pinMode(red,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
while (Serial.available() == 0){
}
  servoPos = Serial.readStringUntil('\r');
  pos = servoPos.toInt();
  myServo.write(pos);
  if(pos>80)
  {
    digitalWrite(red,HIGH);
    digitalWrite(green,LOW);

  }
  else{
    digitalWrite(red,LOW);
    digitalWrite(green, HIGH);
  }
  delay(15);
}