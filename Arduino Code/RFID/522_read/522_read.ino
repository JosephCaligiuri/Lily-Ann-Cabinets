/*
 - Version: 0.5.3
 - Name: 522_read
 - Author: Joseph Caligiuri
 - Description: Arduino Code for using a MFRC522 RFID reader to scad tag blocks for Lily Ann Cabinets invintory
*/

//======================================================//

//Imports 
#include <SPI.h>
#include <MFRC522.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

//======================================================//

//Create MFRC522 (RFID reader)//
#define RST_PIN 9
#define SS_PIN 10
MFRC522 mfrc522(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key;
MFRC522::StatusCode status;

//======================================================//


// 128x32 Adafruit OLED Display (optional mostly used for debuging without serial connection)//
Adafruit_SSD1306 display = Adafruit_SSD1306(128, 32, &Wire);

//======================================================//

// Class for Oled Display//
class WRITE {
  public:

    void printInt(int x) //display int "x"
    {
      display.println(String(x));
      display.display();
    }

    void printStr(String x) // display String "x"
    {
      display.println(x);
      display.display();
    }

    void clear() // clear display
    {
      display.clearDisplay();
      display.setCursor(0, 0);
      display.display();
    }

    void startDisplay(int s) // start display with Text Size "s"
    {

      display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
      display.display();

      display.setTextSize(s);
      display.setTextColor(WHITE);

      display.clearDisplay();

      display.println("waiting for card");

      
    }      

  private:
};

//======================================================//

WRITE D; // call Oled class as "D"

//======================================================//

// Class for RFID reader
class BLOCK {
  public:

  bool valid;  

  void readBlock(int x) // "x" block to be read
  {
    int test = x;
    byte block = test;  //Test 

    if (block < 0 || block > 63) // check if input is valid
    { 
      Serial.println("Invalid block number!");
      D.clear();
      D.printStr("Invalid block number!");
      return;
    }

 
  
  
  // Prepare key - all keys are set to FFFFFFFFFFFFh at chip delivery from the factory.
    for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

    byte len = 18; // set buffer
    byte buffer1[len];
  
  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
  if (!mfrc522.PICC_IsNewCardPresent()) 
  {
    bool valid = false;
    return;
  }
  // Select one of the cards
  if (!mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  
  // checks for authentication with Key
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK) 
  {
    Serial.print("Authentication failed: ");
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  
  // checks to make sure block is read
  status = mfrc522.MIFARE_Read(block, buffer1, &len);
  if (status != MFRC522::STATUS_OK) 
  {
    Serial.print("null");
    D.printStr("Card Read Failed");
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  
  // parses block bytes to a legible string
  String value = "";
  for (uint8_t i = 0; i < 16; i++) 
  {
    value += (char)buffer1[i];
  }
  value.trim();
  
  D.clear();
  Serial.println(value);
  D.printStr(value);
  
  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();
  }


};

//======================================================//

BLOCK B; // call RFID reader as "B"

//======================================================//

// Class for organizing setup loop
class SETUP {

  public:

  void runSetup()
  {
    Serial.begin(9600); // begin Serial com

    SPI.begin(); //int SPI bus
    mfrc522.PCD_Init(); //int RFID Reader

    D.startDisplay(1); // Set Oled display settings       
    D.clear();

    D.printStr("waiting for Card");          
    
  }

};

//======================================================//

SETUP S; // calls Setup class as "S"

//======================================================//

void setup() //Code to be ran on startup
{
  S.runSetup();
}

void loop() //Code to be looped repeatedly after setup()
{
  int b;

  if (Serial.available()){
    String command = Serial.readString();
    if(command == "4"){
      b = 4;
    }
    if(command == "1"){
      b = 1;
    }
    if(command == "2"){
      b = 2;
    }

    B.readBlock(b);
  }

  

}