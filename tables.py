import mysql.connector as mc
connexion = mc.connect(
    host="localhost",
    user="root",
    password="",
    port = 3306,
    database="bybedb")
moncurseur = connexion.cursor()
#creation de la table bebe
moncurseur.execute("CREATE TABLE bebe (\
                    id INT(20) AUTO_INCREMENT PRIMARY KEY,\
                    nom VARCHAR(50),\
                    prenom VARCHAR(50),\
                    sexe VARCHAR(50),\
                    id_pere INT(20),\
                    id_mere INT(20)\
                    );")
#creation de la table parent
moncurseur.execute("CREATE TABLE parent(\
                    id INT(20) AUTO_INCREMENT PRIMARY KEY,\
                    nom VARCHAR(150),\
                    prenom VARCHAR(150),\
                    sexe VARCHAR(150));")
#creation de la table fonctionnaire
moncurseur.execute("CREATE TABLE fonctionnaire(\
                    id INTEGER(20) AUTO_INCREMENT PRIMARY KEY,\
                    nom VARCHAR(150),\
                    prenom VARCHAR(150),\
                    login VARCHAR(150),\
                    passwd VARCHAR(150));")

