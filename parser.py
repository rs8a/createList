#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import threading
import m3u8
import os
from tqdm.auto import tqdm
import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf8')
scriptVersion = '1.1.1'
errorsDownloadList = { "dd" : "dd" }
errorsToMove = { "dd" : "dd" }
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
    print " "
    print "%s ┌──────────────────────────────────────────┐ %s" % (rColour, col.ENDC)
    for i in range(rPadding): print "%s │                                          │ %s" % (rColour, col.ENDC)
    print "%s │ %s%s%s │ %s" % (rColour, " "*(20-(len(rText)/2)), rText, " "*(40-(20-(len(rText)/2))-len(rText)), col.ENDC)
    for i in range(rPadding): print "%s │                                          │ %s" % (rColour, col.ENDC)
    print "%s └──────────────────────────────────────────┘ %s" % (rColour, col.ENDC)
    print " "

def printLong(rText, rColour=col.OKBLUE, rPadding=0):
    print " "
    print "%s ┌%s%s%s┐ %s" % (rColour, "─"*(20-(len(rText)/2)), "─"*(len(rText)+2),"─"*(20-(len(rText)/2)),col.ENDC)
    for i in range(rPadding): print "%s │ %s%s%s │ %s" % (rColour, " "*(20-(len(rText)/2)), " "*(len(rText)), " "*(40-(20-(len(rText)/2))-len(rText)), col.ENDC)
    print "%s │ %s%s%s │ %s" % (rColour, " "*(20-(len(rText)/2)), rText, " "*(40-(20-(len(rText)/2))-len(rText)), col.ENDC)
    for i in range(rPadding): print "%s │ %s%s%s │ %s" % (rColour, " "*(20-(len(rText)/2)), " "*(len(rText)), " "*(40-(20-(len(rText)/2))-len(rText)), col.ENDC)
    print "%s └%s%s%s┘ %s" % (rColour, "─"*(20-(len(rText)/2)), "─"*(len(rText)+2),"─"*(20-(len(rText)/2)),col.ENDC)
    print " "

def printx(rText, rColour=col.OKBLUE):
    print "%s │ %s %s" % (rColour, rText, col.ENDC)

def printxs(rText, rColour=col.OKBLUE):
    print " "
    print "%s │ %s %s" % (rColour, rText, col.ENDC)
    print " "
    
def printTop(rSize=5, rColour=col.OKBLUE, rPadding=0):
    print "%s ┌%s┐ %s" % (rColour, "─"*(rSize),col.ENDC)

def printMarkText( rText, rSize, rColour=col.OKBLUE, rPadding=0):
    print "%s │ %s%s │ %s" % (rColour, rText, " "*(rSize-len(rText)), col.ENDC)

def printEnd(rSize=5, rColour=col.OKBLUE, rPadding=0):
    print "%s └%s┘ %s" % (rColour, "─"*(rSize),col.ENDC)

def getMulDes():
	printLong('Ingrese la cantidad de descargas simultaneas', col.BOLD)
	return raw_input('cantidad:')

def getPath():
	printc('Ingrese el Path de descarga', col.BOLD)
	return raw_input('Path:')

def getUrlList():
	printc('Ingresa la URL de la lista m3u', col.BOLD)
	return raw_input('URL:')

def parserList(url):
	# try:
		printc('Archivos encontrados', col.BOLD)
		r = requests.get(url)
		m3u_master = m3u8.loads(r.text)
		urls = { "dd" : "dd" }
		urls.clear()
		for obj in m3u_master.data['segments']:
			#name = os.path.basename(obj['uri'])
			name = obj['title']
			urls[name] = obj['uri']
		for x in urls:
			printx(x)
	# except:
	# 	printc(" La url ingresada no es compatible con el programa ", col.FAIL)
	# else:
	# 	printc('La URL funciona a la perfeccion', col.OKGREEN, 2)

def downloadFileWithUrlAndPath(x, url, path, pos):
	chunk_size = 1024
	r = requests.get(url, stream = True)
	try:
		total_size = int(r.headers['content-length'])
		with open(x, 'wb') as f:
			for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = total_size/chunk_size, unit = 'KB', position=pos,leave=False,desc=x): f.write(data)
	except:
		errorsDownloadList[x] = url
		return True
		
	try:
		shutil.move(x, path+x)
	except:
		errorsToMove[x] = x

def downloadFromUrlAndPath2(urls,path):
	threads = list()
	index = 0
	for x in urls:
		hilo = threading.Thread(target=downloadFileWithUrlAndPath, args=(x, urls[x], path, index))
		index+=1
		threads.append(hilo)
		hilo.start()

	for index, thread in enumerate(threads):
		thread.join()
	else:
		printx("Bloque de descarga completado!", col.OKGREEN)
		print " "

def prepareFromUrlAndPath(urlList,path, mulDes):
	if mulDes < 1:
		printc("selecciona una cantidad de descargas", col.YELLOW)
		return
	r = requests.get(urlList)
	m3u_master = m3u8.loads(r.text)
	errorsDownloadList.clear()
	errorsToMove.clear()
	urls = { "dd" : "dd" }
	urls.clear()
	for obj in m3u_master.data['segments']:
		name = obj['title']
		urls[name] = obj['uri']
	printc("Archivos a descargar: " + str(len(urls)), col.CYAN)
	urlsToSend = { "dd" : "dd" }
	urlsToSend.clear()
	printc("Enviando Bloques para descarga", col.YELLOW)
	for index, x in enumerate(urls):
		if mulDes == 1:
			printx(str(index) + ': '+ x)
			urlsToSend[x] = urls[x]
			printx('Enviado para descarga', col.BOLD)
			downloadFromUrlAndPath2(urlsToSend,path)
			urlsToSend.clear()
		elif (index+1)%mulDes == 0 and urlsToSend:
			printx(str(index) + ': '+ x)
			urlsToSend[x] = urls[x] 
			printx('Enviado para descarga', col.BOLD)
			downloadFromUrlAndPath2(urlsToSend,path)
			urlsToSend.clear()
		else:
			urlsToSend[x] = urls[x] 
			printx(str(index) + ': '+ x)
	if urlsToSend:
		printx('Enviado para descarga', col.BOLD)
		downloadFromUrlAndPath2(urlsToSend,path)
		# downloadFromUrlAndPath2(urls,path)
	if errorsDownloadList:
		printLong("No se descargaron los siguientes archivos", col.FAIL)
		for x in errorsDownloadList:
			printx(' - \'' + x  + "\'", col.FAIL)
			printx('   \'' +errorsDownloadList[x] + "\'\n", col.FAIL)

	if errorsToMove:
		printLong("No se pudieron mover los siguientes archivos al directorio \'" + path + '\'', col.FAIL)
		for x in errorsToMove:
			printx("\'" + x + "\', pero se descargo correctamente", col.FAIL)
		dirpath = os.getcwd()
		printx('podes buscarlo en: \'' + dirpath + "\'", col.WARNING)
	printc("Se descargaron: " + str(len(urls)-len(errorsDownloadList)) + '/' + str(len(urls)), col.OKGREEN)

os.system('clear')
print "\n  === %sM3U8 Parser V %s - RS8A Parser%s ===" % (col.HEADER, scriptVersion, col.ENDC)
mulDes = 5
path= os.getcwd()+'/'
urlList = getUrlList()
i = -1
os.system('clear')
while i < 0:
	mulSt = str(mulDes)
	mostL = 10 
	if len(mulSt) > len(path):  
		mostL = 33+len(mulSt) 
	elif len(path) > len(urlList):
		mostL = 33+len(path)
	else:
		mostL = 33+len(urlList)
	printc("M3U8 Parser V " + scriptVersion +" - RS8A PARSER ", col.CYAN)
	printTop(mostL+2, col.YELLOW)
	printMarkText('Cantidad de descarga simultaneas: ' + str(mulDes) + " ", mostL, col.YELLOW)
	printMarkText('Path de descarga seleccionado: \'' + path + "\'", mostL, col.YELLOW)
	printMarkText('URL Ingresada: \'' +  urlList + "\'", mostL, col.YELLOW)
	printEnd(mostL+2, col.YELLOW)
	mostL = 49
	printTop(mostL+2, col.DEFAULT)
	printMarkText('Opcion 0: Limpiar Pantalla', mostL, col.DEFAULT)
	printMarkText('Opcion 1: Probar URL', mostL, col.DEFAULT)
	printMarkText('Opcion 2: Cambiar URL', mostL, col.DEFAULT)
	printMarkText('Opcion 3: Cambiar Path', mostL, col.DEFAULT)
	printMarkText('Opcion 4: Cambiar Numero de descargas simultaneas', mostL, col.DEFAULT)
	printMarkText('Opcion 5: Descargar archivos desde URL', mostL, col.DEFAULT)
	printMarkText('Opcion S: Salir', mostL, col.DEFAULT)
	printEnd(mostL+2, col.DEFAULT)
	print " "
	op = raw_input('Elige una opcion:')
	if op == '0':
		os.system('clear')
	elif op == '1':
		parserList(urlList)
	elif op == '2':
		urlList = getUrlList()
		os.system('clear')
	elif op == '3':
		path = getPath()
		os.system('clear')
	elif op == '4':
		mulDes = int(getMulDes())
		os.system('clear')
	elif op == '5':
		os.system('clear')
		prepareFromUrlAndPath(urlList,path,mulDes)
		i = 1
	elif op.upper() == 'S':
		i = 1
		os.system('clear')
	else:
		printc('Esa opcion no existe')

printc("ADIOS!", col.CYAN)
