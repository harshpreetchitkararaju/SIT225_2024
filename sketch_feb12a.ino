#include <ArduinoIoTCloud.h>
#include <Arduino_ConnectionHandler.h>

// Define your Wi-Fi credentials
const char SSID[] = "YOUR_WIFI_SSID";
const char PASS[] = "YOUR_WIFI_PASSWORD";

// Define your sensor variables
float temperature;
float humidity;

void initSensor() {
  // Initialize your sensor here
  // Example for DHT22:
  // dht.begin();
}

void readSensorData() {
  // Read sensor data and update Cloud variables
  // Example for DHT22:
  // temperature = dht.readTemperature();
  // humidity = dht.readHumidity();
}

void setup() {
  Serial.begin(9600);
  initSensor();

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  ArduinoCloud.addProperty(temperature, READ, ON_CHANGE, NULL);
  ArduinoCloud.addProperty(humidity, READ, ON_CHANGE, NULL);
}

void loop() {
  ArduinoCloud.update();
  readSensorData();
  delay(1000); // Adjust delay based on your sampling rate
}