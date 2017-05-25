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
    'ciudad':"Valencia",
    'nombre':3,
    'categoria':5
})

ciudades.append({
    'fichero':'CARRERER.csv',
    'tipo':'CSV',
    'ciudad':"Barcelona",
    'nombre':3,
    'categoria':6
})


categorias={'LETRAS':'escritor\\b|\\bperiodista\\b|\\bfilósofo\\b|\\bhistoriador\\b|\\bpoeta\\b|\\bescriptor\\b|\\bdramaturg\\b|\\bmusico\\b|\\bmaestro\\b|\\bprofesor\\b|\\bcronista\\b|\\bescriptor\\b|\\bperiodista\\b|\\bfilòsof\\b|\\bhistoriador\\b|\\bpoeta\\b|\\bescriptor\\b|\\bdramaturg\\b|\\bmúsic\\b|\\bmestre\\b|\\bprofessor\\b|\\bprofessor\\b|\\bcronista',
            'CIENCIA':'médico\\b|\\bdoctor\\b|\\binvestigador\\b|\\bfísico\\b|\\bquímico\\b|\\beconomista\\b|\\bmetge\\b|\\bcardioleg\\b|\\bingeniero\\b|\\bmetge\\b|\\bdoctor\\b|\\binvestigador\\b|\\bfísic\\b|\\bquímic\\b|\\beconomista\\b|\\bMetge\\b|\\bcardioleg\\b|\\benginyer\\b',
            'RELIGION':'cura\\b|\\bmonja\\b|\\bfray\\b|\\bsanto\\b|\\breligioso\\b|\\barzobispo\\b|\\bhermandad\\b|\\biglesia\\b|\\bparroquia\\b|\\bvirgen\\b|\\bsanta\\b|\\bsan\\b|\\bpadre\\b|\\bobispo\\b|\\bcanonigo\\b|\\breverendo\\b|\\bcardenal\\b|\\bcura\\b|\\bmonja\\b|\\bsant\\b|\\breligiós\\b|\\barquebisbe\\b|\\bgermanor\\b|\\besglésia\\b|\\bparròquia\\b|\\bverge\\b|\\bsanta\\b|\\bsant\\b|\\bpare\\b|\\bbisbe\\b|\\bcanonge\\b|\\breverend\\b|\\bcardenal\\b',
            'ARTE':'ceramista\\b|\\bpintor\\b|\\bescultor\\b|\\bmúsico\\b|\\barquitecto\\b|\\bactor\\b|\\bgrabador\\b|\\bcompositor\\b|\\bpintor\\b|\\bescultor\\b|\\bmúsic\\b|\\barquitecte\\b|\\bactor\\b|\\bgravador\\b|\\bcompositor\\b|\\bmusic\\b',
            'POLITICA':'político\\b|\\bsenador\\b|\\babogado\\b|\\bmilitante\\b|\\bpresidente\\b|\\bministro\\b|\\brepublica\\b|\\balcalde\\b|\\brey\\b|\\breina\\b|\\bpolític\\b|\\bsenador\\b|\\badvocat\\b|\\bmilitant\\b|\\bpresident\\b|\\bministre\\b|\\brepublica\\b|\\balcalde\\b|\\breina\\b',
            'MILITAR':'teniente\\b|\\bcoronel\\b|\\bcomandante\\b|\\bsoldado\\b|\\bmilitar\\b|\\bgeneral\\b|\\btinent\\b|\\bcoronel\\b|\\bcomandant\\b|\\bsoldat\\b|\\bmilitar\\b|\\bgeneral',
           # 'EVENTO':'enero\\b|\\bfebrero\\b|\\bmarzo\\b|\\babril\\b|\\bmayo\\b|\\bjunio\\b|\\bjulio\\b|\\bagosto\\b|\\bseptiembre\\b|\\boctubre\\b|\\bnoviembre\\b|\\bdiciembre\\b|\\bfecha\\b|\\bgener\\b|\\bfebrer\\b|\\bmarç\\b|\\babril\\b|\\bmaig\\b|\\bjuny\\b|\\bjuliol\\b|\\bagost\\b|\\bsetembre\\b|\\boctubre\\b|\\bnovembre\\b|\\bdesembre\\b|\\bdata\\b',
            'TITULO':'duque\\b|\\bduquesa\\b|\\bnoble\\b|\\bconde\\b|\\bcondesa\\b|\\bbaron\\b|\\bbaronesa\\b|\\bmarques\\b|\\bseñorío\\b|\\bduc\\b|\\bduquessa\\b|\\bnoble\\b|\\bcomte\\b|\\bcomtessa\\b|\\bbaron\\b|\\bbaronessa\\b|\\bmarquis\\b|\\bsenyoriu\\b'}
           # 'LUGAR':'municipio\\b|\\bciudad\\b|\\bbarrio\\b|\\bmercado\\b|\\btallafoc\\b|\\bmar\\b|\\brio\\b|\\bcauce\\b|\\bpuente\\b|\\bcasas\\b|\\balqueria\\b|\\bcasa\\b|\\brambla\\b|\\bpoblado\\b|\\bisla\\b|\\bazagador\\b|\\bcamino\\b|\\bmunicipi\\b|\\bciutat\\b|\\bbarri\\b|\\bmercat\\b|\\bTallafoc\\b|\\bmar\\b|\\briu\\b|\\bllera\\b|\\bpont\\b|\\bcases\\b|\\balqueria\\b|\\bcasa\\b|\\bhorta\\b|\\bplatja\\b|\\brambla\\b|\\bpoblat\\b|\\bassagador\\b'}
