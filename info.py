import random

class Info:
    def __init__(self, temp, humidity, warmer):
        self.temp = temp
        self.humidity = humidity
        self.warmer = warmer
    
    def warmer(temp: int):
        return temp < 30
    
    def gen_new():
        temp = random.randrange(2, 42)
        humidity = random.randrange(10, 95)
        return Info(temp, humidity, Info.warmer(temp))
    
    def digital_sensor(self):
        return self.warmer.__int__()