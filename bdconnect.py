import mysql.connector

#####################################################################
#                                                                   #
# connection de la base de données 'Enregistrement_des_Naissances1' #
baseDeDonnees = mysql.connector.connect(
                                        host="localhost",
                                        user="root",
                                        password="21Janvier1995!",
                                        database="Enregistrement_des_Naissances2",
                                        auth_plugin='mysql_native_password'
                                        )
cursor = baseDeDonnees.cursor()