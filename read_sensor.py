#!/usr/bin/python3
from time import sleep
import pigpio
import datetime as t

path_to_file = "/home/hans/temp_log_file.txt"
pi = pigpio.pi()

import DHT22
s = DHT22.sensor(pi, 4)

s.trigger()
now = t.datetime.now()
month = now.month
day = now.day
hour = now.hour
minute = now.minute

sleep(1)
# print('Temperature is {:.1f}'.format(s.temperature()))
# print('Humidity is {:.1f}'.format(s.humidity()))
temp = ('Temperature is {:.1f} measured {}/{} at {}:{}'.format(s.temperature(), day, month, hour, minute))
hum = ('Humidity is {:.1f} measured {}/{} at {}:{}'.format(s.humidity(), day, month, hour, minute))

with open(path_to_file, 'a') as f:
      f.write(temp + "\n")
      f.write(hum + "\n")
      
      
