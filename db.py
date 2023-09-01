import pandas as pd
import sqlite3

#fonction affichant les informations sur un membre à partir de son identifiant
def info_membre(id_recherche):
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    c.execute("SELECT * FROM membre WHERE (ID)= (?)",(id_recherche,))
    informations_membre=c.fetchall()
    #using for loop to move out of the list 
    for i in informations_membre:
        print('Nom: '+ i[2] + '\n'+
              'Prénoms: '+ i[3] + '\n'+
             'Contact: '+ i[4] + '\n'+
             'Cotisation: '+ i[1] + '\n'+
             'Bénévolat: '+ i[5] + '\n'+
             'Statut: '+ i[6] + '\n' +
             'Nombre d\'activités assistées: '+ str(i[7]) + '\n')
    conn.close()

#fonction affichant la liste des membres selon leur assiduité
def liste_selon_assiduité():
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    c.execute("SELECT ID, nom, prénoms, assiduité FROM membre ORDER BY assiduité DESC")
    liste_assiduite=c.fetchall()
    print('Identifiant \t Nom \t\t\t Prénoms \t Nombre d\'activités assistées')
    for i in liste_assiduite:
        print(i[0] + '\t\t' + i[1] + '\t\t' + i[2] + '\t\t' + str(i[3]) )
    conn.close()

#fonction modifiant une information d'un membre
def modification_membre(id_recherche,colomne,donnee):
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    if colomne==1:
        c.execute("UPDATE membre SET (nom)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colomne==2:
        c.execute("UPDATE membre SET (prénoms)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colomne==3:
        c.execute("UPDATE membre SET (contact)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colomne==4:
        c.execute("UPDATE membre SET (cotisation)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colomne==5:
        c.execute("UPDATE membre SET (bénévolat)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colomne==6:
        c.execute("UPDATE membre SET (statut)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colomne==7:
        c.execute("UPDATE membre SET (assiduité)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    else:
        colomne=int(input('Entrez uniquement un chiffre de 1 à 7 \n'))
        modification_membre(id_recherche,colomne,donnee)
    conn.commit()
    conn.close()