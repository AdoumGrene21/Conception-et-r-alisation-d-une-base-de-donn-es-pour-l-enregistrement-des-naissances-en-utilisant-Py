import mysql.connector

#####################################################################
#                                                                   #
# connection de la base de données 'Enregistrement_des_Naissances1' #
baseDeDonnees = mysql.connector.connect(
                                        host="localhost",
                                        user="root",
                                        password="21Janvier1995!",
                                        database="Enregistrement_des_Naissances1",
                                        auth_plugin='mysql_native_password'
                                        )
cursor = baseDeDonnees.cursor()


#####################################################################
#                                                                   #
#   Structure de la table enfant                                  #
#   creation de la table enfant                                    #
cursor.execute("CREATE TABLE IF NOT EXISTS enfant (id int(11) NOT NULL,\
    nom varchar(150) NOT NULL,\
    prenom varchar(150) NOT NULL,\
    sexe varchar(150) NOT NULL,\
    id_parent int(11) NOT NULL,\
    id_fonctionnaire int(11) NOT NULL)\
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
#####################################################################


#####################################################################
#                                                                   #
#   Structure de la table `parent`                                  #
#   creation de la table parent'                                    #
cursor.execute("CREATE TABLE IF NOT EXISTS parent (\
   id int(11) NOT NULL,\
   nom varchar(150) NOT NULL,\
   prenom varchar(150) NOT NULL,\
   sexe varchar(150) NOT NULL\
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
#####################################################################


#####################################################################
#                                                                   #
#   Structure de la table `fonctionnaire`                           #
#   creation de la table fonctionnaire'                             #
cursor.execute("CREATE TABLE IF NOT EXISTS fonctionnaire (\
  id int(11) NOT NULL,\
  nom varchar(150) NOT NULL,\
  prenom varchar(150) NOT NULL,\
  login varchar(150) NOT NULL,\
  password varchar(45) NOT NULL\
) ENGINE=InnoDB DEFAULT CHARSET=utf8")
#####################################################################


#####################################################################
#                   Index pour les tables                           #
#####################################################################

#####################################################################
#                                                                   #
#    Index pour la table enfant                                     #
cursor.execute("ALTER TABLE enfant\
  ADD PRIMARY KEY (id),\
  ADD KEY id_parent (id_parent),\
  ADD KEY id_fonctionnaire (id_fonctionnaire);")
#####################################################################

#####################################################################
#                                                                   #
#    Index pour la table fonctionnaire                              #
cursor.execute("ALTER TABLE  fonctionnaire\
  ADD PRIMARY KEY (id);")
#####################################################################


#####################################################################
#                                                                   #
#    Index pour la table parent                                     #
cursor.execute("ALTER TABLE parent\
  ADD PRIMARY KEY (id);")
#####################################################################

#####################################################################
#                                                                   #
#    auto_increment                                                 #
cursor.execute("ALTER TABLE enfant\
  MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;")
#####################################################################
cursor.execute("ALTER TABLE parent\
  MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;")
#####################################################################
cursor.execute("ALTER TABLE fonctionnaire\
  MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;")
#####################################################################


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










#(select MAX(id) FROM blahblah)