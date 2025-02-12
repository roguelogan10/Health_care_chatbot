# 🤖 Conversation Chatbot

Ce projet est un chatbot de conversation basé sur **Streamlit** et **Ollama**. Il utilise le modèle **Mistral** pour répondre aux questions des utilisateurs.

## 🚀 Fonctionnalités
- Interface utilisateur avec **Streamlit**
- Modèle de langage via **Ollama**
- Historique de conversation
- Déploiement avec **Docker** et **Docker Compose**

## 📂 Structure du projet
```
📁 Health_care_chatbot
├── 📁 src
│    ├── 📁 src
│         ├── app.py            # Code principal du chatbot
│    ├── Dockerfile        # Fichier Docker pour le conteneur
│    ├── requirements.txt  # Dépendances Python
│    ├── docker-compose.yml # Déploiement multi-conteneurs
│    ├──    README.md            # Documentation du projet
```

---

## 💻 Installation et exécution

### 🔹 Prérequis
- Python 3.10+
- Docker & Docker Compose
- Ollama installé ([Télécharger ici](https://ollama.com/download))

### 🔹 Exécuter en local

1. **Cloner le dépôt**
   ```sh
   git clone https://github.com/ton_utilisateur/Health_care_chatbot.git
   cd Health_care_chatbot/src
   ```

2. **Installer les dépendances**
   ```sh
   pip install -r requirements.txt
   ```

3. **Lancer l'application**
   ```sh
   streamlit run app.py
   ```

L'interface est accessible sur `http://localhost:8501`.

---

## 🐳 Déploiement avec Docker

### 🔹 Construire et exécuter le conteneur Docker
```sh
docker build -t mon_chatbot .
docker run -p 8501:8501 mon_chatbot
```

### 🔹 Déploiement avec Docker Compose
1. **Créer et démarrer les services**
   ```sh
   docker-compose up -d --build
   ```
2. **Accéder au chatbot**
   ```
   http://localhost:8501
   ```

---

## 📦 Déploiement sur Docker Hub

1. **Se connecter à Docker Hub**
   ```sh
   docker login
   ```
2. **Taguer et pousser l'image**
   ```sh
   docker tag mon_chatbot ton_utilisateur/chatbot
   docker push ton_utilisateur/chatbot
   ```
3. **Lancer l'image depuis un serveur distant**
   ```sh
   docker pull ton_utilisateur/chatbot
   docker run -d -p 8501:8501 --name chatbot ton_utilisateur/chatbot
   ```

---

## 🛠️ Problèmes et solutions

### ❌ Erreur de connexion à Ollama
> **Problème** : `ConnectionError: Failed to connect to Ollama.`

✅ **Solution** : Utiliser Docker Compose avec Ollama
```sh
docker-compose up -d --build
```

---

## 📜 Licence
Ce projet est sous licence MIT.

---

## 🤝 Contribuer
Les contributions sont les bienvenues ! Ouvrez une **issue** ou faites une **pull request**. 😊

---

## ✨ Auteur
👤 **[Ton Nom](https://github.com/ton_utilisateur)**

---

🚀 _Bon chat avec ton bot !_

