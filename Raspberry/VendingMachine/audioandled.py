# import sounddevice as sd
# import soundfile as sf
import vlc

import MFRC522
from rpi_ws281x import *
import time
import os
import sys

LED_COUNT = (57)
LED_PIN = 21 #GPIO 18 #Board 12 or 21
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 100
LED_INVERT = False
LED_CHANNEL = 0

# sd.default.device = 2
# sd.default.channels = 128

# filename = 'notenoughpoints.wav'
# data, fs = sf.read(filename, dtype='float32')
# sd.play(data, fs)
# sd.wait()
player = vlc.MediaPlayer("notenoughpoints.wav")

player.play()
time.sleep(3)

print("OK")

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

strip.begin()

    #sd.default.samplerate = 44100
MIFAREReader = MFRC522.MFRC522()


for x in range(0, 19):
    strip.setPixelColor(x, Color(255,255,0))

for x in range(19, 38):
    strip.setPixelColor(x, Color(0,128,255))

for x in range(38, 57):
    strip.setPixelColor(x, Color(255,0,255))

strip.show()

       #print(status)
        # If a card is found
while True:
      (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
 
      if status == MIFAREReader.MI_OK:
          print("Card detected")
          for x in range(38, 57):
              strip.setPixelColor(x, Color(0,255,0))
          strip.show()


