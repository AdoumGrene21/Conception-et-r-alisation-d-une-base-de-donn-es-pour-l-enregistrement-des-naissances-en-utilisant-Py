# il faut tout d'abord importer le SGBD de votre serveur en tapant la commande suivante
import mysql.connector as mc
from bdconnect import *

cursor = baseDeDonnees.cursor()
cursor.execute('CREATE DATABASE Enregistrement_des_Naissances2')

