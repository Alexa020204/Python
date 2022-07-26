import msvcrt
from random import *

arreglo=[]
i=0

while i<20:
    arreglo.append(randint(15,86))
    i=i+1

print("**"*10 + "Quinto ejercicio" +"**"*10)
print("Arreglo de forma descendente: \n {}".format(sorted(arreglo,reverse=True)))
print("***"*20)
print("Arreglo Original: \n {}".format(arreglo))

msvcrt.getch()