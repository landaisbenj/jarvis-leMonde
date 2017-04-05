## Dependance
- python 3
- module lxml
- module Requests

## Description
Permet de récuperer les actualités du site 'Le Monde.fr'

Il y a deux modes de lecture des actualités
 -1) Mode général
 
La lecture se fera en fonction des rubriques activées dans le fichier config.sh

 -2) Mode rubrique
Seul la rubrique demandée sera lu par Jarvis


Le fichier config.sh permet égamelement de configurer Jarvis afin qu'il lise les descriptions ou non des actualités
(Le fait de lire les descriptifs peut être assez lourd et long)

## Usage
```
You: Quels sont les actualités du jour ?
Jarvis: Les actualités pour aujourd hui sont :
Jarvis: Rubrique sciences
Jarvis: Jarvis, l'assistant vocal open source qu il vous faut pour votre domotique
Jarvis:
Jarvis: Rubrique politique
Jarvis: on nous aurait menti!
You: Donne moi la liste des rubriques
Jarvis: il y a 12 rubriques : internationale, etc ...
You: quels sont les actualités de la rubrique science
Jarvis: Les actualités de la rubrique science sont :
Jarvis: *******
```

## Author
[RobyBioloid](https://github.com/RobyBioloid/jarvis-leMonde)
