import network
import usocket as socket


class WIFI_Connection:
    def __init__ (self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.connect_wifi()

    def connect_wifi(self):
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)
        while not self.wlan.isconnected():
            pass
        print('Connected to WiFi:', self.wlan.ifconfig())
        
    def disconnect_wifi(self):
        if self.wlan.isconnected():
            self.wlan.disconnect()
            self.wlan.active(False)
            print('WiFi disconnected')

    def reconnect_wifi(self):
        self.disconnect_wifi()
        self.connect_wifi()
        
class TCP_Server:
    def __init__(self, laptop_IP, port, numberOfListeners):
        self.laptop_IP = laptop_IP
        self.port = port
        self.numberOfListeners = numberOfListeners
        self.server_socket = None
        self.TCP_Connect()

    def TCP_Connect(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server_socket.connect((self.laptop_IP, self.port))
            print(f"Connected to TCP server at {self.laptop_IP}:{self.port}")
        except Exception as e:
            print(f"Failed to connect to TCP server: {e}")
            self.server_socket = None
        
    def TCP_SendMessage(self, message):
        if self.server_socket:
            self.server_socket.send(message.encode())
            print("Message is sent !!!!")
            return
        print("Error in sending the message !!!!")
        
    def TCP_ReceiveMessage(self):
        if self.server_socket:
            data = self.server_socket.recv(1024).decode()  # Buffer size can be adjusted
            print(f"Recieved message: {data}")
            return data
        print("No Message is recieved !!!!")
        return None
    
    def close_connection(self):
        self.server_socket.close()
        print("Connection closed")
        