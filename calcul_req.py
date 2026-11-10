import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
# ==================================
# Codes couleurs
# ==================================
couleurs = {0: "black",1: "brown",2: "red",3: "orange",4: "yellow",5: "green",6: "blue",7: "violet",8: "grey",9: "white"}
def code_couleur(R):
    R = int(R)
    if R < 10:
        d1 = 0
        d2 = R
        mult = 0
    elif R < 100:
        txt = str(R)
        d1 = int(txt[0])
        d2 = int(txt[1])
        mult = 0
    else:
        txt = str(R)
        d1 = int(txt[0])
        d2 = int(txt[1])
        mult = len(txt) - 2
    return (couleurs[d1],couleurs[d2],couleurs[mult],"gold")
# ==================================
# Dessin résistance
# ==================================
def dessiner_resistance(ax, x, y, valeur, nom):
    c1, c2, c3, c4 = code_couleur(valeur)
    ax.add_patch(plt.Rectangle((x, y - 0.25),2,0.5,facecolor="#F5DEB3",edgecolor="black",linewidth=2))
    bandes = [(c1, x + 0.3),(c2, x + 0.7),(c3, x + 1.1),(c4, x + 1.6)]
    for couleur, xpos in bandes:
        ax.add_patch(plt.Rectangle((xpos, y - 0.25),0.08,0.5,color=couleur))
    ax.text(x + 1,y + 0.55,f"{nom}\n{valeur:.0f} Ω",ha="center",fontsize=10,fontweight="bold")
# ==================================
# Dessin ohmmètre
# ==================================
def dessiner_ohmmetre(ax, x, y, Req=None):
    cercle = plt.Circle((x, y),0.7,fill=False,linewidth=2,color="blue")
    ax.add_patch(cercle)
    ax.text(x,y + 0.2,"Ω",fontsize=18,fontweight="bold",ha="center")
    valeur = "?"
    if Req is not None:
        valeur = f"{Req:.2f}"
    ax.text(x,y - 0.25,valeur,fontsize=10,fontweight="bold",color="red",ha="center")
# ==================================
# Schéma série
# ==================================
def schema_serie(R1, R2, R3, Req):
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.plot([0, 1], [0, 0], "k", linewidth=2)
    ax.plot([3, 4], [0, 0], "k", linewidth=2)
    ax.plot([6, 7], [0, 0], "k", linewidth=2)
    ax.plot([9, 10], [0, 0], "k", linewidth=2)
    dessiner_resistance(ax, 1, 0, R1, "R1")
    dessiner_resistance(ax, 4, 0, R2, "R2")
    dessiner_resistance(ax, 7, 0, R3, "R3")
    # Connexion ohmmètre
    ax.plot([0, 0], [0, -1], "b")
    ax.plot([10, 10], [0, -1], "b")
    ax.plot([0, 4.3], [-1, -1], "b")
    ax.plot([5.7, 10], [-1, -1], "b")
    dessiner_ohmmetre(ax,5,-1,Req)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-2, 2)
    ax.axis("off")
    return fig
# ==================================
# Schéma parallèle
# ==================================
def schema_parallele(R1, R2, R3, Req):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot([0, 0], [0, 6], "k", linewidth=2)
    ax.plot([8, 8], [0, 6], "k", linewidth=2)
    # R1
    ax.plot([0, 3], [6, 6], "k", linewidth=2)
    ax.plot([5, 8], [6, 6], "k", linewidth=2)
    dessiner_resistance(ax,3,6,R1,"R1")
    # R2
    ax.plot([0, 3], [4, 4], "k", linewidth=2)
    ax.plot([5, 8], [4, 4], "k", linewidth=2)
    dessiner_resistance(ax,3,4,R2,"R2")
    # R3
    ax.plot([0, 3], [2, 2], "k", linewidth=2)
    ax.plot([5, 8], [2, 2], "k", linewidth=2)
    dessiner_resistance(ax,3,2,R3,"R3")
    # Connexion ohmmètre
    ax.plot([0, 0], [0, 0], "b")
    ax.plot([8, 8], [0, 0], "b")
    ax.plot([0, 3.3], [0, 0], "b")
    ax.plot([4.7, 8], [0, 0], "b")
    dessiner_ohmmetre(ax,4,0,Req)
    ax.set_xlim(-1, 9)
    ax.set_ylim(-2, 6.5)
    ax.axis("off")
    return fig
# ==================================
# Montages mixtes
# ==================================
def schema_mixte1(R1, R2, R3, Req):
    fig, ax = plt.subplots(figsize=(12, 6))
    # Branche supérieure
    ax.plot([0, 1], [4, 4], "k", lw=2)
    dessiner_resistance(ax, 1, 4, R1, "R1")
    ax.plot([3, 5], [4, 4], "k", lw=2)
    dessiner_resistance(ax, 5, 4, R2, "R2")
    ax.plot([7, 8], [4, 4], "k", lw=2)
    # Branche inférieure
    ax.plot([0, 3], [1, 1], "k", lw=2)
    dessiner_resistance(ax, 3, 1, R3, "R3")
    ax.plot([5, 8], [1, 1], "k", lw=2)
    # Montants gauche et droite
    ax.plot([0, 0], [1, 4], "k", lw=2)
    ax.plot([8, 8], [1, 4], "k", lw=2)
    # Connexion de l'ohmmètre
    ax.plot([0, 0], [1, -1], "b", lw=2)
    ax.plot([8, 8], [1, -1], "b", lw=2)
    ax.plot([0, 3.3], [-1, -1], "b", lw=2)
    ax.plot([4.7, 8], [-1, -1], "b", lw=2)
    dessiner_ohmmetre(ax, 4, -1, Req)
    ax.set_xlim(-1, 9)
    ax.set_ylim(-2, 6)
    ax.axis("off")
    return fig
def schema_mixte2(R1, R2, R3, Req):
    fig, ax = plt.subplots(figsize=(12, 6))
    # Entrée
    ax.plot([0, 1], [2, 2], "k", lw=2)
    # Noeud gauche
    ax.plot([1, 1], [1, 3], "k", lw=2)
    # Branches hautes
    dessiner_resistance(ax, 2, 3, R1, "R1")
    ax.plot([1, 2], [3, 3], "k", lw=2)
    ax.plot([4, 5], [3, 3], "k", lw=2)
    # Branches basses
    dessiner_resistance(ax, 2, 1, R2, "R2")
    ax.plot([1, 2], [1, 1], "k", lw=2)
    ax.plot([4, 5], [1, 1], "k", lw=2)
    # Noeud droit parallèle
    ax.plot([5, 5], [1, 3], "k", lw=2)
    # Liaison vers R3
    ax.plot([5, 6], [2, 2], "k", lw=2)
    dessiner_resistance(ax, 6, 2, R3, "R3")
    ax.plot([8, 10], [2, 2], "k", lw=2)
    # Bornes
    ax.plot(0, 2, "ko", ms=8)
    ax.plot(10, 2, "ko", ms=8)
    # Ohmmètre
    ax.plot([0, 0], [2, -1], "b", lw=2)
    ax.plot([10, 10], [2, -1], "b", lw=2)
    ax.plot([0, 4.3], [-1, -1], "b", lw=2)
    ax.plot([5.7, 10], [-1, -1], "b", lw=2)
    dessiner_ohmmetre(ax, 5, -1, Req)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-2, 5)
    ax.axis("off")
    return fig
    # ==================================
    # Interface Streamlit
    # ==================================
def afficher():
    # -----------------------------
    # Variables de session
    # -----------------------------
    # ===============================
    if "mesures_parallele" not in st.session_state:
        st.session_state.mesures_parallele = []
    if "mesures_mixte1" not in st.session_state:
        st.session_state.mesures_mixte1 = []
    if "mesures_mixte2" not in st.session_state:
        st.session_state.mesures_mixte2 = []
    if "cours_valide" not in st.session_state:
        st.session_state.cours_valide = False
    if "calculer" not in st.session_state:
        st.session_state.calculer = False
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "question" not in st.session_state:
        st.session_state.question = 0
    if "mesures_serie" not in st.session_state:
        st.session_state.mesures_serie = []
    if "afficher_G" not in st.session_state:
        st.session_state.afficher_G = False
    if "page" not in st.session_state:
        st.session_state.page = "cours"
    if "score_qcm" not in st.session_state:
        st.session_state.score_qcm = 0
    if "qcm_valide" not in st.session_state:
        st.session_state.qcm_valide = False
    if "score_activite" not in st.session_state:
        st.session_state.score_activite = 0
    if "serie_valide" not in st.session_state:
        st.session_state.serie_valide = False
    if "parallele_q1_valide" not in st.session_state:
        st.session_state.parallele_q1_valide = False
    if "gr_relation_valide" not in st.session_state:
        st.session_state.gr_relation_valide = False
    if "additivite_valide" not in st.session_state:
        st.session_state.additivite_valide = False
    if "mixte1_valide" not in st.session_state:
        st.session_state.mixte1_valide = False
    if "mixte2_valide" not in st.session_state:
        st.session_state.mixte2_valide = False
    # ============================
    # Les 4 questions
    # ============================
    questions = [
        {"nom": "Série","bonnes_reponses": ["Req = R1 + R2 + R3"]},
        {"nom": "Parallèle","bonnes_reponses": ["Req = 1/(G1+G2+G3)"]},
        {"nom": "(R1 + R2) // R3",
        "bonnes_reponses": ["Req = 1/(1/(R1+R2) + G3)"]},
        {"nom": "(R1 // R2) + R3","bonnes_reponses": ["Req = 1/(G1 + G2) + R3"]}]
    # ============================
    # BILAN FINAL
    # ============================
    if st.session_state.question >= len(questions):
        # ----------------------------
        # Score et appréciation
        # ----------------------------
        score = st.session_state.score_activite
        st.subheader("🎯 Résultats")
        st.metric(
            "Score global",
            f"{score}/10",)
        if score == 10:
            appreciation = "🏆 Activité terminée avec succès ! - 🌟 Excellent travail !"
            st.balloons()
        elif score >= 7.5:
            appreciation = "👏 Très bon travail !"
        elif score >= 5:
            appreciation = "✅ Travail satisfaisant."
        elif score >= 2.5:
            appreciation = "⚠️ Des notions restent à consolider."
        else:
            appreciation = "📘 Des révisions sont nécessaires."
        st.info(appreciation)
        st.title("🎓 Bilan de l'activité")
        # ----------------------------
        # Montage série
        # ----------------------------
        st.markdown("### 🔴 Montage en série")
        st.write("Les résistances s'ajoutent :")
        st.latex(r"R_{eq}=R_1+R_2+R_3")
        # ----------------------------
        # Montage parallèle
        # ----------------------------
        st.markdown("### 🔵 Montage en parallèle")
        st.write("Les conductances s'ajoutent :")
        st.latex(r"G_{eq}=G_1+G_2+G_3")
        st.write("avec :")
        st.latex(r"G=\frac{1}{R}")
        st.write("donc :")
        st.latex(r"\frac{1}{R_{eq}}=\frac{1}{R_1}+\frac{1}{R_2}+\frac{1}{R_3}")
        # ----------------------------
        # Montage mixte n°1
        # ----------------------------
        st.markdown("### 🟢 Montage mixte n°1")
        st.write("(R₁ + R₂) // R₃")
        st.latex(r"R_{eq}=\frac{1}{\frac{1}{R_1+R_2}+\frac{1}{R_3}}")
        # ----------------------------
        # Montage mixte n°2
        # ----------------------------
        st.markdown("### 🟠 Montage mixte n°2")
        st.write("(R₁ // R₂) + R₃")
        st.latex(r"R_{eq}=\frac{1}{\frac{1}{R_1}+\frac{1}{R_2}}+R_3")
        return
        st.stop()
    # ============================
    # LE RESTE DE L'APPLICATION
    # ============================
    st.title("⚡ Résistance et Conductance")
    # ============================
    # PAGE QCM
    # ============================
    if not st.session_state.cours_valide and st.session_state.page == "qcm":
        st.header("✅ Vérification des connaissances")
        q1 = st.radio(
            "1) Dans une association série :",["Les résistances s'ajoutent","Les conductances s'ajoutent",
                "Req est plus petite que toutes les résistances"],index=None,key="qcm1")
        q2 = st.radio(
            "2) Dans une association parallèle :",["Les résistances s'ajoutent","Les conductances s'ajoutent",
                "Req est plus grande que toutes les résistances"],index=None,key="qcm2")
        q3 = st.radio(
            "3) Dans une association série :",["La résistance équivalente est supérieure à la plus grande résistance",
                "La conductance équivalente est supérieure à la plus grande conductance",
                "La conductance équivalente est égale à la somme des conductances"],index=None,key="qcm3")
        q4 = st.radio(
            "4) Dans une association parallèle :",["La résistance équivalente est supérieure à la plus grande résistance",
                "La conductance équivalente est inférieure à la plus grande conductance",
                "La conductance équivalente est égale à la somme des conductances"],index=None,key="qcm4")
        if st.button("📝 Valider le QCM", use_container_width=True):
            score = 0
            if q1 == "Les résistances s'ajoutent":
                score += 1
            if q2 == "Les conductances s'ajoutent":
                score += 1
            if q3 == "La résistance équivalente est supérieure à la plus grande résistance":
                score += 1
            if q4 == "La conductance équivalente est égale à la somme des conductances":
                score += 1
            st.session_state.score_qcm = score
            st.session_state.qcm_valide = True
            pourcentage = score * 25
            if score == 4:
                st.success(f"✅ {pourcentage}% de bonnes réponses (4/4). Bravo !")
                st.session_state.cours_valide = True
                st.session_state.question = 0
                st.session_state.page = "simulation"
                st.rerun()
            else:
                st.error(f"❌ {pourcentage}% de bonnes réponses ({score}/4).")
        # Affichage du bouton seulement après un échec
        if (st.session_state.qcm_valide and st.session_state.score_qcm < 4):
            if st.button(
                "📘 Revoir le cours",
                use_container_width=True):
                st.session_state.page = "cours"
                st.rerun()
        st.stop()
    # ============================
    # COURS
    # ============================
    if not st.session_state.cours_valide and st.session_state.page == "cours":
        st.header("📘 Essentiel du cours")
        st.markdown("""
    **La résistance :**
    - La résistance électrique (**R**) mesure l'aptitude d'un dipôle à s'opposer au passage du courant électrique.
    - Elle s'exprime en **ohms** (**Ω**).
    **La conductance :**
    - La conductance (**G**) mesure l'aptitude d'un dipôle à conduire le courant électrique.
    - Elle est l'inverse de la résistance :
    G = 1/R
    - Elle s'exprime en **siemens** (**S**).
    ✅ Plus la résistance est grande, plus la conductance est faible.
    **Exemples :**
    - R = 10 Ω  → G = 0,1 S
    - R = 100 Ω → G = 0,01 S""")
        st.subheader("Association en série")
        st.markdown("""
    - Les résistances s'ajoutent :
    **Req = R1 + R2 + R3**
    - La résistance équivalente est supérieure à la plus grande résistance.""")
        st.subheader("Association en parallèle")
        st.markdown("""
    - Les conductances s'ajoutent :
    **Geq = G1 + G2 + G3**
    - La résistance équivalente est :
    **Req = 1 / Geq**
    - La résistance équivalente est inférieure à la plus petite résistance.""")
        st.subheader("Associations mixtes")
        st.code("""
    1. Repérer les résistances en série ou en parallèle.
    2. Calculer leur équivalent.
    3. Recommencer jusqu'à obtenir une seule résistance.
    4. Vérifier la cohérence du résultat.""")
        st.button("✅ Passer au QCM",use_container_width=True,on_click=lambda: st.session_state.update(page="qcm"))
        st.stop()
    # ============================
    # MONTAGE ÉTUDIÉ
    # ============================
    montage = questions[st.session_state.question]["nom"]
    titres = {"Série": "🔴 Montage en série","Parallèle": "🔵 Montage en parallèle","(R1 + R2) // R3": "🟢 Montage mixte n°1","(R1 // R2) + R3": "🟠 Montage mixte n°2"}
    st.header(titres[montage])
    # ============================
    # INITIALISATION DES SLIDERS
    # ============================
    if "R1_slider" not in st.session_state:
        st.session_state.R1_slider = 100
    if "R2_slider" not in st.session_state:
        st.session_state.R2_slider = 220
    if "R3_slider" not in st.session_state:
        st.session_state.R3_slider = 330
    R1 = st.session_state.R1_slider
    R2 = st.session_state.R2_slider
    R3 = st.session_state.R3_slider
    # ============================
    # CALCUL DE LA RÉSISTANCE ÉQUIVALENTE
    # ============================
    G1 = 1 / R1
    G2 = 1 / R2
    G3 = 1 / R3
    if montage == "Série":
        Req = R1 + R2 + R3
    elif montage == "Parallèle":
        Geq = G1 + G2 + G3
        Req = 1 / Geq
    elif montage == "(R1 + R2) // R3":
        R12 = R1 + R2
        G12 = 1 / R12
        Geq = G12 + G3
        Req = 1 / Geq
    elif montage == "(R1 // R2) + R3":
        G12 = G1 + G2
        R12 = 1 / G12
        Req = R12 + R3
    # ============================
    # SCHÉMA DU MONTAGE
    # ============================
    if montage == "Série":
        fig = schema_serie(R1, R2, R3, Req)
    elif montage == "Parallèle":
        fig = schema_parallele(R1, R2, R3, Req)
    elif montage == "(R1 + R2) // R3":
        fig = schema_mixte1(R1, R2, R3, Req)
    elif montage == "(R1 // R2) + R3":
        fig = schema_mixte2(R1, R2, R3, Req)
    st.pyplot(fig)
    plt.close(fig)
    # ============================
    # SLIDERS SOUS LE SCHÉMA
    # ============================
    st.subheader("Valeurs des résistances")
    col1, col2, col3 = st.columns(3)
    with col1:
        R1 = st.slider("R1 (Ω)",min_value=10,max_value=1000,step=10,key="R1_slider")
    with col2:
        R2 = st.slider("R2 (Ω)",min_value=10,max_value=1000,step=10,key="R2_slider")
    with col3:
        R3 = st.slider("R3 (Ω)",min_value=10,max_value=1000,step=10,key="R3_slider")
    st.info('Modifiez les résistances avec les curseurs puis cliquez sur "**➕ Ajouter la mesure**".')
    # ============================
    # GESTION DES MESURES
    # ============================
    if montage == "Série":
        mesures = st.session_state.mesures_serie
    elif montage == "Parallèle":
        mesures = st.session_state.mesures_parallele
    elif montage == "(R1 + R2) // R3":
        mesures = st.session_state.mesures_mixte1
    elif montage == "(R1 // R2) + R3":
        mesures = st.session_state.mesures_mixte2
    # ============================
    # BOUTONS DE MESURE
    # ============================
    # st.subheader("📊 Enregistrement des mesures")
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("➕ Ajouter la mesure",use_container_width=True):
            if len(mesures) < 4:
                mesures.append({"R1": R1,"R2": R2,"R3": R3,"Req": round(Req, 2)})
                st.success(f"Mesure {len(mesures)} enregistrée.")
            else:
                st.warning("Le tableau contient déjà les 4 essais.")
    with col_btn2:
        if st.button("🗑️ Effacer les mesures",use_container_width=True):
            mesures.clear()
            if montage == "Parallèle":
                st.session_state.afficher_G = False
                # st.session_state.gr_valide = False
            st.rerun()
    # ============================
    # TABLEAU D'OBSERVATION ET D'ANALYSE
    # ============================
    st.subheader("🔍 Tableau d'observation")
    tableau = []
    for i in range(4):
        if i < len(mesures):
            m = mesures[i]
            # Cas du tableau des conductances
            if montage == "Parallèle" and st.session_state.afficher_G:
                G1_mes = round(1000 / m["R1"], 2)
                G2_mes = round(1000 / m["R2"], 2)
                G3_mes = round(1000 / m["R3"], 2)
                Geq_mes = round(G1_mes + G2_mes + G3_mes,2)
                tableau.append({"Essai": i + 1,"G1 (mS)": G1_mes,"G2 (mS)": G2_mes,"G3 (mS)": G3_mes,"Geq (mS)": Geq_mes})
            # Cas du tableau des résistances
            else:
                tableau.append({"Essai": i + 1,"R1 (Ω)": int(m["R1"]),"R2 (Ω)": int(m["R2"]),"R3 (Ω)": int(m["R3"]),"Req (Ω)": round(m["Req"], 2)})
        else:
            # Lignes vides jusqu'à 4 essais
            if montage == "Parallèle" and st.session_state.afficher_G :
                tableau.append({"Essai": i + 1,"G1 (mS)": "","G2 (mS)": "","G3 (mS)": "","Geq (mS)": ""})
            else:
                tableau.append({"Essai": i + 1,"R1 (Ω)": "","R2 (Ω)": "","R3 (Ω)": "","Req (Ω)": ""})
    df = pd.DataFrame(tableau)
    st.dataframe(
        df.style
        .format({"Req (Ω)": lambda x: f"{x:.2f}" if x != "" else "",
            "G1 (mS)": lambda x: f"{x:.2f}" if x != "" else "",
            "G2 (mS)": lambda x: f"{x:.2f}" if x != "" else "",
            "G3 (mS)": lambda x: f"{x:.2f}" if x != "" else "",
            "Geq (mS)": lambda x: f"{x:.2f}" if x != "" else ""})
        .set_properties(**{
            "text-align": "center"}),
        hide_index=True,
        use_container_width=True)
    st.caption("Complétez les 4 essais puis observez l'évolution de la résistance ou de la conductance équivalente.")
    # ============================
    # RECHERCHE DE LA RELATION
    # ============================
    # MONTAGE EN SÉRIE
    if "tentative_serie" not in st.session_state:
        st.session_state.tentative_serie = False
    # Initialisation
    if "message_serie" not in st.session_state:
        st.session_state.message_serie = None
    if montage == "Série":
        st.subheader("📝 Recherche de la relation")
        relation = st.text_input("À partir du tableau, écrivez la relation entre R1, R2, R3 et Req :",key="relation_serie",disabled=st.session_state.tentative_serie)
        if not st.session_state.tentative_serie:
            if st.button("✅ Valider"):
                st.session_state.tentative_serie = True
                texte = relation.replace(" ", "").lower()
                if texte == "req=r1+r2+r3":
                    st.session_state.message_serie = ("success","✅ Bonne réponse !")
                    if not st.session_state.serie_valide:
                        st.session_state.score_activite += 2
                        st.session_state.serie_valide = True
                else:
                    st.session_state.message_serie = ("error","❌ Relation incorrecte. Dans un montage série, les résistances s'ajoutent : Req = R1 + R2 + R3")
                st.rerun()
        # Affichage du résultat après le rerun
        if st.session_state.message_serie:
            type_msg, texte_msg = st.session_state.message_serie
            if type_msg == "success":
                st.success(texte_msg)
            else:
                st.error(texte_msg)
    # ------------------------------------------------
    # MONTAGE EN PARALLÈLE
    # ------------------------------------------------
    # Question 1
    if "tentative_parallele_q1" not in st.session_state:
        st.session_state.tentative_parallele_q1 = False
    if "message_parallele_q1" not in st.session_state:
        st.session_state.message_parallele_q1 = None
    # Question 2
    if "tentative_gr" not in st.session_state:
        st.session_state.tentative_gr = False
    if "message_gr" not in st.session_state:
        st.session_state.message_gr = None
    # Question 3
    if "tentative_relation_g" not in st.session_state:
        st.session_state.tentative_relation_g = False
    if "message_relation_g" not in st.session_state:
        st.session_state.message_relation_g = None
    elif montage == "Parallèle":
        # ------------------------------------------------
        # QUESTION 1
        # ------------------------------------------------
        st.subheader("🧐 Recherche de la relation")
        reponse = st.radio("La relation suivante est-elle vérifiée : Req = R1 + R2 + R3 ?",["Oui", "Non"],index=None,key="test_parallele",disabled=st.session_state.tentative_parallele_q1)
        if not st.session_state.tentative_parallele_q1:
            if st.button("✅ Valider", key="valider_q1"):
                st.session_state.tentative_parallele_q1 = True
                if reponse == "Non":
                    st.session_state.message_parallele_q1 = ("success","✅ Bonne réponse !")
                    if not st.session_state.parallele_q1_valide:
                        st.session_state.score_activite += 1
                        st.session_state.parallele_q1_valide = True
                elif reponse == "Oui":
                    st.session_state.message_parallele_q1 = ("error","❌ Erreur : dans un montage parallèle, Req n'est pas égale à R1 + R2 + R3.")
                else:
                    st.session_state.message_parallele_q1 = ("warning","⚠️ Choisissez d'abord une réponse.")
                st.rerun()
        if st.session_state.message_parallele_q1:
            type_msg, texte_msg = st.session_state.message_parallele_q1
            if type_msg == "success":
                st.success(texte_msg)
            elif type_msg == "error":
                st.error(texte_msg)
            else:
                st.warning(texte_msg)
        # ==================================================
        # QUESTION 2
        # ==================================================
        if st.session_state.tentative_parallele_q1:
            st.markdown("### ① Relation entre G et R")
            relation_GR = st.text_input("Quelle est la relation entre la conductance G et la résistance R ?",key="relation_GR",disabled=st.session_state.tentative_gr)
            if not st.session_state.tentative_gr:
                if st.button("✅ Valider", key="valider_gr"):
                    st.session_state.tentative_gr = True
                    texte = relation_GR.replace(" ", "").lower()
                    if texte in ["g=1/r", "g=1÷r"]:
                        st.session_state.message_gr = ("success","✅ Bonne réponse !")
                        if not st.session_state.gr_relation_valide:
                            st.session_state.score_activite += 1
                            st.session_state.gr_relation_valide = True
                    else:
                        st.session_state.message_gr = ("error","❌ Erreur : la conductance est l'inverse de la résistance : G = 1/R")
                    st.rerun()
            if st.session_state.message_gr:
                type_msg, texte_msg = st.session_state.message_gr
                if type_msg == "success":
                    st.success(texte_msg)
                else:
                    st.error(texte_msg)
        # ==================================================
        # QUESTION 3
        # ==================================================
        if st.session_state.tentative_gr:
            st.markdown("### ② Tableau des conductances")
            if len(st.session_state.mesures_parallele) < 4:
                st.warning(f"Complétez d'abord les 4 essais ({len(st.session_state.mesures_parallele)}/4 enregistrés) pour accéder au calcul des conductances.")
            else:
                if not st.session_state.afficher_G:
                    if st.button("🔄 Remplacer les résistances par les conductances"):
                        st.session_state.afficher_G = True
                        st.rerun()
                st.info("Comparez les valeurs de G1, G2, G3 et Geq.")
            relation_G = st.text_input("Écrivez la relation observée :",key="relation_G",disabled=st.session_state.tentative_relation_g)
            if not st.session_state.tentative_relation_g:
                if st.button("✅ Valider", key="valider_relation_G"):
                    st.session_state.tentative_relation_g = True
                    texte = relation_G.replace(" ", "").lower()
                    if texte in ["geq=g1+g2+g3","req=1/(1/r1+1/r2+1/r3)"]:
                        st.session_state.message_relation_g = ("success","✅ Bonne réponse !")
                        if not st.session_state.additivite_valide:
                            st.session_state.score_activite += 2
                            st.session_state.additivite_valide = True
                    else:
                        st.session_state.message_relation_g = ("error","❌ Erreur. Dans un montage parallèle, les conductances s'ajoutent : Geq = G1 + G2 + G3")
                    st.rerun()
            if st.session_state.message_relation_g:
                type_msg, texte_msg = st.session_state.message_relation_g
                if type_msg == "success":
                    st.success(texte_msg)
                else:
                    st.error(texte_msg)
    # ------------------------------------------------
    # MONTAGE MIXTE N°1
    # ------------------------------------------------
    if "tentative_mixte1" not in st.session_state:
        st.session_state.tentative_mixte1 = False
    if "message_mixte1" not in st.session_state:
        st.session_state.message_mixte1 = None
    if montage == "(R1 + R2) // R3":
        st.subheader("📝 Recherche de la relation")
        relation = st.text_input(
            "À partir du tableau, écrivez la relation entre R1, R2, R3 et Req :",
            key="relation_mixte1",
            disabled=st.session_state.tentative_mixte1)
        if not st.session_state.tentative_mixte1:
            if st.button("✅ Valider"):
                st.session_state.tentative_mixte1 = True
                texte = relation.replace(" ", "").lower()
                if texte in ["req=1/(1/(r1+r2)+1/r3)","req=1/(1/(r1+r2)+g3)","req=(r1+r2)*r3/(r1+r2+r3)"]:
                    st.session_state.message_mixte1 = ("success","✅ Bonne réponse !")
                    if not st.session_state.mixte1_valide:
                        st.session_state.score_activite += 2
                        st.session_state.mixte1_valide = True
                else:
                    st.session_state.message_mixte1 = ("error","❌ Relation incorrecte. La bonne relation est : Req = 1/(1/(R1+R2) + 1/R3)")
                st.rerun()
        # Affichage du résultat après le rerun
        if st.session_state.message_mixte1:
            type_msg, texte_msg = st.session_state.message_mixte1
            if type_msg == "success":
                st.success(texte_msg)
            else:
                st.error(texte_msg)
    # ------------------------------------------------
    # MONTAGE MIXTE N°2
    # ------------------------------------------------
    if "tentative_mixte2" not in st.session_state:
        st.session_state.tentative_mixte2 = False
    if "message_mixte2" not in st.session_state:
        st.session_state.message_mixte2 = None
    if montage == "(R1 // R2) + R3":
        st.subheader("📝 Recherche de la relation")
        relation = st.text_input("À partir du tableau, écrivez la relation entre R1, R2, R3 et Req :",key="relation_mixte2",disabled=st.session_state.tentative_mixte2)
        if not st.session_state.tentative_mixte2:
            if st.button("✅ Valider"):
                st.session_state.tentative_mixte2 = True
                texte = relation.replace(" ", "").lower()
                if texte in ["req=(r1*r2)/(r1+r2)+r3","req=1/(1/r1+1/r2)+r3","req=1/(g1+g2)+r3"]:
                    st.session_state.message_mixte2 = ("success","✅ Bonne réponse !")
                    if not st.session_state.mixte2_valide:
                        st.session_state.score_activite += 2
                        st.session_state.mixte2_valide = True
                else:
                    st.session_state.message_mixte2 = ("error","❌ Relation incorrecte. La bonne relation est : Req = 1/(1/R1 + 1/R2) + R3")
                st.rerun()
        # Affichage du résultat après le rerun
        if st.session_state.message_mixte2:
            type_msg, texte_msg = st.session_state.message_mixte2
            if type_msg == "success":
                st.success(texte_msg)
            else:
                st.error(texte_msg)
    st.divider()
    # Détermination de la validation du montage en cours
    validation_montage = False
    if montage == "Série":
        validation_montage = st.session_state.tentative_serie
    elif montage == "Parallèle":
        validation_montage = (st.session_state.tentative_parallele_q1 and st.session_state.tentative_gr and st.session_state.tentative_relation_g)
    elif montage == "(R1 + R2) // R3":
        validation_montage = st.session_state.tentative_mixte1
    elif montage == "(R1 // R2) + R3":
        validation_montage = st.session_state.tentative_mixte2
    # Affichage du bouton uniquement lorsque toutes les questions ont été traitées
    if validation_montage:
        if st.session_state.question == 3:
            st.success("✅ Tous les montages ont été étudiés. Cliquez sur Terminer pour afficher le bilan.")
            if st.button("🏁 Terminer l'activité",use_container_width=True):
                st.session_state.question += 1
                st.rerun()
        else:
            if st.button("➡️ Montage suivant",use_container_width=True):
                st.session_state.afficher_G = False
                st.session_state.question += 1
                st.rerun()
    else:
        st.info("Répondez à toutes les questions de ce montage pour débloquer la suite.")
if __name__ == "__main__":
        afficher()