# Microservices
Projet d'Exemple : Liste de Fruits
Ce projet consiste en une application web simple qui affiche une liste de fruits depuis une base de données MySQL. L'objectif principal est de démontrer l'utilisation de Flask pour créer une interface utilisateur et d'utiliser MySQL pour stocker et récupérer les données.

# Architecture
L'architecture du projet est la suivante :

![image](https://github.com/lucadipisa/Microservices-H3/assets/113420670/91851694-b235-4b90-9c7b-3e2419bd60d1)

Flask : Le composant principal qui gère les requêtes HTTP et affiche les données à l'utilisateur.
MySQL : La base de données qui stocke les informations sur les fruits, notamment leur nom, couleur et prix.
Les communications se font via les protocoles suivants :

Communication entre Flask et MySQL : Utilisation du protocole TCP/IP pour l'échange de requêtes SQL, principalement SELECT et CREATE pour interagir avec la base de données.
Communication entre le client et Flask : Utilisation du protocole HTTP/HTTPS pour accéder à l'application via un navigateur web. Les méthodes HTTP GET et POST sont utilisées pour récupérer des données depuis le serveur ou soumettre des données au serveur.
Les ports exposés sont les suivants :

Côté Client :

Flask expose le port 5000 pour que les clients accèdent à l'application via un navigateur web.
Côté Backend :

MySQL expose le port 3306 pour les connexions internes entre Flask et la base de données.
MySQL expose également le port 3307 côté client pour des connexions externes, bien que cela nécessite une configuration de sécurité appropriée.

#Technologies Utilisées
Flask : Framework web Python pour la création de l'interface utilisateur.
MySQL : Système de gestion de base de données relationnelles.
Docker : Pour l'orchestration et la mise en conteneurs des services Flask et MySQL.
Docker Compose : Pour la gestion multi-conteneur du projet.
HTML/CSS : Pour la création de la page web et de son style.
Python : Pour la logique applicative et la manipulation des données.
Ce projet vise à servir d'exemple de base pour la création d'applications web simples utilisant Flask et MySQL. Vous pouvez cloner le projet, suivre les étapes de configuration et d'exécution décrites dans le README, et l'adapter selon vos besoins.
