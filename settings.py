#!/usr/bin/python
# -*- coding: utf-8 -*-
ciudades=[]

#ASP POR GRUPO
"""
ciudades.append({
    'fichero':'Ejes-calle.KML',
    'tipo':'KML',
    'ciudad':"Valencia"
})
"""
ciudades.append({
    'fichero':'vias.csv',
    'tipo':'CSV',
    'ciudad':"Valencia"
})


categorias={'LETRAS':'escritor|periodista|filósofo|historiador|poeta|escriptor|dramaturg|musico|maestro|profesor|cronista|escriptor|periodista|filòsof|historiador|poeta|escriptor|dramaturg|músic|mestre|professor|professor|cronista',
            'CIENCIA':'médico|doctor|investigador|físico|químico|economista|metge|cardioleg|ingeniero|metge|doctor|investigador|físic|químic|economista|Metge|cardioleg|enginyer',
            'RELIGION':'cura|monja|santo|religioso|arzobispo|hermandad|iglesia|parroquia|virgen|santa|san|padre|obispo|canonigo|reverendo|cardenal|cura|monja|sant|religiós|arquebisbe|germanor|església|parròquia|verge|santa|sant|pare|bisbe|canonge|reverend|cardenal',
            'ARTE':'ceramista|pintor|escultor|músico|arquitecto|actor|grabador|compositor|pintor|escultor|músic|arquitecte|actor|gravador|compositor|music',
            'POLITICA':'político|senador|abogado|militante|presidente|ministro|republica|alcalde|rey|reina|polític|senador|advocat|militant|president|ministre|republica|alcalde|rei|reina',
            'MILITAR':'teniente|coronel|comandante|soldado|militar|general|tinent|coronel|comandant|soldat|militar|general',
            'EVENTO':'enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre|fecha|gener|febrer|març|abril|maig|juny|juliol|agost|setembre|octubre|novembre|desembre|data',
            'TITULO':'duque|duquesa|noble|conde|condesa|baron|baronesa|marques|señorío|duc|duquessa|noble|comte|comtessa|baron|baronessa|marquis|senyoriu',
            'LUGAR':'municipio|ciudad|barrio|mercado|tallafoc|mar|rio|cauce|puente|casas|alqueria|casa|rambla|poblado|isla|azagador|camino|municipi|ciutat|barri|mercat|Tallafoc|mar|riu|llera|pont|cases|alqueria|casa|horta|platja|rambla|poblat|illa|assagador|camí'}

