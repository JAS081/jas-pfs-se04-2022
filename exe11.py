#Autor: Javier de Andrés
#Versión: 0.01
#data: 09/03/2022

#declarar variables
print(" Lee un número por teclado que pida el precio de un productoy calcule el precio final con IVA")
qprecio = float(input("Introduzca el precio:"))

#proceso
qpreciototal = qprecio + float(qprecio * 0.21)
print("El precio con IVA es: " + str(qpreciototal))
