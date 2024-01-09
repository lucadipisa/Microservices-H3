# Microservices
Projet Microservices : Liste de Fruits

Ce projet consiste en une application web simple qui affiche une liste de fruits depuis une base de données MySQL. L'objectif principal est de démontrer l'utilisation de Flask pour créer une interface utilisateur et d'utiliser MySQL pour stocker et récupérer les données.

# Architecture
L'architecture du projet est la suivante :
![image](https://github.com/lucadipisa/Microservices-H3/assets/113420670/5f73454b-8fd9-4b5c-86a0-fc473b93f1ca)

# How to
 ```bash
docker-compose up -d --build
```


**Flask** : Le composant principal qui gère les requêtes HTTP et affiche les données à l'utilisateur.
**MySQL** : La base de données qui stocke les informations sur les fruits, notamment leur nom, couleur et prix.
Les communications se font via les protocoles suivants :

Communication entre Flask et MySQL : Utilisation du protocole TCP/IP pour l'échange de requêtes SQL, principalement SELECT et CREATE pour interagir avec la base de données.
Communication entre le client et Flask : Utilisation du protocole HTTP/HTTPS pour accéder à l'application via un navigateur web. Les méthodes HTTP GET et POST sont utilisées pour récupérer des données depuis le serveur ou soumettre des données au serveur.
Les ports exposés sont les suivants :

Côté Client : Flask expose le port 5000 pour que les clients accèdent à l'application via un navigateur web.

Côté Backend : MySQL expose le port 3306 pour les connexions internes entre Flask et la base de données.
MySQL expose également le port 3307 côté client pour des connexions externes, bien que cela nécessite une configuration de sécurité appropriée.

# Technologies Utilisées
- **Flask** : Framework web Python pour la création de l'interface utilisateur, choisi pour sa simplicité et rapidité de mise en oeuvre.
- **MySQL** : Système de gestion de base de données relationnelles, parfaite pour ma liste de fruits.
- **Docker** : Pour l'orchestration et la mise en conteneurs des services Flask et MySQL.
- **Docker** Compose : Pour la gestion multi-conteneur du projet.
- **HTML** : Pour la création de la page web et de son style en passant par un template. 
- **Python** : Pour la logique applicative et la manipulation des données.

# Image Docker sur Docker Hub
Exécution de la commande  afin de la tag avec mon nom utilisateur Docker
 ```bash
  docker tag myappsql axos15/monappsql
```

![image](https://github.com/lucadipisa/Microservices-H3/assets/113420670/e75678c5-dc6e-4405-9761-82ff7efe1a58).

Exécution de la commande  afin de pousser l'image sur le Hub
 ```bash
  docker push axos15/monappsql
```

![image](https://github.com/lucadipisa/Microservices-H3/assets/113420670/064103b6-39b6-408e-ba35-7d3a02df39aa)

# Axes d'améliorations futures

- Déploiement sur Azure (AKS et Azure SQL Database pour la BDD)
- Utilisation d'Azure Key Vault pour stocker tous les secrets (Ids BDD, SSL keys...)
- Intégrer une solution de monitoring (Azure Monitor...)
