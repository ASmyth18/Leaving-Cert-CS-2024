#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11
#define PIRPIN 3
#define LEDPIN 4
#define BUZZERPIN 5

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(PIRPIN, INPUT);
  pinMode(LEDPIN, OUTPUT);
  pinMode(BUZZERPIN, OUTPUT);
}

void loop() {
  // Read temperature and humidity
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Read motion sensor
  bool motionDetected = digitalRead(PIRPIN);

  // Print sensor readings
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C, Humidity: ");
  Serial.print(humidity);
  Serial.println("%");

  // Control digital outputs based on sensor readings
  if (motionDetected) {
    digitalWrite(LEDPIN, HIGH);
    tone(BUZZERPIN, 1000, 500);
    Serial.println("Motion detected!");
  } else {
    digitalWrite(LEDPIN, LOW);
    noTone(BUZZERPIN);
  }

  delay(1000);
}