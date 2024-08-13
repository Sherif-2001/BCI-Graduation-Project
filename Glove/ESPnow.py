import espnow
import network



class espNow:
    def __init__(self):
        # Initialize ESP-NOW
        self.esp = espnow.ESPNow()
        self.esp.active(True)
        
        # Define the MAC address of the receiving ESP32 (ESP32 B)
        self.peer_master = b'\xa8B\xe3\x91\x12\xa8'
        self.peer_glove = b'\xe8h\xe76\x02\xb8'
        self.peer_fes = b'x!\x84\xd8\x84\xb0'
        
        
        self.esp.add_peer(self.peer_master)
        self.esp.add_peer(self.peer_glove)
        self.esp.add_peer(self.peer_fes)           

    def espNow_Send(self, message, reciver):
        print(f"Sending command : {message}")
        self.esp.send(reciver, message)
        
    def espNow_Receive(self):
        sender, msg = self.esp.recv()
        msg =  msg.decode('utf-8')
        if msg:
            print('Received message from {}: {}'.format(sender, msg))
        return sender, msg
        
    def espNow_activate(self, mode):
        self.sta.active(mode)
        

    