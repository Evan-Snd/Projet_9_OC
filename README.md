# Project_LitReviews
Projet réalisé dans le cadre de ma formation OpenClassrooms Développeur d'Applications Python.  
Il s'agit d'une application web réalisée avec Django pour une société fictive, LitReviews.  
L'application est un réseau social permettant de demander et poster des critiques de livres.

## Fonctionnalités

* Inscription / connexion.
* Consulter un flux personnalisé en fonction de ses abonnements.
* Publier des demandes de critique.
* Publier des critiques en réponse à une demande ou pas en réponse.
* Modifier / supprimer ses demandes et critiques.
* Consulter ses abonnements et ses aboonés
* Rechercher un utilisateur.
* S'abonner / se désabonner d'un autre utilisateur.


## Installation & lancement

Commencez tout d'abord par installer Python.  
Lancez ensuite la console, placez vous dans le dossier de votre choix :
 - cd"Nom_du_dossier"

 Puis clonez ce repository:
- git clone [git@github.com:Evan-Snd/Projet_9_OC.git]

Placez vous dans le dossier P9_sinda_evan :
 - cd P9_sinda_evan

Puis créez un nouvel environnement virtuel si cela n'est pas déja fait:
 - python -m venv env

Ensuite, activez cet environnement
Windows:
 - env\scripts\activate.bat

Linux:
 - source env/bin/activate

Installez ensuite les packages requis:
 - pip install -r requirements.txt

Assurez vous d'être à la racine du projet (là ou se trouve le fichier manage.py)

Il ne vous reste plus qu'à lancer le serveur: 
 - python manage.py runserver

Vous pouvez ensuite utiliser l'applicaton à l'adresse suivante:
 - http://127.0.0.1:8000

Il existe déja trois utilisateurs sur le site :
- Nom d'utilisateur : Evan
- MDP : evan050295

- Nom d'utilisateur : Lilian
- MDP : lilian310898

- Nom d'utilisateur : Anne
- MDP : anne270365

Sinon vous pouvez créer votre propre utilisateur et :
- Suivre les utilisateurs ci-dessus afin de voir et pouvoir repondre à leur publications
- Créer vos propre publications
