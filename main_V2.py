import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime
from tkinter import END, ACTIVE, DISABLED, VERTICAL, RIGHT, Y, BOTH, LEFT
import os

close = 'No'
def  switchframe(f1,f2):
    f1.pack_forget()
    f2.pack(expand='YES',fill='both')

def fermer():
    mainscreen.destroy()
def again():
    mainscreen.destroy()
    os.system('python ./main_V2.py')
def calc():
    temp  = float(temp_entry.get())

    tension = tension_select.index(ACTIVE)
    tension2= extract_selected(tension_select)

    mob = mob_select.index(ACTIVE)
    mob2 = extract_selected(mob_select)

    uri = uri_select.index(ACTIVE)
    uri2= extract_selected(uri_select)

    nut = nut_select.index(ACTIVE)
    nut2 = extract_selected(nut_select)

    douleur = douleur_select.index(ACTIVE)
    douleur2 = extract_selected(douleur_select)

    diab = diab_select.index(ACTIVE)
    diab2 = extract_selected(diab_select)

    hum = hum_select.index(ACTIVE)
    hum2=extract_selected(hum_select)

    edm = edm_select.index(ACTIVE)
    edm2=extract_selected(edm_select)

    epi = epi_select.index(ACTIVE)
    epi2=extract_selected(epi_select)

    corti = corti_select.index(ACTIVE)
    corti2=extract_selected(corti_select) 

    score = 0


    if (temp <37):
        score += 1
    elif (temp <38):
        score += 3
    else:
        score += 5
    
    if (tension == 0):
        score += 1
    elif (tension == 1):
        score += 3
    else:
        score += 5

    if (mob == 0):
        score += 1
    elif (mob == 1):
        score += 3
    else:
        score += 5

    if (uri == 0):
        score += 1
    elif (uri == 1):
        score += 3
    else:
        score += 5 

    if (nut == 0):
        score += 1
    elif (nut == 1):
        score += 3
    else:
        score += 5               
    
    if (douleur == 0):
        score += 1
    elif (douleur == 1):
        score += 3
    else:
        score += 5
    
    if (hum == 0):
        score += 1
    elif (hum == 1):
        score += 3
    else:
        score += 5

    if (diab == 0):
        score += 1
    else:
        score += 4
    
    if (edm == 0):
        score += 1
    else:
        score += 3

    if (epi == 0):
        score += 1
    else:
        score += 3

    if (corti == 0):
        score += 1
    else:
        score += 3             
    msg = str(score) + ' le sujet est considéré à : '
    if (score <=13):
        msg += 'Faible Risque'
    elif (score <=25):
        msg += 'Risque Moyen'
    else:
        msg += 'Haut Risque' 


    insert_patient(name_entry.get(), age_entry.get(), illness_entry.get(), adresse_entry.get())
    insert_record(temp, tension2, mob2, uri2, nut2, douleur2, diab2, hum2, edm2, epi2, corti, score)
    insert_visite()

    result_frame = tk.Frame(mainscreen,padx=10,pady=90,bg='#1da1f2') 
    result_frame.pack()   
    result_label = tk.Label(result_frame,bg='#1da1f2',font=('Arial',30),text='RESULTAT')
    result_label.place(x=510,y=20)     
    concl = tk.Label(result_frame,bg='#1da1f2',font=('Arial',30),text='Le score est :')
    concl.place(x=100,y = 80)
    output_field = tk.Entry(result_frame,bg='#1da1f2',font=('Arial',30),width=35)
    output_field.place(x= 350, y=80)
    output_field.insert(0, msg)
    switchframe(frame4,result_frame)
    againbtn = tk.Button(result_frame,font=('Arial',20),text='Vers le menu principal',command=again)
    againbtn.place(x=280,y=200)

    closebtn = tk.Button(result_frame,font=('Arial',20),text='Fermer',command=fermer)
    closebtn.place(x=650,y=200)

def extract_selected(listbx):
    all_items = listbx.get(0, tk.END)
    print(all_items)
    selected_index=listbx.index(ACTIVE)
    print(selected_index)
    selected_item = all_items[selected_index]
    return str(selected_item)

def create_patient_table():
    print("Creating patient table..")
    conn = sqlite3.connect('visite.db')
    print("Database opened successfully")
    c=conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS patient (
    id_pat    INTEGER  PRIMARY KEY AUTOINCREMENT,
    nom_pat   TEXT NOT NULL,
    age_pat   INTEGER NOT NULL,
    maladie TEXT,
    adresse_pat TEXT );""")
    print(" table created successfully")
    conn.commit()
    conn.close()
    print("Database closed successfully")

def create_record_table():
    print("Creating records table..")
    conn = sqlite3.connect('visite.db')
    print("Database opened successfully")
    c=conn.cursor()
    print("Attempting to create record")
    c.execute("""CREATE TABLE IF NOT EXISTS record (

    id_record INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature   REAL NOT NULL ,
    tension TEXT,
    mobil_autonom TEXT,
    inconscience_uri  TEXT,
    nutrition TEXT,
    douleur   TEXT,
    diab  TEXT,
    humidite  TEXT,
    exist_problem TEXT,
    exist_diapo  TEXT,
    corti TEXT, 
    score REAL NOT NULL
);""")
    print(" table created successfully")
    conn.commit()
    conn.close()
    print("Database closed successfully")

def create_visite_table():
    print("Creating visite table..")
    conn = sqlite3.connect('visite.db')
    print("Database opened successfully")
    c=conn.cursor()
    print("Attempting to create users_expenses")
    c.execute(""" CREATE TABLE IF NOT EXISTS "visite" (
    id_pat    INTEGER,
    id_record INTEGER,
    datee  INTEGER,
    FOREIGN KEY("id_pat") REFERENCES "patient"("id_pat") ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY("id_record") REFERENCES "record"("id_record") ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY("id_pat","id_record")
);""")
    print(" table created successfully")
    conn.commit()
    conn.close()
    print("Database closed successfully")

def insert_record(temp, tension,  mob, uri, nut, douleur, diab, hum, edm, epi, corti, score):
    print("adding record to DB")
    conn=sqlite3.connect('visite.db')
    c=conn.cursor()
    c.execute("""INSERT INTO record(temperature, tension, mobil_autonom, inconscience_uri, nutrition,douleur, diab, humidite, exist_diapo, exist_problem, corti, score)
     VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",(temp, tension, mob, uri, nut, douleur,diab, hum, edm, epi, corti, score))
    conn.commit()
    conn.close()
    print("record was added")

def insert_patient(nom, age, maladie, adresse ):
    print("adding patient's informations to DB")
    conn=sqlite3.connect('visite.db')
    c=conn.cursor()
    c.execute("""INSERT INTO patient(nom_pat, age_pat, maladie,
            adresse_pat) VALUES(?,?,?,?)""",(nom, age, maladie, adresse))

    conn.commit()
    conn.close()
    print("patient's informations were added")


def insert_visite():
    print("adding to visite")
    conn=sqlite3.connect('visite.db')
    c=conn.cursor()
    last_id=c.execute("select max(id_pat) from patient")
    last_id=last_id.fetchall()[0][0]
    print("LAST ID = {}".format(last_id))
    c.execute("""INSERT INTO visite(id_pat, id_record,datee) VALUES(?,?,?)""",(last_id,last_id, datetime.datetime.today().strftime('%d%m%y')))

    conn.commit()
    conn.close()
    print("patient's informations were added")



def searchrecord():
    name = oldsearch_entry.get()

    conn=sqlite3.connect('visite.db')
    c=conn.cursor()
    c.execute("select * from patient where nom_pat = (?)",(name,))
    res=c.fetchall()
    print(res)
    if (len(res) == 0):
        messagebox.showerror("Erreur!","Nom inexistant!")
    else:
        oldresframe = tk.Frame(mainscreen,padx=10,pady=90,bg='#1da1f2')
        oldres_label = tk.Label(oldresframe,bg='#1da1f2',font=('Arial',20),text='Nom du patient : ')
        box = tk.Frame(oldresframe)
        box.place(x=450,y=200)
        oldres_list = tk.Listbox(box,font=('Arial',20),height=4,width=28)
        scroll = tk.Scrollbar(box,orient=VERTICAL)
        scroll.pack(side=RIGHT,fill=Y)
        
        oldres_list.config(yscrollcommand=scroll.set)
        oldres_label.place(x=150,y=100)
        oldres_list.pack(side=LEFT,fill= BOTH)
        scroll.config(command=oldres_list.yview)
        
        ##Insert data instead of this for statement ##

        c.execute("""select score from record where id_record in 
            (select id_record from visite where id_pat in 
            (select id_pat from patient where nom_pat=(?)) )""", (name,))
        scores=c.fetchall()
        scores=[score[0] for score in scores]
        print("LES SCORES SONT :" ,scores)


        c.execute("select datee from visite where id_pat in (select id_pat from patient where nom_pat = (?))",(name,))
        dates=c.fetchall()
        dates=[date[0] for date in dates]
        print("DATES ", dates)
        print("LES SCORES SONT :" ,scores)

        historique=list()
        for i in range(len(scores)):
            historique.append(str(scores[i])+'    DATE : '+ str(dates[i]) )


        for x in historique:
            oldres_list.insert(END, x)

        patientname_entry = tk.Entry(oldresframe,bg='#1da1f2',font=('Arial',20))
        patientname_entry.insert(0, name)
        patientname_entry.place(x=450, y=100)
        listlabel = tk.Label(oldresframe,bg='#1da1f2',font=('Arial',20),text='Historique : ')
        listlabel.place(x=150,y=200)
        switchframe(oldframe,oldresframe)
    conn.commit()
    conn.close()

mainscreen = tk.Tk()
mainscreen.geometry('1300x720')
mainscreen.title("Assistant Plait de Lit")
mainscreen.configure(background='#FFFFFF')
newpatient1 = tk.Frame(mainscreen,padx=10,pady=90,bg='#1da1f2')
mainframe = tk.Frame(mainscreen,padx=10,pady=90,bg='#1da1f2')
############

create_patient_table()
create_record_table()
create_visite_table()

## mainframe ##
maintitle = tk.Label(mainframe,bg='#1da1f2',font=('Arial',30),text='APL - Assistant Plait de Lit ')
maintitle.place(x=430,y=120)
newrecordbtn = tk.Button(mainframe,font=('Arial',20),text='Ajouter un nouveau patient')
newrecordbtn.place(x=150,y=280)
oldrecordbtn = tk.Button(mainframe,font=('Arial',20),text='Consulter un patient')
oldrecordbtn.place(x=850,y=280)

## oldframe ##
oldframe = tk.Frame(mainscreen,padx=10,pady=90,bg='#1da1f2')
oldtitle = tk.Label(oldframe,bg='#1da1f2',font=('Arial',30),text='Consulter un score précedant ')
oldtitle.place(x=400,y=80)

oldsearch_label = tk.Label(oldframe,bg='#1da1f2',font=('Arial',20),text='Nom du patient : ')
oldsearch_entry = tk.Entry(oldframe,font=('Arial',20))
oldsearch_label.place(x=350,y=200)
oldsearch_entry.place(x=650,y=200)

oldsearchbtn = tk.Button(oldframe,font=('Arial',20),text='Chercher',command=searchrecord)
oldsearchbtn.place(x=550,y=350)






## newpatient1 ##
title = tk.Label(newpatient1,bg='#1da1f2',font=('Arial',30),text='Données Personelles ')
title.place(x=450,y=-80)
name_label = tk.Label(newpatient1,bg='#1da1f2',font=('Arial',20),text='Nom :')
name_entry = tk.Entry(newpatient1,font=('Arial',20))
name_label.grid(column=0,row=1,padx=250,pady=10)
name_entry.grid(column=1,row=1)
age_label = tk.Label(newpatient1,bg='#1da1f2',font=('Arial',20),text='Age :')
age_entry = tk.Entry(newpatient1,font=('Arial',20))
age_label.grid(column=0,row=2,pady=10)
age_entry.grid(column=1,row=2)
illness_label = tk.Label(newpatient1,bg='#1da1f2',font=('Arial',20),text='Maladie :')
illness_entry = tk.Entry(newpatient1,font=('Arial',20))
illness_label.grid(column=0,row=3,pady=10)
illness_entry.grid(column=1,row=3)
adresse_label = tk.Label(newpatient1,bg='#1da1f2',font=('Arial',20),text='Adresse :')
adresse_entry = tk.Entry(newpatient1,font=('Arial',20))
adresse_label.grid(column=0,row=4,pady=10)
adresse_entry.grid(column=1,row=4)
nextbtn = tk.Button(newpatient1,text='Suivant',font=('Arial',20))
nextbtn.grid(column=1)
retourbtn1 = tk.Button(newpatient1,text='Retour',font=('Arial',20))
retourbtn1.grid(column=1,row=6,pady=10)

## Frame2 ##
frame2 = tk.Frame(mainscreen,padx=10,pady=50,bg='#1da1f2')
temp_label = tk.Label(frame2,bg='#1da1f2',font=('Arial',20),text='Température :')
temp_entry = tk.Entry(frame2, font=('Arial',20))
temp_label.grid(column=0,row=0,padx=50,pady=10)
temp_entry.grid(column=1,row=0,padx=10)
tension_label = tk.Label(frame2,bg='#1da1f2',font=('Arial',20),text='Tension Artérielle :')
tension_select = tk.Listbox(frame2,font=('Arial',20),height=3)
tension_select.insert(END, 'Dans la norme','Hypertension','Hypotension')
tension_label.grid(column=2,row=0,padx=10,pady=10)
tension_select.grid(column=3,row=0)



mob_label = tk.Label(frame2,bg='#1da1f2',font=('Arial',20),text='Mobilité et autonomie :')
mob_select = tk.Listbox(frame2,font=('Arial',20),height=4)
mob_select.insert(END, 'Légère dépendance','Dépendance modérée','Dépendance sévère','Dépendance entière')
mob_label.grid(column=0,row=1)
mob_select.grid(column=1,row=1)
nextbtn1 = tk.Button(frame2,text='Suivant',font=('Arial',20), command = lambda : extract_selected(tension_select))
nextbtn1.grid(column=2,row=3)

retourbtn2 = tk.Button(frame2,text='Retour',font=('Arial',20))
retourbtn2.grid(column=1,row=3,pady=10)

## Frame3 ##
frame3 = tk.Frame(mainscreen,padx=10,pady=50,bg='#1da1f2')
uri_label = tk.Label(frame3,bg='#1da1f2',font=('Arial',20),text='Incontinence urinaire :')
uri_select = tk.Listbox(frame3,font=('Arial',20),height=3,width=30)
uri_select.insert(END, 'Pas d''incontinence','Incontinence occasionnelle','Incontinence urinaire et fécaleva')
uri_label.grid(column=0,row=0,padx=50,pady=10)
uri_select.grid(column=1,row=0)

nut_label = tk.Label(frame3,bg='#1da1f2',font=('Arial',20),text='Nutrition:')
nut_select = tk.Listbox(frame3,font=('Arial',20),height=3,width=60)
nut_select.insert(END, 'Etat nutritionnel satisfaisant','Risque de malnutrition malgré l''abscence de signe clinique ou biologique','Malnutrition protéino-énergétique')
nut_label.grid(column=0,row=1,pady=20)
nut_select.grid(column=1,row=1,pady=20)

douleur_label = tk.Label(frame3,bg='#1da1f2',font=('Arial',20),text='Perception de la douleur :')
douleur_select = tk.Listbox(frame3,font=('Arial',20),height=3,width=30)
douleur_select.insert(END, 'Normal','Limité','Nulle')
douleur_label.grid(column=0,row=2,pady=10)
douleur_select.grid(column=1,row=2)

nextbtn2 = tk.Button(frame3,text='Suivant',font=('Arial',20))
nextbtn2.grid(column=1,row=3,pady=50)

retourbtn3 = tk.Button(frame3,text='Retour',font=('Arial',20))
retourbtn3.grid(column=0,row=3,pady=10)

## frame 4 ##
frame4 = tk.Frame(mainscreen,padx=10,pady=50,bg='#1da1f2')
diab_label = tk.Label(frame4,bg='#1da1f2',font=('Arial',20),text='Diabétique :')
diab_select = tk.Listbox(frame4,font=('Arial',20),height=2,width=30)
diab_select.insert(END, 'Non','Oui')
diab_label.grid(column=0,row=0,padx=50,pady=10)
diab_select.grid(column=1,row=0)

hum_label = tk.Label(frame4,bg='#1da1f2',font=('Arial',20),text='Humidité:')
hum_select = tk.Listbox(frame4,font=('Arial',20),height=3,width=30)
hum_select.insert(END, 'Peau normal','Peau parfois humide','Peau très humide')
hum_label.grid(column=0,row=1,pady=20)
hum_select.grid(column=1,row=1,pady=20)

edm_label = tk.Label(frame4,bg='#1da1f2',font=('Arial',20),text='Existence de diapositif médicale :')
edm_select = tk.Listbox(frame4,font=('Arial',20),height=2,width=30)
edm_select.insert(END, 'Non','Oui')
edm_label.grid(column=0,row=2,pady=10)
edm_select.grid(column=1,row=2)

epi_label = tk.Label(frame4,bg='#1da1f2',font=('Arial',20),text='Existence de problème immunitaire :')
epi_select = tk.Listbox(frame4,font=('Arial',20),height=2,width=30)
epi_select.insert(END, 'Non','Oui')
epi_label.grid(column=0,row=3,pady=10)
epi_select.grid(column=1,row=3)

corti_label = tk.Label(frame4,bg='#1da1f2',font=('Arial',20),text='Le sujet reçoit ine corticothérapie :')
corti_select = tk.Listbox(frame4,font=('Arial',20),height=2,width=30)
corti_select.insert(END, 'Non','Oui')
corti_label.grid(column=0,row=4,pady=10)
corti_select.grid(column=1,row=4)

calc_btn = tk.Button(frame4,text='Calculer',font=('Arial',20),command=calc)
calc_btn.grid(column=1,row=5,pady=30)

retourbtn4 = tk.Button(frame4,text='Retour',font=('Arial',20))
retourbtn4.grid(column=1,row=6)



nextbtn['command'] = lambda arg1=newpatient1 , arg2=frame2: switchframe(arg1,arg2)
retourbtn1['command'] = lambda arg1=mainframe , arg2=newpatient1: switchframe(arg2,arg1)
nextbtn1['command'] = lambda arg1=frame2 , arg2=frame3: switchframe(arg1,arg2)
retourbtn2['command'] = lambda arg1=frame2 , arg2=newpatient1: switchframe(arg1,arg2)
nextbtn2['command'] = lambda arg1=frame3 , arg2=frame4: switchframe(arg1,arg2)
retourbtn3['command'] = lambda arg1=frame3 , arg2=frame2: switchframe(arg1,arg2)
retourbtn4['command'] = lambda arg1=frame4 , arg2=frame3: switchframe(arg1,arg2)
newrecordbtn['command'] = lambda arg1=mainframe , arg2=newpatient1: switchframe(arg1,arg2)
oldrecordbtn['command'] = lambda arg1=mainframe , arg2=oldframe: switchframe(arg1,arg2)



mainframe.pack(expand='YES',fill='both')
mainscreen.mainloop()

