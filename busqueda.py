#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'jpradas'
import wikipedia
import settings as set
from fastkml import kml
import csv, re


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


def listaunica(seq):
   # not order preserving
   set = {}
   map(set.__setitem__, seq, [])
   return set.keys()


def categoriza(pagina):
    print(pagina)
    result=re.findall(categorias,pagina)
    return result

def procesa_csv(fichero):
    wikipedia.set_lang("es")
    i=0
    #temp = open(fichero+'_tmp'.csv, 'wb')
    with open(fichero, newline='') as csvfile:


        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            i=i+1
            if (i>6):
                break
            print(row[3])
            result=wikipedia.search(row[3])
            categoria=[]
            for cad in result[:3]:
                try:
                    pag=wikipedia.page(cad)
                    #head = list(islice(pag.content, 10))
                    cat_temp=categoriza(pag.content[:200].lower())
                    if cat_temp!='':
                        categoria.append(cat_temp)
                except:
                    pass
            cat=[]
            categoria=[item for sublist in categoria for item in sublist]
            print(categoria)
            if len(categoria)>0:
                for k, v in set.categorias.items():
                    for c in categoria:
                        if c in v:
                            cat.append(k)
            print(cat)
            max=0
            cat_final=''
            if len(cat)>0:
                for unica in list(set(cat)):
                    cont=cat.count(unica)
                    if cont>max:
                        max=cont
                        cat_final=unica

            print(cat_final)
            #writer.writerow(row[0], row[1],row[2],row[3],row[4], categoria)



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

