import msvcrt
lista_numeros=[]

print("**"*10 + "Segundo ejercicio" +"**"*10)
cant=int(input("Ingrese la cantidad de números: "))
print("Ingrese los  números: ")
try:
    for i in range(cant):
       num=int(input())
       lista_numeros.append(num)

    num_mayor=max(lista_numeros)
    cant_mayor=lista_numeros.count(num_mayor)

    print(f"El número mayor es: {num_mayor} y las veces que fue ingresado son: {cant_mayor}")
except:
    print("El valor no es permitido")

msvcrt.getch()