📱 Restaurant App – README

Une application mobile développée avec Kivy et KivyMD permettant la gestion d’un profil utilisateur avec inscription, connexion, déconnexion et persistance des données via un fichier JSON.

📌 Fonctionnalités

Écran de bienvenue, d’inscription et de connexion

Sauvegarde locale des informations utilisateur (user_data.json)

Connexion automatique si les données utilisateurs existent

Modification et affichage de la photo de profil via plyer.filechooser

Navigation fluide entre les écrans grâce à ScreenManager

Toast notifications pour les messages d’erreurs ou de succès

Déconnexion avec suppression automatique des données

🛠️ Technologies utilisées

Python 3

Kivy

KivyMD

Plyer

JSON / Pathlib

📂 Structure du projet
/
├── main.py
├── welcome.kv
├── login.kv
├── sign_up.kv
├── home.kv
├── user_data.json (généré automatiquement)
└── assets/
     └── user_photo.png

▶️ Lancement de l’application

Assure-toi d’avoir installé les dépendances :

pip install kivy kivymd plyer


Puis exécute simplement :

python main.py

🔍 Description du fonctionnement
◼️ 1. Chargement initial (on_start)

Au démarrage :

Le programme tente de charger les données du fichier user_data.json

Si elles existent → l’utilisateur est automatiquement connecté

Sinon → redirection vers l’écran de welcome

◼️ 2. Connexion (data_login_on)

Comparaison entre les informations entrées et celles enregistrées

Mise à jour de l’interface (nom, numéro, photo)

Affichage d’un message toast : “Connecté…”

◼️ 3. Inscription (sign_in)

Création d’un dictionnaire utilisateur

Sauvegarde dans user_data.json

Redirection vers la page d’accueil

◼️ 4. Déconnexion (deconnect)

Suppression du fichier user_data.json

Retour à l’écran de bienvenue

◼️ 5. Ajout d’une photo (add_picture)

Ouverture du sélecteur de fichiers (plyer.filechooser)

Mise à jour de l’image de profil dans l’écran d’inscription

🖼️ Interface

L’application est composée de :

welcome.kv : écran d’accueil

login.kv : connexion

sign_up.kv : inscription

home.kv : tableau de bord utilisateur

📌 Améliorations possibles

Ajout d’une base de données (SQLite)

Gestion de plusieurs utilisateurs

Masquage/affichage du mot de passe

Optimisation des chemins KV avec une structure modulaire

Ajout d’un thème sombre/clair

👤 Auteur

Projet développé avec Kivy/KivyMD.
