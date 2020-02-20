'''
Created on 4 feb. 2020

@author: Jonathan Isso Zuich
'''
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo import MongoClient
from _hashlib import new
from pymongo import collection
from pprint import pprint 
from pymongo import MongoClient, ReadPreference
from pymongo.client_session import ClientSession
import glob, os
from idlelib.iomenu import encoding
from enum import Enum
from ctypes.test.test_pickling import name
from cgitb import text
from collections import Counter
from _overlapped import NULL
from collections import OrderedDict
import random
import collections
from itertools import islice
from test.test_configparser import SortedDict
import numpy as np
import matplotlib.pyplot as plt
from math import log
from matplotlib._layoutbox import align
from numpy.ma.core import sort
from test.test_typing import Label
import re
from distutils.command.clean import clean

client = pymongo.MongoClient ("mongodb+srv://issojonathan:Uy123123@jonathanisso-er8ve.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('colectionML')

records = db.documents
records.find()
collection_taxonomy = db['collection']
db = client.colectionML

numero = 0
for file in os.listdir("C:\\Users\\Hsbc\\Desktop\\coleccion_2020"):
    if file.endswith(".txt"):
        
        pathArchivo = (os.path.join("C:\\Users\\Hsbc\\Desktop\\coleccion_2020", file))
        a = open(pathArchivo, encoding="utf-8-sig")
        contenidoArchivo = a.read().lower()
        contenidoArchivo = re.sub('\W+', ' ', contenidoArchivo)
        contenidoArchivo = re.sub(r'[0-9]+', ' ', contenidoArchivo)
        contenidoArchivo = re.sub('_', ' ', contenidoArchivo)
        contenidoArchivo = re.sub(' a ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' a ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' al ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' asi ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' con ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' cual ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' cuales ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' cuan ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' de ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' del ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' el ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' ella ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' ellos ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' ellas ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' en ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' era ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' es ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' esta ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' estas ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' estan ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' etc ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' fue ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' ha ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' la ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' los ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' ni ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' no ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' nos ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' otra ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' otros ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' otro ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' para ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' pero ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' por ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' porque ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' que ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' si ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' sr ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' sra ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' sres ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' sta ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' tan ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' tu ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' tus ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' y ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' se', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' un ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' su ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' le ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' me ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' las ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' mas ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' lo ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' una ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' mi ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' yo ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' sin ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' como ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' \xE1 ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' dos ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' este ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' sus ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' muy ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' \xe9l ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' este ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' qu\xe9 ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' todo ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' bien ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' todos ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' eh ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' he ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' r ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' cuando ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' ya ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' sobre ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' m\xE1s ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' habia ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' habia ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' o ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' \xf3n ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' \xf3 ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' hay ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' son ', ' ' , contenidoArchivo)
        contenidoArchivo = re.sub(' dijo ', ' ' , contenidoArchivo)
        
        archivo = {"name":file, "text":contenidoArchivo}
        
        # CAMBIOS PARA ACTUALIZAR DOCUMENTOS
        
        if db.documents.find_one({"name":file}):
            db.documents.delete_one({})
            db.documents.insert_one(archivo)
        else:
            db.documents.insert_one(archivo)
            numero = numero + 1
        
###  FIN CARGA  ###

"""INICIO DE CONSULTAS PARA CHALLENGE"""

"""1-CANTIDAD DE DOCUMENTOS"""
"""Se parsea la cantidad de documentos a string ya que la funcion PRINT no permite concatener un string con un int"""

"""2-CANTIDAD DE PALABRAS DIFERENTES EN LA COLECCION"""
"""https://programminghistorian.org/es/lecciones/contar-frecuencias"""
"""ACA TRAIGO TODO LO DE LA TABLA DOCUMENTOS"""

documentos = db.documents.find()
frecuenciaPalabras = []
np.asarray(frecuenciaPalabras)
frecuenciaPalabrasXdocumento = []
np.asarray(frecuenciaPalabrasXdocumento)
frecuenciasTotales = []
np.asarray(frecuenciasTotales)

unapalabra = "esto es una palabra"
unapalabra += " esto es otra palabra"

unaListaPalabra = unapalabra.split()

for w in unaListaPalabra:
    frecuenciaPalabras.append(unaListaPalabra.count(w))

otrasPalabras = ""

PalabrasXdocumento = ""
documentoConMasPalabras = ""
cantidadTextosProcesados = 0
nombreDocumentoMasPalabras = ""
nombreDocumentoMasFrecuenciaPalabras = ""
maximoCantidadPalabrasTemp = 0
contadorPalabras = 0
contadorPalabrasTemp = 0
listaTempPalabrasPorDocumento = []
np.asarray(listaTempPalabrasPorDocumento)

### ARRANCO A PROCESAR LOS DOCUMENTOS ###

for x in db.documents.find({}, no_cursor_timeout=True):
    # Me traigo todo lo que es el indice TEXT del documento posicion "X
    otrasPalabras += (x.get("text"))
    otrasPalabras += " "
    # print("estoy guardandome los textos en una lista")
    
    # Incremento en 1 la cantidad de textos procesados para actualizar el contador
    cantidadTextosProcesados += 1
    # Imprimo cantidad de documentos procesados
    # print(cantidadTextosProcesados)
    
    # Me traigo el nombre del documento de la posicion "X"
    documentoConMasPalabras = (x.get("name"))
    
    # Me traigo todo lo que es el indice TEXT del documento posicion "X"
    PalabrasXdocumento = (x.get("text"))
    
    # A todas las palabras del texto de la posicion "X" las corto y las agrego a una lista
    # llamada listaPalabrasXdocumentos
    listaPalabrasXdocumento = (PalabrasXdocumento.split())
    
    # ##ACA ANTES DE ROMPER
    ##ACA TENGO QUE HACER LA CARGA EN LA BASE!!! 
    # YA TENGO LAS PALABRAS GUARDADAS, TENGO QUE RECORRER LA TABLA  Y CARGARLAS
    tablaFrecuenciaPalabrasXdocumento = Counter(listaPalabrasXdocumento)
    # print(tablaFrecuenciaPalabrasXdocumento)
    nombreDocumentoFrecuencia = (x.get("name"))
    frecuencias = {"name":nombreDocumentoFrecuencia, "table":tablaFrecuenciaPalabrasXdocumento}
    
    # ACA VAMOS A HACER UN IF PARA VER SI YA ESTA LA FRECUENCIA EN LA TABLA, O ESTA VACIA
    # ASI ESTABA ANTES
    
    valorTable = (x.get("table"))
     
    nuevoValorTable = {"$set":tablaFrecuenciaPalabrasXdocumento}

    if db.frequence.find_one({"name":x.get("name")}, no_cursor_timeout=True):

        db.frequence.delete_one({"name":x.get("name")})
        db.frequence.insert_one(frecuencias)
        
    else:

        db.frequence.insert_one(frecuencias)
    
    countsPalabras = Counter(listaPalabrasXdocumento)
    
    if contadorPalabrasTemp <= (len(countsPalabras)):         
        contadorPalabrasTemp = (len(countsPalabras))
        nombreDocumentoMasPalabras = (x.get("name"))
    
    # Recorro toda la lista de palabras de un documento en particular (posicion "X")
    for j in listaPalabrasXdocumento:
        # Matriz definida en el inicio del proyecto que va a mantener una relacion de frecuencia
        # de palabra por documento. 
        # Borramos la matriz al comenzar para que comience en 0
        frecuenciaPalabrasXdocumento.clear()
        
        # Le agrego a la matrix frecuenciaPalabrasXdocumento 
        frecuenciaPalabrasXdocumento.append(listaPalabrasXdocumento.count(j))
        
        if frecuenciaPalabrasXdocumento.count(j) >= maximoCantidadPalabrasTemp:
            maximoCantidadPalabrasTemp = frecuenciaPalabrasXdocumento.count(j)
            nombreDocumentoMasFrecuenciaPalabras = documentoConMasPalabras
    db.documents.find({}).close()

otraListaPalabras = otrasPalabras.split()

contador = 0

"""
for o in otraListaPalabras:
    contador += 1
    # estoy agregarndo palabras a frecuencias
    frecuenciaPalabras.append(otraListaPalabras.count(o))
    print(len(otraListaPalabras))
    print(contador)
"""
print("CANTIDAD DE PALABRAS TOTALES:")
print(len.otraListaPalabras)
counts = Counter(otraListaPalabras)

####################################################################
# IMPRIMO LA SALIDA DE LA CONSOLA  PARA EL CHALLENGE
print("CANTIDAD DE PALABRAS DISTINTAS EN TODA LA COLECCION:")
print(len(counts))
print("CANTIDAD DE DOCUMENTOS PROCESADOS:")
print(cantidadTextosProcesados)
print("EL DOCUMENTO CON MAS PALABRAS ES:")
print(nombreDocumentoMasPalabras)

sorted_dict_top10 = counts.most_common(10)
sorted_dict_insert = OrderedDict(sorted(counts.items(), key=lambda kv : kv[1], reverse=True)[:10])

if db.topwords.find_one({}):
    db.topwords.delete_one({})
    
    db.topwords.insert_one(counts)
else:
    db.topwords.insert_one(counts)
    
if db.top10words.find_one({}):
    db.top10words.delete_one({})
    
    db.top10words.insert_one(sorted_dict_insert)
else:
    db.top10words.insert_one(sorted_dict_insert)

valoresGrafica = np.array(sorted_dict_top10)
palabrasGrafica = valoresGrafica[:, 0]
frecuenciaGrafica = valoresGrafica[:, 1]

frecuenciaGraficaInt = list(map(int, frecuenciaGrafica))

x_pos = np.arange(len(palabrasGrafica))
arrayEjemplo = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

plt.figure(figsize=(12, 6))

plt.xticks(x_pos, palabrasGrafica)
plt.xticks(rotation=70)
plt.bar(x_pos, frecuenciaGraficaInt, align='center', color='green', bottom=0)

plt.show()                                 
