#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygame, sys, time
from pygame.locals import *

pygame.init()#inicializa o pygame
windowSurface = pygame.display.set_mode((1024, 768), 0, 32)#tamanho da tela
pygame.display.set_caption("Joselito's Adventure")#título da tela
mainClock = pygame.time.Clock()

pygame.mixer.music.load("Projeto/music.mp3") #Música do menu
pygame.mixer.music.play(-1, 0.0)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #definir background
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('Projeto/bckg.jpg', [0,0])#imagem do bckg
windowSurface.fill([255, 255, 255])
windowSurface.blit(BackGround.image, BackGround.rect)

def drawText(text, font, surface, x, y):#função para escrever na tela
	textobj = font.render(text, 1, WHITE)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

def mudafundo(img):
	BackGround = Background(img, [0,0])#pasta/imagem
	windowSurface.fill([255, 255, 255])
	windowSurface.blit(BackGround.image, BackGround.rect)
	pygame.display.update()

font = pygame.font.SysFont(None, 48)#fonte e tamanho
font2=pygame.font.SysFont(None, 24)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)#cores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

drawText("Clique para jogar!", font, windowSurface, (450), (620))#texto na tela
drawText("Aperte 'Esc' para fechar o jogo.", font2, windowSurface, (10), (0))#texto na tela
pygame.display.update()#atualizando tela

menu=True

while True:
# check for the QUIT event
	for event in pygame.event.get():
		if event.type == KEYUP:
			if event.key == K_ESCAPE: #aperta esc para sair
				pygame.quit()
				sys.exit()
	if menu==True:	
		if pygame.mouse.get_pressed()[0]:
			pygame.mixer.music.stop()#para a música do menu
			mudafundo("Projeto/load.jpg")#tela de carregamento
			time.sleep(3.5)#atraso no tempo de carregamento
			mudafundo("Projeto/map.jpg")#mudando o fundo para o mapa do jogo
			menu=False



pygame.display.update() #atualiza tela

sys.stdin.read(1)#não fecha a tela


