void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {  // check for incoming serial data
      

      String Com = Serial.readString();
      
      Serial.println(Com);
      if (Com == "p"){
        Serial.println(Com);
        digitalWrite(LED_BUILTIN, LOW);
      } 
      if (Com == "n") {
        Serial.println(Com);
        digitalWrite(LED_BUILTIN, HIGH);
      }

}
}