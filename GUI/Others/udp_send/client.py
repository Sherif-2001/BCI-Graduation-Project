import socket
import time

# Server IP and Port
SERVER_IP = "127.0.0.1"   # Replace with your server's IP address
SERVER_PORT = 12345  # Replace with your server's port number

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



# Create a list with 10 "Grasp" strings and 10 "Release" strings
task_list = ["Grasp"] * 10 + ["Release"] * 10

def send_predictions(task_list):
    for task in task_list:
        prediction = task
        print("Prediction:", prediction)
        
        # Send the prediction to the server
        sock.sendto(prediction.encode('utf-8'), (SERVER_IP, SERVER_PORT))
        
        # Wait for 2 seconds
        time.sleep(2)

# Start the process
send_predictions(task_list)
