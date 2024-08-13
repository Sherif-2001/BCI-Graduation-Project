#include <WiFi.h>
#include <WiFiUdp.h>

// Define the pins for the LEDs
#define GraspPin 22
#define ReleasePin 23
#define HIGH_VOLT 19

#define Button_Mode 25
#define MODE_LED 12
#define Grasp_Button 26
#define Release_Button 27

int modeFlag = 1;     // Initial state of the flag
int graspFlag = 0;    // Initial state of the flag
int releaseFlag = 0;  // Initial state of the flag

const char* ssid = "Omar Saad's Laptop";
const char* password = "bciOmarSbme";
// const char* ssid = "Anwar's Laptop";
// const char* password = "Anwar12345";
const int local_port = 55000;


WiFiUDP udp;

void setup() {

  // Set the Relay pins as outputs
  pinMode(GraspPin, OUTPUT);
  digitalWrite(GraspPin, HIGH);  //Grasping OFF

  pinMode(ReleasePin, OUTPUT);
  digitalWrite(ReleasePin, HIGH);  //Releasing OFF

  pinMode(HIGH_VOLT, OUTPUT);
  digitalWrite(HIGH_VOLT, HIGH);  //Releasing OFF

  // delay(2000);
  // # ############# Buttons Setup ###########
  pinMode(Button_Mode, INPUT_PULLUP);
  pinMode(Grasp_Button, INPUT_PULLUP);
  pinMode(Release_Button, INPUT_PULLUP);

  pinMode(MODE_LED, OUTPUT);
  digitalWrite(MODE_LED, LOW);

  Serial.begin(115200);

  Serial.println("Grasp");
  digitalWrite(GraspPin, HIGH);   //Grasping ON
  digitalWrite(ReleasePin, LOW);  //Releasingf OFF

  // Connect to Wi - Fi
  WiFi.begin(ssid, password);
  // WiFi.config(staticIP);

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
  int mode_Buttons_State = digitalRead(Button_Mode);
  int grasp_Buttons_State = digitalRead(Grasp_Button);
  int release_Buttons_State = digitalRead(Release_Button);


  // Ask for 3 buttons
  if (mode_Buttons_State == LOW) {
    // Toggle the flag
    Serial.println("Mode Toggled:");
    modeFlag = !modeFlag;
    delay(100);
  }

  if (grasp_Buttons_State == LOW) {
    // Toggle the flag
    Serial.println("Grasp Toggled:");
    graspFlag = !graspFlag;
    delay(100);
  }

  if (release_Buttons_State == LOW) {
    Serial.println("Release Toggled:");
    // Toggle the flag
    releaseFlag = !releaseFlag;
    delay(100);
  }

  // Serial.println("Button_Mode :");
  // Serial.println(modeFlag);

  // Modes Handler
  if (modeFlag == 0) {
    digitalWrite(MODE_LED, LOW);

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

  } else {
    digitalWrite(MODE_LED, HIGH);

    if (graspFlag == 1) {
      releaseFlag = 0;
      digitalWrite(GraspPin, LOW);     //Grasping ON
      digitalWrite(ReleasePin, HIGH);  //Releasingf OFF
    } 
    else if (releaseFlag == 1) {
      graspFlag = 0;
      digitalWrite(GraspPin, HIGH);   //Grasping OFF
      digitalWrite(ReleasePin, LOW);  //Releasing ON
    } else {
      digitalWrite(GraspPin, HIGH);    //Grasping OFF
      digitalWrite(ReleasePin, HIGH);  //Releasing OFF
    }
  }
  delay(50);
}
