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

def procesa_sql(municipio, provincia):
    conn = pypyodbc.connect("DRIVER={SQL Server};SERVER=DHARMA\SQLEXPRESS;UID=loginR;PWD=loginR;DATABASE=CARRERS")
    cur = conn.cursor()
    cur.execute("SELECT nvia FROM VIAS where CMUM='%s' and  CPRO='%s' and SUBCAT is null and CAT is null" % (municipio, provincia))
    categorias=settings.categorias
    for row in cur.fetchall():
        cat_temp=categoriza(categorias,row["nvia"].lower().strip())
        if cat_temp!="":
            print(row["nvia"])
            sql="UPDATE VIAS set SUBCAT=? where nvia=?"
            cur.execute(sql, (cat_temp,row["nvia"])) #Actualizamos de todos los municipios
            cur.commit()
    cur.close()
    conn.close()

def procesa_sql(municipio, provincia,tipo):
    conn = pypyodbc.connect("DRIVER={SQL Server};SERVER=DHARMA\SQLEXPRESS;UID=loginR;PWD=loginR;DATABASE=CARRERS")
    cur = conn.cursor()
    #cur.execute("SELECT nvia FROM VIAS where CMUM='%s' and  CPRO='%s' and SUBCAT is null and CAT is null" % (municipio, provincia))
    cur.execute("SELECT nvia FROM VIAS where CMUM='%s' and  CPRO='%s' and genero is null" % (municipio, provincia))
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
                url=search(calle +" -calle -falla -linkedin -paginasamarillas -facebook", tld='es', lang='es', num=5,stop=5)

                #search_results = google.search(row["nvia"].lower().strip().replace("'","") +" -calle -falla -linkedin -paginasamarillas -facebook", tld='es', lang='es', tbs='0', safe='off', num=5, stop=1)

                [cad.append(result) for result in url]
                cad=' '.join(cad)
                cat_temp=categoriza(categorias,cad)
            except:
                print("No se ha podido acceder a Google")

        if (tipo=="wiki"):
            try:
                result=wikipedia.search(calle)
                cad=result[:1]
                try:
                    pag=wikipedia.page(cad)
                    cat_temp=categoriza(categorias,pag.content[:200].lower())
                except:
                    pass
            except:
                print("No se ha podido acceder a la wikipedia")
        guesser = genderator.Parser()
        answer = guesser.guess_gender(calle)
        genero=''
        if answer:
            print(answer)
            genero=answer['gender']
        else:
            print('Name doesn\'t match')
        if cat_temp!="":
            print(row["nvia"],cat_temp)
            sql="UPDATE VIAS set SUBCAT=?, ACTUALIZADO=GETDATE(), GENERO=? where nvia=?"
            cur.execute(sql, (cat_temp,genero,row["nvia"])) #Actualizamos de todos los municipios
            cur.commit()
        if cat_temp=="" and (genero=="Male" or genero=="Female"):
            sql="UPDATE VIAS set ACTUALIZADO=GETDATE(), GENERO=? where nvia=?"
            cur.execute(sql, (genero,row["nvia"])) #Actualizamos de todos los municipios
            cur.commit()
    cur.close()
    conn.close()


def procesa_csv(fichero, pos_nombre, pos_categoria):

    wikipedia.set_lang("es")
    i=0
    total_cat=0
    total_cat_total=0
    total=0
    fich_temp=fichero.replace('.csv','_temp.csv')
    fich_old=fichero.replace('.csv','_old.csv')
    temp = open(fich_temp,'w', newline='')
    writer = csv.writer(temp, delimiter=';')

    texto=""
    with open(fichero, newline='') as csvfile:

        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            total=total+1
            if (row[pos_categoria]==''):
                categorias=settings.categorias
                #buscamos por nombre primero
                cat_temp=categoriza(categorias,row[pos_nombre].lower())

                #buscamos por google
                if len(cat_temp)==666:
                    try:
                        search_results = google.search(row[3].lower() +" -calle -falla -linkedin -paginasamarillas -facebook", tld='es', lang='es', tbs='0', safe='off', num=5, stop=1)
                        cad=[]
                        [cad.append(result) for result in search_results]
                        cad=' '.join(cad)
                        cat_temp=categoriza(categorias,cad)
                        print(row[3],cat_temp)
                    except:
                        print("No se ha podido acceder a Google")

                #buscamos por Wikipedia
                if len(cat_temp)==666:
                    try:
                        result=wikipedia.search(row[3])
                        print(row[3])

                        for cad in result[:1]:
                            try:
                                pag=wikipedia.page(cad)
                                cat_temp=categoriza(categorias,pag.content[:200].lower())
                            except:
                                pass
                    except:
                        print("No se ha podido acceder a la wikipedia")

                if cat_temp=="":
                    writer.writerow(row)
                    texto=texto +" "+  row[pos_nombre].lower()
                else:
                    total_cat = total_cat + 1
                    row=row[:-1]
                    row.append(cat_temp)
                    writer.writerow(row)
                    #texto.append(row[3].lower())

            else:
                total_cat_total = total_cat_total + 1
                writer.writerow(row)

    temp.close()

    try:
        os.remove(fich_old)
    except:
        pass

    os.rename(fichero, fich_old)
    os.rename(fich_temp,fichero)

    print("Total Categorizadas en esta ejecución",total_cat)
    print("Total Categorizadas ",total_cat_total)
    print("Total Procesadas ",total)
    texto = re.sub(r'\b\w{1,3}\b', '', texto)
    texto = re.findall(r'\w+', texto)

    print(Counter(texto).most_common(100))


ciudades=settings.ciudades

# for c in ciudades:
#     if c['tipo']=='KML':
#         procesa_KML(c['fichero'])


#
#     if c['tipo']=="CSV":
#         procesa_csv(c['fichero'],c['nombre'],c['categoria'])


localidades=[['019','08'],['020','48'],['091','41'],['079','28'],['46','250']]

for i in localidades:
    procesa_sql(i[0],i[1],"genero")
