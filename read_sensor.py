from time import sleep
import pigpio
# sleep(2)
pi = pigpio.pi()
# sleep(1)
import DHT22
# sleep(1)
s = DHT22.sensor(pi, 4)
sleep(1)
s.trigger()
sleep(1)
print(s.temperature())
print(s.humidity())

      
