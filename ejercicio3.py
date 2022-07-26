import msvcrt

print("**"*10 + "Tercer ejercicio" +"**"*10)
print("Ingrese un número primo: ")
cant=int(input())
cont=0
i=2
lista=[]
def primos(n):
    for i in range (2,n):
        if n%i==0:
            return False
    return True

while cont<cant:
    if primos(i) :
        lista.append(i)
        cont=cont+1
    i=i+1

print(lista)

msvcrt.getch()