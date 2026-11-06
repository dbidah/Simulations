import streamlit as st
import matplotlib.pyplot as plt
import random
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

def afficher():
    nom_eleve = st.text_input("Nom et prénom de l'élève",key="nom_eleve")
    st.set_page_config(page_title="Le courant électrique",page_icon="⚡",layout="wide")
    st.title("⚡ Le courant électrique")
    if "page" not in st.session_state:
        st.session_state.page = "cours"
    if "score_qcm" not in st.session_state:
        st.session_state.score_qcm = 0
    if st.button("📘 Cours"):
        st.session_state.page = "cours"
    if st.session_state.page == "cours":
        st.subheader("1. Nature du courant électrique")
        st.markdown(""" Dans un métal : Le courant électrique correspond à un déplacement ordonné des électrons libres. Les électrons circulent dans le sens inverse.""")
        st.markdown("""<div style="display:flex; justify-content:center;">
        <div style="position:relative;width:700px;height:120px;border:3px solid black;border-radius:10px;overflow:hidden;background:#f0f0f0;">
    <style>@keyframes electron {from { left:650px; }to { left:-40px; }}
    .electron {position:absolute;width:24px;height:24px;border-radius:50%;background:blue;color:white;font-size:12px;font-weight:bold;text-align:center;line-height:24px;top:60px;animation: electron 4s linear infinite;}
    </style><!-- Sens du courant conventionnel --><div style="position:absolute;top:15px;left:250px;font-size:24px;font-weight:bold;color:green;">
    Sens du courant ➜</div><div class="electron" style="animation-delay:0s;">e⁻</div><div class="electron" style="animation-delay:1s;">e⁻</div><div class="electron" style="animation-delay:2s;">e⁻</div><div class="electron" style="animation-delay:3s;">e⁻</div></div>""", unsafe_allow_html=True)
        st.markdown("""✅ Porteurs de charge : les électrons.""")
        st.markdown(""" Dans une solution ionique : Le courant électrique est dû au déplacement simultané des ions positifs (cations) et des ions négatifs (anions)""")
        st.markdown("""<div style="display:flex; justify-content:center;">
    <div style="position:relative;width:700px;height:140px;border:3px solid black;border-radius:10px;overflow:hidden;background:#e8f8ff;">
    <style>@keyframes cation {from { left:40px; }to { left:620px; }}@keyframes anion {from { left:620px; }to { left:40px; }}.cation{position:absolute;width:30px;height:30px;border-radius:50%;background:red;color:white;text-align:center;line-height:30px;font-weight:bold;animation:cation 5s linear infinite;}
    .anion{position:absolute;width:30px;height:30px;border-radius:50%;background:blue;color:white;text-align:center;line-height:30px;font-weight:bold;animation:anion 5s linear infinite;}
    </style><!-- Ions Na+ en haut --><div class="cation" style="top:15px;">Na⁺</div><div class="cation" style="top:15px; animation-delay:2.5s;">Na⁺</div>
    <!-- Sens du courant conventionnel --><div style="position:absolute;top:55px;left:220px;font-size:24px;font-weight:bold;color:green;">Sens du courant ➜</div>
    <!-- Ions Cl- en bas --><div class="anion" style="top:95px;">Cl⁻</div><div class="anion" style="top:95px; animation-delay:2.5s;">Cl⁻</div>
    </div>""", unsafe_allow_html=True)
        st.markdown("""✅ Porteurs de charge : les ions.""")
        st.subheader("2. Sens conventionnel du courant")
        st.markdown("""Par convention, dans un circuit, le courant circule du pôle positif du générateur vers le pôle négatif.""")
        st.subheader("3. Quantité d'électricité")
        st.markdown("""Q = n × e    **avec**     Q : quantité d'électricité (C)    n : nombre d'électrons     e : 1,6x10-19 (C)""")
        st.subheader("4. Intensité du courant")
        st.markdown(r"$I=\frac{Q}{t}$    **avec**     Q : quantité d'électricité (C)    I : intensité (A)     t : durée (s)""")
        st.subheader("5. Unicité du courant")
        st.markdown("""
    Dans un circuit, les ampèremètre doivent toujours être branchés en série""")
        st.markdown("""
    <div style="
    position:relative;
    width:800px;
    height:220px;
    border:3px solid black;
    border-radius:10px;
    background:white;
    margin:auto;
    ">
    <!-- Fil supérieur -->
    <div style="
    position:absolute;
    top:100px;
    left:50px;
    width:700px;
    height:4px;
    background:black;
    "></div>
    <!-- A1 -->
    <div style="
    position:absolute;
    top:70px;
    left:80px;
    width:70px;
    height:70px;
    border:3px solid black;
    border-radius:60%;
    background:#d0f0ff;
    text-align:center;
    line-height:25px;
    font-weight:bold;
    ">
    A1<br>0,35 A
    </div>
    <!-- L1 -->
    <div style="
    position:absolute;
    top:75px;
    left:240px;
    width:50px;
    height:50px;
    border:3px solid black;
    border-radius:50%;
    background:yellow;
    text-align:center;
    line-height:50px;
    font-weight:bold;
    ">
    L1
    </div>
    <!-- A2 -->
    <div style="
    position:absolute;
    top:70px;
    left:400px;
    width:70px;
    height:70px;
    border:3px solid black;
    border-radius:50%;
    background:#d0f0ff;
    text-align:center;
    line-height:25px;
    font-weight:bold;
    ">
    A2<br>0,35 A
    </div>
    <!-- L2 -->
    <div style="
    position:absolute;
    top:75px;
    left:560px;
    width:50px;
    height:50px;
    border:3px solid black;
    border-radius:50%;
    background:yellow;
    text-align:center;
    line-height:50px;
    font-weight:bold;
    ">
    L2
    </div>
    <!-- A3 -->
    <div style="
    position:absolute;
    top:70px;
    left:650px;
    width:70px;
    height:70px;
    border:3px solid black;
    border-radius:50%;
    background:#d0f0ff;
    text-align:center;
    line-height:25px;
    font-weight:bold;
    ">
    A3<br>0,35 A
    </div>
    <!-- Générateur -->
    <div style="
    position:absolute;
    top:170px;
    left:340px;
    width:120px;
    height:40px;
    border:3px solid black;
    background:#eeeeee;
    text-align:center;
    line-height:40px;
    font-weight:bold;
    ">
    Pile
    </div>
    <!-- Retour vers la pile -->
    <div style="
    position:absolute;
    left:50px;
    top:100px;
    width:4px;
    height:90px;
    background:black;
    "></div>
    <div style="
    position:absolute;
    left:750px;
    top:100px;
    width:4px;
    height:90px;
    background:black;
    "></div>
    <div style="
    position:absolute;
    left:50px;
    top:190px;
    width:704px;
    height:4px;
    background:black;
    "></div>
    <!-- Générateur -->
    <div style="
    position:absolute;
    top:170px;
    left:340px;
    width:120px;
    height:40px;
    border:3px solid black;
    background:#eeeeee;
    text-align:center;
    line-height:40px;
    font-weight:bold;
    ">
    Pile
    </div>
    </div>
    """, unsafe_allow_html=True)
        st.markdown("""✅Dans un circuit en série, l'intensité électrique est la même en tous points.""")
        st.subheader("6. Loi des nœuds")
        st.markdown("""Un noeud est un point où arrivent au moins trois conducteurs.""")
        st.markdown("""
    <div style="
    position:relative;
    width:700px;
    height:300px;
    border:3px solid black;
    border-radius:10px;
    background:white;
    margin:auto;
    ">
    <!-- Branche horizontale -->
    <div style="
    position:absolute;
    left:50px;
    top:145px;
    width:600px;
    height:4px;
    background:black;
    "></div>
    <!-- Branche verticale -->
    <div style="
    position:absolute;
    left:348px;
    top:50px;
    width:4px;
    height:200px;
    background:black;
    "></div>
    <!-- Nœud -->
    <div style="
    position:absolute;
    left:340px;
    top:137px;
    width:20px;
    height:20px;
    border-radius:50%;
    background:red;
    "></div>
    <!-- I1 entrant -->
    <div style="
    position:absolute;
    left:120px;
    top:105px;
    font-size:28px;
    font-weight:bold;
    color:#4B22FF;
    ">
    I₁ ➜
    </div>
    <!-- I2 entrant -->
    <div style="
    position:absolute;
    left:300px;
    top:60px;
    font-size:28px;
    font-weight:bold;
    color:green;
    ">
    ↓ I₂
    </div>
    <!-- I3 sortant -->
    <div style="
    position:absolute;
    left:470px;
    top:105px;
    font-size:28px;
    font-weight:bold;
    color:purple;
    ">
    I₃ ➜
    </div>
    <!-- I4 sortant -->
    <div style="
    position:absolute;
    left:300px;
    top:190px;
    font-size:28px;
    font-weight:bold;
    color:orange;
    ">
    I₄ ↓
    </div>
    <!-- Relation -->
    <div style="
    position:absolute;
    left:285px;
    top:255px;
    font-size:24px;
    font-weight:bold;
    color:brown;
    ">
    I₁ + I₂ = I₃ + I₄
    </div>
    </div>
    """, unsafe_allow_html=True)
        st.markdown("""
    ✅La somme des intensités des courants arrivant à un nœud est égale à la somme des intensités des courants partant de ce nœud.
    """)
    st.markdown("---")
    if st.session_state.page == "cours":

        st.success("✅ Si vous avez compris, passez au QCM")

        if st.button("➡️ QCM", key="btn_qcm"):
            st.session_state.page = "qcm"
            st.rerun()
    elif st.session_state.page == "qcm":
        st.header("✅ Vérification des connaissances")
        q1 = st.radio(
            "Dans un métal, quels sont les porteurs de charge ?",
            ["Les cations", "Les électrons", "Les anions"],key="q1")
        q2 = st.radio(
            "Dans une solution ionique, le courant est dû au déplacement :",
            ["Des électrons","Des ions positifs et négatifs","Des molécules"],key="q2")
        q3 = st.radio(
            "Le courant conventionnel circule :",
            ["Du + vers le - du générateur","Du - vers le + du générateur"],key="q3")
        q4 = st.radio(
            "Quelle relation est correcte ?",
            ["Q = I × t","Q = I / t","I = Q × t"],key="q4")
        q5 = st.radio(
            "Dans un circuit sans dérivation :",
            ["La somme des intensités du courant est nulle",
            "La somme des intensités des courants entrant est égale à la somme des intensités des courants sortant",
            "L'intensité du courant est la même en tout point du circuit"],key="q5")
        q6 = st.radio(
            "Dans un nœuds :",
            ["La somme des intensités du courant est nulle'",
            "La somme des intensités des courants entrant est égale à la somme des intensités des courants sortant",
            "L'intensité du courant est la même en tout point du circuit"],key="q6")
        if st.button("Valider le QCM"):
            score = 0
            if q1 == "Les électrons":
                score += 1
            if q2 == "Des ions positifs et négatifs":
                score += 1
            if q3 == "Du + vers le - du générateur":
                score += 1
            if q4 == "Q = I × t":
                score += 1
            if q5 == "L'intensité du courant est la même en tout point du circuit":
                score += 1
            if q6 == "La somme des intensités des courants entrant est égale à la somme des intensités des courants sortant":
                score += 1
            st.session_state.score_qcm = score
            if score == 6:
                st.success("🎉 Félicitations ! Tu as obtenu 6/6 au QCM.")
            else:
                st.session_state.score_qcm = 0
                st.error(
                    "❌ Tu n'as pas obtenu 100 %. 📘 Revois le cours puis réessaie le QCM."
                )
        # Accès permanent aux simulations uniquement si 6/6
        if st.session_state.get("score_qcm", 0) == 6:

            # st.markdown("---")
            # st.success("✅ Simulation débloquée")

            if st.button("🔬 Ouvrir la simulation"):
                st.session_state.page = "simulation"
                st.rerun()

    # ==================================
    # PAGE SIMULATION
    # ==================================
    elif st.session_state.page == "simulation":
        # Sécurité d'accès
        if st.session_state.get("score_qcm", 0) != 6:
            st.error(
                "⛔ Accès refusé. Tu dois obtenir 6/6 au QCM avant d'accéder à la simulation.")
            if st.button("📘 Retour au cours"):
                st.session_state.page = "cours"
                st.rerun()
            st.stop()
        st.header("🔬 Simulation : Lois des intensités")
        st.markdown("""
        ### 📋 Consigne
        - Observe le circuit.
        - Choisis le sens des courants.
        - Complète les relations entre les intensités.
        - Vérifie tes réponses.
        - Calcule les intensités manquantes.
        """)
        # ==================================
        # Génération exercice
        # ==================================
        if "I2_donnee" not in st.session_state:
            st.session_state.I2_donnee = round(
                random.choice(range(10, 51, 5)) / 100, 2)
        if "I4_donnee" not in st.session_state:
            st.session_state.I4_donnee = round(
                random.choice(range(10, 51, 5)) / 100, 2)
        # ==================================
        # Initialisation
        # ==================================
        if "score_sens" not in st.session_state:
            st.session_state.score_sens = 0

        if "erreurs_sens" not in st.session_state:
            st.session_state.erreurs_sens = []

        if "etape1_validee" not in st.session_state:
            st.session_state.etape1_validee = False

        if "etape1_validee" not in st.session_state:
            st.session_state.etape1_validee = False

        if "etape2_validee" not in st.session_state:
            st.session_state.etape2_validee = False

        if "etape3_validee" not in st.session_state:
            st.session_state.etape3_validee = False

        if "exercice_termine" not in st.session_state:
            st.session_state.exercice_termine = False

        if "simulation_terminee" not in st.session_state:
            st.session_state.simulation_terminee = False
        # ==================================
        # Initialisation sens courants
        # ==================================
        if "sens" not in st.session_state:

            st.session_state.sens = {
                "I1": random.choice(["droite", "gauche"]),
                "I2": random.choice(["haut", "bas"]),
                "I3": random.choice(["haut", "bas"]),
                "I4": random.choice(["droite", "gauche"]),
                "I5": random.choice(["haut", "bas"]),
                "I6": random.choice(["haut", "bas"]),
                "I7": random.choice(["droite", "gauche"])
            }
        # ==================================
        # Boutons choix sens
        # ==================================
        st.subheader("🔄 Étape 1 : Choisir le sens des courants")
        courants = ["I1", "I2", "I3", "I4", "I5", "I6", "I7"]
        cols = st.columns(7)
        for i, courant in enumerate(courants):
            with cols[i]:
                if st.button(
                    f"↺ {courant}",
                    disabled=st.session_state.etape1_validee
                ):
                    sens = st.session_state.sens[courant]
                    if sens == "droite":
                        st.session_state.sens[courant] = "gauche"
                    elif sens == "gauche":
                        st.session_state.sens[courant] = "droite"
                    elif sens == "haut":
                        st.session_state.sens[courant] = "bas"
                    else:
                        st.session_state.sens[courant] = "haut"
                    st.rerun()
        # ==================================
        # Dessin lampe
        # ==================================
        def dessiner_lampe(ax, x, y, nom):
            lampe = plt.Circle((x, y),0.4,facecolor="yellow",edgecolor="black",linewidth=2)
            ax.add_patch(lampe)
            ax.text(x,y,nom,ha="center",va="center",fontsize=11,fontweight="bold")
        # ==================================
        # Dessin pile
        # ==================================
        def dessiner_pile(ax, x, y):
            rect = plt.Rectangle((x - 0.8, y - 0.5),1.6, 1.0,fill=False,edgecolor="black",linewidth=2)
            ax.add_patch(rect)
            ax.text(x, y, "Pile",ha="center", va="center",fontsize=10, fontweight="bold")
            ax.text(x - 0.55, y, "+",ha="center", va="center",fontsize=14, fontweight="bold", color="red")
            ax.text(x + 0.55, y, "−",ha="center", va="center",fontsize=14, fontweight="bold", color="blue")
        # ==================================
        # Etiquettes
        # ==================================
        def etiquettes_intensites(ax):
            positions = {"I₁": (2.75, 4.5),"I₂": (-0.5, 2),"I₃": (8.5, 2),"I₄": (2.75, 1.5),"I₅": (-0.5, -0.5),"I₆": (8.5, -0.5),"I₇": (2.75, -1.5)}
            for nom, (x, y) in positions.items():
                ax.text(x,y,nom,fontsize=14,color="red",fontweight="bold",ha="center",va="center")
        # ==================================
        # Schéma du circuit
        # ==================================
        def schema_circuit():
            fig, ax = plt.subplots(figsize=(10, 4))
            # Haut horizontal
            ax.plot([0, 4.1], [4, 4], "k", lw=2)
            ax.plot([4.9, 8], [4, 4], "k", lw=2)
            # Haut vertical
            ax.plot([0, 0], [1, 4], "k", lw=2)
            ax.plot([8, 8], [1, 4], "k", lw=2)
            # Milieu horizontal
            ax.plot([0, 4.1], [1, 1], "k", lw=2)
            ax.plot([4.9, 8], [1, 1], "k", lw=2)
            # Bas horizontal
            ax.plot([0, 1.1], [-1, -1], "k", lw=2)
            ax.plot([1.9, 3.7], [-1, -1], "k", lw=2)
            ax.plot([5.3, 8], [-1, -1], "k", lw=2)
            # Bas vertical
            ax.plot([0, 0], [-1, 1], "k", lw=2)
            ax.plot([8, 8], [-1, 1], "k", lw=2)
            # Lampes
            dessiner_lampe(ax, 4.5, 4, "L3")
            dessiner_lampe(ax, 4.5, 1, "L2")
            dessiner_lampe(ax, 1.5, -1, "L1")
            # pile
            dessiner_pile(ax, 4.5, -1)
            # Intensités
            etiquettes_intensites(ax)
            # I1
            if st.session_state.sens["I1"] == "droite":
                ax.arrow(2, 4, 0.5, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            else:
                ax.arrow(3.5, 4, -0.5, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            # I2
            if st.session_state.sens["I2"] == "haut":
                ax.arrow(0, 1.4, 0, 0.5,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            else:
                ax.arrow(0, 2.9, 0, -0.5,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            # I3
            if st.session_state.sens["I3"] == "haut":
                ax.arrow(8, 1.4, 0, 0.5,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            else:
                ax.arrow(8, 2.9, 0, -0.5,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            # I4
            if st.session_state.sens["I4"] == "droite":
                ax.arrow(2, 1, 0.5, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            else:
                ax.arrow(3.5, 1, -0.5, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            # I5
            if st.session_state.sens["I5"] == "haut":
                ax.arrow(0, -0.9, 0, 0.5,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            else:
                ax.arrow(0, 0.6, 0, -0.5,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            # I6
            if st.session_state.sens["I6"] == "haut":
                ax.arrow(8, -0.9, 0, 0.5,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            else:
                ax.arrow(8, 0.6, 0, -0.5,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            # I7
            if st.session_state.sens["I7"] == "droite":
                ax.arrow(2, -1, 0.5, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            else:
                ax.arrow(3.5, -1, -0.5, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            ax.set_xlim(-0.3, 8.3)
            ax.set_ylim(-1.6, 4.6)

            ax.axis("off")

            plt.tight_layout(pad=0)

            return fig

        # ==================================
        # Affichage schéma
        # ==================================
        fig = schema_circuit()
        st.pyplot(fig, use_container_width=True)
        # ==================================
        # GESTION DES ETAPES
        # ==================================

        if "etape" not in st.session_state:
            st.session_state.etape = 1
        if "score_sens" not in st.session_state:
            st.session_state.score_sens = 0
        if "score_relations" not in st.session_state:
            st.session_state.score_relations = 0
        if "score_calculs" not in st.session_state:
            st.session_state.score_calculs = 0
        st.markdown("---")

        # ==================================
        # ETAPE 1
        # ==================================

        if "etape1_validee" not in st.session_state:
            st.session_state.etape1_validee = False

        if "score_sens" not in st.session_state:
            st.session_state.score_sens = 0

        if "erreurs_sens" not in st.session_state:
            st.session_state.erreurs_sens = []

        if st.session_state.etape == 1:

            if not st.session_state.etape1_validee:

                if st.button(
                    "✅ Valider les sens",
                    key="valider_sens"
                ):

                    score_sens = 0

                    BON_SENS = {
                        "I1": "droite",
                        "I2": "haut",
                        "I3": "bas",
                        "I4": "droite",
                        "I5": "haut",
                        "I6": "bas",
                        "I7": "gauche",
                    }

                    erreurs = []

                    for courant, sens_correct in BON_SENS.items():

                        if st.session_state.sens[courant] == sens_correct:
                            score_sens += 1
                        else:
                            erreurs.append(courant)

                    st.session_state.score_sens = score_sens
                    st.session_state.erreurs_sens = erreurs
                    st.session_state.etape1_validee = True

                    st.rerun()

            # ----------------------------
            # RESULTAT ETAPE 1
            # ----------------------------

            if st.session_state.etape1_validee:

                st.info(
                    f"🎯 Score sens : "
                    f"{st.session_state.score_sens}/7"
                )

                if st.session_state.score_sens == 7:

                    st.success(
                        "✅ Bravo ! Tous les sens des courants sont corrects."
                    )

                else:

                    st.error(
                        f"❌ {7 - st.session_state.score_sens} erreur(s)."
                    )

                    with st.expander("✅ Voir la correction"):

                        st.write("I₁ : droite")
                        st.write("I₂ : haut")
                        st.write("I₃ : bas")
                        st.write("I₄ : droite")
                        st.write("I₅ : haut")
                        st.write("I₆ : bas")
                        st.write("I₇ : gauche")

                st.markdown("---")

                if st.button(
                    "➡️ Passer à l'étape 2",
                    key="passage_etape2"
                ):
                    st.session_state.etape = 2
                    st.rerun()

        # ==================================
        # ETAPE 2
        # ==================================

        if "etape2_validee" not in st.session_state:
            st.session_state.etape2_validee = False

        if "score_relations" not in st.session_state:
            st.session_state.score_relations = 0

        if st.session_state.etape == 2:

            st.subheader("✏️ Étape 2 : Relations entre les intensités")
            st.write("Compléter les relations suivantes :")

            relation1 = st.text_input(
                "Relation entre I₁, I₂ et I₃",
                key="relation1",
                disabled=st.session_state.etape2_validee
            )

            relation2 = st.text_input(
                "Relation entre I₅, I₆ et I₇",
                key="relation2",
                disabled=st.session_state.etape2_validee
            )

            relation3 = st.text_input(
                "Relation entre I₃, I₄ et I₆",
                key="relation3",
                disabled=st.session_state.etape2_validee
            )

            relation4 = st.text_input(
                "Relation entre I₂, I₄ et I₅",
                key="relation4",
                disabled=st.session_state.etape2_validee
            )

            # ----------------------------------
            # APERÇU DES RÉPONSES
            # ----------------------------------

            with st.expander("🔍 Vérifier mes saisies avant validation"):

                st.write(
                    "Relation 1 :",
                    relation1 if relation1 else "Aucune saisie"
                )

                st.write(
                    "Relation 2 :",
                    relation2 if relation2 else "Aucune saisie"
                )

                st.write(
                    "Relation 3 :",
                    relation3 if relation3 else "Aucune saisie"
                )

                st.write(
                    "Relation 4 :",
                    relation4 if relation4 else "Aucune saisie"
                )

            # ----------------------------------
            # VALIDATION
            # ----------------------------------

            if not st.session_state.etape2_validee:

                if st.button(
                    "✅ Valider les relations",
                    key="valider_relations"
                ):

                    score = 0

                    r1 = relation1.upper().replace(" ", "")
                    r2 = relation2.upper().replace(" ", "")
                    r3 = relation3.upper().replace(" ", "")
                    r4 = relation4.upper().replace(" ", "")

                    if r1 in [
                        "I1=I2=I3",
                        "I1=I3=I2",
                        "I2=I1=I3",
                        "I2=I3=I1",
                        "I3=I1=I2",
                        "I3=I2=I1",
                    ]:
                        score += 1

                    if r2 in [
                        "I5=I6=I7",
                        "I5=I7=I6",
                        "I6=I5=I7",
                        "I6=I7=I5",
                        "I7=I5=I6",
                        "I7=I6=I5",
                    ]:
                        score += 1

                    if r3 in [
                        "I3+I4=I6",
                        "I4+I3=I6",
                        "I6=I3+I4",
                        "I6=I4+I3",
                    ]:
                        score += 1

                    if r4 in [
                        "I2+I4=I5",
                        "I4+I2=I5",
                        "I5=I2+I4",
                        "I5=I4+I2",
                    ]:
                        score += 1

                    st.session_state.score_relations = score
                    st.session_state.etape2_validee = True

                    st.rerun()

            # ----------------------------------
            # RESULTATS
            # ----------------------------------

            if st.session_state.etape2_validee:

                score = st.session_state.score_relations

                st.info(
                    f"🎯 Score relations : {score}/4"
                )

                if score == 4:

                    st.success(
                        "✅ Bravo ! Toutes les relations sont correctes."
                    )

                else:

                    st.error(
                        f"❌ {4 - score} relation(s) incorrecte(s)."
                    )

                    st.markdown("### ✅ Correction")

                    st.markdown("""
        - **I1 = I2 = I3**
        - **I5 = I6 = I7**
        - **I3 + I4 = I6**
        - **I2 + I4 = I5**
        """)

                st.markdown("---")

                if st.button(
                    "➡️ Passer à l'étape 3",
                    key="vers_etape3"
                ):
                    st.session_state.etape = 3
                    st.rerun()
        # ==================================
        # ETAPE 3
        # ==================================
        if "etape3_validee" not in st.session_state:
            st.session_state.etape3_validee = False
        if "score_calculs" not in st.session_state:
            st.session_state.score_calculs = 0
        if "erreurs_calculs" not in st.session_state:
            st.session_state.erreurs_calculs = []
        if st.session_state.etape == 3:
            st.markdown("---")
            st.subheader("🧮 Étape 3 : Calcul des intensités")
            I2 = st.session_state.I2_donnee
            I4 = st.session_state.I4_donnee
            st.write(f"**I₂ = {I2:.2f} A**")
            st.write(f"**I₄ = {I4:.2f} A**")
            st.write("Calculer les intensités manquantes :")
            r_I1 = st.number_input("I₁ (A)",min_value=0.0,step=0.01,format="%.2f",key="calc_I1",disabled=st.session_state.etape3_validee)
            r_I3 = st.number_input("I₃ (A)",min_value=0.0,step=0.01,format="%.2f",key="calc_I3",disabled=st.session_state.etape3_validee)
            r_I5 = st.number_input("I₅ (A)",min_value=0.0,step=0.01,format="%.2f",key="calc_I5",disabled=st.session_state.etape3_validee)
            r_I6 = st.number_input("I₆ (A)",min_value=0.0,step=0.01,format="%.2f",key="calc_I6",disabled=st.session_state.etape3_validee)
            r_I7 = st.number_input("I₇ (A)",min_value=0.0,step=0.01,format="%.2f",key="calc_I7",disabled=st.session_state.etape3_validee)
            # ----------------------------
            # Valeurs attendues
            # ----------------------------
            I1 = I2
            I3 = I2
            I5 = round(I2 + I4, 2)
            I6 = I5
            I7 = I5
            # ---------------------------
            # Validation
            # ---------------------------
            if not st.session_state.etape3_validee:
                if st.button("✅ Vérifier les calculs",key="verifier_calculs"):
                    score_calculs = 0
                    erreurs = []
                    if abs(r_I1 - I1) <= 0.01:
                        score_calculs += 1
                    else:
                        erreurs.append("I₁")
                    if abs(r_I3 - I3) <= 0.01:
                        score_calculs += 1
                    else:
                        erreurs.append("I₃")
                    if abs(r_I5 - I5) <= 0.01:
                        score_calculs += 1
                    else:
                        erreurs.append("I₅")
                    if abs(r_I6 - I6) <= 0.01:
                        score_calculs += 1
                    else:
                        erreurs.append("I₆")
                    if abs(r_I7 - I7) <= 0.01:
                        score_calculs += 1
                    else:
                        erreurs.append("I₇")
                    st.session_state.score_calculs = score_calculs
                    st.session_state.erreurs_calculs = erreurs
                    st.session_state.etape3_validee = True
                    st.session_state.simulation_terminee = True
                    st.rerun()
                # ----------------------------
                # RESULTATS ETAPE 3
                # ----------------------------
                if st.session_state.etape3_validee:
                    st.info(f"🎯 Score calculs : "f"{st.session_state.score_calculs}/5")
                    if len(st.session_state.erreurs_calculs) == 0:
                        st.success("✅ Bravo ! Tous les calculs sont corrects.")
                    else:
                        st.error("❌ Erreurs pour : "+ ", ".join(st.session_state.erreurs_calculs))
                        with st.expander("✅ Voir la correction"):
                            st.write(f"**I₁ = {I1:.2f} A**")
                            st.write(f"**I₂ = {I2:.2f} A**")
                            st.write(f"**I₃ = {I3:.2f} A**")
                            st.write(f"**I₄ = {I4:.2f} A**")
                            st.write(f"**I₅ = {I5:.2f} A**")
                            st.write(f"**I₆ = {I6:.2f} A**")
                            st.write(f"**I₇ = {I7:.2f} A**")
        # ==================================
        # RESULTATS FINAUX
        # ==================================
        if st.session_state.simulation_terminee:
            score_sens = st.session_state.get("score_sens", 0)
            score_relations = st.session_state.get("score_relations", 0)
            score_calculs = st.session_state.get("score_calculs", 0)
            total = (score_sens+ score_relations+ score_calculs)
            pourcentage = round(total * 100 / 16,1)
            st.markdown("---")
            st.subheader("🏆 Résultat final")
            st.metric("Score obtenu",f"{pourcentage}%")
            st.write(f"Score sens : {score_sens}/7")
            st.write(
                f"Score relations : {score_relations}/4")
            st.write(f"Score calculs : {score_calculs}/5")
            st.warning("🔒 Exercice terminé. ""Les réponses ne peuvent plus être modifiées. ""Clique sur 'Nouvel exercice' pour recommencer.")
            if pourcentage >= 90:
                st.success("🌟 Excellent travail !")
                st.balloons()
            elif pourcentage >= 75:
                st.success("✅ Très bon travail.")
            elif pourcentage >= 50:
                st.warning("⚠️ Résultat satisfaisant.")
            else:
                st.error("❌ Les lois des intensités ne sont pas encore acquises.")
            if st.button("🔄 Nouvel exercice",key="nouvel_exercice"):
                a_supprimer = [
                    # étapes
                    "etape",
                    "etape1_validee",
                    "etape2_validee",
                    "etape3_validee",
                    # simulation
                    "simulation_terminee",
                    "exercice_termine",
                    # courants
                    "sens",
                    # scores
                    "score_sens",
                    "score_relations",
                    "score_calculs",
                    # erreurs
                    "erreurs_sens",
                    "erreurs_calculs",
                    # données exercice
                    "I2_donnee",
                    "I4_donnee",
                    # relations
                    "relation1",
                    "relation2",
                    "relation3",
                    "relation4",
                    # calculs
                    "calc_I1",
                    "calc_I3",
                    "calc_I5",
                    "calc_I6",
                    "calc_I7"]
                for cle in a_supprimer:
                    if cle in st.session_state:
                        del st.session_state[cle]
                st.session_state.page = "simulation"
                st.rerun()
if __name__ == "__main__":
    afficher()