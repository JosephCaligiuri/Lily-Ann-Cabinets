//See BareMinimum example for a list of library functions

//Includes required to use Roboclaw library
#include <SoftwareSerial.h>
#include "RoboClaw.h"

//See limitations of Arduino SoftwareSerial
SoftwareSerial serial(10,11);	
RoboClaw roboclaw(&serial,10000);
int x;
int speed;
#define address 0x80

void setup() {
  //Open roboclaw serial ports
  Serial.begin(115200);
  roboclaw.begin(38400);
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());

  x = Serial.readString().toInt();
  if(x < 0){
    speed = abs(x);
   roboclaw.BackwardM1(address, speed );
  } 
  else if(x > 0){
   roboclaw.ForwardM1(address, x);
  }else
   roboclaw.ForwardM1(address, 0);

}