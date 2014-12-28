from phue import Bridge
import time

BPM = 136
BRIDGE_IP = '192.168.99.161'

# Colors
ORANGE = 6000
YELLOW = 14500
GREEN = 26000
BLUE = 46920
PURPLE = 49000
PINK = 56100
RED = 65280

colorlist = [YELLOW, BLUE, RED, GREEN, PINK, ORANGE, PURPLE]

b = Bridge(BRIDGE_IP)
b.connect()

def flash():
    for i in xrange(65):
        for color in colorlist:
            command = {
                'transitiontime' : 0,
                'on' : True,
                'bri' : 255,
                'sat' : 255,
                'hue' : color
            }
            b.set_light(1, command)
            time.sleep(0.188)
            b.set_light(3, command)
            time.sleep(0.188)

def slut():
	light_1_state = b.get_light(1)
	light_3_state = b.get_light(3)
	flash()
	b.set_light(1, light_1_state['state'])
	b.set_light(3, light_3_state['state'])

