import RPi.GPIO as gpio
import sounddevice as sd
import soundfile as sf
#sd.default.samplerate = 44100
sd.default.device = 2
sd.default.channels = 128


filename = 'notenoughpoints.wav'
data, fs = sf.read(filename, dtype='float32')
sd.play(data, fs)
sd.wait()
print("OK")


#sd.play(myarray)