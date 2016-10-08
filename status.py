#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random

#
# DEFININDO LEVEL E STATUS DE JOSELITO
#
lv = 1
hpmax = 10 * (lv + 1)
hp=hpmax
exp = 0
exp_max = 10 * (lv + 1)

hpm1=20
hpmaxm1=20
matk1=random.randint(1,3)

hpm2=25
hpmaxm2=25
matk2=random.randint(2,5)

hpm3=30
hpmaxm3=30
matk3=random.randint(3,8)

hpm4=40
hpmaxm4=40
matk4=random.randint(4,10)

hpb1=60
hpmaxb1=60
matkb1=random.randint(5,20)


#
# INICIANDO LEVEL UP
#
if exp >= exp_max:
	lv = lv + 1
	exp = 0
#
# CONDIÇÕES DE COMBATE
#
dmg = 5 * random.randint(1, 3)
hab1 = 3 * random.randint(2,8)


'''            print ("A) - Ataque fraco")
            print ("B) - Ataque fraco")
            player_h = str(raw_input(" Qual habilidade deseja usar: ")).lower()
            if player_h == "a":
            dmg = 2 * random.randint(1, 3)
            print ("Player atacou")
            print (dmg)
            print ("")
            if player_h == "b":
            dmg = 2 * random.randint(3, 6)
            print ("Player atacou")
            print (dmg)
            print ("")
        time.sleep(2)
        hp = hp - 4
#momento em que o inimigo ataca
#
# QUANDO HP DO PLAYER CHEGAR A ZERO ALTERA VIVO PARA 0 QUEBRANDO O LOOP
#
    if hp == 0:
        print ("Você faleceu")
        vivo = 0
        break'''
