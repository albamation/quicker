import pygame
import os

_sound_library = {}
pygame.mixer.init()

def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()

# this code from: http://www.nerdparadise.com/tech/python/pygame/basics/part3/
