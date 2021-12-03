from bdconnect import *





nom = input("nom enfant: ")
prenom = input("prenom enfant: ")
sexe= input("sexe: ")

lastidP = 6
lastidF = 6


 

cursor.execute("INSERT INTO enfant (nom, prenom, sexe, id_parent,id_fonctionnaire) VALUES (%s, %s, %s,%s, %s)", [nom, prenom ,sexe, lastidP, lastidF])
baseDeDonnees.commit()






baseDeDonnees.close()