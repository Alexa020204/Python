import msvcrt
import numpy as np
from random import *

i=0

print("**"*10 + " Noveno ejercicio "+"**"*10)
print("Un arreglo tiene tamaño axb, siendo a el números de filas y b el de columnas. Indique el tamaño que desee")
print("Ingrese a: ")
a = int(input())
print("Ingrese b: ")
b = int(input())
arr=np.random.randint(1,50,size=(a,b))

print("Ingrese el número que quiere buscar en el arreglo")
num=int(input())
result= num in arr
if result is True:
    print("El número se encuntra en el arreglo")
else:
    print("El número no se encuentra en el arreglo")

print("***"*20)
print("El arreglo es el siguiente: ")
print(arr) 

msvcrt.getch()