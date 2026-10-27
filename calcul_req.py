import streamlit as st
import matplotlib.pyplot as plt
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
    st.title("⚡ Associations de résistances")
    # -----------------------------
    # Variables de session
    # ----------------------------- 
    # ===============================
    if "calculer" not in st.session_state:
        st.session_state.calculer = False
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "question" not in st.session_state:
        st.session_state.question = 0
    if "etape" not in st.session_state:
        st.session_state.etape = 1
    if "validation_formule" not in st.session_state:
        st.session_state.validation_formule = False
    if "validation_calcul" not in st.session_state:
        st.session_state.validation_calcul = False
    if "message_qcm" not in st.session_state:
        st.session_state.message_qcm = ""
    if "resultat_estimation" not in st.session_state:
        st.session_state.resultat_estimation = ""
    if "resultat_formule" not in st.session_state:
        st.session_state.resultat_formule = ""
    if "resultat_calcul" not in st.session_state:
        st.session_state.resultat_calcul = ""
    # ============================
    # Saisie des résistances
    # ============================
    st.subheader("Valeurs des résistances")
    col1, col2, col3 = st.columns(3)
    with col1:
        R1 = st.number_input("R1 (Ω)",min_value=1.0,value=100.0)
    with col2:
        R2 = st.number_input("R2 (Ω)",min_value=1.0,value=220.0)
    with col3:
        R3 = st.number_input("R3 (Ω)",min_value=1.0,value=330.0)
    # ============================
    # Les 4 questions
    # ============================
    questions = [{"nom": "Série","bonnes_reponses": ["Req = R1 + R2 + R3"]},
    {"nom": "Parallèle","bonnes_reponses": ["Req = 1/(1/R1 + 1/R2 + 1/R3)",
    "Req = (R1*R2*R3)/(R1*R2 + R1*R3 + R2*R3)"]},{"nom": "(R1 + R2) // R3",
    "bonnes_reponses": ["Req = 1/(1/(R1+R2) + 1/R3)","Req = (R1+R2)*R3/(R1+R2+R3)"]},
    {"nom": "(R1 // R2) + R3","bonnes_reponses": ["Req = (R1*R2)/(R1+R2) + R3","Req = 1/(1/R1 + 1/R2) + R3"]}]
    # ============================
    # Fin du quiz
    # ============================
    if st.session_state.question >= 4:
        pourcentage = (st.session_state.score / 12) * 100
        if pourcentage == 100:
            appreciation = "Excellent !"
        elif pourcentage >= 75:
            appreciation = "Très bien !"
        elif pourcentage >= 50:
            appreciation = "Assez bien."
        else:
            appreciation = "À retravailler."
        st.balloons()
        st.markdown(f"🏆 Quiz terminé !&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Score :{pourcentage:.0f} %&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; {appreciation}",
        unsafe_allow_html=True)
        return
    # ============================
    # Question courante
    # ============================
    montage = questions[st.session_state.question]["nom"]
    bonnes_reponses = questions[st.session_state.question]["bonnes_reponses"]

    # ============================
    # Calcul de Req
    # ============================
    if montage == "Série":
        Req = R1 + R2 + R3
    elif montage == "Parallèle":
        Req = 1/(1/R1 + 1/R2 + 1/R3)
    elif montage == "(R1 + R2) // R3":
        Req = 1/(1/(R1+R2) + 1/R3)
    elif montage == "(R1 // R2) + R3":
        Req = 1/(1/R1+1/R2) + R3
    # ============================
    # Affichage de Req dans le schéma
    # ============================
    Req_affiche = None
    if st.session_state.validation_calcul:
        Req_affiche = Req
    if montage == "Série":
        fig = schema_serie(R1, R2, R3, Req_affiche)
    elif montage == "Parallèle":
        fig = schema_parallele(R1, R2, R3, Req_affiche)
    elif montage == "(R1 + R2) // R3":
        fig = schema_mixte1(R1, R2, R3, Req_affiche)
    elif montage == "(R1 // R2) + R3":
        fig = schema_mixte2(R1, R2, R3, Req_affiche)
    st.pyplot(fig)
    # ====================================
    # Résultats de la question
    # ====================================
    if (st.session_state.resultat_estimation != ""or st.session_state.resultat_formule != ""or st.session_state.resultat_calcul != ""):
        score_question = 0
    if st.session_state.resultat_estimation == "bonne":
        st.success("✅ Estimation : Bonne réponse")
        score_question += 1
    elif st.session_state.resultat_estimation == "mauvaise":
        st.error("❌ Estimation : Mauvaise réponse")

    if st.session_state.resultat_formule == "bonne":
        st.success("✅ Formule : Bonne réponse")
        score_question += 1
    elif st.session_state.resultat_formule == "mauvaise":
        st.error("❌ Formule : Mauvaise réponse")

    if st.session_state.resultat_calcul == "bonne":
        st.success("✅ Calcul : Bonne réponse")
        score_question += 1
    elif st.session_state.resultat_calcul == "mauvaise":
        st.error("❌ Calcul : Mauvaise réponse")
    # ====================================
    # ETAPE 1 : Estimation physique
    # ====================================
    if st.session_state.etape == 1:
        if montage == "Série":
            estimation = st.radio(
            "Avant de calculer, laquelle de ces affirmations est vraie ?",[
            "Req est inférieure à la plus petite résistance",
            "Req est comprise entre la résistance minimale et la résistance maximale",
            "Req est supérieure à la plus grande résistance"])
            bonne_estimation = "Req est supérieure à la plus grande résistance"
        elif montage == "Parallèle":
            estimation = st.radio(
            "Avant de calculer, laquelle de ces affirmations est vraie ?",
            ["Req est inférieure à la plus petite résistance",
             "Req est comprise entre la résistance minimale et la résistance maximale",
             "Req est supérieure à la plus grande résistance"])
            bonne_estimation = "Req est inférieure à la plus petite résistance"
        elif montage == "(R1 + R2) // R3":
            estimation = st.radio(
            "Avant de calculer, laquelle de ces affirmations est vraie ?",
            ["Req est supérieure à R3",
             "Req est inférieure à R3 et inférieure à (R1+R2)",
             "Req est inférieure à R3 et Req est supérieure à (R1+R2)"])
            bonne_estimation = "Req est inférieure à R3 et inférieure à (R1+R2)"
        elif montage == "(R1 // R2) + R3":
            estimation = st.radio(
            "Avant de calculer, laquelle de ces affirmations est vraie ?",
            ["Req est supérieure à R3 et inférieure à (R1+R2)",
             "Req est supérieure à R3",
            "Req est inférieure à R3 et supérieure à (R1+R2)"])
            bonne_estimation = "Req est supérieure à R3"
        if st.button("Valider l'estimation"):
            if estimation == bonne_estimation:
                st.session_state.resultat_estimation = "bonne"
                st.session_state.score += 1
            else:
                st.session_state.resultat_estimation = "mauvaise"
            st.session_state.etape = 2
            st.rerun()
    # ====================================
    # ETAPE 2 : Choix de la formule
    # ====================================
    elif st.session_state.etape == 2:
        propositions = {r"$R_{eq}=R_1+R_2+R_3$":"Req = R1 + R2 + R3",
        r"$R_{eq}=\dfrac{1}{\dfrac{1}{R_1}+\dfrac{1}{R_2}+\dfrac{1}{R_3}}$":"Req = 1/(1/R1 + 1/R2 + 1/R3)",
        r"$R_{eq}=\dfrac{1}{\dfrac{1}{R_1+R_2}+\dfrac{1}{R_3}}$":"Req = 1/(1/(R1+R2) + 1/R3)",
        r"$R_{eq}=\dfrac{1}{\dfrac{1}{R_1}+\dfrac{1}{R_2}}+R_3$":"Req = 1/(1/R1 + 1/R2) + R3",}
        liste_formules = list(propositions.keys())
        reponse = st.radio(
        "Choisir la formule correcte :",
        liste_formules,
        format_func=lambda x: x)
        if st.button("Valider la formule"):
            formule_choisie = propositions[reponse]
            if formule_choisie in bonnes_reponses:
                st.session_state.resultat_formule = "bonne"
                st.session_state.score += 1
            else:
                st.session_state.resultat_formule = "mauvaise"
            st.session_state.etape = 3
            st.rerun()
    # ====================================
    # ETAPE 3 : Calcul de Req
    # ====================================

    if "resultat_calcul" not in st.session_state:
        st.session_state.resultat_calcul = ""

    elif st.session_state.etape == 3 and not st.session_state.validation_calcul:

        with st.form("form_req"):

            reponse_req = st.text_input(
            "Calculer Req (Ω) au centième près",
            placeholder="Entrer la valeur de Req"
        )

            valider = st.form_submit_button("Valider le calcul")

        if valider:

            try:
                reponse_req = float(reponse_req.replace(",", "."))

                if abs(reponse_req - Req) < 0.1:
                    st.session_state.resultat_calcul = "bonne"
                    st.session_state.score += 1
                else:
                    st.session_state.resultat_calcul = "mauvaise"

                st.session_state.validation_calcul = True
                st.rerun()

            except ValueError:
                st.error("Veuillez saisir une valeur numérique.")
    # ====================================
    # Après validation du calcul
    # ====================================
    if st.session_state.validation_calcul:
        score_question = 0
        if st.session_state.resultat_estimation == "bonne":
            score_question += 1
        if st.session_state.resultat_formule == "bonne":
            score_question += 1
        if st.session_state.resultat_calcul == "bonne":
            score_question += 1
        st.info(f"🎯 Score de cette question : {score_question}/3")
    # Boutons de navigation
        if st.session_state.question == 3:
            if st.button("✅ Terminer"):
                st.session_state.question += 1
                st.rerun()
        else:
            if st.button("➡️ Question suivante"):
                st.session_state.question += 1
                st.session_state.etape = 1
                st.session_state.validation_formule = False
                st.session_state.validation_calcul = False
                st.session_state.message_qcm = ""
                st.session_state.resultat_calcul = ""
                st.session_state.resultat_estimation = ""
                st.session_state.resultat_formule = ""
                st.session_state.resultat_calcul = ""
                st.rerun()
if __name__ == "__main__":
    afficher()
