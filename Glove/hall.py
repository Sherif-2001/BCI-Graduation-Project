from machine import Pin, ADC

class HallSensor:
    def __init__(self, pinNum):
        self.pinNum = pinNum 
        self.hall = ADC(Pin(self.pinNum))
        self.hall.atten(ADC.ATTN_11DB) #Full range: 3.3v

    def getAngle(self):
        reading = self.hall.read()
        print(reading)
        #print(str(self.pinNum) + ' ' + str(reading))
        return reading
    
    
def getAllAngles(sensors):
    sensorReadings = []
    for sensor in sensors:
        reading = sensor.hall.read()
        sensorReadings.append(reading)
        print(str(sensor.pinNum) + ' ' + str(reading))
    return sensorReadings
        
  
