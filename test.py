#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'jpradas'
import wikipedia
import settings
from collections import Counter
from fastkml import kml
import csv, re, os

import operator


#pasa las categorias y el texto, devuelve la categoría mayor
def search(values, searchFor):
    resultado={}
    for k in values:
        for v in values[k].split():
                print(k,v)
                busqueda=re.findall(v,searchFor)
                if (len(busqueda)>0):
                    resultado[k]=resultado.get(k,0) + len(busqueda)
    print(len(resultado))
    print(resultado)
    if len(resultado)==0:
        maximo=""
    else:
        maximo=max(resultado.items(), key=operator.itemgetter(1))[0]
    #print(max(resultado.items(), key=operator.itemgetter(1))[0])
    return maximo

#res=search(settings.categorias, "esto es gravador un cronista escriptor")
#print(res)


# try:
#     from google import search
#     cad=[]
#     url=search("FRANCISCO EXIMENIS" +" -calle -falla -linkedin -paginasamarillas -facebook", tld='es', lang='es', num=5,stop=5)
#
#     #search_results = google.search(row["nvia"].lower().strip().replace("'","") +" -calle -falla -linkedin -paginasamarillas -facebook", tld='es', lang='es', tbs='0', safe='off', num=5, stop=1)
#
#     [cad.append(result) for result in url]
#     cad=' '.join(cad)
#     print(cad)
# except:
#     print("No se ha podido acceder a Google")

# try:
#     result=wikipedia.search("FRANCISCO EXIMENIS", results=1)
#
#     cad=result[:1]
#     try:
#         pag=wikipedia.page(cad)
#         print(pag.content[:200].lower())
#         #cat_temp=categoriza(categorias,pag.content[:200].lower())
#     except:
#         pass
# except:
#     print("No se ha podido acceder a la wikipedia")
#
#

from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk
spanish_stops = set(stopwords.words('spanish'))
