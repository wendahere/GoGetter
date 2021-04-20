import vlc
import time

player = vlc.MediaPlayer("notenoughpoints.wav")

player.play()
time.sleep(3)