#Autor: Javier de Andrés
#Versión: 0.01
#data: 09/03/2022

#declarar variables
print("Lee un número por teclado e indica si es divisible entre 2 o no")
qnumero = float(input("Introduzca un número: "))

#proceso
if (qnumero % 2) == 0:
    print("El número " + str(qnumero) + " Si lo es")
else:
    print("El número " + str(qnumero) + " No lo es")
