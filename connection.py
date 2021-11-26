from tkinter import *
import mysql.connector

baseDeDonnees = mysql.connector.connect(
                                        host="localhost",
                                        user="root",
                                        password="21Janvier1995!",
                                        database="naissancedb",
                                        auth_plugin='mysql_native_password'
                                        )

cursor = baseDeDonnees.cursor()





# ref. Swinnen, Apprendre à programmer avec Python, page 97
# Introduction to TKinter, page 84 ...
#
# le layer grid ; le widget Entry
#
fen = Tk () # la fenêtre de l'application
# les labels
labelUn = Label (fen, text="votre prénom :")
labelUn.grid (row = 1,column = 1, sticky = "E", padx = 10)
labelDeux = Label (fen, text="votre nom :")
labelDeux.grid (row = 2, column = 1, sticky = "E", padx = 10)
labelTrois = Label (fen, text="votre ville :")
labelTrois.grid (row = 3, column = 1, sticky = "E", padx = 10)
labelValider = Label (fen, text="") # label de la chaîne de validation
labelValider.grid (row = 4, column = 1, columnspan = 2,\
 sticky ="W",padx = 10)
# les entrées
entreeUn = Entry (fen)
entreeUn.grid (row = 1, column = 2)
entreeUn.focus_set()
entreeDeux = Entry (fen)
entreeDeux.grid (row = 2, column = 2)
entreeTrois = Entry (fen)
entreeTrois.grid (row = 3, column = 2)
# le cannevas et son image (232x245)
#cannevasImg = Canvas (fen, width =245, height = 258, bg = "dark green")
#photo = PhotoImage (file="a1_lotus.gif")
#image = cannevasImg.create_image(124, 131, image = photo)
#cannevasImg.grid(row = 1, column = 3, rowspan = 4, padx = 10, pady = 10)

# les boutons et leur gestion
def valider () :
 nom = str(entreeUn.get())
 prenom = str(entreeDeux.get())
 sexe = str(entreeTrois.get())

 chn = nom+" // "+ prenom+ " // "+ \
 sexe
 labelValider.config(text = chn)

 sql = "INSERT INTO parent(nom, prenom, sexe) VALUES(%s, %s, %s)"
 val = [nom, prenom, sexe]
 cursor.execute(sql,val)
 baseDeDonnees.commit()
 #baseDeDonnees.close()




def initialiser ():
 labelValider.config(text = "")
 entreeTrois.delete (0, END)
 entreeDeux.delete (0, END)
 entreeUn.delete (0, END)
 entreeUn.focus_set()
boutonQuitter = Button (fen, text=' Quitter ',command=fen.quit)
boutonQuitter.grid (row = 5, column = 3, pady = 10)
boutonValider = Button (fen, text=' Valider ',command=valider)
boutonValider.grid (row = 5, column = 1, pady = 10)
boutonInitialiser = Button (fen, text=' Réinitialiser ',\
 command=initialiser)
boutonInitialiser.grid (row = 5, column = 2, pady = 10)
fen.mainloop() # boucle de capture des événements
#fen.destroy() # fin de l'application


