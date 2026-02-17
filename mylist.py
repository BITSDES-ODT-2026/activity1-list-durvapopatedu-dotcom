#list in list x LED

from machine import Pin
import time
led1 = Pin(19, Pin.OUT)
led2 = Pin(4, Pin.OUT)
led3 = Pin(5, Pin.OUT)
led4 = Pin(21, Pin.OUT)

num = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True : 
    for i in num :
        led1.value(i[0])
        time.sleep(0.2)
        led2.value(i[1])
        time.sleep(0.2)
        led3.value(i[2])
        time.sleep(0.2)
        led4.value(i[3])
        time.sleep(0.2)

#Create any list
