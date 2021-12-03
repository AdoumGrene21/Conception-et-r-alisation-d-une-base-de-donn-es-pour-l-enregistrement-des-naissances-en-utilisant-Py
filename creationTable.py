from bdconnect import *


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




baseDeDonnees.commit()






baseDeDonnees.close()










#(select MAX(id) FROM blahblah)