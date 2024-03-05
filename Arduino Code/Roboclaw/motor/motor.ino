//See BareMinimum example for a list of library functions

//Includes required to use Roboclaw library
#include <SoftwareSerial.h>
#include "RoboClaw.h"

//See limitations of Arduino SoftwareSerial
SoftwareSerial serial(10,11);	
RoboClaw roboclaw(&serial,10000);

int x;
int speed;


#define addressfl 0x80
#define addressfr 0x81

#define addressbl 0x82
#define addressbr 0x83

#define speed 20

class RUN{

  public:

  int s;

void forward(int s) {
  roboclaw.BackwardM1(addressfl, s);
  roboclaw.ForwardM1(addressfr, s);

  roboclaw.BackwardM1(addressbl, s);
  roboclaw.ForwardM1(addressbr, s);
}

void backward(int s) {
  roboclaw.ForwardM1(addressfl, s);
  roboclaw.BackwardM1(addressfr, s);

  roboclaw.ForwardM1(addressbl, s);
  roboclaw.BackwardM1(addressbr, s);
}

void stop(int s){
  roboclaw.ForwardM1(addressfl, 0);
  roboclaw.ForwardM1(addressfr, 0);

  roboclaw.ForwardM1(addressbl, 0);
  roboclaw.ForwardM1(addressbr, 0);
}

void left(int s){
  roboclaw.BackwardM1(addressfl, s);
  roboclaw.BackwardM1(addressfr, s);

  roboclaw.ForwardM1(addressbl, s);
  roboclaw.ForwardM1(addressbr, s);
}

void right(int s){
  roboclaw.ForwardM1(addressfl, s);
  roboclaw.ForwardM1(addressfr, s);

  roboclaw.BackwardM1(addressbl, s);
  roboclaw.BackwardM1(addressbr, s);
}

void drive(int s){
  roboclaw.ForwardBackwardM1(addressfl, s);
  roboclaw.ForwardBackwardM1(addressfr, s);

  roboclaw.ForwardBackwardM1(addressbl, s);
  roboclaw.ForwardBackwardM1(addressbr, s);
}

private:

};

RUN Motor;

void setup() {
  //Open roboclaw serial ports

  Motor.stop(0);

  Serial.begin(115200);
  roboclaw.begin(38400);
  Serial.setTimeout(1);

}

void loop() {
 
 Motor.drive(0);
 delay(2000);
 Motor.drive(64);
 delay(2000);
 Motor.drive(127);
 delay(2000);
 Motor.drive(64);
 delay(2000);


 }