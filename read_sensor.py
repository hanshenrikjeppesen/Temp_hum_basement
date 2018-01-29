from time import sleep
import pigpio

pi = pigpio.pi()

import DHT22

s = DHT22.sensor(pi, 4)

s.trigger()

print('Temperature is {:3.2f}'.format(s.temperature() / 1.))
print('Humidity is {:3.2f}'.format(s.humidity() / 1.))

      
