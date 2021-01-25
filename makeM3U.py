#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    CYAN = "\033[36m"
    FAIL = '\033[91m'
    YELLOW = '\033[33m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEFAULT = "\033[39m"
def printx(rText, rColour=col.OKBLUE):
    print "%s │ %s %s" % (rColour, rText, col.ENDC)

preffix = raw_input("Ingrese el nombre del archivo: ")
isBad = True
while isBad:
    printx("La direccion princial es a donde apunta el archivo",col.WARNING)
    printx('Ejemplo: https://dominio.com/peliculas/',col.WARNING)
    domain = raw_input("Ingrese la direccion principal: ")
    printx("Es importante haber agregado la \"/\" al final de la direccion",col.YELLOW)
    printx("Su direccion es:", col.YELLOW)
    printx(domain, col.OKBLUE)
    preg = raw_input("Esto es correcto? (N para volver a ingresar la direccion):")
    if preg != 'N' and preg != 'n':
        print preg
        isBad = False

result = []
fileResult = []
flist = os.listdir('.')
for mfile in flist:
    if (mfile.endswith(".txt") != True) and (mfile.endswith(".py") != True):
        result.append(mfile)
with open(preffix+".m3u", "w") as txt_file:
    txt_file.write("#EXTM3U" + "\n")
    for mfile in result:
        filename = "#EXTINF:0," + mfile + '\n' + domain + mfile + "\n"
        fileResult.append(filename)
        txt_file.write(filename)
printx("El archivo \"" + preffix + ".m3u\" se creo con exito", col.OKGREEN)
