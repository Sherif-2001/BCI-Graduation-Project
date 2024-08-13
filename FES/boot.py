# FES
import time
from machine import Pin
from ESPnow import *
from message_formating import *
from NetworkSetup import *

peer_GLOVE = b'x!\x84\xd8\x84\xb0'  # Replace with the MAC address of the receiver

ssid = 'AnwarLaptop'
password = 'Anwar12345'
wifi = WIFI_Connection(ssid, password)

fes = espNow(peer_GLOVE)

# Define the pins for the Relays and Button
GraspPin = Pin(22, Pin.OUT)
ReleasePin = Pin(23, Pin.OUT)
Grasp_Release_Button = Pin(26, Pin.IN, Pin.PULL_UP)

# Ensure the relays are off initially
GraspPin.value(0)  # Grasping OFF
ReleasePin.value(0)  # Releasing OFF

print("System initialized. Both relays are off.")

# State variable to track the relay status
current_state = "none"
calibration_state = 1 

while True:
    rec_msg = fes.espNow_Receive()
    header,sub_header,values = MessageDecoding(rec_msg)
    if header is not None: 
        if header ==  GLOVE_HEADER:
            calibration_state = 0
            if values == GLOVE_STATE_GRASP:
                    GraspPin.value(1)    # Grasping ON
                    ReleasePin.value(0)  # Releasing OFF
                    current_state = "grasping"
            elif values == GLOVE_STATE_RELEASE :
                    GraspPin.value(0)    # Grasping OFF
                    ReleasePin.value(1)  # Releasing ON
                    current_state = "releasing"

    if calibration_state == 1 :    
        # Read the button state
        button_state = Grasp_Release_Button.value()
        if button_state == 0:  # Button pressed
            if current_state == "none" or current_state == "releasing":
                msg = MessageEncoding(FES_HEADER, FES_PARAM_SUBHEADER,FES_ROM_RELEASE)
                fes.espNow_Send(fes.peer_glove, msg)
                print("Grasp button pressed. Grasping OFF, Releasing ON")
                GraspPin.value(1)    # Grasping ON
                ReleasePin.value(0)  # Releasing OFF
                current_state = "grasping"
            elif current_state == "grasping":
                msg = MessageEncoding(FES_HEADER, FES_PARAM_SUBHEADER,FES_ROM_GRASP)
                fes.espNow_Send(fes.peer_glove, msg)
                print("Grasp button pressed. Grasping ON, Releasing OFF")
                GraspPin.value(0)    # Grasping OFF
                ReleasePin.value(1)  # Releasing ON
                current_state = "releasing"

            # Wait until the button is released to avoid multiple toggles
            while Grasp_Release_Button.value() == 0:
                time.sleep(0.05)

        time.sleep(0.5)  # Additional debounce delay to ensure stable state

    time.sleep(0.05)  # Loop delay to avoid rapid polling
