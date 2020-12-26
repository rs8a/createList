#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
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
    
def printc(rText, rColour=col.OKBLUE):
    print "%s%s%s" % (rColour, rText, col.ENDC)

os.system('clear')
print ""
printc("┌───────────────────────────────────────────────────────────┐")
printc("│   Instrucciones:                                          │")
printc("│   Ingresa el nombre generico por el que vas a sustituir   │")
printc("│   los nombres de tus archivos.                            │")
printc("│   Dicho nombre se utilizara como prefijo del archivo      │")
printc("│   Ejemplo:                                                │")
printc("│                                                           │")
printc("│   Nombre generico asignado: \033[39m\033[1mvideo_serie_tal\033[0m\033[94m               │")
printc("│   Resultado:                                              │")
printc("│   \033[92mvideo_serie_tal_0000001.mp4\033[0m\033[94m                             │")
printc("│   \033[92mvideo_serie_tal_0000002.mp4\033[0m\033[94m                             │")
printc("│   \033[92mvideo_serie_tal_0000003.mp4\033[0m\033[94m                             │")
printc("│   \033[92m.                                                       │")
printc("│   \033[92m.                                                       │")
printc("│   \033[92m.                                                       │")
printc("│   \033[92mvideo_serie_tal_9999999.mp4\033[0m\033[94m                             │")
printc("│                                                           │")
printc("│   Los archivos \033[91m\033[4m\033[1m.txt y .py \033[0m\033[94mno se veran afectados.          │")
printc("│   Todos los demas archivos sin importar su extencion si,  │")
printc("│   intenta mantener solo los archivos que necesitas        │")
printc("│   modificar.                                              │")
printc("└───────────────────────────────────────────────────────────┘")
print ""
preffix = raw_input("ingrese el nombre generico: ")
flist = os.listdir('.')
ignoredFiles = []
count = 0
for mfile in flist:
    if mfile.endswith(".txt") or mfile.endswith(".py"):
        ignoredFiles.append(mfile)
    else:
        count+=1
        print ""
        printc("  From: \033[1m" + mfile, col.HEADER)
        printc("    To: \033[1m" + preffix + "_" + '{:07d}'.format(count) + "."+ mfile.split(".")[-1], col.OKGREEN)
        os.rename(mfile, preffix + "_" + '{:07d}'.format(count) + "."+ mfile.split(".")[-1])

print ""
for mfile in ignoredFiles:
    printc("││  ignored: \033[1m" + mfile, col.FAIL)
print ""