
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print('MAC Address:', wlan.config('mac'))