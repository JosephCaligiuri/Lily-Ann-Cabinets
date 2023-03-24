/*
    Version: 0.0.2
    Created: March 23, 2023
    By: Joseph Caligiuri
    Description: For Lily Ann Cabinets for intergrating 128x32 oled displays
*/



#ifndef MyLibrary_h
#define MyLibrary_h

#include "Arduino.h"
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

class MyLibrary {
  public:
    MyLibrary();
    void printInt(int x);
    void printStr(String x);
    void clear();
  private:
    Adafruit_SSD1306 _display;
};

#endif