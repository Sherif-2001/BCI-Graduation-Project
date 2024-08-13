import network
import usocket as socket
import select

class WIFI_Connection:
    def __init__ (self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.connect_wifi()

    def connect_wifi(self):
        self.wlan.active(True)
#         self.wlan.connect(self.ssid, self.password)
#         while not self.wlan.isconnected():
#             pass
#         print('Connected to WiFi:', self.wlan.ifconfig())
#         
    def disconnect_wifi(self):
#         if self.wlan.isconnected():
#             self.wlan.disconnect()
            self.wlan.active(False)
            print('WiFi disconnected')
        
class UDP_Server:
    def __init__(self, laptop_IP, port):
        self.laptop_IP = laptop_IP
        self.port = port
        self.server_socket = None
        self.UDP_Connect()

    def UDP_Connect(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.server_socket.bind(('0.0.0.0', self.port))
            print(f"Connected to UDP server at {self.laptop_IP}:{self.port}")
        except Exception as e:
            print(f"Failed to connect to UDP server: {e}")
        
    def UDP_ReceiveMessage(self):
        if self.server_socket:
            ready = select.select([self.server_socket], [], [], 0.1)  # Timeout of 0.1 seconds
            if ready[0]:
                data = self.server_socket.recv(1024).decode()  # Buffer size can be adjusted
                return data
        return None
    
    
    
    def close_connection(self):
        self.server_socket.close()
        print("Connection closed")
        