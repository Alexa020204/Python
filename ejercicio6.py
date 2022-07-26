import msvcrt
import numpy as np
from random import *

A = np.empty(10, dtype="int")
B = np.empty(10, dtype="int")
i = 0
while i < 10:
      A[i] = randint(200,1000)
      i += 1

while i < 10:
    B[i]= randint(200,1000)
    i+=1


print("**"*10 + " Sexto ejercicio "+"**"*10)
print("Arreglos originales")
print("A = ", A)
print("B = ", B)

b=A[(A%2!=0)]
a=B[(B%2==0)]

A=a 
B=b

print("***"*20)
print("Arreglos Actuales")
print("A = ", A)
print("B = ", B)

msvcrt.getch()