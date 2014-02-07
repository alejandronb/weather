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
	final = "%sq=%s,spain" % (direccion,ciudades[consulta])
	print final
	peticion = requests.get(final)
	print peticion
#Trabajar con json.loads



#params={'q':%'s,spain' % capital}

print "La temparatura actual de %s es grados centígrados" % ciudades[consulta]
