
// Title: DriveTrain
//
// Description: Base code for the drive train of 
// the robot for lily ann cabinets (currently specifically for the invintory robot may become universial)
// 
// version: 0.1.5
//
// date: 3-8-2023
//





#include <AccelStepper.h>

#define MotorInterfaceType 8

#define frontLeftPin1 22
#define frontLeftPin2 23
#define frontLeftPin3 24
#define frontLeftPin4 25
#define frontRightPin1 26
#define frontRightPin2 27
#define frontRightPin3 28
#define frontRightPin4 29
#define backRightPin1 30
#define backRightPin2 31
#define backRightPin3 32
#define backRightPin4 33
#define backLeftPin1 34
#define backLeftPin2 35
#define backLeftPin3 36
#define backLeftPin4 37

int mSpeed = 1000;

AccelStepper frontR = AccelStepper(MotorInterfaceType, frontRightPin1, frontRightPin3, frontRightPin2, frontRightPin4);
AccelStepper frontL = AccelStepper(MotorInterfaceType, frontLeftPin1, frontLeftPin3, frontLeftPin2, frontLeftPin4);

AccelStepper backR = AccelStepper(MotorInterfaceType, backRightPin1, backRightPin3, backRightPin2, backRightPin4);
AccelStepper backL = AccelStepper(MotorInterfaceType, backLeftPin1, backLeftPin3, backLeftPin2, backLeftPin4);

String testc = "led_on";

class TEST {
  public:

  void set(){
    backR.runSpeed();
    backL.runSpeed();
    frontR.runSpeed();
    frontL.runSpeed();

  }  
  private:
};

TEST Test;


// Class for controlling the motors 
class RUN {
 
  public:
  
  // move forward
  void forward(){

    backR.setSpeed(mSpeed);
    backL.setSpeed(-mSpeed);
    frontR.setSpeed(mSpeed);
    frontL.setSpeed(-mSpeed);
    
    Test.set(); //(runSpeed)
  }

  //move back
  void back() {

    backR.setSpeed(-mSpeed);
    backL.setSpeed(mSpeed);
    frontR.setSpeed(-mSpeed);
    frontL.setSpeed(mSpeed);

    Test.set();
  }

  //stop motion
  void stop() {

    backR.setSpeed(0);
    backL.setSpeed(0);
    frontR.setSpeed(0);
    frontL.setSpeed(0);
    
    Test.set();
  }

  void strafeLeft() {
    
  }

  void strafeRight() {

  }
  //turns motor off
  private:
};


RUN Motor; // motor class

void setup(){

  Serial.begin(9600);


  backR.setMaxSpeed(1700);
  backL.setMaxSpeed(1700);
  frontR.setMaxSpeed(1700);
  frontL.setMaxSpeed(1700);

  
}

void loop(){
  

  if (Serial.available()) {  // check for incoming serial data
      Serial.println("link found");

      String command = Serial.readString();  // read command from serial port
      if (testc == "led_on") {  // turn on LED
         Serial.println("moving forward");
         Motor.forward();
      } else if (command == "led_off") {  // turn off LED
         Motor.back();
         Serial.println("stopped");
      } else if (command == "read_a0") {  // read and send A0 analog value
         Serial.println(analogRead(A0));
      }
  

  }
}

