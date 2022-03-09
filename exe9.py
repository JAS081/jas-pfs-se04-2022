#Autor: Javier de Andrés
#Versión: 0.01
#data: 09/03/2022

import math
#declarar variables
print("El área de un círculo según su radio.")
radio = float(input("Introduzca el valor del radio: "))

#proceso
qpi = math.pi
area = qpi * (math.pow(radio, 2))
print("El área es: " + str(area))

