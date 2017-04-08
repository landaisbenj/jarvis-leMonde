# -*- coding: utf-8 -*-
import os
import lxml.html
import requests
from datetime import date


PLUGIN_PATH = os.getcwd() + "/plugins/jarvis-leMonde"

nomRubrique = ["international","politique","societe","economie","culture","idees",
            "planete","sport","sciences","pixels","campus","m-le-mag"]

lireRubrique = [0,0,0,0,0,0,0,0,0,0,0,0]


file = open(PLUGIN_PATH + "/config.sh")
lines = file.readlines()
file.close()

def favoriteNews() :
    reply = ""
    i = 4
    rubriques = ""
    while i < len(lines) :
        line = lines[i]
        if line[len(line)-6:len(line)-2] == "True" :
            lireRubrique[i-4] = 1
            rubriques += nomRubrique[i-4] + " \n"
        i += 1

    if rubriques == "" :
        reply = "Vous n'avez aucunes rubriques favorites !\n"
    else :
        reply = " Voici la liste de vos rubriques favorites :\n\n" + rubriques

    file = open(PLUGIN_PATH + "/python/favoriteNews.txt", "w")
    file.write(reply)
    file.close()

favoriteNews()
