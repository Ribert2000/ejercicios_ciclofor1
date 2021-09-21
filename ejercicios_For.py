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
    
#ej6
for i in range (5):
    pesoAn = int(input(f"Digite su peso anterior perona {i+1}: "))
    pesoAc = int(input(f"Digite su peso actual persona {i+1}: "))  
    if(pesoAn < pesoAc):
        print("Subio!")
    else:
        pesoAc < pesoAn
        print("Usted bajo de peso!")
        
#ej7

#eje8
precioA = int(input("Digite el precio de los asientos: "))
numC = int(input("Digite el numero de clientes: "))
edad514 = 0
edad1519 = 0
edad2045 = 0
edad4665 = 0
edad66 = 0

for i in range (1, numC + 1):
    edad = int(input(f"Digite la edad persona {i}: "))
    
    porcentaje1 = precioA * 0.35
    porcentaje2 = precioA * 0.25
    porcentaje3 = precioA * 0.10
    
    if (edad >= 5 and edad <= 14):
        edad514 += porcentaje1
    if (edad >= 15 and edad <= 19):
        edad1519 += porcentaje2
    if (edad >= 20 and edad <= 45):
        edad2045 += porcentaje3
    if (edad >= 46 and edad <= 65):
        edad4665 = porcentaje2
    if (edad >= 66):
        edad66 += porcentaje1 
        
        print(f"El teatro dejo de percibir en el rango de 5 - 14:  {edad514}")
        print(f"El teatro dejo de percibir en el rango de 15 - 18: {edad1519}")
        print(f"El teatro dejo de percibir en el rango de 20 - 45: {edad2045}")
        print(f"El teatro dejo de percibir en el rango de 46 - 65: {edad4665}")
        print(f"El teatro dejo de percibir en el rango de 66:      {edad66}")
        
#eje9
sumatoria1 = 0
sumatoria2 = 0
sumatoria3 = 0
sumatoria4 = 0
sumatoria5 = 0



for i in range (100):
    
    valorV = random.randint(0, 180000000)

    #vendido = int(input("Digite el valor vendido por la persona {i}"))
    
    if (valorV < 20000000):
        sumatoria1 += (valorV * 0.10)
    if (valorV >= 20000000 and valorV < 40000000):
        sumatoria2 += (valorV * 0.15)
    if (valorV >= 40000000 and valorV < 80000000):
        sumatoria3 += (valorV * 0.20)
    if (valorV >= 80000000 and valorV < 160000000):
        sumatoria4 += (valorV * 0.25)
    if (valorV >= 1600000000):
        sumatoria5 += (valorV * 0.30)
        
#ej10
votantes = int(input("Digite cuantos votantes son: "))

contador1 = 0
contador2 = 0
contador3 = 0

for i in range (1, votantes+1):
    ref_candidato = int(input(f"Persona {i} digite el numero del candidato que obtendra su voto, sea 1, 2 o 3: "))
    if (ref_candidato == 1):
        contador1 = contador1 + 1
    elif (ref_candidato == 2):
        contador2 = contador2 + 1
    elif (ref_candidato == 3):
        contador3 = contador3 + 1
if (contador1 > contador2 and contador1 > contador3):
    print(f"El candidato electo fue el 1 con {contador1} votos")
if (contador2 > contador1 and contador2 > contador3):
    print(f"El candidato electo fue el 2 con {contador2} votos")
if (contador3 > contador2 and contador3 > contador1):
    print(f"El candidato electo fue el 3 con {contador3} votos")
if (contador1 == contador2 and contador1 == contador3 and contador3 == contador2):
    print(f"Hubo empate con {contador1} votos")


        
