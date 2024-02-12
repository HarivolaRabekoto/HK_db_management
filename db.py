import pandas as pd
import sqlite3

#fonction affichant les informations sur un membre à partir de son identifiant
def info_membre(id_recherche):
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    c.execute("SELECT * FROM membre WHERE (ID)= (?)",(id_recherche,))
    informations_membre=c.fetchall()
    #test d'existence de l'identifiant; si la requête renvoie une liste vide, on affecte false à la variable booléenne check que la fonction va retourner 
    if informations_membre==[]:
        check=False
    else:
        check=True
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
    return check

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
    
#fonction affichant les membres et les activités d'une pôle 
def info_pole(pole):
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    c.execute('SELECT nombre_activités FROM pôle WHERE nom_pôle=(?)', (pole,))
    nombre=c.fetchall()
    for i in nombre:
        nombre=i[0]
    print('Nombre d\'activités:',nombre)
    c.execute('SELECT ID, nom, prénoms FROM membre WHERE ID IN (SELECT ID_membre FROM membre_pôle WHERE pôle=(?))',(pole,))
    liste=c.fetchall()
    print ('Liste des membres:')
    print('Identifiant \t Nom \t\t\t Prénoms ')
    for i in liste:
        print(i[0] + '\t\t' + i[1] + '\t\t' + i[2] )
    c.execute('SELECT activité FROM pôle_activité WHERE pôle=(?)',(pole,))
    liste=c.fetchall()
    print ('Liste des activités:')
    for i in liste:
        print(i[0])
    conn.close()

#fonction modifiant une information sur un membre
def modification_membre(id_recherche,colonne,donnee):
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    if colonne==1:
        c.execute("UPDATE membre SET (nom)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colonne==2:
        c.execute("UPDATE membre SET (prénoms)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colonne==3:
        c.execute("UPDATE membre SET (email)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colonne==4:
        c.execute("UPDATE membre SET (cotisation)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colonne==5:
        c.execute("UPDATE membre SET (bénévolat)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colonne==6:
        c.execute("UPDATE membre SET (statut)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colonne==7:
        c.execute("UPDATE membre SET (assiduité)=(?) WHERE (ID)=(?)",(donnee,id_recherche,))
    elif colonne==8:
        c.execute("INSERT INTO membre_pôle VALUES(?,?))",(id_recherche,donnee,))
    conn.commit()
    conn.close()
    
#fonction ajoutant un membre
def ajout_membre(liste_info):
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    c.execute('INSERT INTO membre(ID, cotisation, nom, prénoms, email, bénévolat, statut) VALUES(?,?,?,?,?,?,?)',(liste_info))
    conn.commit()
    conn.close()
    
#fonction insérant les informations sur une activité
def creation_activite(intitule, date, lieu):
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    c.execute('INSERT INTO activité VALUES (?,?,?)',(intitule,date,lieu))
    conn.commit()
    conn.close
    
#fonction mettant en relation une activité et ses pôles d'organisation et incréméntant 
#le nombred'activités de la pôle concernée
def pole_organisation(pole, intitule):
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    if pole==1:
        nom_pole="outreach"
    elif pole==2:
        nom_pole="éducation"
    elif pole==3:
        nom_pole="observation et instrumentation"
    elif pole==4:
        nom_pole="développement et partenariat"
    c.execute('INSERT INTO pôle_activité VALUES (?,?)',(nom_pole,intitule))
    c.execute('SELECT nombre_activités FROM pôle WHERE nom_pôle=(?)',(nom_pole,))
    query_result=c.fetchall()
    for i in query_result:
        nombre=i[0]+1
    c.execute('UPDATE pôle SET nombre_activités=(?) WHERE nom_pôle=(?)',(nombre,nom_pole))
    conn.commit()
    conn.close()

#fonction enregistrant la présence d'une membre à une activité et incréméntant son assiduité
def presence(id_present,intitule):
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    c.execute("SELECT ID FROM membre WHERE (ID)= (?)",(id_present,))
    test=c.fetchall()
    if test==[]:
        check=False
    else:
        check=True
        c.execute('INSERT INTO membre_activité VALUES (?,?)',(id_present,intitule))
        c.execute('SELECT assiduité FROM membre WHERE ID=(?)',(id_present,))
        query_result=c.fetchall()
        for i in query_result:
            nombre=i[0]+1
        c.execute('UPDATE membre SET assiduité=(?) WHERE ID=(?)',(nombre,id_present,))
        conn.commit()
    conn.close()
    return check

#fonction affichant le nombre de membres présents à une activité et la liste de présence 
def liste_presence(intitule):
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    c.execute('SELECT COUNT(*) FROM membre_activité WHERE activité=(?)',(intitule,))
    nombre=c.fetchall()
    #using for loop to move out of the list
    for i in nombre:
            nombre=i[0]
    #test d'existence de l'activité; si on compte aucun membre correspondant à l'activité, l'activité ne peut exister, on affecte false à la variable booléenne check que la fonction va retourner 
    if nombre==0:
        check=False
    else:
        check=True
        print('Nombre de membres présents:',nombre)
        c.execute('SELECT ID, nom, prénoms FROM membre WHERE ID IN (SELECT ID_membre FROM membre_activité WHERE activité=(?))',(intitule,))
        liste=c.fetchall()
        print ('Liste de présence à l\'activité:')
        print('Identifiant \t Nom \t\t\t Prénoms ')
        for i in liste:
            print(i[0] + '\t\t' + i[1] + '\t\t' + i[2] )
    conn.close()
    return check

#fonction retournant le prochain identifiant 
def next_id():
    conn = sqlite3.connect("haikintana.db")
    c= conn.cursor()
    c.execute('SELECT rowid FROM membre ORDER BY rowid DESC LIMIT 1')
    num=c.fetchall()
    for i in num:
        num=i[0]
    #Le premier ID étant HK-0000 associé au rowid 1,le numéro dans l'ID suivant sera le même que le dernier rowid dans la base, on n'incrémente plus de 1
    if num<10:
        result='HK-000'+str(num)
    elif num>=10 and num<100:
        result='HK-00'+str(num)
    elif num>=100 and num<1000:
        result='HK-0'+str(num)
    else:
        result='HK-'+str(num)
    conn.close()
    return result
