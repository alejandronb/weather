#coding: utf-8
import requests
import json

direccion = "http://api.openweathermap.org/data/2.5/weather?" #q=London,uk
ciudades = {"1":"Almería","2":"Cádiz","3":"Córdoba","4":"Granada","5":"Huelva","6":"Jaén","7":"Málaga","8":"Sevilla"}

print """1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla"""


consulta = raw_input("Introduce el número de la ciudad a consultar: ")

if consulta in ciudades:
	final = "%sq=%s,spain" % (direccion,ciudades[consulta]) #Esto construye la dirección de la API completa
	peticion = requests.get(final)
	json = json.loads(peticion.text)
	temperatura = json["main"]["temp"] #Con esta línea cogemos lo que nos interesa del fichero json
	celsius = round(temperatura - 273,1)

print "La temperatura actual de %s es %s grados centígrados" % (ciudades[consulta],celsius)
