#!/usr/bin/python
# -*- coding: utf-8 -*-

# Jesús Galán Barba
# Ing. en Sitemas de Telecomunicaciones

print "\nEjercicio 13.5: Ficheros, diccionarios y excepciones\n"

fd = open("/etc/passwd","r")
lineas = fd.readlines()
usuarios = {}

for linea in lineas:
	trozos_linea = linea.split(':')
	usuario = trozos_linea[0]
	shell = trozos_linea[-1]
	usuarios[usuario] = shell

fd.close()

try:
	claves = ['root','imaginario']
	for clave in claves:
		shell_diccionario = usuarios[clave]
		print "Usuario:", clave, "=> Shell:", shell_diccionario[0:-1]

except KeyError:
	print "ERROR: Usuario '", clave, "' no encontrado en el diccionario"
