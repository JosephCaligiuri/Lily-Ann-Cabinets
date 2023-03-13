// Title: DriveTrain
//
// Description: Base code for the drive train of 
// the robot for lily ann cabinets (currently specifically for the invintory robot may become universial)
// 
// version: 0.2.0
//
// date: 3-13-2023


// front MC
#define fenA 7
#define fin1 6
#define fin2 5
#define fenB 2
#define fin3 4
#define fin4 3

// back MC
#define benA 13
#define bin1 12
#define bin2 11
#define benB 8
#define bin3 10
#define bin4 9

// Class for controlling the motors 
class RUN {
 
  public:
  
  // move forward
  void forward(){
    digitalWrite(fin1, HIGH);
    digitalWrite(fin2, LOW);

    digitalWrite(fin3, HIGH);
    digitalWrite(fin4, LOW);

    digitalWrite(bin1, HIGH);
    digitalWrite(bin2, LOW);

    digitalWrite(bin3, HIGH);
    digitalWrite(bin4, LOW);


  }

  //move back
  void back() {
    digitalWrite(fin1, LOW);
    digitalWrite(fin2, HIGH);

    digitalWrite(fin3, LOW);
    digitalWrite(fin4, HIGH);

    digitalWrite(bin1, LOW);
    digitalWrite(bin2, HIGH);

    digitalWrite(bin3, LOW);
    digitalWrite(bin4, HIGH);
  }

  //stop motion
  void stop() {
    digitalWrite(fin1, LOW);
    digitalWrite(fin2, LOW);

    digitalWrite(fin3, LOW);
    digitalWrite(fin4, LOW);

    digitalWrite(bin1, LOW);
    digitalWrite(bin2, LOW);

    digitalWrite(bin3, LOW);
    digitalWrite(bin4, LOW);
  }

  void left() {
    digitalWrite(fin1, LOW);
    digitalWrite(fin2, HIGH);

    digitalWrite(fin3, HIGH);
    digitalWrite(fin4, LOW);

    digitalWrite(bin1, HIGH);
    digitalWrite(bin2, LOW);

    digitalWrite(bin3, LOW);
    digitalWrite(bin4, HIGH);

    
  }

  void right() {
    digitalWrite(fin1, HIGH);
    digitalWrite(fin2, LOW);

    digitalWrite(fin3, LOW);
    digitalWrite(fin4, HIGH);

    digitalWrite(bin1, LOW);
    digitalWrite(bin2, HIGH);

    digitalWrite(bin3, HIGH);
    digitalWrite(bin4, LOW);

  }
  //turns motor off
  private:
};


RUN Motor; // motor class

void setup(){

  Motor.stop();

  Serial.begin(9600);

  pinMode(fin1, OUTPUT);
  pinMode(fin2, OUTPUT);
  pinMode(fin3, OUTPUT);
  pinMode(fin4, OUTPUT);

  pinMode(bin1, OUTPUT);
  pinMode(bin2, OUTPUT);
  pinMode(bin3, OUTPUT);
  pinMode(bin4, OUTPUT);

  
}

void loop(){
  
   if (Serial.available()) {  // check for incoming serial data
      

      String command = Serial.readString();  // read command from serial port
      if (command == "move_f") {  // turn on LED
         Serial.println("moving forward");
         Motor.forward();
      } else if (command == "stop") {  // turn off LED
         Motor.stop();
         Serial.println("stopped");
      } else if (command == "move_b") {  // read and send A0 analog value
         Motor.back();
      } else if (command == "move_l") {
         Motor.left();
      } else if (command == "move_r") {
         Motor.right();
      }

  

  }  
  
}

