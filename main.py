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
	if exp == exp_max or exp > exp_max:
		lv+= 1
		exp_max = 8 * (lv + 1) + exp_max
		hpmax = 8 * (lv + 1)
		hp=hpmax
		manamax=3 * (lv + 1)
		mana=manamax
		up()


def savarq():
	danoalt=danoj[0]
	danohalt=danojh[0]	
	for i in danoj:
		if danoalt<i:
			danoalt=i
	for j in danojh:
		if danohalt<j:
			danohalt=j
	
	r=open("Joselito Demo.txt",'w')
	r.write("Obrigado por jogar a demo!\n") #Agradece por jogar a demo
	r.write("Maior dano normal: "+str(danoalt)+"\n")
	r.write("Maior dano de habilidade: "+str(danohalt))
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
	pygame.mixer.music.stop()
	up()
	mudafundo("Projeto/map.jpg")#mudando o fundo para o mapa do jogo
	game=True#entra no mapa
	drawText("Aperte enter para entrar na luta!", font2, windowSurface, (10), (0), WHITE)
	drawText("LV: " + str(lv), font2, windowSurface, (10), (30), WHITE)
	drawText("EXP: " + str(exp)+"/"+str(exp_max), font2, windowSurface, (10), (50), WHITE)
	pygame.display.update()

def gameover():
	pygame.mixer.music.stop()
	drawText("JOSELITO MOOOOOOOOOORRRRREEEUUUUU",font2, windowSurface,(384),(513), WHITE)
	time.sleep(2.5)
	mudafundo("Projeto/game_over.png")#colocando tela de gameover
	pygame.display.update()
	time.sleep(2.0)
	savarq()
	pygame.quit()
	sys.exit()


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
			drawText("Aperte enter para entrar na luta!", font2, windowSurface, (10), (10), WHITE)
			drawText("LV: "+str(lv), font2, windowSurface, (10), (30), WHITE)
			drawText("EXP: "+str(exp)+"/"+str(exp_max), font2, windowSurface, (10), (50), WHITE)
			pygame.display.update()

	if game==True:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_RETURN: #aperta enter para entrar em uma luta
					pygame.mixer.music.load("Projeto/battle.mp3")
					pygame.mixer.music.set_volume(70)
					pygame.mixer.music.play(-1, 0.0)
					fght=True
				
				if fght==True and miss==1:#primeiro monstro
					mudafundo("Projeto/bkg_1.png")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/ene1.png", 630,170)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("A - Atacar", font3, windowSurface,(60),(570), WHITE)#opção para atacar
					drawText("S - Habilidades", font3, windowSurface,(60),(605), WHITE)#opção para usar habilidade
					drawText("D - Potion", font3, windowSurface, (60), (675), WHITE)#opção para usar poção
					pygame.display.update()#atualizar a tela

					if event.key == K_d and potv > 0:
						potionv()
						drawText("Joselito usou uma potion de HP", font3, windowSurface, (20), (300), WHITE)
						drawText(str(potv)+"potions de hp restante", font3, windowSurface, (360), (675), WHITE)
						matkm1 = random.randint(1,3)
						drawText(inim[0]+" causou " +str(matkm1) + " de dano", font3, windowSurface, (670), (300), WHITE)
						hp-=matkm1
					if event.key == K_a:
						dmg = (2 * lv) * random.randint(1,3)
						matkm1 = random.randint(1,3)
						drawText("Joselito causou " +str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(inim[0]+" causou " + str(matkm1) + " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpm1-=dmg#ataque do player
						hp-=matkm1#ataque do monstro
						danoj[0:0]=[dmg]
					if event.key == K_s and mana > 0:
						dmg = (3 * lv) * random.randint(3, 5)
						matkm1 = random.randint(1,3)
						drawText("Joselito causou " + str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(inim[0]+" causou " + str(matkm1)+ " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpm1-=dmg#habilidade
						hp-=matkm1#ataque do monstro
						mana-=1
						danojh[0:0]=[dmg]
					if mana <= 0 and event.key == K_s:
						drawText("Joselito está sem mana", font3, windowSurface, (20), (300), WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)#vida do jogador
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (600), WHITE)#mana do jogador
					drawText(inim[0]+" HP: "+str(hpm1)+"/"+str(hpmaxm1), font3, windowSurface, (560), (570), WHITE)#vida do jogador
					if hp<=0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						gameover()
					if hpm1<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xp =random.randint(5, 20)
						exp+=xp
						drawText("Exp ganha: "+str(xp), font3, windowSurface, (300), (270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()

					pygame.display.update()

				if fght==True and miss==2:#primeiro boss
					mudafundo("Projeto/bkg_1.png")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/boss1.png", 0,-30)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("A - Atacar", font3, windowSurface,(60),(570), WHITE)#opção para atacar
					drawText("S - Habilidades", font3, windowSurface,(60),(605), WHITE)#opção para usar habilidade
					drawText("D - Potion", font3, windowSurface, (60), (675), WHITE)#opção para usar poção
					pygame.display.update()#atualizar a tela

					if event.key == K_d and potv > 0:
						potionv()
						drawText("Joselito usou uma potion de HP", font3, windowSurface, (20), (300), WHITE)
						drawText(str(potv)+"potions de hp restante", font3, windowSurface, (360), (675), WHITE)
						matkb1=random.randint(4,10)
						drawText(boss[0]+" causou " +str(matkb1) + " de dano", font3, windowSurface, (670), (300), WHITE)
						hp-=matkb1
					if event.key == K_a:
						dmg = (2 * lv) * random.randint(1,3)
						matkb1 = random.randint(4,10)
						drawText("Joselito causou " +str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(boss[0]+" causou " + str(matkb1) + " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpb1-=dmg#ataque do player
						hp-=matkb1#ataque do monstro
						danoj[0:0]=[dmg]
					if event.key == K_s and mana > 0:
						dmg = (3 * lv) * random.randint(3, 5)
						matkb1 = random.randint(4,10)
						drawText("Joselito causou " + str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(boss[0]+" causou " + str(matkb1)+ " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpb1-=dmg#habilidade
						hp-=matkb1#ataque do monstro
						mana-=1
						danojh[0:0]=[dmg]
					if mana <= 0 and event.key == K_s:
						drawText("Joselito está sem mana", font3, windowSurface, (20), (300), WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)#vida do jogador
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (600), WHITE)#mana do jogador
					drawText(boss[0]+" HP: "+str(hpb1)+"/"+str(hpmaxb1), font3, windowSurface, (560), (570), WHITE)#vida do jogador
					if hp<=0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						gameover()
					if hpb1<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xp =random.randint(5, 20)
						exp+=xp
						drawText("Exp ganha: "+str(xp), font3, windowSurface, (300), (270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()
					pygame.display.update()

				if fght==True and miss==3:#segundo inimigo
					mudafundo("Projeto/bkg_2.png")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/ene2.png", 0,-20)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("A - Atacar", font3, windowSurface,(60),(570), WHITE)#opção para atacar
					drawText("S - Habilidades", font3, windowSurface,(60),(605), WHITE)#opção para usar habilidade
					drawText("D - Potion", font3, windowSurface, (60), (675), WHITE)#opção para usar poção
					pygame.display.update()#atualizar a tela

					if event.key == K_d and potv > 0:
						potionv()
						drawText("Joselito usou uma potion de HP", font3, windowSurface, (20), (300), WHITE)
						drawText(str(potv)+"potions de hp restante", font3, windowSurface, (360), (675), WHITE)
						matk2=random.randint(3,6)
						drawText(inim[1]+" causou " +str(matk2) + " de dano", font3, windowSurface, (670), (300), WHITE)
						hp-=matk2
					if event.key == K_a:
						dmg = (2 * lv) * random.randint(1,3)
						matk2 = random.randint(3,6)
						drawText("Joselito causou " +str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(inim[1]+" causou " + str(matk2) + " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpm2-=dmg#ataque do player
						hp-=matk2#ataque do monstro
						danoj[0:0]=[dmg]
					if event.key == K_s and mana > 0:
						dmg = (3 * lv) * random.randint(3, 5)
						matk2 = random.randint(3,6)
						drawText("Joselito causou " + str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(inim[1]+" causou " + str(matk2)+ " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpm2-=dmg#habilidade
						hp-=matk2#ataque do monstro
						mana-=1
						danojh[0:0]=[dmg]
					if mana <= 0 and event.key == K_s:
						drawText("Joselito está sem mana", font3, windowSurface, (20), (300), WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)#vida do jogador
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (600), WHITE)#mana do jogador
					drawText(inim[1]+" HP: "+str(hpm2)+"/"+str(hpmaxm2), font3, windowSurface, (560), (570), WHITE)#vida do jogador
					if hp<=0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						gameover()
					if hpm2<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xp =random.randint(5, 20)
						exp+=xp
						drawText("Exp ganha: "+str(xp), font3, windowSurface, (300), (270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()
					pygame.display.update()

				if fght==True and miss==4:#segundo boss
					mudafundo("Projeto/bkg_2.png")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/boss2.png", 0,-50)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("A - Atacar", font3, windowSurface,(60),(570), WHITE)#opção para atacar
					drawText("S - Habilidades", font3, windowSurface,(60),(605), WHITE)#opção para usar habilidade
					drawText("D - Potion", font3, windowSurface, (60), (675), WHITE)#opção para usar poção
					pygame.display.update()#atualizar a tela

					if event.key == K_d and potv > 0:
						potionv()
						drawText("Joselito usou uma potion de HP", font3, windowSurface, (20), (300), WHITE)
						drawText(str(potv)+"potions de hp restante", font3, windowSurface, (360), (675), WHITE)
						matk2=random.randint(6,10)
						drawText(boss[1]+" causou " +str(matkb2) + " de dano", font3, windowSurface, (670), (300), WHITE)
						hp-=matkb2
					if event.key == K_a:
						dmg = (2 * lv) * random.randint(1,3)
						matkb2 = random.randint(6,10)
						drawText("Joselito causou " +str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(boss[1]+" causou " + str(matkb2) + " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpb2-=dmg#ataque do player
						hp-=matkb2#ataque do monstro
						danoj[0:0]=[dmg]
					if event.key == K_s and mana > 0:
						dmg = (3 * lv) * random.randint(3, 5)
						matkb2 = random.randint(6,10)
						drawText("Joselito causou " + str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(boss[1]+" causou " + str(matkb2)+ " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpb2-=dmg#habilidade
						hp-=matkb2#ataque do monstro
						mana-=1
						danojh[0:0]=[dmg]
					if mana <= 0 and event.key == K_s:
						drawText("Joselito está sem mana", font3, windowSurface, (20), (300), WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)#vida do jogador
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (600), WHITE)#mana do jogador
					drawText(boss[1]+" HP: "+str(hpb2)+"/"+str(hpmaxb2), font3, windowSurface, (560), (570), WHITE)#vida do jogador
					if hp<=0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						gameover()
					if hpb2<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xp =random.randint(5, 20)
						exp+=xp
						drawText("Exp ganha: "+str(xp), font3, windowSurface, (300), (270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()
					pygame.display.update()

				if fght==True and miss==5:#terceiro inimigo
					mudafundo("Projeto/bkg_3.png")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/ene3.png", 0,-10)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("A - Atacar", font3, windowSurface,(60),(570), WHITE)#opção para atacar
					drawText("S - Habilidades", font3, windowSurface,(60),(605), WHITE)#opção para usar habilidade
					drawText("D - Potion", font3, windowSurface, (60), (675), WHITE)#opção para usar poção
					pygame.display.update()#atualizar a tela

					if event.key == K_d and potv > 0:
						potionv()
						drawText("Joselito usou uma potion de HP", font3, windowSurface, (20), (300), WHITE)
						drawText(str(potv)+"potions de hp restante", font3, windowSurface, (360), (675), WHITE)
						matkm3=random.randint(7,9)
						drawText(inim[2]+" causou " +str(matkm3) + " de dano", font3, windowSurface, (670), (300), WHITE)
						hp-=matkm3
					if event.key == K_a:
						dmg = (2 * lv) * random.randint(1,3)
						matkm3 = random.randint(7,9)
						drawText("Joselito causou " +str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(inim[2]+" causou " + str(matkm3) + " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpm3-=dmg#ataque do player
						hp-=matkm3#ataque do monstro
						danoj[0:0]=[dmg]
					if event.key == K_s and mana > 0:
						dmg = (3 * lv) * random.randint(3, 5)
						matkm3 = random.randint(7,9)
						drawText("Joselito causou " + str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(inim[2]+" causou " + str(matkm3)+ " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpm3-=dmg#habilidade
						hp-=matkm3#ataque do monstro
						mana-=1
						danojh[0:0]=[dmg]
					if mana <= 0 and event.key == K_s:
						drawText("Joselito está sem mana", font3, windowSurface, (20), (300), WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)#vida do jogador
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (600), WHITE)#mana do jogador
					drawText(inim[2]+" HP: "+str(hpm3)+"/"+str(hpmaxm3), font3, windowSurface, (560), (570), WHITE)#vida do jogador
					if hp<=0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						gameover()
					if hpm3<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xp =random.randint(5, 20)
						exp+=xp
						drawText("Exp ganha: "+str(xp), font3, windowSurface, (300), (270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()
					pygame.display.update()

				if fght==True and miss==6:#terceiro boss
					mudafundo("Projeto/bkg_3.png")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/boss3.png", 0,0)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("A - Atacar", font3, windowSurface,(60),(570), WHITE)#opção para atacar
					drawText("S - Habilidades", font3, windowSurface,(60),(605), WHITE)#opção para usar habilidade
					drawText("D - Potion", font3, windowSurface, (60), (675), WHITE)#opção para usar poção
					pygame.display.update()#atualizar a tela

					if event.key == K_d and potv > 0:
						potionv()
						drawText("Joselito usou uma potion de HP", font3, windowSurface, (20), (300), WHITE)
						drawText(str(potv)+"potions de hp restante", font3, windowSurface, (360), (675), WHITE)
						matkb3=random.randint(10,15)
						drawText(boss[2]+" causou " +str(matkb3) + " de dano", font3, windowSurface, (670), (300), WHITE)
						hp-=matkb3
					if event.key == K_a:
						dmg = (2 * lv) * random.randint(1,3)
						matkb3 = random.randint(10,15)
						drawText("Joselito causou " +str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(boss[2]+" causou " + str(matkb3) + " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpb3-=dmg#ataque do player
						hp-=matkb3#ataque do monstro
						danoj[0:0]=[dmg]
					if event.key == K_s and mana > 0:
						dmg = (3 * lv) * random.randint(3, 5)
						matkb3 = random.randint(10,15)
						drawText("Joselito causou " + str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(boss[2]+" causou " + str(matkb3)+ " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpb3-=dmg#habilidade
						hp-=matkb3#ataque do monstro
						mana-=1
						danojh[0:0]=[dmg]
					if mana <= 0 and event.key == K_s:
						drawText("Joselito está sem mana", font3, windowSurface, (20), (300), WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)#vida do jogador
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (600), WHITE)#mana do jogador
					drawText(boss[2]+" HP: "+str(hpb3)+"/"+str(hpmaxb3), font3, windowSurface, (560), (570), WHITE)#vida do jogador
					if hp<=0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						gameover()
					if hpb3<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xp =random.randint(5, 20)
						exp+=xp
						drawText("Exp ganha: "+str(xp), font3, windowSurface, (300), (270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()
					pygame.display.update()

				if fght==True and miss==7:#quarto inimigo
					mudafundo("Projeto/bkg_4.png")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/ene4.png", 0,-50)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("A - Atacar", font3, windowSurface,(60),(570), WHITE)#opção para atacar
					drawText("S - Habilidades", font3, windowSurface,(60),(605), WHITE)#opção para usar habilidade
					drawText("D - Potion", font3, windowSurface, (60), (675), WHITE)#opção para usar poção
					pygame.display.update()#atualizar a tela

					if event.key == K_d and potv > 0:
						potionv()
						drawText("Joselito usou uma potion de HP", font3, windowSurface, (20), (300), WHITE)
						drawText(str(potv)+"potions de hp restante", font3, windowSurface, (360), (675), WHITE)
						matkm4=random.randint(11,13)
						drawText(inim[3]+" causou " +str(matkm4) + " de dano", font3, windowSurface, (670), (300), WHITE)
						hp-=matkm4
					if event.key == K_a:
						dmg = (2 * lv) * random.randint(1,3)
						matkm4 = random.randint(11,13)
						drawText("Joselito causou " +str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(inim[3]+" causou " + str(matkm4) + " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpm4-=dmg#ataque do player
						hp-=matkm4#ataque do monstro
						danoj[0:0]=[dmg]
					if event.key == K_s and mana > 0:
						dmg = (3 * lv) * random.randint(3, 5)
						matkm4 = random.randint(11,13)
						drawText("Joselito causou " + str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(inim[3]+" causou " + str(matkm4)+ " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpm4-=dmg#habilidade
						hp-=matkm4#ataque do monstro
						mana-=1
						danojh[0:0]=[dmg]
					if mana <= 0 and event.key == K_s:
						drawText("Joselito está sem mana", font3, windowSurface, (20), (300), WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)#vida do jogador
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (600), WHITE)#mana do jogador
					drawText(inim[3]+" HP: "+str(hpm4)+"/"+str(hpmaxm4), font3, windowSurface, (560), (570), WHITE)#vida do jogador
					if hp<=0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						gameover()
					if hpm4<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xp =random.randint(5, 20)
						exp+=xp
						drawText("Exp ganha: "+str(xp), font3, windowSurface, (300), (270), BLUE)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()
					pygame.display.update()

				if fght==True and miss==8:#quarto boss
					mudafundo("Projeto/bkg_4.png")#fundo da luta
					printimg("Projeto/char.png",-180,200)#personagem jogador
					printimg("Projeto/boss4.png", 0,0)#inimigo
					printimg("Projeto/bar.png",0,0)#barra de ação
					drawText("A - Atacar", font3, windowSurface,(60),(570), WHITE)#opção para atacar
					drawText("S - Habilidades", font3, windowSurface,(60),(605), WHITE)#opção para usar habilidade
					drawText("D - Potion", font3, windowSurface, (60), (675), WHITE)#opção para usar poção
					pygame.display.update()#atualizar a tela

					if event.key == K_d and potv > 0:
						potionv()
						drawText("Joselito usou uma potion de HP", font3, windowSurface, (20), (300), WHITE)
						drawText(str(potv)+"potions de hp restante", font3, windowSurface, (360), (675), WHITE)
						matkb4=random.randint(15,20)
						drawText(boss[3]+" causou " +str(matkb4) + " de dano", font3, windowSurface, (670), (300), WHITE)
						hp-=matkb4
					if event.key == K_a:
						dmg = (2 * lv) * random.randint(1,3)
						matkb4 = random.randint(15,20)
						drawText("Joselito causou " +str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(boss[3]+" causou " + str(matkb4) + " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpb4-=dmg#ataque do player
						hp-=matkb4#ataque do monstro
						danoj[0:0]=[dmg]
					if event.key == K_s and mana > 0:
						dmg = (3 * lv) * random.randint(3, 5)
						matkb4 = random.randint(15,20)
						drawText("Joselito causou " + str(dmg) + " de dano", font3, windowSurface, (20), (300), WHITE)
						time.sleep(0.5)
						drawText(boss[3]+" causou " + str(matkb4)+ " de dano", font3, windowSurface, (670), (300), WHITE)
						time.sleep(0.5)
						hpb4-=dmg#habilidade
						hp-=matkb4#ataque do monstro
						mana-=1
						danojh[0:0]=[dmg]
					if mana <= 0 and event.key == K_s:
						drawText("Joselito está sem mana", font3, windowSurface, (20), (300), WHITE)
					drawText("HP: "+str(hp)+"/"+str(hpmax), font3, windowSurface, (360), (570), WHITE)#vida do jogador
					drawText("SP: "+str(mana)+"/"+str(manamax), font3, windowSurface, (360), (600), WHITE)#mana do jogador
					drawText(boss[3]+" HP: "+str(hpb4)+"/"+str(hpmaxb4), font3, windowSurface, (560), (570), WHITE)#vida do jogador
					if hp<=0:
						hp=0
						drawText("Joselito morreu!", font, windowSurface, (300),(200), RED)
						pygame.display.update()
						time.sleep(1.5)
						gameover()
					if hpb4<=0:
						drawText("Inimigo vencido!", font, windowSurface, (300),(200), WHITE)
						xp =random.randint(5, 20)
						exp+=xp
						drawText("Exp ganha: "+str(xp), font3, windowSurface, (300), (270), BLUE)
						pygame.display.update()
						drawText("Parabens, voce derrotou o dragao!", font3,windowSurface, (300), (270),RED)
						pygame.display.update()
						time.sleep(2.0)
						fght=False
						miss+=1
						nmapa()
						hp=hpmax
						up()
						savarq()
						pygame.quit()
						sys.exit()
					pygame.display.update()

				if event.key == K_ESCAPE: #aperta esc para sair
					savarq()
					pygame.quit()
					sys.exit()

pygame.display.update() #atualiza tela

sys.stdin.read(1)#não fecha a tela


