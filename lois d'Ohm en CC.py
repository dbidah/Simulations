from tkinter import *
# ===================== Fenêtre =====================
window = Tk()
window.title("Circuits électriques en CC")
window.geometry("1100x700")
# ===================== Variables globales =====================
mode_calcul = False
type_montage = "serie"
# ===================== Entrées =====================
Label(window, text="R1 (Ω)").grid(row=0, column=0)
A = Entry(window); A.grid(row=0, column=1)
Label(window, text="R2 (Ω)").grid(row=0, column=2)
B = Entry(window); B.grid(row=0, column=3)
Label(window, text="R3 (Ω)").grid(row=0, column=4)
C = Entry(window); C.grid(row=0, column=5)
Label(window, text="Tension U (V)").grid(row=0, column=6)
U_entry = Entry(window); U_entry.grid(row=0, column=7)
canvas = Canvas(window, width=1000, height=500, bg="white")
canvas.grid(row=3, column=0, columnspan=10)
resultat = Label(window, text="", font=("Arial", 14), fg="red")
resultat.grid(row=2, column=0, columnspan=10)
# ===================== Codes couleurs =====================
couleurs = {0:"black",1:"brown",2:"red",3:"orange",4:"yellow",
            5:"green",6:"blue",7:"violet",8:"grey",9:"white"}
def code_couleur(val):
    val = int(val)
    val_str = str(val)
    if val < 10:
        d1, d2, mult = 0, val, 0
    elif val < 100:
        d1, d2 = int(val_str[0]), int(val_str[1])
        mult = 0
    else:
        d1, d2 = int(val_str[0]), int(val_str[1])
        mult = len(val_str) - 2
    return couleurs[d1], couleurs[d2], couleurs[mult], "gold"
# ===================== Dessin =====================
def fil(x1,y1,x2,y2):
    canvas.create_line(x1,y1,x2,y2,width=2)
def R(x, y, nom, valeur):
    canvas.create_rectangle(x, y, x+80, y+30, fill="beige")
    canvas.create_text(x+40, y-10, text=nom, font=("Arial",12,"bold"))
    bandes = code_couleur(valeur)
    for i, c in enumerate(bandes):
        canvas.create_rectangle(x+10+i*20, y, x+20+i*20, y+30, fill=c)
# ✅ Générateur avec pôles
def G(x,y):
    r=40
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="lightblue")
    canvas.create_text(x,y,text=" G\nCC",font=("Arial",12,"bold"))
# ✅ Ampèremètre
def Ametre_fil(x1,y1,x2,y2,valeur=None):
    xm=(x1+x2)/2
    ym=(y1+y2)/2
    r=30
    canvas.create_oval(xm-r,ym-r,xm+r,ym+r,fill="green")
    txt="A"
    if valeur is not None:
        txt=f"{round(valeur,3)}"
    canvas.create_text(xm,ym+10,text="A",font=("Arial",18,"bold"), fill="white")
    canvas.create_text(xm,ym-10,text=txt,font=("Arial",9,"bold"), fill="white")
# ✅ Voltmètre
def Voltmetre(x,y,valeur=None,position="haut"):
    yv = y-45 if position=="haut" else y+60
    x1=x
    x2=x+80
    canvas.create_line(x1,y,x1,yv)
    canvas.create_line(x2,y,x2,yv)
    canvas.create_line(x1,yv,x2,yv)
    xm=(x1+x2)/2
    r=25
    canvas.create_oval(xm-r,yv-r,xm+r,yv+r,fill="blue")
    txt="V"
    if valeur is not None:
        txt=f"{round(valeur,2)}"
    canvas.create_text(xm,yv+10,text="V",font=("Arial",18,"bold"), fill="white")
    canvas.create_text(xm,yv-10,text=txt,font=("Arial",12,"bold"),fill="white")
# ✅ Flèche courant uniforme
def courant(x1, y1, x2, y2, nom, couleur="green"):
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2
    dx = x2 - x1
    dy = y2 - y1
    L = (dx**2 + dy**2) ** 0.5
    ux = dx / L
    uy = dy / L
    longueur = 40
    x_deb = xm - ux * longueur/2
    y_deb = ym - uy * longueur/2
    x_fin = xm + ux * longueur/2
    y_fin = ym + uy * longueur/2
    canvas.create_line(
        x_deb, y_deb, x_fin, y_fin,
        arrow=LAST,
        width=4,
        fill=couleur,
        arrowshape=(18,20,8))
    canvas.create_text(xm, ym - 15, text=nom,
                       font=("Arial", 11, "bold"),
                       fill=couleur)
# ===================== Lecture =====================
def get_values():
    return float(A.get()), float(B.get()), float(C.get()), float(U_entry.get())
def base():
    fil(200,100,200,400)
    fil(820,100,820,400)
    fil(200,400,820,400)
    fil(200,100,820,100)
    G(500,400)
    canvas.create_text(500, 450,text=(float(U_entry.get()),"V"),font=("Arial", 11, "bold"),tag="zeq_text")
def montage(type_montage):
    canvas.delete("all")
    base()
    R1, R2, R3, U = get_values()

    if type_montage == "serie":
        R(220,87,"R1", R1)
        R(420,87,"R2", R2)
        R(620,87,"R3", R3)

    elif type_montage == "derivation":
        fil(200,220,820,220)
        fil(200,340,820,340)
        R(460,87,"R1", R1)
        R(460,205,"R2", R2)
        R(460,325,"R3", R3)

    elif type_montage == "mixte1":
        fil(450,215,450,100)
        fil(450,215,820,215)
        R(350,87,"R1",R1)
        R(600,87,"R2",R2)
        R(600,200,"R3",R3)

    elif type_montage == "mixte2":
        fil(450,215,450,100)
        fil(450,215,820,215)
        R(350,87,"R2",R2)
        R(600,87,"R1",R1)
        R(600,200,"R3",R3)

    elif type_montage == "mixte3":
        fil(450,215,450,100)
        fil(450,215,820,215)
        R(350,87,"R3",R3)
        R(600,87,"R2",R2)
        R(600,200,"R1",R1)

    elif type_montage == "mixte4":
        fil(200,215,820,215)
        R(350,87,"R1",R1)
        R(600,87,"R2",R2)
        R(475,200,"R3",R3)

    elif type_montage == "mixte5":
        fil(200,215,820,215)
        R(350,87,"R1",R1)
        R(600,87,"R3",R3)
        R(475,200,"R2",R2)

    elif type_montage == "mixte6":
        fil(200,215,820,215)
        R(350,87,"R2",R2)
        R(600,87,"R3",R3)
        R(475,200,"R1",R1)

# ✅ R1_R2_R3
def mesures_serie():
    R1, R2, R3, U = get_values()
    # calculs
    Req = R1 + R2 + R3
    I = U / Req
    U1 = R1 * I
    U2 = R2 * I
    U3 = R3 * I
    I1 = I
    I2 = I
    I3 = I
    # ampèremètres
    Ametre_fil(320,100,420,100,I1)
    Ametre_fil(520,100,620,100,I2)
    Ametre_fil(720,100,820,100,I3)
    Ametre_fil(300,400,400,400,I)
    # Courants
    courant(600,400,200,400,"I")
    courant(192,100,450,100,"I1")
    courant(470,100,570,100,"I2")
    courant(670,100,770,100,"I3")
    # voltmètres
    Voltmetre(220,87,U1)
    Voltmetre(420,87,U2)
    Voltmetre(620,87,U3)
    # affichage résultat
    resultat.config(text=f"Req = {round(Req,1)} Ω")
# ✅ R1//R2//R3
def mesures_derivation():
    R1, R2, R3, U = get_values()
    Req = 1/(1/R1+1/R2+1/R3)
    I=U/Req
    U1 = U
    U2 = U
    U3 = U
    I1 = U/R1
    I2 = U/R2
    I3 = U/R3
    # Courant
    courant(600,400,200,400,"I")
    courant(140,100,500,100,"I1")
    courant(140,220,500,220,"I2")
    courant(140,340,500,340,"I3")
    # ampèremètres
    Ametre_fil(290,100,450,100,I1)
    Ametre_fil(290,220,450,220,I2)
    Ametre_fil(290,340,450,340,I3)
    Ametre_fil(300,400,400,400,I)
    # voltmètres
    Voltmetre(460,87,U)
    Voltmetre(460,205,U)
    Voltmetre(460,325,U)
    # affichage résultat
    resultat.config(text=f"Req = {round(Req,1)} Ω")
# ✅ R1_(R2 // R3)
def mesures_mixte_1():
    R1, R2, R3, U = get_values()
    # ===== calculs =====
    Req = R1 + (R2*R3)/(R2+R3)
    I = U / Req
    U1 = I * R1
    U2 = U - U1   # tension sur le dipôle parallèle
    U3 = U2
    I1 = I
    I2 = U2 / R2
    I3 = U3 / R3
    # ===== courants =====
    courant(600,400,200,400,"I")
    courant(200,100,450,100,"I1")
    courant(300,100,720,100,"I2")
    courant(300,215,720,215,"I3")
    # ===== ampèremètres =====
    Ametre_fil(250,100,300,100,I1)
    Ametre_fil(520,100,600,100,I2)
    Ametre_fil(520,215,600,215,I3)
    Ametre_fil(300,400,400,400,I)
    # ===== voltmètres =====
    Voltmetre(350,87,U1)
    Voltmetre(600,87,U2)
    Voltmetre(600,200,U3)
    # ===== résultat =====
    resultat.config(text=f"Req = {round(Req,2)} Ω")
# ✅ R2_(R1 // R3)
def mesures_mixte_2():
    R1, R2, R3, U = get_values()
    # ===== calculs =====
    Req = R2 + (R1*R3)/(R2+R3)
    I = U / Req
    I2 = I
    U2 = I2 * R2
    U1 = U - U2   # tension sur le dipôle parallèle
    U3 = U1
    I1 = U1 / R1
    I3 = U3 / R3
    # ===== courants =====
    courant(600,400,200,400,"I")
    courant(200,100,450,100,"I2")
    courant(300,100,720,100,"I1")
    courant(300,215,720,215,"I3")
    # ===== ampèremètres =====
    Ametre_fil(250,100,300,100,I2)
    Ametre_fil(520,100,600,100,I1)
    Ametre_fil(520,215,600,215,I3)
    Ametre_fil(300,400,400,400,I)
    # ===== voltmètres =====
    Voltmetre(350,87,U2)
    Voltmetre(600,87,U1)
    Voltmetre(600,200,U3)
    # ===== résultat =====
    resultat.config(text=f"Req = {round(Req,2)} Ω ")
# ✅ R3_(R2 // R1)
def mesures_mixte_3():
    R1, R2, R3, U = get_values()
    # ===== calculs =====
    Req = R3 + (R2*R1)/(R2+R1)
    I = U / Req
    U3 = I * R3
    U2 = U - U3   # tension sur le dipôle parallèle
    U1 = U2
    I3 = I
    I2 = U2 / R2
    I1 = U1 / R1
    # ===== courants =====
    courant(600,400,200,400,"I")
    courant(200,100,450,100,"I3")
    courant(300,100,720,100,"I2")
    courant(300,215,720,215,"I1")
    # ===== ampèremètres =====
    Ametre_fil(250,100,300,100,I3)
    Ametre_fil(520,100,600,100,I2)
    Ametre_fil(520,215,600,215,I1)
    Ametre_fil(300,400,400,400,I)
    # ===== voltmètres =====
    Voltmetre(350,87,U3)
    Voltmetre(600,87,U2)
    Voltmetre(600,200,U1)
    # ===== résultat =====
    resultat.config(text=f"Req = {round(Req,2)} Ω")
# ✅ (R1_R2)//R3
def mesures_mixte_4():
    R1, R2, R3, U = get_values()
    # ===== calculs =====
    Req = 1/(1/(R1+R2)+1/R3)
    I = U / Req
    # tension commune (montage parallèle)
    U3 = U
    # courants
    I3 = U / R3
    I1 = U / (R1 + R2)
    I2 = I1
    # répartition dans la série R1-R2
    U1 = I1 * R1
    U2 = I2 * R2
    # ===== courants =====
    courant(600,400,200,400,"I")
    courant(200,100,450,100,"I1")
    courant(300,100,720,100,"I2")
    courant(275,215,375,215,"I3")
    # ===== ampèremètres =====
    Ametre_fil(250,100,300,100,I1)
    Ametre_fil(520,100,600,100,I2)
    Ametre_fil(225,215,325,215,I3)
    Ametre_fil(300,400,400,400,I)
    # ===== voltmètres =====
    Voltmetre(350,87,U1)
    Voltmetre(600,87,U2)
    Voltmetre(475,200,U3)
    # ===== résultat =====
    resultat.config(text=f"Req = {round(Req,2)} Ω")
# ✅ (R1_R3)//R2
def mesures_mixte_5():
    R1, R2, R3, U = get_values()
    # ===== calculs =====
    Req = 1/(1/(R1+R3)+1/R2)
    I = U / Req
    # tension commune (montage parallèle)
    U2 = U
    # courants
    I2 = U / R2
    I1 = U / (R1 + R3)
    I3 = I1
    # répartition dans la série R1-R2
    U1 = I1 * R1
    U3 = I3 * R3
    # ===== courants =====
    courant(600,400,200,400,"I")
    courant(200,100,450,100,"I1")
    courant(300,100,720,100,"I3")
    courant(275,215,375,215,"I2")
    # ===== ampèremètres =====
    Ametre_fil(250,100,300,100,I1)
    Ametre_fil(520,100,600,100,I3)
    Ametre_fil(225,215,325,215,I2)
    Ametre_fil(300,400,400,400,I)
    # ===== voltmètres =====
    Voltmetre(350,87,U1)
    Voltmetre(600,87,U3)
    Voltmetre(475,200,U2)
    # ===== résultat =====
    resultat.config(text=f"Req = {round(Req,2)} Ω")
# ✅ (R2_R3)//R1
def mesures_mixte_6():
    R1, R2, R3, U = get_values()
    # ===== calculs =====
    Req = 1/(1/(R3+R2)+1/R1)
    I = U / Req
    # tension commune (montage parallèle)
    U1 = U
    # courants
    I1 = U / R1
    I2 = U / (R3 + R2)
    I3 = I2
    # répartition dans la série R3-R2
    U3 = I3 * R3
    U2 = I2 * R2
    # ===== courants =====
    courant(600,400,200,400,"I")
    courant(200,100,450,100,"I2")
    courant(300,100,720,100,"I3")
    courant(275,215,375,215,"I1")
    # ===== ampèremètres =====
    Ametre_fil(250,100,300,100,I2)
    Ametre_fil(520,100,600,100,I3)
    Ametre_fil(225,215,325,215,I1)
    Ametre_fil(300,400,400,400,I)
    # ===== voltmètres =====
    Voltmetre(350,87,U2)
    Voltmetre(600,87,U3)
    Voltmetre(475,200,U1)
    # ===== résultat =====
    resultat.config(text=f"Req = {round(Req,2)} Ω")
# ===================== RESET =====================
def reset():
    canvas.delete("all")
    resultat.config(text="")
    A.delete(0,END)
    B.delete(0,END)
    C.delete(0,END)
    U_entry.delete(0,END)
# ===================== GESTION MONTAGES =====================
type_montage = None
def choisir_montage(type_m):
    global type_montage
    type_montage = type_m
    montage(type_m)
# ===================== DICTIONNAIRE DES CALCULS =====================
dico_calculs = {
    "serie": mesures_serie,
    "derivation": mesures_derivation,
    "mixte1": mesures_mixte_1,
    "mixte2": mesures_mixte_2,
    "mixte3": mesures_mixte_3,
    "mixte4": mesures_mixte_4,
    "mixte5": mesures_mixte_5,
    "mixte6": mesures_mixte_6}
# ===================== FONCTION UNIQUE CALCUL =====================
def calculer():
    if type_montage is None:
        resultat.config(text="Choisir un montage")
        return
    # on redessine proprement le circuit
    canvas.delete("all")
    montage(type_montage)
    try:
        dico_calculs[type_montage]()  # lance la bonne fonction
    except ZeroDivisionError:
        resultat.config(text="Erreur : division par 0")
# ===================== BOUTONS =====================
Button(window, text="Série", bg="blue", fg="white",
       command=lambda: choisir_montage("serie")).grid(row=1, column=0)
Button(window, text="Dérivation", bg="red", fg="white",
       command=lambda: choisir_montage("derivation")).grid(row=1, column=1)
Button(window, text="R1_(R2//R3)", bg="green", fg="white",
       command=lambda: choisir_montage("mixte1")).grid(row=1, column=2)
Button(window, text="R2_(R1//R3)", bg="green", fg="white",
       command=lambda: choisir_montage("mixte2")).grid(row=1, column=3)
Button(window, text="R3_(R2//R1)", bg="green", fg="white",
       command=lambda: choisir_montage("mixte3")).grid(row=1, column=4)
Button(window, text="(R1_R2)//R3", bg="green", fg="white",
       command=lambda: choisir_montage("mixte4")).grid(row=1, column=5)
Button(window, text="(R1_R3)//R2", bg="green", fg="white",
       command=lambda: choisir_montage("mixte5")).grid(row=1, column=6)
Button(window, text="(R2_R3)//R1", bg="green", fg="white",
       command=lambda: choisir_montage("mixte6")).grid(row=1, column=7)
Button(window, text="CALCULER", bg="black", fg="white",
       command=calculer).grid(row=6, column=3, columnspan=2)
Button(window,text="RESET",bg="orange",command=reset).grid(row=6,column=5)
window.mainloop()
