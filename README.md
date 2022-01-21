# hexagones
Animation dhexagones depuis fichiers python

1. Introduction
L’objectif est de récupérer les travail des élèves effectués sous Scratch (en réalité Blockly), via l’application Sofuspy (voir partie 2), et de récupérer les codes Python générés.
Ces codes Python sont lus par un programme externe (écrit aussi en Python), qui génère une vidéo animée du tracé des différents hexagones.
Pour cela, il faut respecter des conditions lors de la création des hexagones, explicitées dans la partie 3.
Le code général du programme est déposé sur la plateforme Github.

2. Qu’est-ce que SofusPy ?
C’est une application web qui permet de traduire un code blockly (cousin de Scratch) vers du code Python.
On peut accéder à Sofuspy via le site de l’IREM de la réunion :
https://irem.univ-reunion.fr/blockly/extensions/sofuspy/run.html

Ce billet du site de l’IREM de la réunion apporte des précisions : 
https://irem.univ-reunion.fr/spip.php?article924

Il est aussi possible de récupérer l’ensemble de l’application pour la faire tourner offline, elle est présente ici :
https://github.com/kerimbm/sofuspy3
L’application se lance dans un navigateur web en lançant index.html situé dans le dossier static.

3. Conditions pour l’hexagone
    • Chaque hexagone doit être orienté de façon à avoir deux côtés verticaux (et non pas horizontaux)
    • Le programme principal fait partir les hexagone depuis le centre.
    • Il ne faut pas utiliser de "Aller à la position (x,y)", car la position de chaque hexagone n'est pas absolue.
    
4. Lien pour déposer les fichiers
Les fichiers élèves pourront être déposés sur le lien https://cloud.divingeek.com/owncloud/index.php/s/myxgPg2zOgH0E2W dans le dossier sas.

5. Génération de la vidéo
Le script hexagone.py execute les différents scripts élèves du dossier travaux, et génère des images au format eps.
Ensuite, un script shell (linux) transforme ces eps en png, puis à l'aide de la librairie ffmpeg, crée une vidéo out.mp4
