#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random

inim=["Zumbi","Slime","Vampiro","Orc"]
boss=["Cavaleiro","Ent","Lobisomen","Dragão"]
potv=10
danoj=[]
danojh=[]

#
# DEFININDO LEVEL E STATUS DE JOSELITO
#
lv = 1 #nível de joselito
hpmax = 8 * (lv + 1) #definindo a quantidade de vida baseado em seu nível
hp = hpmax #hp de joselito
manamax = 3 * (lv + 1) #definindo a quantidade de mana de joselito baseado em seu nível
mana = manamax #mana de joselito
exp = 0 #quantidade de experiencia de joselito
exp_max = 0
exp_max = 8 * (lv + 1) + exp_max # definindo a capacidade máxima de experiencia baseado em seu nível
#inicio das variáveis de inimigos
#zumbi
hpm1=30 #hp do monstro
hpmaxm1=30 #hp max do monstro
matkm1=random.randint(1,3)
#slime
hpm2=50 #hp do monstro
hpmaxm2=50 #hp max do monstro
matkm2=random.randint(3,6)
#vampiro
hpm3=70 #hp do monstro
hpmaxm3=70 #hp max do monstro
matkm3=random.randint(7,9)
#orc
hpm4=90 #hp do monstro
hpmaxm4=90 #hp max do monstro
matkm4=random.randint(11,13)
#inicio das variáveis dos boss
#cavaleiro
hpb1=40 #hp do boss
hpmaxb1=40 #hp max do boss
matkb1=random.randint(4,10)
#arvore do capeta
hpb2=60 #hp do boss
hpmaxb2=60 #hp max do boss
matkb2=random.randint(6,10)
#lobisomen
hpb3=80 #hp do boss
hpmaxb3=80 #hp max do boss
matkb3=random.randint(10,15)
#dragão
hpb4=100 #hp do boss
hpmaxb4=100 #hp max do boss
matkb4=random.randint(15,20)
