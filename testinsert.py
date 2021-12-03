from bdconnect import *




fonctionnaires = [
	{"nom":"abakar", "prenom":"souleyman", "login":"code0", "password":"1234"},
	{"nom":"hassane", "prenom":"nasir", "login":"code1", "password":"1234"},
	{"nom":"haoua", "prenom":"mahamat", "login":"code2", "password":"1234"},
	{"nom":"ache", "prenom":"oumar", "login":"code3", "password":"1234"}
]
for fonctionnaire in fonctionnaires:
	cursor.execute("INSERT INTO fonctionnaire (nom, prenom,login,password) VALUES (%(nom)s, %(prenom)s, %(login)s, %(password)s)", fonctionnaire)
baseDeDonnees.commit()




parents = [
	{"nom":"abakar", "prenom":"souleyman", "sexe":"M"},
	{"nom":"hassane", "prenom":"nasir", "sexe":"M"},
	{"nom":"haoua", "prenom":"mahamat", "sexe":"F"},
	{"nom":"ache", "prenom":"oumar", "sexe":"F"}
]
for parent in parents:
	cursor.execute("INSERT INTO parent (nom, prenom,sexe) VALUES (%(nom)s, %(prenom)s, %(sexe)s)", parent)


baseDeDonnees.commit()






baseDeDonnees.close()