#include <LAC.h>


LAC lac;

void setup() {
  // do setup
}

void loop() {

  lac.clear();
  lac.printInt(42);
  
  delay(1000);

  lac.clear();
  lac.printStr("Hello, world!");

  delay(1000);
  // do other things
}