#include <WiFi.h>
#include <WiFiUdp.h>

// Define the pins for the LEDs
#define GraspPin 22
#define ReleasePin 23

const char* ssid = "Omar Saad's Laptop";
const char* password = "bciOmarSbme";
const int local_port = 55000;

WiFiUDP udp;

void setup() {

  // Set the Relay pins as outputs
  pinMode(GraspPin, OUTPUT);
  digitalWrite(GraspPin, HIGH);  //Grasping OFF

  pinMode(ReleasePin, OUTPUT);
  digitalWrite(ReleasePin, HIGH);  //Releasing OFF


  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.println("My IP:");
  Serial.println(WiFi.localIP());

  // Set up UDP
  udp.begin(local_port);
  Serial.printf("UDP server started on port %d\n", local_port);
}

void loop() {
  // Check for data from the sender ESP323
  int packetSize = udp.parsePacket();
  if (packetSize) {
    // Reserve buffer to read the packet
    char packetBuffer[255];
    int len = udp.read(packetBuffer, sizeof(packetBuffer));

    // Check for errors
    if (len > 0) {
      packetBuffer[len] = '\0';  // Null-terminate the string
      Serial.printf("Received data: %s\n", packetBuffer);

      Serial.println(packetBuffer[0]);

      // Serial.println(packetBuffer[1]);

      if (packetBuffer[0] == '1') {
        Serial.println("Stop");
        digitalWrite(GraspPin, HIGH);    //Grasping OFF
        digitalWrite(ReleasePin, HIGH);  //Releasing OFF
      } else if (packetBuffer[0] == '2') {
        Serial.println("Grasp");
        digitalWrite(GraspPin, LOW);     //Grasping ON
        digitalWrite(ReleasePin, HIGH);  //Releasingf OFF
      } else if (packetBuffer[0] == '3') {
        Serial.println("Release");
        digitalWrite(GraspPin, HIGH);   //Grasping OFF
        digitalWrite(ReleasePin, LOW);  //Releasing ON
      }
    }
  }

  // delay(1000);  // Adjust the delay as needed
}
