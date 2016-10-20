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
#goblin
hpm2=25 #hp do monstro
hpmaxm2=25 #hp max do monstro
#morcego
hpm3=30 #hp do monstro
hpmaxm3=30 #hp max do monstro
#orc
hpm4=40 #hp do monstro
hpmaxm4=40 #hp max do monstro
#inicio das variáveis dos boss
#cavaleiro
hpb1=60 #hp do boss
hpmaxb1=60 #hp max do boss
#arvore do capeta
hpb2=65 #hp do boss
hpmaxb2=65 #hp max do boss
#troll
hpb3=70 #hp do boss
hpmaxb3=70 #hp max do boss
#dragão
hpb4=80 #hp do boss
hpmaxb4=80 #hp max do boss
