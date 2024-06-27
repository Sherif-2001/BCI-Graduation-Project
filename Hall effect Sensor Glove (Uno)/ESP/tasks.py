import uasyncio as asyncio
import time
from message_formating import *
from hall import *
from NetworkSetup import *
from senderESPnow import *


shared_message = [""]


print("--------------------")


Mac = b'dscdcdc'

# Hall sensor pin configuration
hallPins = [12, 14, 27, 26, 25]

sensors = [HallSensor(pin) for pin in hallPins]

# Initialize WiFi connection
wifi = WIFI_Connection("AnwarLaptop", 'Anwar12345')

# Initialize TCP server
server = TCP_Server('192.168.137.1', 65432, 5)

espNow = espNow(Mac)

angles = []


async def read_sensors():
    while True:
        start_time = time.ticks_ms()  # Record the start time
        espNow.espNow_activate(False)
        wifi.disconnect_wifi()
        angles = getAllAngles(sensors)
        shared_message[0] = MessageEncoding("GLOVE", angles)
#         print(f"message var: {shared_message[0]}")
        end_time = time.ticks_ms()  # Record the end time
        elapsed_time = time.ticks_diff(end_time, start_time)  # Calculate elapsed time
        print(f"Sensor reading task took {elapsed_time} ms")
        await asyncio.sleep(0.01)  # Adjust the timing as needed
        
# async def send_espnow():
#     while True:
#         wifi.disconnect_wifi()
#         espNow.espNow_activate(True)
#         print("Sending ESP-NOW:", message)
#         espNow.espNow_Send(message.encode())
#         await asyncio.sleep(1)  # Adjust the timing as needed
        
async def send_tcp():
    while True:
        espNow.espNow_activate(False)
        wifi.connect_wifi()
        server.TCP_Connect()
#         print("Sending TCP:", shared_message[0])
        server.TCP_SendMessage(shared_message[0])
        message = server.TCP_ReceiveMessage()
        sender, anglesList = MessageDecoding(message)
#         print(f"Sender : {sender}")
#         print(f"Angles : {anglesList}")
        await asyncio.sleep(0.02)  # Adjust the timing as needed
        
        