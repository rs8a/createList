#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, shutil

rsMainPath = "/home/geshtue"
rsURL = "https://raw.githubusercontent.com/rs8a/createList/master/parser.py"
rsUpdateURL = "https://raw.githubusercontent.com/rs8a/createList/master/update.py"
scriptVersion = '1.0.2'
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

def printc(rText, rColour=col.OKBLUE, rPadding=0):
    print "%s ┌──────────────────────────────────────────┐ %s" % (rColour, col.ENDC)
    for i in range(rPadding): print "%s │                                          │ %s" % (rColour, col.ENDC)
    print "%s │ %s%s%s │ %s" % (rColour, " "*(20-(len(rText)/2)), rText, " "*(40-(20-(len(rText)/2))-len(rText)), col.ENDC)
    for i in range(rPadding): print "%s │                                          │ %s" % (rColour, col.ENDC)
    print "%s └──────────────────────────────────────────┘ %s" % (rColour, col.ENDC)
    print " "

def printx(rText, rColour=col.OKBLUE):
    print "%s │ %s %s" % (rColour, rText, col.ENDC)

def prepare():
    if not os.path.exists(rsMainPath):
        try:
            os.mkdir(rsMainPath)
            os.mkdir(rsMainPath+'/tmp')
        except :
            printx("Error al crear la carpeta del entorno automaticamente", col.FAIL)
            printx("Antes de continuar crea la carpeta con el comando:", col.FAIL)
            printc("mkdir "+rsMainPath, col.FAIL)
            return False
    printc("Preparando Entorno")
    os.system('apt install python-pip -y')
    printc("Instalando libreria requests")
    os.system('pip install requests')
    printc("Instalando libreria M3U8")
    os.system('pip install m3u8')
    printc("Instalando libreria tqdm")
    os.system('pip install tqdm')
    printc("Instalando libreria wget")
    os.system('pip install wget')
    os.system('wget -q -O "%s/parser.py" "%s"' % (rsMainPath,rsURL))
    os.system('wget -q -O "%s/update.py" "%s"' % (rsMainPath,rsUpdateURL))
    printc("Configuracion completa!", col.BOLD)
    printx("Para actualizar el script usa el comando:", col.OKGREEN)
    printc("sudo python "+rsMainPath + "/update.py", col.OKGREEN, 2)
    printx("Para correr el script usa el comando:", col.OKGREEN)
    printc("sudo python "+rsMainPath + "/parser.py", col.OKGREEN, 2)


if __name__ == "__main__":
    printc("M3U8 Parser V " + scriptVersion + " - RS8A Installer", col.HEADER, 1)
    print "%s │ NOTA:  Script para descargar archivos de listas M3U8 %s" % (col.HEADER, col.ENDC)
    print "%s │ DESARROLLADO POR: R.San.8a %s" % (col.HEADER, col.ENDC)
    print " "
    prepare()
 
