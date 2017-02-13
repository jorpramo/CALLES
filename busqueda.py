#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'jpradas'
import wikipedia
import settings
from collections import Counter
from fastkml import kml
import operator
import csv, re, os


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

def categoriza(values, searchFor):
    resultado={}
    for k in values:
        for v in values[k].split():
                #print(k,v)
                busqueda=re.findall(v,searchFor)
                if (len(busqueda)>0):
                    resultado[k]=resultado.get(k,0) + len(busqueda)

    if len(resultado)==0:
        maximo=""
    else:
        maximo=max(resultado.items(), key=operator.itemgetter(1))[0]
    #print(max(resultado.items(), key=operator.itemgetter(1))[0])
    return maximo

def procesa_csv(fichero):
    try:
        os.remove('sincategorizar.csv')
    except:
        pass
    wikipedia.set_lang("es")
    i=0
    total_cat=0
    total_cat_total=0
    total=0
    sin = open('sin.csv','w', newline='')
    temp = open('tmp.csv','w', newline='')
    writer = csv.writer(temp, delimiter=';')
    writer_sin = csv.writer(sin, delimiter=';')
    texto=""
    with open(fichero, newline='') as csvfile:

        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            total=total+1
            if (len(row)<=5) | (row[5]==''):
                categorias=settings.categorias
                #buscamos por nombre primero
                cat_temp=categoriza(categorias,row[3].lower())

                if len(cat_temp)==0:
                    result=wikipedia.search(row[3])
                    print(row[3])

                    for cad in result[:1]:
                        try:
                            pag=wikipedia.page(cad)
                            cat_temp=categoriza(categorias,pag.content[:200].lower())
                        except:
                            pass
                # cat=[]
                # categoria=[item for sublist in categoria for item in sublist]
                # if len(categoria)>0:
                #     for k, v in settings.categorias.items():
                #         for c in categoria:
                #             if c in v:
                #                 cat.append(k)
                # max=0
                # cat_final=''
                # if len(cat)>0:
                #     total_cat = total_cat + 1
                #     for unica in set(cat):
                #         cont=cat.count(unica)
                #         if cont>max:
                #             max=cont
                #             cat_final=unica

                if cat_temp!="":
                    total_cat = total_cat + 1
                writer.writerow([row[0], row[1],row[2],row[3],row[4],cat_temp])
                #texto.append(row[3].lower())
                texto=texto +" "+  row[3].lower()
            else:
                total_cat_total = total_cat_total + 1
                writer.writerow(row)

    temp.close()
    sin.close()
    try:
        os.remove('old.csv')
    except:
        pass

    os.rename(fichero, 'old.csv')
    os.rename('tmp.csv',fichero)
    print("Total Categorizadas en esta ejecución",total_cat)
    print("Total Categorizadas ",total_cat_total)
    print("Total Procesadas ",total)
    texto = re.sub(r'\b\w{1,3}\b', '', texto)
    texto = re.findall(r'\w+', texto)

    print(Counter(texto).most_common(100))


ciudades=settings.ciudades

for c in ciudades:
    if c['tipo']=='KML':
        procesa_KML(c['fichero'])

    if c['tipo']=="CSV":
        procesa_csv(c['fichero'])

