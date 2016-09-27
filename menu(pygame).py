import pygame, sys
from pygame.locals import *

pygame.init()
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hello world!")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basicFont = pygame.font.SysFont(None, 48)

text = basicFont.render("Hello World!", True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery
sys.stdin.read(1)