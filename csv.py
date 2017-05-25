#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'jpradas'
import wikipedia
import settings
from collections import Counter
import csv, re, os
import google


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

