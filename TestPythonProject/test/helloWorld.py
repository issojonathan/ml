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

client = pymongo.MongoClient ("mongodb+srv://issojonathan:Uy123123@jonathanisso-er8ve.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('colectionML')

"""print(client.list_database_names())"""
records = db.documents
records.find()
collection_taxonomy = db['collection']
db = client.colectionML

"""db.documents.insert_one({"name": "My first post", "text": "This is the body of my first blog post", "id": 2})"""
"""print('hello World4')"""
"""db.documents.insert_one({"name": "pablito", "text": "prueba pablo", "id": 3})"""
"""print('hello World5')"""
# files = db.files
# f = open('C:\\Users\\Hsbc\\Desktop\\coleccion_2020\\320-8.txt')
# text = f.read()
"""doc = {
    "name":"320-8", "text":text
    }
"""
"""db.documents.insert_one(doc)"""

###  INICIO DE CARGA DE DOCUMENTOS  ###
numero = 0
for file in os.listdir("C:\\Users\\Hsbc\\Desktop\\coleccion_2021"):
    if file.endswith(".txt"):
        # print(os.path.join("C:\\Users\\Hsbc\\Desktop\\coleccion_2021", file))
        pathArchivo = (os.path.join("C:\\Users\\Hsbc\\Desktop\\coleccion_2021", file))
        print(pathArchivo)
        a = open(pathArchivo, encoding="utf-8-sig")
        contenidoArchivo = a.read()
        # print("llego")
        archivo = {"name":file, "text":contenidoArchivo}
        
        # CAMBIOS PARA ACTUALIZAR DOCUMENTOS
        
        if db.documents.find_one({"name":file}):
            print (db.documents.find({"name":file}))
            db.documents.delete_one({})
            print("BORRADO!!!!")
            db.documents.insert_one(archivo)
        else:
            db.documents.insert_one(archivo)
            print(numero)
            print("lo agrego")
            numero = numero + 1
            
            # db.documents.update(archivo)
        # #ANTES DE TOCAR NADA ESTABA SOLO ESTO## 
        """db.documents.insert_one(archivo)
        print(numero)
        numero = numero + 1"""
        ########################################
        
###  FIN CARGA  ###
print("Fin de carga")

"""INICIO DE CONSULTAS PARA CHALLENGE"""

"""1-CANTIDAD DE DOCUMENTOS"""
"""Se parsea la cantidad de documentos a string ya que la funcion PRINT no permite concatener un string con un int"""
print("La cantidad de documentos cargados es de: " + str(db.documents.estimated_document_count()))

"""2-CANTIDAD DE PALABRAS DIFERENTES EN LA COLECCION"""
"""https://programminghistorian.org/es/lecciones/contar-frecuencias"""

print("llego1")
"""ACA TRAIGO TODO LO DE LA TABLA DOCUMENTOS"""
"""documentos = db.documents.find({})"""

documentos = db.documents.find()
frecuenciaPalabras = []
frecuenciaPalabrasXdocumento = []

unapalabra = "esto es una palabra"
unapalabra += " esto es otra palabra"

unaListaPalabra = unapalabra.split()

for w in unaListaPalabra:
    frecuenciaPalabras.append(unaListaPalabra.count(w))

otrasPalabras = ""
print("Cree la variable otras palabras")

PalabrasXdocumento = ""
documentoConMasPalabras = ""
cantidadTextosProcesados = 0
nombreDocumentoMasPalabras = ""
nombreDocumentoMasFrecuenciaPalabras = ""
maximoCantidadPalabrasTemp = 0
contadorPalabras = 0
contadorPalabrasTemp = 0
listaTempPalabrasPorDocumento = []

### ARRANCO A PROCESAR LOS DOCUMENTOS ###
# for x in db.documents.find({}, {"_id":0}):
for x in db.documents.find({}):
    # Imprimo el texto entero del documento posicion "X"
    """print(x.get("text"))"""

    # Me traigo todo lo que es el indice TEXT del documento posicion "X
    otrasPalabras += (x.get("text"))
    otrasPalabras += " "
    print("estoy guardandome los textos en una lista")
    
    # Incremento en 1 la cantidad de textos procesados para actualizar el contador
    cantidadTextosProcesados += 1
    # Imprimo cantidad de documentos procesados
    print(cantidadTextosProcesados)
    
    # Me traigo el nombre del documento de la posicion "X"
    documentoConMasPalabras = (x.get("name"))
    
    # Me traigo todo lo que es el indice TEXT del documento posicion "X"
    PalabrasXdocumento = (x.get("text"))
    
    # A todas las palabras del texto de la posicion "X" las corto y las agrego a una lista
    # llamada listaPalabrasXdocumentos
    listaPalabrasXdocumento = PalabrasXdocumento.split()
    
    # ##ACA ANTES DE ROMPER
    ##ACA TENGO QUE HACER LA CARGA EN LA BASE!!! 
    # YA TENGO LAS PALABRAS GUARDADAS, TENGO QUE RECORRER LA TABLA  Y CARGARLAS
    # tablaFrecuenciaPalabrasXdocumento = (list(zip(listaPalabrasXdocumento, frecuenciaPalabrasXdocumento)))
    # print("solo imprimir una vez")
    tablaFrecuenciaPalabrasXdocumento = Counter(listaPalabrasXdocumento)
    print(tablaFrecuenciaPalabrasXdocumento)
    nombreDocumentoFrecuencia = (x.get("name"))
    frecuencias = {"name":nombreDocumentoFrecuencia, "table":tablaFrecuenciaPalabrasXdocumento}
    
    # ACA VAMOS A HACER UN IF PARA VER SI YA ESTA LA FRECUENCIA EN LA TABLA, O ESTA VACIA
    # ASI ESTABA ANTES
    
    valorTable = (x.get("table"))
     
    nuevoValorTable = {"$set":tablaFrecuenciaPalabrasXdocumento}
    
    # ANDA if db.frequence.find_one({"name":file}):
    if db.frequence.find_one({"name":x.get("name")}):
        # print("ESTO TENGO GUARDADO EN LA BASE")
        # print(x.get("name"))
        db.frequence.delete_one({"name":x.get("name")})
        print("BORRADO!!!!")
        db.frequence.insert_one(frecuencias)
        
    else:
        print("voy a agregar la frecuencia")
        db.frequence.insert_one(frecuencias)
        print("agrego la frecuencia")
    
    """
    db.frequence.insert_one(frecuencias)
    """
    
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
        
    # print("ESTE ES EL DOCUMENTO CON MAS PALABRAS -- TEST")
    # print(documentoConMasPalabras)
    # print("CON UNA FRECUENCIA DE PALABRAS: ") 
    # print(frecuenciaPalabrasXdocumento)
    
otraListaPalabras = otrasPalabras.split()

for o in otraListaPalabras:
 
    frecuenciaPalabras.append(otraListaPalabras.count(o))
    # print("estoy agregarndo palabras a frecuencias")

print (otraListaPalabras)
print (otraListaPalabras)
print (otraListaPalabras)
print("FRECUENCIAS POR PALABRAS")
print (frecuenciaPalabras)
print (frecuenciaPalabras)
print (frecuenciaPalabras)
# Aca imprimo la frecuencia por palabra
print (list(zip(otraListaPalabras, frecuenciaPalabras)))

# Dada una lista de palabras, devuelve un diccionario de
# pares de palabra-frecuencia.

print ("voy a imprimir dict")

counts = Counter(otraListaPalabras)

print(counts)

####################################################################
# IMPRIMO LA SALIDA DE LA CONSOLA  PARA EL CHALLENGE
print("#######################################################")
print("#######################################################")
print("CANTIDAD DE PALABRAS DISTINTAS EN TODA LA COLECCION")
print(len(counts))

print("CANTIDAD DE DOCUMENTOS PROCESADOS")
print(cantidadTextosProcesados)
# print("EL DOCUMENTO CON MAS FRECUENCIA DE UNA MISMA PALABRA ES:")
# print(nombreDocumentoMasFrecuenciaPalabras)
print("EL DOCUMENTO CON MAS PALABRAS ES:")
print(nombreDocumentoMasPalabras)
print("#######################################################")
print("Se almaceno en la DB la frecuencia de las palabras por documento")
print("prueba imprimir frecuencia")

