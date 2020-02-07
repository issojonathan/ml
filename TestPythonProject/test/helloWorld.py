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

client = pymongo.MongoClient ("mongodb+srv://issojonathan:Uy123123@jonathanisso-er8ve.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('colectionML')

"""print(client.list_database_names())"""
records = db.documents
records.find()
collection_taxonomy = db['collection']
"""
print(db.getName)

print(db)
print(client)

print('hello World')
print('hello World2')

print('hello World3')
"""
db = client.colectionML
"""db.documents.insert_one({"name": "My first post", "text": "This is the body of my first blog post", "id": 2})"""
"""print('hello World4')"""

"""db.documents.insert_one({"name": "pablito", "text": "prueba pablo", "id": 3})"""

"""print('hello World5')"""

# files = db.files

# f = open('C:\\Users\\Hsbc\\Desktop\\coleccion_2020\\320-8.txt')
# text = f.read()
"""print(text)"""

"""doc = {
    "name":"320-8", "text":text
    }
"""
"""db.documents.insert_one(doc)"""

"""print('hello World6')"""

"""INICIO DE CARGA"""
numero = 0
for file in os.listdir("C:\\Users\\Hsbc\\Desktop\\coleccion_2021"):
    if file.endswith(".txt"):
        # print(os.path.join("C:\\Users\\Hsbc\\Desktop\\coleccion_2021", file))
        pathArchivo = (os.path.join("C:\\Users\\Hsbc\\Desktop\\coleccion_2021", file))
        print(pathArchivo)
        a = open(pathArchivo, encoding="utf8")
        contenidoArchivo = a.read()
        print("llego")
        archivo = {"name":file, "text":contenidoArchivo}
        db.documents.insert_one(archivo)
        print(numero)
        numero = numero + 1
        
# FIN CARGA
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

unapalabra = "esto es una palabra"
unapalabra += " esto es otra palabra"

unaListaPalabra = unapalabra.split()

for w in unaListaPalabra:
    frecuenciaPalabras.append(unaListaPalabra.count(w))

print (unaListaPalabra)
print("FRECUENCIAS POR PALABRAS")
print (frecuenciaPalabras)

otrasPalabras = ""
print("Cree la variable otras palabras")

cantidadTextosProcesados = 0
for x in db.documents.find({}, {"_id":0, "name":0}):
    """print(x.get("text"))"""
    print("entre en el for")
    otrasPalabras += (x.get("text"))
    print("estoy guardandome los textos en una lista")
    print(cantidadTextosProcesados)
    cantidadTextosProcesados += 1
    
otraListaPalabras = otrasPalabras.split()

for o in otraListaPalabras:
    frecuenciaPalabras.append(otraListaPalabras.count(w))
    print("estoy agregarndo palabras a frecuencias")

print (otraListaPalabras)
print("FRECUENCIAS POR PALABRAS")
print (frecuenciaPalabras)
print (list(zip(otraListaPalabras, frecuenciaPalabras)))

# Dada una lista de palabras, devuelve un diccionario de
# pares de palabra-frecuencia.

print ("voy a imprimir dict")

counts = Counter(otraListaPalabras)

print(counts)

print("CANTIDAD DE PALABRAS DISTINTAS EN TODA LA COLECCION")
print(len(counts))

print("CANTIDAD DE TEXTOS PROCESADOS")
print(cantidadTextosProcesados)

print("Fin de carga")

