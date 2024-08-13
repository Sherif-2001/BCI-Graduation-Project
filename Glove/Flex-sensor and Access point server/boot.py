from flex import *

flexPin = 34
angle = 0
flex = FlexSensor(flexPin)

try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Flex-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

def web_page():
    angle = flex.getReading()
    html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body><span id='angle'>----</span></body>
    <script>
    var xhttp = new XMLHttpRequest();
    
      setInterval(function () {
        getAngle();
        }, 500);
        
        function getAngle() {
        xhttp.open("GET", "getAngle", true);
        xhttp.onreadystatechange = function()  
            {  
                if(xhttp.readyState == 4 && xhttp.status==200)  
                     {  
                        var ajaxResult = xhttp.responseText;
                        document.getElementById("angle").innerHTML = ajaxResult;
                     }
            }
            xhttp.send();
        }
    </script></html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % str(request))
    update = request.find('/getAngle')
    print("-------------------------------update---------------------------------")
    print(update)
    

    if update == 6:
        angle = flex.getReading()
        response = str(angle)
    else:
        response = web_page()
        
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()