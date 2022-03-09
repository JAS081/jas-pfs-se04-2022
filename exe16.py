#Autor: Javier de Andrés
#Versión: 0.01
#data: 09/03/2022

#declarar variables
qdia = str(input("Dime un día de la semana: "))
Jornada = "tipo"

#proceso
if (qdia.upper() == "LUNES"):
    Jornada = "laboral"
if (qdia.upper() == "MARTES"):
    Jornada = "laboral"
if (qdia.upper() == "MIERCOLES") | (qdia.upper() == "MIÉRCOLES"):
    Jornada = "laboral"
if qdia.upper() == "JUEVES":
    Jornada = "laboral"
if qdia.upper() == "VIERNES":
    Jornada = "laboral"
if (qdia.upper() == "SABADO") | (qdia.upper() == "SÁBADO"):
    Jornada = "no laboral"
if qdia.upper() == "DOMINGO":
    Jornada = "no laboral"

    print("El día " + str(qdia) + " es " + Jornada)

