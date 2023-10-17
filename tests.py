import requests
import pymysql

# Vérification de la santé des conteneurs Docker
def test_sante_conteneurs():
    # Nom des conteneurs à vérifier (remplacez-les par les noms réels de vos conteneurs)
    conteneurs = ["monappflask", "monappsql"]

    for conteneur in conteneurs:
        try:
            # Utilisation de la commande "docker ps" pour vérifier si le conteneur est en cours d'exécution
            subprocess.check_output(["docker", "ps", "--filter", f"name={conteneur}"])
            print(f"Le conteneur {conteneur} est en cours d'exécution.")
        except subprocess.CalledProcessError:
            print(f"Le conteneur {conteneur} n'est pas en cours d'exécution.")


# Vérification du bon fonctionnement de l'application Flask
def test_bon_fonctionnement_application():
    # Insérez ici le code pour vérifier le bon fonctionnement de l'application Flask
    url = "http://adresse-du-serveur:5000/fruits"
    response = requests.get(url)
    if response.status_code == 200:
        print("L'application Flask fonctionne correctement.")
    else:
        print("Problème avec l'application Flask.")

# Vérification du bon fonctionnement de la base de données MySQL
def test_bon_fonctionnement_base_de_donnees():
    # Insérez ici le code pour vérifier le bon fonctionnement de la base de données MySQL
    connection = pymysql.connect(host='adresse-du-serveur', user='user', password='user', db='sampledb')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM fruits")
    results = cursor.fetchall()
    if len(results) > 0:
        print("La base de données fonctionne correctement.")
    else:
        print("Problème avec la base de données.")

# Exécution des tests
if __name__ == "__main__":
    test_sante_conteneurs()
    test_bon_fonctionnement_application()
    test_bon_fonctionnement_base_de_donnees()
