#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygame, sys, time, status, random
from pygame.locals import *
from status import *

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

def drawText(text, font, surface, x, y, cor):#função para escrever na tela
	textobj = font.render(text, 1, cor)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

def mudafundo(img):
	BackGround = Background(img, [0,0])#pasta/imagem
	windowSurface.fill([255, 255, 255])
	windowSurface.blit(BackGround.image, BackGround.rect)
	pygame.display.update()

def printimg(mdl,x,y):#imagens na tela
	img=pygame.image.load(mdl)#pasta/imagem
    	windowSurface.blit(img,(x,y))#local na tela

def up():#level up
	global exp, exp_max, lv, hp, hpmax, mana, manamax
	if exp >= exp_max:
		lv+= 1
		exp = 0
		exp_max = 10 * (lv + 1)
		hpmax = 10 * (lv + 1)
		hp=hpmax
		manamax=5 * (lv + 1)
		mana=manamax

def savarq():
	r=open("Joselito Demo.txt",'w')
	r.write("Obrigado por jogar a demo!") #Agradece por jogar a demo
	r.close()

def potionv():
	global hp, potv, hpmax
	hp+=20
	potv-=1
	if hp>hpmax:
		hp=hpmax

font = pygame.font.SysFont(None, 48)#fonte e tamanho
font2=pygame.font.SysFont(None, 24)
font3=pygame.font.SysFont(None, 36)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)#cores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

drawText("Clique para jogar!", font, windowSurface, (400), (620), WHITE)#texto na tela
drawText("Aperte 'Esc' para fechar o jogo.", font2, windowSurface, (10), (0), WHITE)#texto na tela
pygame.display.update()#atualizando tela

menu=True
game=False
fght=False
miss=1

def nmapa():
	mudafundo("Projeto/map.jpg")#mudando o fundo para o mapa do jogo
	game=True#entra no mapa
	drawText("Aperte enter para entrar na luta!", font3, windowSurface, (10), (0), WHITE)
	drawText("LV: "+str(lv), font2, windowSurface, (10), (710), WHITE)
	drawText("EXP: "+str(exp)+"/"+str(exp_max), font2, windowSurface, (10), (730), WHITE)
	pygame.display.update()

while True:
# check for the QUIT event

	for event in pygame.event.get():
		if event.type == KEYUP:
			if event.key == K_ESCAPE: #aperta esc para sair
				savarq()				
				pygame.quit()
				sys.exit()
	if menu==True:	
		if pygame.mouse.get_pressed()[0]:
			pygame.mixer.music.stop()#para a música do menu
			mudafundo("Projeto/load.jpg")#tela de carregamento
			time.sleep(3.5)#atraso no tempo de carregamento
			mudafundo("Projeto/map.jpg")#mudando o fundo para o mapa do jogo
			menu=False#sai do menu
			game=True#entra no game
			drawText("Aperte enter para entrar na luta!", font3, windowSurface, (10), (0), WHITE)
			drawText("LV: "+str(lv), font2, windowSurface, (10), (710), WHITE)
			drawText("EXP: "+str(exp)+"/"+str(exp_max), font2, windowSurface, (10), (730), WHITE)
			pygame.display.update()

	if game==True:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_RETURN: #aperta enter para entrar em uma luta
					fght=True
				
				if fght==True and miss==1:#primeiro inimigo
					mudafundo("Projeto/luta.jpg")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/ene1.png", 630,170)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("F1 - Atacar", font3, windowSurface,(60),(570), WHITE)
					drawText("F2 - Habilidades", font3, windowSurface,(60),(640), WHITE)
					drawText("F3 - Pots", font3, windowSurface,(60),(710), WHITE)
					pygame.display.update()

					if event.key == K_F3 and potv>0:
						potionv()
						drawText("Joselito usou uma pot de hp", font3, windowSurface,(20),(300), WHITE)
						drawText(str(potv)+" pots de hp restantes", font3, windowSurface,(360),(710), WHITE)
						matk=random.randint(1,3)
						drawText("O inimigo causou "+str(matk), font3, windowSurface,(670),(300), WHITE)
						hp-=matk#ataque do inimigo
					if event.key == K_F1:
						dmg = 5 * random.randint(1, 3)
						matk1=random.randint(1,3)
						drawText("Joselito causou "+str(dmg), font3, windowSurface,(20),(300), WHITE)
						drawText("O inimigo causou "+str(matk1), font3, windowSurface,(670),(300), WHITE)
						hpm1-=dmg#ataque do player
						hp-=matk1#ataque do inimigo
					if event.key == K_F2 and mana>0:
						hab1 = 3 * random.randint(2,8)
						matk1=random.randint(1,3)
						drawText("Joselito causou "+str(hab1), font3, windowSurface,(20),(300), WHITE)
						drawText("O inimigo causou "+str(matk1), font3, windowSurface,(670),(300), WHITE)
						hpm1-=hab1#habilidade
						hp-=matk1#ataque do inimigo
						mana-=1
						
					if mana<=0 and event.key == K_F2:
						drawText("Sem Mana",font3,windowSurface,(360),(670),WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)#vida do jogador
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (640), WHITE)#mana
					drawText("Inimigo HP: "+str(hpm1)+"/"+str(hpmaxm1), font3, windowSurface, (560), (570), WHITE)#vida do inimigo
					if hp<0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						savarq()
						pygame.quit()
						sys.exit()
					if hpm1<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xpg=random.randint(1,3)
						exp+=xpg
						drawText("Exp ganha: "+str(xpg), font3, windowSurface, (300),(270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1#próximo combate
						nmapa()
						hp=hpmax
						up()

					pygame.display.update()

				if fght==True and miss==2:#segundo inimigo
					mudafundo("Projeto/luta.jpg")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/ene2.png", 630,100)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("F1 - Atacar", font3, windowSurface,(60),(570), WHITE)
					drawText("F2 - Habilidades", font3, windowSurface,(60),(640), WHITE)
					drawText("F3 - Pots", font3, windowSurface,(60),(710), WHITE)
					pygame.display.update()

					if event.key == K_F3 and potv>0:
						potionv()
						drawText("Joselito usou uma pot de hp", font3, windowSurface,(20),(300), WHITE)
						drawText(str(potv)+" pots de hp restantes", font3, windowSurface,(360),(710), WHITE)
						matk=random.randint(2,5)
						drawText("O inimigo causou "+str(matk), font3, windowSurface,(670),(300), WHITE)
						hp-=matk#ataque do inimigo
					if event.key == K_F1:
						dmg = 5 * random.randint(1, 3)
						matk2=random.randint(2,5)
						drawText("Joselito causou "+str(dmg), font3, windowSurface,(20),(300), WHITE)
						drawText("O inimigo causou "+str(matk2), font3, windowSurface,(670),(300), WHITE)
						hpm2-=dmg
						hp-=matk2
					if event.key == K_F2 and mana>0:
						hab1 = 3 * random.randint(2,8)
						matk2=random.randint(2,5)
						drawText("Joselito causou "+str(hab1), font3, windowSurface,(20),(300), WHITE)
						drawText("O inimigo causou "+str(matk2), font3, windowSurface,(670),(300), WHITE)
						hpm2-=hab1
						hp-=matk2
						mana-=1
					if mana<=0 and event.key == K_F2:
						drawText("Sem Mana",font3,windowSurface,(360),(670),WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (640), WHITE)
					drawText("Inimigo HP: "+str(hpm2)+"/"+str(hpmaxm2), font3, windowSurface, (560), (570), WHITE)
					if hp<0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						savarq()
						pygame.quit()
						sys.exit()
					if hpm2<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xpg=random.randint(2,7)
						exp+=xpg
						drawText("Exp ganha: "+str(xpg), font3, windowSurface, (300),(270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()

					pygame.display.update()

				if fght==True and miss==3:#terceiro inimigo
					mudafundo("Projeto/luta.jpg")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/ene3.png", 400,10)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("F1 - Atacar", font3, windowSurface,(60),(570), WHITE)
					drawText("F2 - Habilidades", font3, windowSurface,(60),(640), WHITE)
					drawText("F3 - Pots", font3, windowSurface,(60),(710), WHITE)
					pygame.display.update()

					if event.key == K_F3 and potv>0:
						potionv()
						drawText("Joselito usou uma pot de hp", font3, windowSurface,(20),(300), WHITE)
						drawText(str(potv)+" pots de hp restantes", font3, windowSurface,(360),(710), WHITE)
						matk=random.randint(3,8)
						drawText("O inimigo causou "+str(matk), font3, windowSurface,(670),(300), WHITE)
						hp-=matk#ataque do inimigo
					if event.key == K_F1:
						dmg = 5 * random.randint(1, 3)
						matk3=random.randint(3,8)
						drawText("Joselito causou "+str(dmg), font3, windowSurface,(20),(300), WHITE)
						drawText("O inimigo causou "+str(matk3), font3, windowSurface,(670),(300), WHITE)
						hpm3-=dmg
						hp-=matk3
					if event.key == K_F2 and mana>0:
						hab1 = 3 * random.randint(2,8)
						matk3=random.randint(3,8)
						drawText("Joselito causou "+str(hab1), font3, windowSurface,(20),(300), WHITE)
						drawText("O inimigo causou "+str(matk3), font3, windowSurface,(670),(300), WHITE)
						hpm3-=hab1
						hp-=matk3
						mana-=1
					if mana<=0 and event.key == K_F2:
						drawText("Sem Mana",font3,windowSurface,(360),(670),WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (640), WHITE)
					drawText("Inimigo HP: "+str(hpm3)+"/"+str(hpmaxm3), font3, windowSurface, (560), (570), WHITE)
					if hp<0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						savarq()
						pygame.quit()
						sys.exit()
					if hpm3<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xpg=random.randint(3,10)
						exp+=xpg
						drawText("Exp ganha: "+str(xpg), font3, windowSurface, (300),(270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()

					pygame.display.update()

				if fght==True and miss==4:#quarto inimigo
					mudafundo("Projeto/luta.jpg")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/ene4.png", 350,-180)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("F1 - Atacar", font3, windowSurface,(60),(570), WHITE)
					drawText("F2 - Habilidades", font3, windowSurface,(60),(640), WHITE)
					drawText("F3 - Pots", font3, windowSurface,(60),(710), WHITE)
					pygame.display.update()

					if event.key == K_F3 and potv>0:
						potionv()
						drawText("Joselito usou uma pot de hp", font3, windowSurface,(20),(300), WHITE)
						drawText(str(potv)+" pots de hp restantes", font3, windowSurface,(360),(710), WHITE)
						matk=random.randint(4,10)
						drawText("O inimigo causou "+str(matk), font3, windowSurface,(670),(300), WHITE)
						hp-=matk#ataque do inimigo
					if event.key == K_F1:
						dmg = 5 * random.randint(1, 3)
						matk4=random.randint(4,10)
						drawText("Joselito causou "+str(dmg), font3, windowSurface,(20),(300), WHITE)
						drawText("O inimigo causou "+str(matk4), font3, windowSurface,(670),(300), WHITE)
						hpm4-=dmg
						hp-=matk4
					if event.key == K_F2 and mana>0:
						hab1 = 3 * random.randint(2,8)
						matk4=random.randint(4,10)
						drawText("Joselito causou "+str(hab1), font3, windowSurface,(20),(300), WHITE)
						drawText("O inimigo causou "+str(matk4), font3, windowSurface,(670),(300), WHITE)
						hpm4-=hab1
						hp-=matk4
						mana-=1
					if mana<=0 and event.key == K_F2:
						drawText("Sem Mana",font3,windowSurface,(360),(670),WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (640), WHITE)
					drawText("Inimigo HP: "+str(hpm4)+"/"+str(hpmaxm4), font3, windowSurface, (560), (570), WHITE)
					if hp<0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						savarq()
						pygame.quit()
						sys.exit()
					if hpm4<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xpg=random.randint(4,14)
						exp+=xpg
						drawText("Exp ganha: "+str(xpg), font3, windowSurface, (300),(270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()

					pygame.display.update()

				if fght==True and miss==5:#primeiro boss
					mudafundo("Projeto/luta.jpg")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/boss1.png", 460,-120)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("F1 - Atacar", font3, windowSurface,(60),(570), WHITE)
					drawText("F2 - Habilidades", font3, windowSurface,(60),(640), WHITE)
					drawText("F3 - Pots", font3, windowSurface,(60),(710), WHITE)
					pygame.display.update()

					if event.key == K_F3 and potv>0:
						potionv()
						drawText("Joselito usou uma pot de hp", font3, windowSurface,(20),(300), WHITE)
						drawText(str(potv)+" pots de hp restantes", font3, windowSurface,(360),(710), WHITE)
						matk=random.randint(5,20)
						drawText("O inimigo causou "+str(matk), font3, windowSurface,(670),(300), WHITE)
						hp-=matk#ataque do inimigo
					if event.key == K_F1:
						dmg = 5 * random.randint(1, 3)
						matkb1=random.randint(5,20)
						drawText("Joselito causou "+str(dmg), font3, windowSurface,(20),(300), WHITE)
						drawText("O inimigo causou "+str(matkb1), font3, windowSurface,(670),(300), WHITE)
						hpb1-=dmg
						hp-=matkb1
					if event.key == K_F2 and mana>0:
						hab1 = 3 * random.randint(2,8)
						matkb1=random.randint(5,20)
						drawText("Joselito causou "+str(hab1), font3, windowSurface,(20),(300), WHITE)
						drawText("O inimigo causou "+str(matkb1), font3, windowSurface,(670),(300), WHITE)
						hpb1-=hab1
						hp-=matkb1
						mana-=1
					if mana<=0 and event.key == K_F2:
						drawText("Sem Mana",font3,windowSurface,(360),(670),WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (640), WHITE)
					drawText("Inimigo HP: "+str(hpb1)+"/"+str(hpmaxb1), font3, windowSurface, (560), (570), WHITE)
					if hp<0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						savarq()
						pygame.quit()
						sys.exit()
					if hpb1<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xpg=random.randint(10,30)
						exp+=xpg
						drawText("Exp ganha: "+str(xpg), font3, windowSurface, (300),(270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()

					pygame.display.update()

				if event.key == K_ESCAPE: #aperta esc para sair
					savarq()					
					pygame.quit()
					sys.exit()

pygame.display.update() #atualiza tela

sys.stdin.read(1)#não fecha a tela
