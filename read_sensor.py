from time import sleep
import pigpio

pi = pigpio.pi()

import DHT22
s = DHT22.sensor(pi, 4)

s.trigger()
sleep(1)
# print('Temperature is {:.1f}'.format(s.temperature()))
# print('Humidity is {:.1f}'.format(s.humidity()))
temp = s.temperature()
hum = s.humidity()

print(temp)
print(hum)
      
