/*
    Version: 0.0.2
    Created: March 23, 2023
    By: Joseph Caligiuri
    Description: For Lily Ann Cabinets for intergrating 128x32 oled displays
*/

#include "MyLibrary.h"

MyLibrary::MyLibrary() : _display(128, 32, &Wire) {}

void MyLibrary::printInt(int x) {
  int i = x;
  _display.println(String(i));
  _display.display();
}

void MyLibrary::printStr(String x) {
  String s = x;
  _display.println(s);
  _display.display();
}

void MyLibrary::clear() {
  _display.clearDisplay();
  _display.setCursor(0, 0);
}