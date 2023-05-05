int emg = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {

  emg = analogRead(2);
  Serial.println(emg);

}
