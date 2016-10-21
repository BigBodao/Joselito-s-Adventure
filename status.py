#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random

potv=10
#
# DEFININDO LEVEL E STATUS DE JOSELITO
#
lv = 1 #nível de joselito
hpmax = 10 * (lv + 1) #definindo a quantidade de joselito baseado em seu nível
hp = hpmax #hp de joselito
manamax = 5 * (lv + 1) #definindo a quantidade de mana de joselito baseado em seu nível
mana = manamax #mana de joselito
exp = 0 #quantidade de experiencia de joselito
exp_max = 8 * (lv + 1) # definindo a capacidade máxima de experiencia baseado em seu nível
#inicio das variáveis de inimigos
#zumbi
hpm1=20 #hp do monstro
hpmaxm1=20 #hp max do monstro
matkm1=random.randint(1,3)
#goblin
hpm2=25 #hp do monstro
hpmaxm2=25 #hp max do monstro
matkm2=random.randint(3,6)
#morcego
hpm3=30 #hp do monstro
hpmaxm3=30 #hp max do monstro
matkm3=random.randint(7,9)
#orc
hpm4=40 #hp do monstro
hpmaxm4=40 #hp max do monstro
matkm4=random.randint(11,13)
#inicio das variáveis dos boss
#cavaleiro
hpb1=30 #hp do boss
hpmaxb1=30 #hp max do boss
matkb1=random.randint(4,10)
#arvore do capeta
hpb2=35 #hp do boss
hpmaxb2=35 #hp max do boss
matkb2=random.randint(6,10)
#troll
hpb3=40 #hp do boss
hpmaxb3=40 #hp max do boss
matkb3=random.randint(10,15)
#dragão
hpb4=50 #hp do boss
hpmaxb4=50 #hp max do boss
matkb4=random.randint(15,20)
