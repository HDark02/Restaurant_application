# 📱 Restaurant App

Application mobile réalisée avec **Kivy** et **KivyMD**, permettant l’inscription, la connexion, la gestion de profil utilisateur et la sauvegarde locale des données.

---

## ✨ Fonctionnalités

* 🟢 Écran de bienvenue, connexion et inscription
* 🟢 Connexion automatique si les données utilisateur existent
* 🟢 Sauvegarde des informations utilisateur dans `user_data.json`
* 🟢 Ajout et affichage d’une **photo de profil** via `filechooser`
* 🟢 Navigation fluide avec `ScreenManager`
* 🟢 Déconnexion avec suppression des données
* 🟢 Notifications "toast" intégrées

---

## 📸 Aperçu (facultatif)

> Ajoutez ici des captures d’écran de votre app :
> ![screenshot](assets/screenshot.png)

---

## 🛠️ Technologies utilisées

* **Python 3**
* **Kivy**
* **KivyMD**
* **Plyer**
* **JSON**

---

## 📁 Structure du projet

```
/
├── main.py
├── welcome.kv
├── login.kv
├── sign_up.kv
├── home.kv
├── user_data.json         # généré automatiquement
└── assets/
     └── user_photo.png
```

---

## 🚀 Installation

1. Clonez le projet :

```bash
git clone https://github.com/mon-projet/restaurant-app.git
cd restaurant-app
```

2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

ou manuellement :

```bash
pip install kivy kivymd plyer
```

3. Lancez l'application :

```bash
python main.py
```

---

## 🔍 Fonctionnement

### ✔ 1. Chargement initial

Au démarrage, l'application :

* tente de lire `user_data.json`
* connecte automatiquement l’utilisateur si les données existent
* sinon redirige vers l’écran **welcome**

### ✔ 2. Connexion (`data_login_on`)

* Vérification du nom/mot de passe
* Mise à jour des données dans l’interface
* Toast : *“Connecté…”*

### ✔ 3. Inscription (`sign_in`)

* Création et sauvegarde des données utilisateur
* Redirection vers la page d’accueil

### ✔ 4. Déconnexion (`deconnect`)

* Suppression de `user_data.json`
* Retour à l’écran de bienvenue

### ✔ 5. Ajout d’une photo

* Utilisation de `plyer.filechooser`
* Mise à jour dynamique de la photo de profil

---

## 🧩 Améliorations possibles

* Support de plusieurs utilisateurs
* Mot de passe masqué/affiché
* Base de données SQLite
* Mode sombre / clair
* Version APK Android via Buildozer

---

## 📄 Licence

Ce projet est distribué sous licence **MIT**.
Vous pouvez l’utiliser librement dans vos propres projets.

---

## 👤 Auteur

Projet développé par **Alex Dynamo**.
