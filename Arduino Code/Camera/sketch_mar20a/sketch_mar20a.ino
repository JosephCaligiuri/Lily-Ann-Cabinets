#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 display = Adafruit_SSD1306(128, 32, &Wire);

byte compteur;

// front MC
#define fenA 10
#define fin1 7
#define fin2 6
#define fenB 3
#define fin3 5
#define fin4 4

bool check;

class WRITE {
  public:

    void printInt(int x){
      int i = x;
      display.println(String(i));
      display.display();    
    }

    void clear(){
      display.clearDisplay();
      display.setCursor(0, 0);
    }

    void printStr(String x){
      String s = x;
      display.println(s);
      display.display();
    }
  private:
};

WRITE D;

// Class for controlling the motors 
class RUN {
 
  public:
  
  // move forward
  void Right(){
    D.clear();
    D.printStr("Right");
    digitalWrite(fin3, HIGH);
    digitalWrite(fin4, LOW);
  }
  void Left(){
    D.clear();
    D.printStr("Left");
    digitalWrite(fin3, LOW);
    digitalWrite(fin4, HIGH);
  }

  void stop(){
    D.clear();
    D.printStr("Stopped");
    digitalWrite(fin3, LOW);
    digitalWrite(fin4, LOW);
  }

  void speed(int x){
    int speed = x;
    analogWrite(fenB, speed);
    analogWrite(fenA, speed);
  }
  

  private:
};




RUN Motor; // motor class

void setup(){

  Motor.stop();

  Serial.begin(9600);

  delay(10000);

  pinMode(fin1, OUTPUT);
  pinMode(fin2, OUTPUT);
  pinMode(fin3, OUTPUT);
  pinMode(fin4, OUTPUT);

  Motor.speed(50);

  Serial.println("OLED intialized");
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C); // Address 0x3C for 128x32

  display.display();
  delay(1000);

  // Clear the buffer.
  D.clear();
  

  // text display tests
  display.setTextSize(2);
  display.setTextColor(WHITE);

  bool check = false;

  D.printStr("init");

  delay(5000);
}

void loop(){
  
    // check for incoming serial data
      
      if (Serial.available()) {  // check for incoming serial data
      

      String Com = Serial.readString();  // read command from serial port
      if (Com == "p"){
        Motor.Left();
        
      } 
      if (Com == "n") {
        Motor.Right();
      }
      if (Com == "c") {
        Motor.stop();
      }
      else{
        Motor.stop();
      }
      }

  

  }  
  


