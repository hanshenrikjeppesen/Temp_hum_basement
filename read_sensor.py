from time import sleep
import pigpio

path_to_file = "/home/hans/temp_log_file"
pi = pigpio.pi()

import DHT22
s = DHT22.sensor(pi, 4)

s.trigger()
sleep(1)
# print('Temperature is {:.1f}'.format(s.temperature()))
# print('Humidity is {:.1f}'.format(s.humidity()))
temp = ('Temperature is {:.1f}'.format(s.temperature()))
hum = ('Humidity is {:.1f}'.format(s.humidity()))
print(temp)
with open(path_to_file, 'a') as f:
      f.write(temp)
      
      
