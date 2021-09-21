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

#ej3
num_obre = int(input("Digite el numero de obreros: "))
for i in range(1, num_obre+1):
    nhoras = float(input(f"Digite el numero de horas trabajadas del {i} trabajador: "))
    if(nhoras <= 40):
        salario = 20 * nhoras
    else:
        nhoras_extras = nhoras - 40
        salario = 40 * 20 + nhoras_extras * 25
    print(f"El salario del obrero {i} es: ${salario}")
    
#ej4

#ej5
minimo = 9999
numeros = int(input("¿Cuantos numeros desea ingresar?: "))
for i in range (1, numeros+1):
    num = int(input(f"Digite su {i} numero: "))
    if num < minimo:
        minimo = num
    print(f"El numero menor es: {minimo}")