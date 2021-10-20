#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, shutil, wget

rsMainPath = "/home/geshtue"
rsURL = "https://raw.githubusercontent.com/rs8a/createList/master/parser.py"
rsUpdateURL = "https://raw.githubusercontent.com/rs8a/createList/master/update.py"
rsInstallerURL = "https://raw.githubusercontent.com/rs8a/createList/master/installParser.py"

scriptVersion = '1.0.3'
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
    printx("i Iniciando Actualización!\n", col.WARNING)
    try:
        os.system("rm -rf "+rsMainPath+"/parser.py")
        os.system("rm -rf "+rsMainPath+"/update.py")
        os.system("rm -rf "+rsMainPath+"/update.py")
        wget.download(rsURL, rsMainPath)
        wget.download(rsUpdateURL, rsMainPath)
        wget.download(rsInstallerURL, rsMainPath)
    except:
        printx("✗ Error al actualizar los scripts\n", col.FAIL)
        return False
    print " \n"
    printx("✔ Actualización completa!\n", col.OKGREEN)
    printx("Para actualizar el script usa el comando:", col.BOLD)
    printc("sudo python "+rsMainPath + "/update.py", col.WARNING)
    printx("Para correr el script usa el comando:", col.BOLD)
    printc("sudo python "+rsMainPath + "/parser.py", col.WARNING)

if __name__ == "__main__":
    print "\n  === %sM3U8 Parser V %s - RS8A updater%s ===" % (col.HEADER, scriptVersion, col.ENDC)
    print "  === %sDESARROLLADO POR: R.San.8a %s ===\n" % (col.HEADER, col.ENDC)
    prepare()
    printc("ADIOS!", col.CYAN)
