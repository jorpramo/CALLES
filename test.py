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


# import google
# num_page = 4
# search_results = google.search("DON JUAN DE DIOS MONTAÑES -calle", tld='es', lang='es', tbs='0', safe='off', num=5, stop=1)
# for result in search_results:
#     print(result)
    # Get the first 20 hits for "Mariposa botnet" in Google Spain
from google import search
cad=[]
url=search('Mariposa botnet', tld='es', lang='es', num=5,stop=5)
[cad.append(result) for result in url]
cad=' '.join(cad)
print(cad)
