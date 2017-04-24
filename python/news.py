# -*- coding: utf-8 -*-
import os
import lxml.html
import requests
from datetime import date

PLUGIN_PATH = os.getcwd() + "/plugins_installed/jarvis-leMonde"


def getRubrique(rubrique) :
    if rubrique == "international" or rubrique == "national" :
        return "international"
    elif rubrique == "politique" or rubrique == "tique" :
        return "politique"
    elif rubrique == "societe" :
        return "societe"
    elif rubrique == "economie" or rubrique == "eco" or rubrique == "momie" :
        return "economie"
    elif rubrique == "culture" or rubrique == "le cul" :
        return "culture"
    elif rubrique == "idees" or rubrique == "id" :
        return "idees"
    elif rubrique == "planete" or rubrique == "pleine" or rubrique == "plane" or rubrique == "plaine" :
        return "planete"
    elif rubrique == "sport" :
        return "sport"
    elif rubrique == "science" or rubrique == "sciences" or rubrique == "chien" or rubrique == "cyan" or rubrique == "sion" :
        return "sciences"
    elif rubrique == "pixels" or rubrique == "pixel" or rubrique == "sel" :
        return "pixels"
    elif rubrique == "campus" or rubrique == "quand tu" or rubrique == "puce" :
        return "campus"
    elif rubrique == "le mag" or rubrique == "le mat" or rubrique == "le mal" :
        return "m-le-mag"
    else :
        return "non reconnu"
        
def news() :
    file = open(PLUGIN_PATH + "/python/rubrique.txt")
    line = file.readline()
    line = line[0:len(line)-1]
    file.close()
    
    
    file = open(PLUGIN_PATH + "/config.sh")
    lines = file.readlines()
    file.close()

    reply = ""
    rubrique = getRubrique(line)
    if rubrique != "non reconnu" :
        reply = "Les actualités concernant la rubrique " + rubrique + " sont :\n\n"
        
        res = requests.get("http://www.lemonde.fr/" + rubrique + "/rss_full.xml")
        doc = lxml.etree.fromstring(res.content)
        
        items = False
        for item in doc.xpath('//item') :
            myDate = item.find('pubDate').text
            if myDate[0:2] == date.today().ctime()[0:2] :
                items = True
                reply += item.find('title').text.encode('utf-8') + "\n"
                line = lines[18]
                if line[len(line)-6:len(line)-2] == "True" :
                    reply += item.find('description').text.encode('utf-8') + "\n"
        if items == False :
            reply += "Pas d'actualistés aujourd'hui.\n"
     
    else :
        reply = "Il n'y a pas de rubrique " + line + "\n"
        
    file = open(PLUGIN_PATH + "/python/news.txt", "w")
    file.write(reply)
    file.close

news()
