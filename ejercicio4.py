import msvcrt
from random import *

print("**"*10 + "Cuarto ejercicio" +"**"*10)
print("Ingrese una cantidad de números: ")
cant= int(input())
cont=0
lista=[]

while cont<cant:
    n= randint(1,100)
    lista.append(n)
    cont=cont+1

mayor=max(lista)
menor=min(lista)
suma=sum(lista)
promedio=suma/cant
print("La lista de números es: {} \n El número mayor es: {} \n El número menor es: {} \n El promedio de los números es: {:.2f}".format(lista,mayor,menor,promedio))

msvcrt.getch()