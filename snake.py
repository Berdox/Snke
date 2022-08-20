import pygame
from pygame.locals import *
from Game import *
import time

if __name__ == "__main__":
    instance = Game()
    instance.startup()
    instance.run(instance)