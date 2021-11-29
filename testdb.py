# il faut tout d'abord importer le SGBD de votre serveur en tapant la commande suivante
import mysql.connector as mc
# connecter votre serveur au python
connexion = mc.connect(
    host='127.0.0.1',
    user="root",
    password="",
    port=3306
)
# maintenat que la connexion est faite nous povons passer a la creation de la base de donneé
# on affect la valeur de la connexion dans une varibble où on lui  applique une fonction cursor
moncurser = connexion.cursor()
moncurser.execute('CREATE DATABASE bybeDB')




