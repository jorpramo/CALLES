#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'jpradas'
import wikipedia
import settings as set
from fastkml import kml
import csv, re
from itertools import islice

def procesa_KML(fichero):
    f = open(fichero, 'r')
    doc=f.read()
    k = kml.KML()
    k.from_string(doc)
    calles = list(k.features())
    calles[0].features()
    list_calles = list(calles[0].features())
    list_detallado=list(list_calles[0].features())
    #for i in range(0,len(list_calles)):
    for i in range(0,10):
        print(list_detallado[i].name)

categorias=[]
for k, v in set.categorias.items():
    categorias.append(v)
categorias='|'.join(categorias)

def categoriza(pagina):
    print(pagina)
    result=re.findall(categorias,pagina)
    return result

def procesa_csv(fichero):
    wikipedia.set_lang("es")
    i=0
    with open(fichero, newline='') as csvfile:


        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            i=i+1
            if (i>3):
                break
            print(row[3])
            result=wikipedia.search(row[3])
            categoria=[]
            for cad in result[:3]:
                try:
                    pag=wikipedia.page(cad)
                    #head = list(islice(pag.content, 10))
                    categoria.append(categoriza(pag.content[:200].lower()))
                except:
                    pass
            print(categoria)




ciudades=set.ciudades

for c in ciudades:
    if c['tipo']=='KML':
        procesa_KML(c['fichero'])

    if c['tipo']=="CSV":
        procesa_csv(c['fichero']
                    )
"""
wikipedia.set_lang("es")
result=wikipedia.search("Peset Aleixandre")

for cad in result:
    pag=wikipedia.page(cad)
    print(pag.content)
"""

