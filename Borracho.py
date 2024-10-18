import random as r
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

#variables
texitos = 0 #Almacena el total de exitos
#variables de la grafica
fig, ax = plt.subplots()
aux = 0 #valor auxiliar para calcular el numero de iteraciones
#pedir valores por consola 
n = int(input("¿Cuantas veces quieres hacer la simulación? "))


for i in range(n):
    #variables para la tabla
    tabla = [[]]
    iteraciones_n= [] 
    iteraciones = [] 
    num_ale_gen = []
    exito= [] 
    valoresxy = []
    #variables de la grafica
    xl = [0]
    yl = [0]
    ax.plot([-5,5],[0,0], c='black')#plano
    ax.plot([0,0],[-5,5], c='black')#cartesiano

    x = 0
    y = 0
    #ciclo para las 10 cuadras
    for j in range(10):
        #generar puntos en la tabla :
        xa = x
        ya = y
        ax.step(xl,yl,"r")
        ax.step(xl,yl,"ro")
        a = ax.step(xa,ya,"bo")
        iteraciones_n.append("-")
        exito.append("-")
        iteraciones.append(j+1)
        #generar valor aleatorio
        valor  =r.random()
        num_ale_gen.append(valor)
        #aplicando el método de montecarlo
        if(valor < 0.25):
            y = y +1 
            valoresxy.append(f"({x},{y})")
        elif(valor < 0.50):
            y = y-1
            valoresxy.append(f"({x},{y})")
        elif(valor < 0.75):
            x = x+1
            valoresxy.append(f"({x},{y})")
        else:
            x = x-1
            valoresxy.append(f"({x},{y})")
        #agregar los valores de x y y a una lista
        xl.append(x)
        yl.append(y)
        #velocidad de generado de la grafica
        plt.pause(0.01)
    
    ax.step(xl,yl,"r")
    ax.step(xl,yl,"ro")
    a = ax.step(x,y,"bo")
    plt.pause(0.01)
    vexito = abs(x) + abs(y)
    #Calcular el exito
    if(vexito >= 2):
        exito[9] = "SI"
        texitos += 1
    else:
        exito[9] = "NO"
        
    #Calcular las iteraciones de N
    iteraciones_n[0] = i+1
    #Generar tabla
    for k in range(j+1):
        tabla = tabla + [[iteraciones_n[k], iteraciones[k], num_ale_gen[k], valoresxy[k], exito[k]]]
    #Imprimir tabla 
    print(tabulate(tabla, headers=["N", "# de cuadras\n recorridas", "numero aleatorio", "localización\n(x,y)","exito?"]))
    print()
    #limpiar grafica en cada iteración
    if (i != n-1):
        ax.clear()

#imprimir el numero de exitos
print(f'El borracho se desplazo dos cuadras {texitos} veces ')
porcentaje = (texitos*100) / n
print(f'Lo que representa el {int(porcentaje)}% de las {n} simulaciones')
#mostrar grafica
plt.show()