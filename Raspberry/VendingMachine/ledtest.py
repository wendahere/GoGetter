from rpi_ws281x import *
import time
import os
import sys
import RPi.GPIO as gpio

LED_COUNT = (57)
LED_PIN = 21 #GPIO 18 #Board 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 100
LED_INVERT = False
LED_CHANNEL = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

for x in range(0, 19):
    strip.setPixelColor(x, Color(255,255,0))

for x in range(19, 38):
    strip.setPixelColor(x, Color(0,128,255))

for x in range(38, 57):
    strip.setPixelColor(x, Color(0,0,0))

strip.show()

print("Done")

time.sleep(3)


#time.sleep(3)
#os.execv(sys.executable,
#             [sys.executable, os.path.join(sys.path[0], __file__)] + sys.argv[1:])
