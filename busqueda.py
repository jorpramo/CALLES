#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'jpradas'
import wikipedia
import settings
from collections import Counter
from fastkml import kml
import operator
import csv, re, os
import google
import genderator
import pypyodbc

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
        busqueda=re.findall(values[k].lower(),searchFor)
        if (len(busqueda)>0):
            resultado[k]=resultado.get(k,0) + len(busqueda)

    if len(resultado)==0:
        maximo=""
    else:
        maximo=max(resultado.items(), key=operator.itemgetter(1))[0]
    #print(max(resultado.items(), key=operator.itemgetter(1))[0])
    return maximo

# def procesa_sql(municipio, provincia):
#     conn = pypyodbc.connect("DRIVER={SQL Server};SERVER=DHARMA\SQLEXPRESS;UID=loginR;PWD=loginR;DATABASE=CARRERS")
#     cur = conn.cursor()
#     cur.execute("SELECT nvia FROM VIAS where CMUM='%s' and  CPRO='%s' and SUBCAT is null and CAT is null" % (municipio, provincia))
#     categorias=settings.categorias
#     for row in cur.fetchall():
#         cat_temp=categoriza(categorias,row["nvia"].lower().strip())
#         if cat_temp!="":
#             print(row["nvia"])
#             sql="UPDATE VIAS set SUBCAT=? where nvia=?"
#             cur.execute(sql, (cat_temp,row["nvia"])) #Actualizamos de todos los municipios
#             cur.commit()
#     cur.close()
#     conn.close()

def procesa_sql(municipio, provincia,tipo):
    conn = pypyodbc.connect("DRIVER={SQL Server};SERVER=DHARMA\SQLEXPRESS;UID=loginR;PWD=loginR;DATABASE=CARRERS")
    cur = conn.cursor()
    cur.execute("SELECT nvia FROM VIAS where CMUM='%s' and  CPRO='%s' and SUBCAT is null and CAT is null" % (municipio, provincia))
    #cur.execute("SELECT nvia FROM VIAS where CMUM='%s' and  CPRO='%s' and genero is null and ACTUALIZADO IS NULL" % (municipio, provincia))
    categorias=settings.categorias
    cat_temp=""
    for row in cur.fetchall():
        calle=row["nvia"].lower().strip().replace("'","")
        if (tipo=="nombre"):
            cat_temp=categoriza(categorias,calle)
        if (tipo=="google"):
            try:
                from google import search
                cad=[]
                url=search(calle +" -calle -falla -linkedin -paginasamarillas -facebook", tld='es', lang='es', num=5,stop=5, pause=10.0)

                #search_results = google.search(row["nvia"].lower().strip().replace("'","") +" -calle -falla -linkedin -paginasamarillas -facebook", tld='es', lang='es', tbs='0', safe='off', num=5, stop=1)

                [cad.append(result) for result in url]
                cad=' '.join(cad)
                cat_temp=categoriza(categorias,cad)
            except:
                print("No se ha podido acceder a Google")

        if (tipo=="wiki"):
            try:
                result=wikipedia.search(calle, results=5)
                cad=result[:1]
                try:
                    pag=wikipedia.page(cad)
                    cat_temp=categoriza(categorias,pag.content[:200].lower())
                except:
                    pass
            except:
                print("No se ha podido acceder a la wikipedia")
        genero=''
        if (tipo=="genero"):
            guesser = genderator.Parser()
            answer = guesser.guess_gender(calle)

            if answer:
                print(answer)
                genero=answer['gender']
            else:
                print('Name doesn\'t match')
        if cat_temp!="":
            print(row["nvia"],cat_temp)
            sql="UPDATE VIAS set SUBCAT=?, ACTUALIZADO=GETDATE() where nvia=?"
            cur.execute(sql, (cat_temp,row["nvia"])) #Actualizamos de todos los municipios
            cur.commit()
        if cat_temp=="" and (genero=="Male" or genero=="Female"):
            sql="UPDATE VIAS set ACTUALIZADO=GETDATE(), GENERO=? where nvia=?"
            cur.execute(sql, (genero,row["nvia"])) #Actualizamos de todos los municipios
            cur.commit()
    cur.close()
    conn.close()



ciudades=settings.ciudades

# for c in ciudades:
#     if c['tipo']=='KML':
#         procesa_KML(c['fichero'])


#
#     if c['tipo']=="CSV":
#         procesa_csv(c['fichero'],c['nombre'],c['categoria'])


localidades=[['019','08'],['020','48'],['091','41'],['079','28'],['250','46']]

for i in localidades:
    procesa_sql(i[0],i[1],"wiki")
