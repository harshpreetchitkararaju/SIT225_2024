#include <Arduino_LSM6DS3.h>

void setup() {
    Serial.begin(9600);
    while (!Serial);

    if (!IMU.begin()) {
        Serial.println("Failed to initialize IMU!");
        while (1);
    }
}

void loop() {
    float x, y, z;

    if (IMU.accelerationAvailable()) {
        IMU.readAcceleration(x, y, z);
        Serial.print(millis());
        Serial.print(",");
        Serial.print(x, 6);
        Serial.print(",");
        Serial.print(y, 6);
        Serial.print(",");
        Serial.println(z, 6);
    }

    delay(1000);
}
