#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// Rotary Encoder Inputs

#define CLK 9
#define DT 8
#define SW 7


Adafruit_SSD1306 display = Adafruit_SSD1306(128, 32, &Wire);

int counter = 0;
int currentStateCLK;
int lastStateCLK;
String currentDir ="";
unsigned long lastButtonPress = 0;
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

void setup() {
        
	// Set encoder pins as inputs
	pinMode(CLK,INPUT);
	pinMode(DT,INPUT);
	pinMode(SW, INPUT_PULLUP);

	// Setup Serial Monitor
	Serial.begin(9600);
  Serial.println("OLED intialized");
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C); // Address 0x3C for 128x32

  display.display();
  delay(1000);

  // Clear the buffer.
  D.clear();

  display.setTextSize(2);
  display.setTextColor(WHITE);

	// Read the initial state of CLK
	lastStateCLK = digitalRead(CLK);
}

void loop() {
        
	// Read the current state of CLK
	currentStateCLK = digitalRead(CLK);

	// If last and current state of CLK are different, then pulse occurred
	// React to only 1 state change to avoid double count
	if (currentStateCLK != lastStateCLK  && currentStateCLK == 1){

		// If the DT state is different than the CLK state then
		// the encoder is rotating CCW so decrement
		if (digitalRead(DT) != currentStateCLK) {
			counter --;
			currentDir ="CCW";
		} else {
			// Encoder is rotating CW so increment
			counter ++;
			currentDir ="CW";
		}

    D.clear();

		Serial.print("Direction: ");
		Serial.print(currentDir);
		Serial.print(" | Counter: ");
		Serial.println(counter);

    D.printStr(String(counter) + "mm");
	}

	// Remember last CLK state
	lastStateCLK = currentStateCLK;

	// Read the button state
	int btnState = digitalRead(SW);

	//If we detect LOW signal, button is pressed
	if (btnState == LOW) {
		//if 50ms have passed since last LOW pulse, it means that the
		//button has been pressed, released and pressed again
		if (millis() - lastButtonPress > 50) {
			Serial.println("Button pressed!");
      counter = 0;
      ;
      
		}

		// Remember last button press event
		lastButtonPress = millis();
	}

  if (counter <= 0) {
    D.clear();
    D.printStr("None");
  }

	// Put in a slight delay to help debounce the reading
	delay(1);
}