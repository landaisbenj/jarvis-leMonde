# -*- coding: utf-8 -*-
import os
import lxml.html
import requests
from datetime import date


PLUGIN_PATH = os.getcwd() + "/plugins_installed/jarvis-leMonde"

nomRubrique = ["international","politique","societe","economie","culture","idees",
            "planete","sport","sciences","pixels","campus","m-le-mag"]

lireRubrique = [0,0,0,0,0,0,0,0,0,0,0,0]


file = open(PLUGIN_PATH + "/config.sh")
lines = file.readlines()
file.close()

def dayNews() :
    i = 4
    while i < 16 :
        line = lines[i]
        if line[len(line)-6:len(line)-2] == "True" :
            lireRubrique[i-4] = 1
        i += 1

    reply = "Les actualités pour aujourd'hui sont :\n\n"
    i = 0
    nbr = 0
    while i < len(nomRubrique) :
        rubriqueOk = False
        if lireRubrique[i] == 1 :
            res = requests.get("http://www.lemonde.fr/" + nomRubrique[i] + "/rss_full.xml")
            doc = lxml.etree.fromstring(res.content)
            
            for item in doc.xpath('//item') :
                myDate = item.find('pubDate').text
                if myDate[0:2] == date.today().ctime()[0:2] :
                    nbr += 1
                    if rubriqueOk == False :
                        reply += "Rubrique " + nomRubrique[i] + ":\n\n"
                    rubriqueOk = True
                    reply += item.find('title').text.encode('utf-8') + "\n"
                    line = lines[18]
                    if line[len(line)-6:len(line)-2] == "True" :
                        reply += item.find('description').text.encode('utf-8') + "\n\n"
        i += 1

    if nbr == 0 :
        reply = "Il n'y a aucune actualités aujourd'hui.\n"
        
    file = open(PLUGIN_PATH + "/python/news.txt", "w")
    file.write(reply)
    file.close


dayNews()
