import tkinter as tk
from tkinter import END, ACTIVE
import os

close = 'No'
def  switchframe(f1,f2):
    f1.pack_forget()
    f2.pack(expand='YES',fill='both')

def fermer():
    mainscreen.destroy()
def again():
    mainscreen.destroy()
    os.system('python c:/Users/Adel/Desktop/main.py')
def calc():
    temp  = float(temp_entry.get())
    tension = tension_select.index(ACTIVE)
    mob = mob_select.index(ACTIVE)
    uri = uri_select.index(ACTIVE)
    nut = nut_select.index(ACTIVE)
    douleur = douleur_select.index(ACTIVE)
    diab = diab_select.index(ACTIVE)
    hum = hum_select.index(ACTIVE)
    edm = edm_select.index(ACTIVE)
    epi = epi_select.index(ACTIVE)
    corti = corti_select.index(ACTIVE) 
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
    againbtn = tk.Button(result_frame,font=('Arial',30),text='Nouveau patient',command=again)
    againbtn.place(x=250,y=200)

    closebtn = tk.Button(result_frame,font=('Arial',30),text='Fermer',command=fermer)
    closebtn.place(x=650,y=200)


mainscreen = tk.Tk()
mainscreen.geometry('1300x720')
mainscreen.title("Assistant Plait de Lit")
mainscreen.configure(background='#FFFFFF')
mainframe = tk.Frame(mainscreen,padx=10,pady=90,bg='#1da1f2')
## main frame ##
title = tk.Label(mainframe,bg='#1da1f2',font=('Arial',30),text='APL - Assistant Plait de Lit ')
title.place(x=450,y=-80)
name_label = tk.Label(mainframe,bg='#1da1f2',font=('Arial',20),text='Nom :')
name_entry = tk.Entry(mainframe,font=('Arial',20))
name_label.grid(column=0,row=1,padx=250,pady=10)
name_entry.grid(column=1,row=1)
age_label = tk.Label(mainframe,bg='#1da1f2',font=('Arial',20),text='Age :')
age_entry = tk.Entry(mainframe,font=('Arial',20))
age_label.grid(column=0,row=2,pady=10)
age_entry.grid(column=1,row=2)
illness_label = tk.Label(mainframe,bg='#1da1f2',font=('Arial',20),text='Maladie :')
illness_entry = tk.Entry(mainframe,font=('Arial',20))
illness_label.grid(column=0,row=3,pady=10)
illness_entry.grid(column=1,row=3)
adresse_label = tk.Label(mainframe,bg='#1da1f2',font=('Arial',20),text='Adresse :')
adresse_entry = tk.Entry(mainframe,font=('Arial',20))
adresse_label.grid(column=0,row=4,pady=10)
adresse_entry.grid(column=1,row=4)
nextbtn = tk.Button(mainframe,text='Suivant',font=('Arial',20))


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
mob_label.grid(column=0,row=1,pady=200)
mob_select.grid(column=1,row=1)
nextbtn1 = tk.Button(frame2,text='Suivant',font=('Arial',20))
nextbtn1.grid(column=2,row=1)

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
calc_btn.grid(column=1,row=5,pady=50)



nextbtn['command'] = lambda arg1=mainframe , arg2=frame2: switchframe(arg1,arg2)
nextbtn1['command'] = lambda arg1=frame2 , arg2=frame3: switchframe(arg1,arg2)
nextbtn2['command'] = lambda arg1=frame3 , arg2=frame4: switchframe(arg1,arg2)

nextbtn.grid(column=1)
mainframe.pack(expand='YES',fill='both')

mainscreen.mainloop()

