# Trouver une dose de vaccin avec Python et un Raspberry Pi

Petit script python permettant de trouver une dose de vaccin anti covid en fonction de nos coordonnées géographique et de la distance maximum souhaité.

## Prérequis
- Un compte sur l'api d'[open street maps](https://maps.open-street.com/gui/). Voici la [doc](https://fr.open-street.com/doc/api/route/) de l'api que j'ai utilisé. Vous aurez besoin d'une clé d'api qui vous sera fournit.
- Afin d'envoyer des notifications directement sur votre téléphone vous pouvez créer un compte gratuit sur pushover et télécharger l'appli. [https://pushover.net/](https://pushover.net/). Là encore vous aurez besoin du token et du user fournit à l'inscription.
- Éventuellement un petit serveur type Raspberry Pi pour faire tourner le script pendant une longue période.
- Vos coordonnées sous formes de longitude, latitude.

## Installation
- Créer à la racine du projet un fichier .env et copier à l'intérieur le contenu du fichier .env.exemple. Vous pouvez ensuite remplacer les infos avec vos infos. Ce fichier permet de configurer les différentes apis
- Installer les différents packages python s'ils ne le sont pas déjà :
    - python-dotenv
    - requests
    - os
    - Path
## Lancer le script

Vous pouvez installer le script sur un raspberry pi et appeler son execution toutes les 15 mins via un cron : 
```shell
0,15,30,45 * * * * /bin/python3 /home/pi/chronodose/main.py
```
