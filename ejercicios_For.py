# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:27:50 2021

@author: riber
"""

import random

#eje1
numA = int(input("Digite el numero de autos: "))

for i in range (1, numA + 1):
    digito = int(input(f"Digite el ultimo digito de el {i} auto: "))
    if (digito == 1 or digito == 2):
        print(f" EL {i} auto tiene su calcomania Amarilla")
        
    if (digito == 3 or digito == 4):
        print(f" EL {i} auto tiene su calcomania Rosa")
    if (digito == 5 or digito == 6):
        print(f" EL {i} auto tiene su calcomania Roja")
    if (digito == 7 or digito == 8):
        print(f" EL {i} auto tiene su calcomania Verde")
    if (digito == 9 or digito == 0):
        print(f" EL {i} auto tiene su calcomania Azul")
        
#ej2