import msvcrt
import numpy as np
from random import *

A = np.empty(20, dtype="int")

i = 0
while i < 20:
      A[i] = randint(0,10)
      i += 1

b=A[(A==0)]
a=A[(A!=0)]

b=np.append(a,b)

print("**"*10 + " Septimo ejercicio "+"**"*10)
print("Arreglo con los ceros al final")
print(b)
print("***"*20)
print("Arreglo original")
print(A)

msvcrt.getch()