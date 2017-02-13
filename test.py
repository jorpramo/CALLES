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

res=search(settings.categorias, "esto es gravador un cronista escriptor")
print(res)
