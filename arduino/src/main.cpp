#include <Arduino.h>

int led[] = {13,12,11,10,9,8,7,6,5,4,3,2,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41};


void setled(){
  for (int i = 0; i < 40; i++){
    pinMode(i, OUTPUT);
  }
}


void setup() {
  Serial.begin(9600);
  setled();
}


int led_on(int l){
  digitalWrite(led[l-1], HIGH);
  return 0;
}


void turnalloff(){
  for (int i = 0; i <= 39; i++){
    digitalWrite(led[i], LOW);
  }
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print("You sent me: ");
    Serial.println(data);
    if (data == "100"){
      turnalloff();
    }else{
      int num = data.toInt();
      led_on(num);
    }
  }
}