import espnow
import network



class espNow:
    def __init__(self, MAC):
        
        # A WLAN interface must be active to send()/recv()
        self.sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
        self.espNow_activate(True)
        
        # Initialize ESP-NOW
        self.esp = espnow.ESPNow()
        self.esp.active(True)
        
        # Define the MAC address of the receiving ESP32 (ESP32 B)
        self.peer = MAC 
        self.esp.add_peer(self.peer)
    
    def espNow_Send(self, message):
        print(f"Sending command : {message}")
        self.esp.send(self.peer, message)
        
    def espNow_Receive(self):
        sender, msg = self.esp.recv()
        msg = msg.decode('utf-8')
        if msg:
            print('Received message from {}: {}'.format(sender, msg))
        return sender, msg
        
    def espNow_activate(self, mode):
        self.sta.active(mode)
        

    