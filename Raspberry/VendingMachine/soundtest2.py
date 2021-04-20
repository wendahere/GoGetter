import os

os.putenv('SDL_AUDIODRIVER', 'alsa')
os.putenv('SDL_AUDIODEV', '/dev/audio')

import pygame
pygame.init()

#music = pygame.mixer.music.load("music.mp3")

#pygame.mixer.music.play(-1)
selectPrizeAudio = pygame.mixer.Sound("plsselectyourprize.wav")
tapYourCardAudio = pygame.mixer.Sound("plstapyourcard.wav")
waitPrizeAudio = pygame.mixer.Sound("plswaitforyourprize.wav")
collectCardAudio = pygame.mixer.Sound("plscollectyourcard.wav")
notEnoughPointsAudio = pygame.mixer.Sound("notenoughpoints.wav")

collectCardAudio.play()
notEnoughPointsAudio.play()
#selectPrizeAudio.play()
#waitPrizeAudio.play()
#tapYourCardAudio.play()