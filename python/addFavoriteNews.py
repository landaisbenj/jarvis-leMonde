# -*- coding: utf-8 -*-
import os
import lxml.html
import requests
from datetime import date


PLUGIN_PATH = os.getcwd() + "/plugins/jarvis-leMonde"

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


def addFavoriteNews() :
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
        i = 0
        while i < len(lines) :
            l = lines[i]
            if l[0:len(rubrique) +11] == "jv_leMonde_" + rubrique :
                lines[i] = 'jv_leMonde_' + rubrique + '="True"\n'

            i += 1

        newLines = ""
        for l in lines :
            newLines += l

        file = open(PLUGIN_PATH + "/config.sh", "w")
        file.write(newLines)
        file.close()

        reply = "La rubrique " + rubrique + u" à bien été ajoutées\n"    
    else :
        reply = "Il n'y a pas de rubrique " + line + "\n"

    file = open(PLUGIN_PATH + "/python/rubrique.txt", "w")
    file.write(reply.encode('utf-8'))
    file.close()



addFavoriteNews()
