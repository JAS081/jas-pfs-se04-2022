#Autor: Javier de Andrés
#Versión: 0.01
#data: 09/03/2022

#declarar variables
numventas = (int(input("Introduzca el número total de ventas: ")))
sumventas = 0

#proceso
for i in range(numventas):
    qventa = float(input("Importe Venta " + str(i + 1) + ": "))
    sumventas = float(sumventas) + float(qventa)
print("El importe total de las " + str(numventas) + " ventas es: " + str(sumventas))
