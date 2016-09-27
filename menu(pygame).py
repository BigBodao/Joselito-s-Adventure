import pygame, sys
from pygame.locals import *

pygame.init()
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Joselito's Adventure")

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('fed.jpg', [0,0])#imagem do bckg
windowSurface.fill([255, 255, 255])
windowSurface.blit(BackGround.image, BackGround.rect)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basicFont = pygame.font.SysFont(None, 48)

pygame.display.update()#atualizando tela

#text = basicFont.render("Hello World!", True, WHITE, BLUE)
#textRect = text.get_rect()
#textRect.centerx = windowSurface.get_rect().centerx
#textRect.centery = windowSurface.get_rect().centery
sys.stdin.read(1)


