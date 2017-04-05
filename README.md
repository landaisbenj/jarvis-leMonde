## Dependance
- python 3
- module lxml
- module Requests

## Description
Permet de récupérer les actualités du site 'Le Monde.fr' et de les faire dire par Jarvis

Il y a deux modes de lecture des actualités
 -1) Mode général
La lecture se fera en fonction des rubriques qui ont été activées dans le fichier config.sh

 -2) Mode rubrique
Seul la rubrique demandé sera lu par Jarvis


Le fichier config.sh permet égamelement de configurer Jarvis afin qu'il lise les description ou non des actualité
(le fait de lire les descriptif peut être assez lourd et long)

## Usage
```
You: Quels sont les actualités du jour ?
Jarvis: Les actualités pour aujourd'hui sont :
Jarvis: Rubrique sciences
Jarvis: Jarvis, l'assistant vocal open source qu'il vous faut pour votre domotique
Jarvis:
Jarvis: Rubrique politique
Jarvis: on nous aurait menti!
You: Donne moi la liste des rubriques
Jarvis: il y a 12 rubriques : internationale, etc ...
You: quels sont les actualité de la rubrique science
Jarvis: Les actualités de la rubrique science sont :
Jarvis: ********

```

## Author
[RobyBioloid](https://github.com/RobyBioloid/jarvis-leMonde)
