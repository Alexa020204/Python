import msvcrt

print("**"*10 + "Primer ejercicio" +"**"*10)
cant=int(input("Ingrese la cantidad de números que quiere sumar: "))
acum_suma=0
acum_positivos=0
acum_negativo=0
print("Ingrese los números")

for i in range(cant):
    num=int(input())
    acum_suma=acum_suma+num
    if num>=0:
        acum_positivos=acum_positivos+num
    else:
        acum_negativo=acum_negativo+num



print(f"La suma total de números es {acum_suma} \n La suma de los números positivos es {acum_positivos} \n La suma de los números negativos es {acum_negativo}")   

msvcrt.getch()