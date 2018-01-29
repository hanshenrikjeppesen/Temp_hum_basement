from time import sleep
import pigpio

pi = pigpio.pi()

import DHT22

s = DHT22.sensor(pi, 4)

s.trigger()

print(s.temperature())
print(s.humidity())

      
