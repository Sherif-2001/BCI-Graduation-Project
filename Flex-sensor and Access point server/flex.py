from machine import Pin, ADC
from time import sleep

# flexPin = 34

class FlexSensor:
    def __init__(self, pin):
        self.pin = pin 
        self.flex = ADC(Pin(self.pin))
        self.flex.atten(ADC.ATTN_11DB) #Full range: 3.3v
    
    def getReading(self):
        angle = self.flex.read()
        return angle
    
#flex = FlexSensor(flexPin)

#while True:
#  angle = flex.getReading()
#  print(angle)
#  sleep(0.1)
  
