import msvcrt

bultos=[]
pesos=[]
dolares=[]
i=0

print("**"*10 + " Decimo ejercicio "+"**"*10)
while i < 15:
    print("Ingrese el peso del bulto en kg:")
    peso_bulto=int(input())
    i=i+1
    if peso_bulto <=500:
       
        bultos.append(peso_bulto)
        
        if peso_bulto <=25:
            valor_bulto=0
        elif 26<=peso_bulto<=300:
            valor_bulto=1500*peso_bulto
            valor_dolar=valor_bulto*4400
            pesos.append(valor_bulto)
            dolares.append(valor_dolar)
        else  :
            valor_bulto=2500*peso_bulto
            valor_dolar=valor_bulto*4400
            pesos.append(valor_bulto)
            dolares.append(valor_dolar)
            
    else:
        print("El peso del bulto no es permitido")
        i=i-1

cantidad=len(bultos)
pesado=max(bultos)
liviano=min(bultos)
promedio=(sum(bultos)/15)
peso_total=sum(pesos)
dolar_total=sum(dolares)

print("***"*20)
print("Tabla de Seguimiento \n")
print("{:<20} {:<20} {:<10}".format("Número de Bultos","|",cantidad))
print("{:<20} {:<20} {:<10}".format("Bulto más pesado","|",pesado))
print("{:<20} {:<20} {:<10}".format("Búlto más liviano","|",liviano))
print("{:<20} {:<20} {:<10,.2f}".format("Peso Promedio Bultos","|",promedio))
print("{:<20} {:<20} {:<10}".format("Ganancia en Pesos","|",peso_total))
print("{:<20} {:<20} {:<10}".format("Ganacia en Dolares","|",dolar_total))

msvcrt.getch()