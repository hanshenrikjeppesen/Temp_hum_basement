import os
from time import sleep
os.chdir('DHT22_py')
import pigpio

pi = pigpio.pi()

import DHT22

s = DHT22.sensor(pi, 4)

temp = 0
hum = 0

for i in range(10):
    sleep(2)
    s.trigger()
    temp = temp + str(s.temperature())

temp = temp/10
print('avag temp is=: ' + temp)

