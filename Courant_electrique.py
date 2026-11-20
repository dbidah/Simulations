import streamlit as st
import matplotlib.pyplot as plt
import random
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from matplotlib.patches import Circle, Rectangle
from google.oauth2.service_account import Credentials
from datetime import datetime
st.set_page_config(page_title="Le courant électrique",page_icon="⚡",layout="wide")
st.markdown("""<style>[data-testid="stSidebar"] {display: none;}[data-testid="collapsedControl"] {display: none;}</style>""", unsafe_allow_html=True)
st.markdown("""<style>.block-container {padding-top: 0.8rem;padding-bottom: 1rem;}</style>""", unsafe_allow_html=True)
st.markdown("""
<style>
.block-container {padding-top: 0rem !important;}
</style>
""", unsafe_allow_html=True)
def connecter_google_sheet():
    scope = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"],scopes=scope)
    client = gspread.authorize(creds)
    feuille = client.open("Résultats courant électrique").sheet1
    return feuille
def enregistrer_resultat(nom,score_sens,score_relations,score_calculs,score_total):
    feuille = connecter_google_sheet()
    feuille.append_row([datetime.now().strftime("%d/%m/%Y %H:%M:%S"),nom,score_sens,score_relations,score_calculs,score_total])
def afficher():
    if "id_eleve" not in st.session_state:
        st.session_state.id_eleve = 0
    if "qcm_rate" not in st.session_state:
        st.session_state.qcm_rate = False
    if "page" not in st.session_state:
        st.session_state.page = "cours"
        st.title("⚡ Le courant électrique")
    if "score_qcm" not in st.session_state:
        st.session_state.score_qcm = 0
    if st.session_state.page == "cours":
        # ------------------------------------------------------------------
        # 1. Nature du courant électrique
        # ------------------------------------------------------------------
        st.info("📚 Cours interactif et activités de découverte des lois des intensités.")
        st.subheader("1. Nature du courant électrique")
        st.write("Dans un métal, le courant électrique correspond à un déplacement ordonné des électrons libres. Les électrons circulent dans le sens inverse du courant.")
        st.markdown("""
<div style="display:flex;justify-content:center;">
<div style="
    position:relative;width:1000px;height:160px;border:3px solid black;border-radius:10px;overflow:hidden;background:#f0f0f0;">
<style>
@keyframes electron {from { left:1020px; }to   { left:-300px; }}
.electron{position:absolute;width:32px;height:32px;border-radius:50%;background:#5618ff;color:white;font-weight:bold;font-size:16px;text-align:center;line-height:32px;animation:electron 6s linear infinite;}
.sens{position:absolute;top:58px;left:50%;transform:translateX(-50%);color:green;font-size:28px;font-weight:bold;}
</style>
<div class="sens">Sens du courant ➜</div>
<!-- Ligne du haut -->
<div class="electron" style="top:15px;animation-delay:0s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:0.5s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:1s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:1.5s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:2s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:2.5s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:3s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:3.5s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:4s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:4.5s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:5s;">e⁻</div>
<div class="electron" style="top:15px;animation-delay:5.5s;">e⁻</div>
<!-- Ligne du bas -->
<div class="electron" style="top:110px;animation-delay:0.25s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:0.75s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:1.25s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:1.75s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:2.25s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:2.75s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:3.25s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:3.75s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:4.25s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:4.75s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:5.25s;">e⁻</div>
<div class="electron" style="top:110px;animation-delay:5.75s;">e⁻</div>
</div>
</div>
""", unsafe_allow_html=True)
        st.markdown('<div style="color:green;font-weight:bold;">✅ Porteurs de charge : les électrons.</div>',unsafe_allow_html=True)
        st.write("Dans une solution ionique, le courant électrique est dû au déplacement simultané des ions positifs (cations) et des ions négatifs (anions).")
        st.markdown("""
<div style="display:flex;justify-content:center;">
<div style="position:relative;width:1000px;height:160px;border:3px solid black;border-radius:10px;overflow:hidden;background:#e8f8ff;">
<style>
@keyframes cation {from { left:-300px; }to   { left:1020px; }}
@keyframes anion {from { left:1020px; }to   { left:-300px; }}
.cation{position:absolute;width:32px;height:32px;border-radius:50%;background:#ff4d35;color:white;font-weight:bold;font-size:16px;text-align:center;line-height:32px;animation:cation 6s linear infinite;}
.anion{position:absolute;width:32px;height:32px;border-radius:50%;background:#5618ff;color:white;font-weight:bold;font-size:16px;text-align:center;line-height:32px;animation:anion 6s linear infinite;}
.sens{position:absolute;top:58px;left:50%;transform:translateX(-50%);color:green;font-size:28px;font-weight:bold;}
</style>
<div class="sens">Sens du courant ➜</div>
<!-- Ligne du haut : Na+ -->
<div class="cation" style="top:15px;animation-delay:0s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:0.5s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:1s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:1.5s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:2s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:2.5s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:3s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:3.5s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:4s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:4.5s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:5s;">Na⁺</div>
<div class="cation" style="top:15px;animation-delay:5.5s;">Na⁺</div>
<!-- Ligne du bas : Cl- -->
<div class="anion" style="top:110px;animation-delay:0.25s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:0.75s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:1.25s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:1.75s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:2.25s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:2.75s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:3.25s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:3.75s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:4.25s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:4.75s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:5.25s;">Cl⁻</div>
<div class="anion" style="top:110px;animation-delay:5.75s;">Cl⁻</div>
</div>
</div>
""", unsafe_allow_html=True)
        st.markdown('<div style="color:green;font-weight:bold;">✅ Porteurs de charge : les ions.</div>',unsafe_allow_html=True)
        # ------------------------------------------------------------------
        # 2. Quantité d'électricité
        # ------------------------------------------------------------------
        st.subheader(" 2. Quantité d'électricité")
        col1, col2 = st.columns(2)

        with col1:
            st.latex(r"Q=n\times e")

        with col2:
            st.write("**Q** : quantité d'électricité (C) | **n** : nombre d'électrons | **e** = 1,6 × 10⁻¹⁹ C")
        # ------------------------------------------------------------------
        # 3. Intensité du courant
        # ------------------------------------------------------------------
        st.subheader(" 3. Intensité du courant")
        col1, col2 = st.columns(2)

        with col1:
            st.latex(r"I=\frac{Q}{t}")

        with col2:
            st.write("**Q** : quantité d'électricité (C) | **I** : intensité du courant (A) | **t** : durée (s)")
        # ------------------------------------------------------------------
        # 4. Sens conventionnel du courant
        # ------------------------------------------------------------------
        st.subheader("4. Sens conventionnel du courant")
        st.markdown("Par convention, dans un circuit, le courant circule du pôle positif du générateur vers le pôle négatif.")
        # ------------------------------------------------------------------
        # 5. Unicité du courant
        # ------------------------------------------------------------------
        st.subheader("5. Unicité du courant")
        st.markdown("Dans un circuit en série, les ampèremètres doivent toujours être branchés en série.")
        # ------------------------------------------------------------------
        # Schéma du circuit en série
        # ------------------------------------------------------------------
        fig, ax = plt.subplots(figsize=(10, 2.6))
        # --------------------------------------------------
        # Composants
        # --------------------------------------------------
        rA = 0.40
        rL = 0.40
        # Positions
        A1 = (2, 0)
        A2 = (4.5, 1.4)
        A3 = (7, 0)
        L1 = (2.5, 1.4)
        L2 = (6.5, 1.4)
        # Pile
        pile_x = 4
        pile_y = -0.20
        pile_w = 1.5
        pile_h = 0.40
        # --------------------------------------------------
        # Fil du haut
        # --------------------------------------------------
        ax.plot([0, L1[0]-rL], [1.4, 1.4], color="black", linewidth=3)
        ax.plot([L1[0]+rL, A2[0]-rA], [1.4, 1.4], color="black", linewidth=3)
        ax.plot([A2[0]+rA, L2[0]-rL], [1.4, 1.4], color="black", linewidth=3)
        ax.plot([L2[0]+rL, 9], [1.4, 1.4], color="black", linewidth=3)
        # --------------------------------------------------
        # Montants verticaux
        # --------------------------------------------------
        ax.plot([0, 0], [0, 1.4], color="black", linewidth=3)
        ax.plot([9, 9], [0, 1.4], color="black", linewidth=3)
        # --------------------------------------------------
        # Fil du bas
        # --------------------------------------------------
        ax.plot([0, A1[0]-rA], [0, 0], color="black", linewidth=3)
        ax.plot([A1[0]+rA, pile_x], [0, 0], color="black", linewidth=3)
        ax.plot([pile_x+pile_w, A3[0]-rA], [0, 0], color="black", linewidth=3)
        ax.plot([A3[0]+rA, 9], [0, 0], color="black", linewidth=3)
        # --------------------------------------------------
        # Lampes
        # --------------------------------------------------
        for x, y, nom in [(L1[0], L1[1], "L1"),(L2[0], L2[1], "L2")]:
            lampe = Circle((x, y),rL,facecolor="yellow",edgecolor="black",linewidth=2)
            ax.add_patch(lampe)
            ax.text(x,y,nom,ha="center",va="center",fontsize=11,fontweight="bold")
        # --------------------------------------------------
        # Ampèremètres
        # --------------------------------------------------
        for x, y, nom in [(A1[0], A1[1], "A1"),(A2[0], A2[1], "A2"),(A3[0], A3[1], "A3")]:
            amp = Circle((x, y),rA,facecolor="#d0f0ff",edgecolor="black",linewidth=2)
            ax.add_patch(amp)
            ax.text(x,y,f"{nom}\n0,35 A",ha="center",va="center",fontsize=7,fontweight="bold")
        # --------------------------------------------------
        # Pile
        # --------------------------------------------------
        pile = Rectangle((pile_x, pile_y),pile_w,pile_h,facecolor="#eeeeee",edgecolor="black",linewidth=2)
        ax.add_patch(pile)
        ax.text(pile_x + pile_w/2,0,"Pile",ha="center",va="center",fontsize=10,fontweight="bold")
        ax.text(pile_x + 0.20,0,"+",fontsize=16,fontweight="bold",color="red",ha="center",va="center")
        ax.text(pile_x + pile_w - 0.20,0,"-",fontsize=16,fontweight="bold",color="blue",ha="center",va="center")
        # --------------------------------------------------
        # Flèches
        # --------------------------------------------------
        for x in [1, 7]:
            ax.arrow(x,1.4,0.35,0,head_width=0.10,head_length=0.18,fc="green",ec="green",linewidth=2)
        for x in [3.5, 8.5]:
            ax.arrow(x,0,-0.35,0,head_width=0.10,head_length=0.18,fc="green",ec="green",linewidth=2)
        # --------------------------------------------------
        # Intensités
        # --------------------------------------------------
        ax.text(1.5,1.72,"I₁",color="green",fontsize=11,fontweight="bold",ha="center")
        ax.text(7.5,1.72,"I₂",color="green",fontsize=11,fontweight="bold",ha="center")
        ax.text(3,-0.35,"I₃",color="green",fontsize=11,fontweight="bold",ha="center")
        ax.text(8,-0.35,"I₄",color="green",fontsize=11,fontweight="bold",ha="center")
        # --------------------------------------------------
        # Mise en forme
        # --------------------------------------------------
        ax.set_xlim(-0.3, 9.3)
        ax.set_ylim(-0.55, 1.95)
        ax.set_aspect("equal")
        ax.axis("off")
        fig.subplots_adjust(left=0.01,right=0.99,bottom=0.01,top=0.99)
        st.pyplot(fig, use_container_width=True)
        st.info("💡 Les trois ampèremètres indiquent la même valeur.")
        st.latex(r"I_1 = I_2 = I_3 = 0,35\ A")
        st.markdown("✅ Dans un circuit en série, l'intensité électrique est la même en tous points.")
        st.subheader("6. Loi des nœuds")
        st.write("Un nœud est un point où arrivent au moins trois conducteurs.")
        fig, ax = plt.subplots(figsize=(10, 4))
        # ==================================================
        # Niveaux verticaux
        # ==================================================
        Y_HAUT = 3.0
        Y_BAS = 1.5
        rA = 0.45
        rL = 0.45
        # ==================================================
        # FILS
        # ==================================================
        # Côté gauche
        ax.plot([0, 0], [0, Y_HAUT], color="black", lw=3)
        # Haut gauche jusqu'à L1
        ax.plot([0, 2], [Y_HAUT, Y_HAUT], color="black", lw=3)
        # Entre L1 et le nœud
        ax.plot([3, 5], [Y_HAUT, Y_HAUT], color="black", lw=3)
        # Branche du haut
        ax.plot([5, 6], [Y_HAUT, Y_HAUT], color="black", lw=3)
        ax.plot([7, 8], [Y_HAUT, Y_HAUT], color="black", lw=3)
        ax.plot([9, 11], [Y_HAUT, Y_HAUT], color="black", lw=3)
        # Branche du bas
        ax.plot([5, 6], [Y_BAS, Y_BAS], color="black", lw=3)
        ax.plot([7, 8], [Y_BAS, Y_BAS], color="black", lw=3)
        ax.plot([9, 11], [Y_BAS, Y_BAS], color="black", lw=3)
        # Liaison verticale gauche
        ax.plot([5, 5], [Y_BAS, Y_HAUT], color="black", lw=3)
        # Liaison verticale droite
        ax.plot([11, 11], [Y_BAS, Y_HAUT], color="black", lw=3)
        # Retour vers la pile
        ax.plot([11, 11], [Y_BAS, 0], color="black", lw=3)
        ax.plot([11, 8], [0, 0], color="black", lw=3)
        # Vers A1
        ax.plot([0, 2], [0, 0], color="black", lw=3)
        # De A1 à la pile
        ax.plot([3, 5], [0, 0], color="black", lw=3)
        # De la pile au retour
        ax.plot([7, 8], [0, 0], color="black", lw=3)
        # ==================================================
        # AMPÈREMÈTRES
        # ==================================================
        a1 = Circle((2.5, 0),rA,facecolor="#d0f0ff",edgecolor="black",linewidth=2)
        ax.add_patch(a1)
        ax.text(2.5,0,"I₁\n7,0 mA",ha="center",va="center",fontsize=8,fontweight="bold")
        a2 = Circle((6.5, Y_HAUT),rA,facecolor="#d0f0ff",edgecolor="black",linewidth=2)
        ax.add_patch(a2)
        ax.text(6.5,Y_HAUT,"I₂\n3,5 mA",ha="center",va="center",fontsize=8,fontweight="bold")
        a3 = Circle((6.5, Y_BAS),rA,facecolor="#d0f0ff",edgecolor="black",linewidth=2)
        ax.add_patch(a3)
        ax.text(6.5,Y_BAS,"I₃\n3,5 mA",ha="center",va="center",fontsize=8,fontweight="bold")
        # ==================================================
        # PILE
        # ==================================================
        pile = Rectangle((5, -0.4),2,0.8,facecolor="#eeeeee",edgecolor="black",linewidth=2)
        ax.add_patch(pile)
        ax.text(6,0,"Pile",ha="center",va="center",fontsize=10,fontweight="bold")
        ax.text(5.4,0,"+",fontsize=16,fontweight="bold",color="red",ha="center",va="center")
        ax.text(6.6,0,"-",fontsize=16,fontweight="bold",color="blue",ha="center",va="center")
        # ==================================================
        # LAMPES
        # ==================================================
        l1 = Circle((2.5, Y_HAUT),rL,facecolor="yellow",edgecolor="black",linewidth=2)
        ax.add_patch(l1)
        ax.text(2.5,Y_HAUT,"L1",ha="center",va="center",fontsize=10,fontweight="bold")
        l2 = Circle((8.5, Y_HAUT),rL,facecolor="yellow",edgecolor="black",linewidth=2)
        ax.add_patch(l2)
        ax.text(8.5,Y_HAUT,"L2",ha="center",va="center",fontsize=10,fontweight="bold")
        l3 = Circle((8.5, Y_BAS),rL,facecolor="yellow",edgecolor="black",linewidth=2)
        ax.add_patch(l3)
        ax.text(8.5,Y_BAS,"L3",ha="center",va="center",fontsize=10,fontweight="bold")
        # ==================================================
        # FLÈCHES DES COURANTS
        # ==================================================
        ax.arrow(2,0,-0.6,0,head_width=0.12,head_length=0.20,fc="green",ec="green",linewidth=2)
        ax.text(0.9,0.35,"I₁",color="green",fontsize=14,fontweight="bold")
        ax.arrow(9.5,Y_HAUT,0.6,0,head_width=0.12,head_length=0.20,fc="green",ec="green",linewidth=2)
        ax.text(10.15,Y_HAUT + 0.30,"I₂",color="green",fontsize=14,fontweight="bold")
        ax.arrow(9.5,Y_BAS,0.6,0,head_width=0.12,head_length=0.20,fc="green",ec="green",linewidth=2)
        ax.text(0.15,Y_BAS + 0.30,"I₃",color="green",fontsize=14,fontweight="bold")
        # ==================================================
        # AFFICHAGE
        # ==================================================
        ax.set_xlim(-0.5, 11.5)
        ax.set_ylim(-0.8, 3.6)
        ax.set_aspect("equal")
        ax.axis("off")
        fig.subplots_adjust(left=0.01,right=0.99,bottom=0.01,top=0.99)
        st.pyplot(fig, use_container_width=True)
        st.latex(r"I₁ = I₂ + I₃ ")
        st.markdown("✅ La somme des intensités des courants arrivant à un nœud est égale à la somme des intensités des courants partant de ce nœud.")
    if st.session_state.page == "cours":
        col1, col2 = st.columns([5, 1])
        with col1:
            st.write(" Si vous avez compris, cliquez sur le bouton : QCM 👉")
        with col2:
            if st.button("➡️ QCM", key="btn_vers_qcm", use_container_width=True):
                st.session_state.page = "qcm"
                st.rerun()
    elif st.session_state.page == "qcm":
        # ==================================
        # En-tête
        # ==================================
        st.markdown("<h1 style='margin-bottom:0px;'>⚡ Défi : Le courant électrique</h1>",unsafe_allow_html=True)
        st.caption("Obtiens 100 % pour accéder à la simulation.")
        # ==================================
        # Questions
        # ==================================
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("### 1️⃣ Porteurs de charge")
                q1 = st.radio("Dans un métal, quels sont les porteurs de charge ?",["Les cations", "Les électrons", "Les anions"],key="q1",index=None,horizontal=True)
            with st.container(border=True):
                st.markdown("### 2️⃣ Solution ionique")
                q2 = st.radio("Dans une solution ionique, le courant est dû au déplacement :",["Des électrons","Des ions positifs et négatifs","Des molécules"],key="q2",index=None,horizontal=True)
            with st.container(border=True):
                st.markdown("### 3️⃣ Sens du courant")
                q3 = st.radio("Le courant conventionnel circule :",["Du + vers le - à l'extérieur du générateur","Du + vers le - à l'intérieur du générateur"],key="q3",index=None,horizontal=True)
        with col2:
            with st.container(border=True):
                st.markdown("### 4️⃣ Relation fondamentale")
                q4 = st.radio("Quelle relation est correcte ?",["Q = I × t","Q = I / t","Q = t / I"],key="q4",index=None,horizontal=True)
            with st.container(border=True):
                st.markdown("### 5️⃣ Circuit sans dérivation")
                q5 = st.radio("Dans un circuit sans dérivation :",["La somme des intensités de courant est nulle","Le courant est le même en tout point"],key="q5",index=None,horizontal=True)
            with st.container(border=True):
                st.markdown("### 6️⃣ Loi des nœuds")
                q6 = st.radio("Dans un nœud :",["Le courant n'est pas le même en tout point","La somme des intensités de courant est nulle"],key="q6",index=None,horizontal=True)
        # ==================================
        # Progression
        # ==================================
        # Initialisation
        if "qcm_valide" not in st.session_state:
            st.session_state.qcm_valide = False
        st.markdown("<br>", unsafe_allow_html=True)
        nb_reponses = sum(rep is not None for rep in [q1, q2, q3, q4, q5, q6])
        reste = 6 - nb_reponses
        toutes_reponses = nb_reponses == 6
        c1, c2 = st.columns(2)
        with c1:
            if reste == 6:
                st.info("🎯 Réponds aux 6 questions.")
            elif reste > 0:
                st.warning(f"🎯 Il reste {reste} question(s) à compléter.")
            else:
                if st.session_state.qcm_valide:
                    st.success("✅ QCM déjà validé")
                else:
                    st.success("✅ Toutes les questions sont complétées")
        with c2:
            if st.button("✅ Valider le QCM",use_container_width=True,disabled=(not toutes_reponses) or st.session_state.qcm_valide):
                score = 0
                if q1 == "Les électrons":
                    score += 1
                if q2 == "Des ions positifs et négatifs":
                    score += 1
                if q3 == "Du + vers le - à l'extérieur du générateur":
                    score += 1
                if q4 == "Q = I × t":
                    score += 1
                if q5 == "Le courant est le même en tout point":
                    score += 1
                if q6 == "Le courant n'est pas le même en tout point":
                    score += 1
                st.session_state.score_qcm = score
                st.session_state.qcm_rate = score != 6
                st.session_state.qcm_valide = True
                st.rerun()
        # ==================================
        # Résultat
        # ==================================
        score = st.session_state.get("score_qcm", 0)
        if score == 6:
            st.balloons()
            c1, c2, c3 = st.columns(3)
            with c1:
                st.success("🏆 Félicitations !")
            with c2:
                st.success("6 / 6")
            with c3:
                if st.button("🔬 Accéder à la simulation",key="btn_vers_simulation",use_container_width=True):
                    st.session_state.page = "simulation"
                    st.rerun()
        elif st.session_state.get("qcm_rate", False):
            c1, c2, c3 = st.columns(3)
            with c1:
                st.error(f"❌ Score : {score}/6")
            with c2:
                st.warning("📘 Revois le cours")
            with c3:
                if st.button("📘 Retour au cours",use_container_width=True):
                    st.session_state.page = "cours"
                    st.session_state.qcm_rate = False
                    st.session_state.qcm_valide = False
                    st.session_state.score_qcm = 0
                    for cle in ["q1", "q2", "q3", "q4", "q5", "q6"]:
                        if cle in st.session_state:
                            del st.session_state[cle]
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
        # st.header("🔬 Simulation : Lois des intensités")
        # ==================================
        # Initialisation
        # ==================================
        if "score_sens" not in st.session_state:
            st.session_state.score_sens = 0
        if "qcm_rate" not in st.session_state:
            st.session_state.qcm_rate = False
        if "erreurs_sens" not in st.session_state:
            st.session_state.erreurs_sens = []
        if "etape1_validee" not in st.session_state:
            st.session_state.etape1_validee = False
        if "etape2_validee" not in st.session_state:
            st.session_state.etape2_validee = False
        if "etape3_validee" not in st.session_state:
            st.session_state.etape3_validee = False
        if "partie_etape3" not in st.session_state:
            st.session_state.partie_etape3 = 1
    # ==================================
        # INTERRUPTEURS
        # ==================================
        if "S1" not in st.session_state:
            st.session_state.S1 = True
        if "S2" not in st.session_state:
            st.session_state.S2 = True
        if "S3" not in st.session_state:
            st.session_state.S3 = True
        if "S4" not in st.session_state:
            st.session_state.S4 = True
        # ==================================
        # Initialisation sens courant
        # ==================================
        if "sens" not in st.session_state:
            st.session_state.sens = {"I1": random.choice(["droite", "gauche"]),"I2": random.choice(["droite", "gauche"]),
                "I3": random.choice(["droite", "gauche"]),"I4": random.choice(["droite", "gauche"]),"I5": random.choice(["droite", "gauche"]),
                "I6": random.choice(["haut", "bas"]),"I7": random.choice(["haut", "bas"]),"I8": random.choice(["haut", "bas"])}
        # ==========================================
        # INITIALISATION DES COURANTS
        # ==========================================
        if "courants_generes" not in st.session_state:
            S1 = st.session_state.S1
            S2 = st.session_state.S2
            S3 = st.session_state.S3
            S4 = st.session_state.S4
            # Branche milieu
            I2 = round(random.uniform(0.30, 1.20), 2) if S2 else 0
            # Branches supérieures
            I3 = round(random.uniform(0.20, 0.80), 2) if S3 else 0
            I4 = round(random.uniform(0.20, 0.80), 2) if S4 else 0
            # Si S1 est ouvert, toute la partie haute est coupée
            if not S1:
                I3 = 0
                I4 = 0
            # Lois des nœuds
            I5 = round(I3 + I4, 2)
            I6 = I5
            I8 = I5
            I7 = round(I2 + I6, 2)
            I1 = I7
            st.session_state.intensites = {"I1": I1,"I2": I2,"I3": I3,"I4": I4,"I5": I5,"I6": I6,"I7": I7,"I8": I8}
            st.session_state.intensites_initiales = st.session_state.intensites.copy()
            st.session_state.courants_generes = True
        # ==================================
        # Dessin lampe
        # ==================================
        def dessiner_lampe(ax, x, y, nom):
            lampe = plt.Circle((x, y),0.4,facecolor="yellow",edgecolor="black",linewidth=2)
            ax.add_patch(lampe)
            ax.text(x,y,nom,ha="center",va="center",fontsize=11,fontweight="bold")
        # ==================================
        # Dessin ampèremetre
        # ==================================
        def dessiner_amperemetre(ax, x, y, texte, nom):
            cercle = plt.Circle((x, y),0.5,facecolor="#d0f0ff",edgecolor="black",linewidth=2)
            ax.add_patch(cercle)
            ax.text(x,y + 0.12,nom,ha="center",va="center",fontsize=8,fontweight="bold",color="black")
            ax.text(x,y - 0.10,texte,ha="center",va="center",fontsize=8,fontweight="bold")
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
            positions = {"I₃": (5.6, 3),"I₅": (3, 4.5),"I₆": (8.3, 1.1),"I₂": (2.5, 1.7),"I₇": (8.3, 0),"I₁": (3.2, -1.5),"I₄": (5.6, 4.5),"I₈": (0.3, 2)}
            for nom, (x, y) in positions.items():
                ax.text(x,y,nom,fontsize=14,color="red",fontweight="bold",ha="center",va="center")
        def dessiner_interrupteur(ax, x, y, ferme=True, nom="S", orientation="horizontal"):
            if orientation == "horizontal":
                if ferme:
                    ax.plot([x - 0.25, x + 0.25],[y, y],color="green",linewidth=4)
                else:
                    ax.plot([x - 0.25, x],[y, y],color="red",linewidth=2)
                    ax.plot([x, x + 0.18],[y, y + 0.15],color="red",linewidth=2)
                    ax.plot([x + 0.25, x + 0.45],[y, y],color="black",linewidth=2)
                ax.text(x,y + 0.25,nom,color="red",fontsize=10,ha="center",weight="bold")
            else:  # orientation verticale
                if ferme:
                    ax.plot([x, x],[y - 0.25, y + 0.25],color="green",linewidth=4)
                else:
                    ax.plot([x, x],[y - 0.25, y],color="red",linewidth=2)
                    ax.plot([x, x + 0.15],[y, y + 0.18],color="red",linewidth=2)
                    ax.plot([x, x],[y + 0.25, y + 0.45],color="black",linewidth=2)
                ax.text(x + 0.20,y,nom,color="red",fontsize=10,va="center",weight="bold")
        # ==================================
        # Schéma du circuit
        # ==================================
        def schema_circuit():
            fig, ax = plt.subplots(figsize=(10, 4))
            intensites = st.session_state.intensites.copy()
            S1 = st.session_state.S1
            S2 = st.session_state.S2
            S3 = st.session_state.S3
            S4 = st.session_state.S4
            # Application des interrupteurs
            if not S2:
                intensites["I2"] = 0
            if not S3:
                intensites["I3"] = 0
            if not S4:
                intensites["I4"] = 0
            intensites["I5"] = intensites["I3"] + intensites["I4"]
            intensites["I6"] = intensites["I5"]
            intensites["I8"] = intensites["I5"]
            intensites["I7"] = intensites["I2"] + intensites["I6"]
            intensites["I1"] = intensites["I7"]
            if not S1:
                intensites["I3"] = 0
                intensites["I4"] = 0
                intensites["I5"] = 0
                intensites["I6"] = 0
                intensites["I8"] = 0
                intensites["I7"] = intensites["I2"]
                intensites["I1"] = intensites["I7"]
            BON_SENS = {"I1": "gauche","I2": "droite","I3": "droite","I4": "droite","I5": "droite","I6": "bas","I7": "bas","I8": "haut"}
            # Étape 1 : afficher les choix de l'élève
            if (st.session_state.etape == 1and not st.session_state.etape1_validee):
                sens_affiches = st.session_state.sens
            else:
                sens_affiches = BON_SENS
            # Haut horizontal
            ax.plot([0, 0.6], [4, 4], "k", lw=2)
            ax.plot([1.4, 1.7], [4, 4], "k", lw=2)
            ax.plot([2.7, 4.1], [4, 4], "k", lw=2)
            ax.plot([4.9, 6], [4, 4], "k", lw=2)
            ax.plot([7, 7.2], [4, 4], "k", lw=2)
            ax.plot([7.7, 8], [4, 4], "k", lw=2)
            # Milieu horizontal
            ax.plot([3.5, 4.1], [2.5, 2.5], "k", lw=2)
            ax.plot([4.9, 6], [2.5, 2.5], "k", lw=2)
            ax.plot([7, 7.2], [2.5, 2.5], "k", lw=2)
            ax.plot([7.7, 8], [2.5, 2.5], "k", lw=2)
            ax.plot([0, 3], [0.7, 0.7], "k", lw=2)
            ax.plot([3.5, 4.1], [0.7, 0.7], "k", lw=2)
            ax.plot([4.9, 6], [0.7, 0.7], "k", lw=2)
            ax.plot([7, 8], [0.7, 0.7], "k", lw=2)
            # Bas horizontal
            ax.plot([0, 0.6], [-1, -1], "k", lw=2)
            ax.plot([1.4, 1.7], [-1, -1], "k", lw=2)
            ax.plot([2.7, 3.7], [-1, -1], "k", lw=2)
            ax.plot([5.3, 6], [-1, -1], "k", lw=2)
            ax.plot([7, 8], [-1, -1], "k", lw=2)
            # Gauche vertical
            ax.plot([0, 0], [-1, 2], "k", lw=2)
            ax.plot([0, 0], [2.3, 2.5], "k", lw=2)
            ax.plot([0, 0], [3.5, 4], "k", lw=2)
            # if st.session_state.etape < 3:
            ax.plot([8, 8], [-1, 1.3], "k", lw=2)
            ax.plot([8, 8], [2.3, 4], "k", lw=2)
            ax.plot([3.5, 3.5], [2.5, 4], "k", lw=2)
            if st.session_state.etape < 3:
                ax.plot([0, 4.1], [0.7, 0.7], "k", lw=2)
                ax.plot([7, 8], [4, 4], "k", lw=2)
                ax.plot([7, 8], [2.5, 2.5], "k", lw=2)
                ax.plot([0, 0], [-1, 0.2], "k", lw=2)
                ax.plot([0, 0], [1.2, 2.5], "k", lw=2)
            def valeur_affichee(nom):
                if not st.session_state.etape3_validee:
                    return ""
                valeur = intensites[nom]
                if valeur is None:
                    return ""
                return f"{valeur:.2f} A"
            dessiner_amperemetre(ax, 2.2, -1, valeur_affichee("I1"), "A1")
            dessiner_amperemetre(ax, 6.5, 0.7, valeur_affichee("I2"), "A2")
            dessiner_amperemetre(ax, 6.5, 2.5, valeur_affichee("I3"), "A3")
            dessiner_amperemetre(ax, 6.5, 4, valeur_affichee("I4"), "A4")
            dessiner_amperemetre(ax, 2.2, 4, valeur_affichee("I5"), "A5")
            dessiner_amperemetre(ax, 8, 1.8, valeur_affichee("I6"), "A6")
            dessiner_amperemetre(ax, 6.5, -1, valeur_affichee("I7"), "A7")
            dessiner_amperemetre(ax, 0, 3, valeur_affichee("I8"), "A8")
            # Lampes
            dessiner_lampe(ax, 1, 4, "L5")
            dessiner_lampe(ax, 1, -1, "L1")
            dessiner_lampe(ax, 4.5, 4, "L4")
            dessiner_lampe(ax, 4.5, 0.7, "L2")
            dessiner_lampe(ax, 4.5, 2.5, "L3")
                # ==================================
                # Interrupteurs
                # ==================================
            if st.session_state.etape == 3:
                # S1 avant I8
                dessiner_interrupteur(ax,x=0,y=2,ferme=st.session_state.S1,nom="S1",orientation="vertical")
                dessiner_interrupteur(ax,3.2,0.7,st.session_state.S2,"S2")
                # S4 après I4
                dessiner_interrupteur(ax,7.4,4.0,st.session_state.S4,"S4")
                # S3 après I3
                dessiner_interrupteur(ax,7.4,2.5,st.session_state.S3,"S3")
            # pile
            dessiner_pile(ax, 4.5, -1)
            # Intensités
            if st.session_state.etape <= 2:
                etiquettes_intensites(ax)
                # I1
                if sens_affiches["I1"] == "droite":
                    ax.arrow(3.2, -1, 0.01, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                else:
                    ax.arrow(3.2, -1, -0.01, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                # I2
                if sens_affiches["I2"] == "droite":
                    ax.arrow(2.5, 0.7, 0.01, 0,head_width=0.3, head_length=0.4,fc="blue", ec="blue")
                else:
                    ax.arrow(2.5, 0.7, -0.01, 0,head_width=0.3, head_length=0.4,fc="blue", ec="blue")
                # I3
                if sens_affiches["I3"] == "droite":
                    ax.arrow(5.5, 2.5, 0.01, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                else:
                    ax.arrow(5.5, 2.5, -0.01, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                # I4
                if sens_affiches["I4"] == "droite":
                    ax.arrow(5.5, 4, 0.01, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                else:
                    ax.arrow(5.5, 4, -0.01, 0,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                # I5
                if sens_affiches["I5"] == "droite":
                    ax.arrow(3.1, 4, 0.01, 0,head_width=0.3, head_length=0.4,fc="blue", ec="blue")
                else:
                    ax.arrow(3.1, 4, -0.01, 0,head_width=0.3, head_length=0.4,fc="blue", ec="blue")
                # I6
                if sens_affiches["I6"] == "haut":
                    ax.arrow(8, 0.8, 0, 0.01,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                else:
                    ax.arrow(8, 1.2, 0, -0.01,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                # I7
                if sens_affiches["I7"] == "haut":
                    ax.arrow(8, 0, 0, 0.01,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                else:
                    ax.arrow(8, 0, 0, -0.01,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                # # I8
                if sens_affiches["I8"] == "haut":
                    ax.arrow(0, 2, 0, 0.01,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
                else:
                    ax.arrow(0, 2, 0, -0.01,head_width=0.3,head_length=0.4,fc="blue", ec="blue")
            ax.set_xlim(-1, 9)
            ax.set_ylim(-1.6, 4.6)
            ax.axis("off")
            plt.tight_layout(pad=0)
            return fig
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
            # ==================================
            # Boutons choix sens
            # ==================================
            st.subheader("🔄 Étape 1 : Observe le circuit et choisis le bon sens des courants")
            courants = ["I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8"]
            cols = st.columns(8)
            for i, courant in enumerate(courants):
                with cols[i]:
                    directions_h = ["gauche", "droite"]
                    directions_v = ["haut", "bas"]
                    if st.button(f"↺ {courant}", disabled=st.session_state.etape1_validee):
                        if courant in ["I1", "I2", "I3", "I4", "I5"]:
                            sens = st.session_state.sens[courant]
                            idx = directions_h.index(sens)
                            st.session_state.sens[courant] = directions_h[(idx + 1) % 2]
                        else:
                            sens = st.session_state.sens[courant]
                            idx = directions_v.index(sens)
                            st.session_state.sens[courant] = directions_v[(idx + 1) % 2]
                        st.rerun()
            # Affichage du schéma
            fig = schema_circuit()
            st.pyplot(fig, use_container_width=True)
            if not st.session_state.etape1_validee:
                if st.button("✅ Valider les sens", key="valider_sens"):
                    score_sens = 0
                    BON_SENS = {"I1": "gauche","I2": "droite","I3": "droite","I4": "droite","I5": "droite","I6": "bas","I7": "bas","I8": "haut"}
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
                # Ligne 1 : score + erreurs
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.info(f"🎯 Score sens : {st.session_state.score_sens}/8")
                with col2:
                    nb_erreurs = len(st.session_state.erreurs_sens)
                    if nb_erreurs == 0:
                        st.success("✅ 0 erreur")
                    else:
                        st.error(f"❌ {nb_erreurs} erreur(s)")
                with col3:
                        if nb_erreurs > 0:
                            st.write("Courants incorrects :",", ".join(st.session_state.erreurs_sens))
                        else:
                            st.write("Tous les sens sont corrects")
                # Ligne 2 : étape suivante + correction
                col_next, col_corr = st.columns([1, 3])
                with col_next:
                    if st.button("➡️ Étape suivante", key="vers_etape2"):
                        st.session_state.etape = 2
                        st.rerun()
                with col_corr:
                    with st.expander("✅ Voir la correction"):
                        c1, c2, c3, c4, c5, c6, c7,c8 = st.columns(8)
                        c1.write("I₁ : gauche")
                        c2.write("I₂ : droite")
                        c3.write("I₃ : droite")
                        c4.write("I₄ : droite")
                        c5.write("I₅ : droite")
                        c6.write("I₆ : bas")
                        c7.write("I₇ : bas")
                        c8.write("I₈ : haut")
        # ==================================
        # ETAPE 2
        # ==================================
        if "etape2_validee" not in st.session_state:
            st.session_state.etape2_validee = False
        if "score_relations" not in st.session_state:
            st.session_state.score_relations = 0
        if st.session_state.etape == 2:
            st.subheader("✏️ Étape 2 : Observe le circuit et trouve les relations entre les intensités")
            c1, c2, c3, c4, c5, c6 = st.columns(6)
            with c1:
                relation1 = st.text_area("I₁, I₂, I₈",key=f"relation1_{st.session_state.id_eleve}",disabled=st.session_state.etape2_validee)
            with c2:
                relation2 = st.text_area("I₃, I₅, I₄",key=f"relation2_{st.session_state.id_eleve}",disabled=st.session_state.etape2_validee)
            with c3:
                relation3 = st.text_area("I₅, I₆, I₈",key=f"relation3_{st.session_state.id_eleve}",disabled=st.session_state.etape2_validee)
            with c4:
                relation4 = st.text_area("I₂, I₆, I₇",key=f"relation4_{st.session_state.id_eleve}",disabled=st.session_state.etape2_validee)
            with c5:
                relation5 = st.text_area("I₃, I₆, I₄",key=f"relation5_{st.session_state.id_eleve}",disabled=st.session_state.etape2_validee)
            with c6:
                relation6 = st.text_area("I₁, I₇",key=f"relation6_{st.session_state.id_eleve}",disabled=st.session_state.etape2_validee)
            # ----------------------------------
            # APERÇU DES RÉPONSES
            # ----------------------------------
            with st.expander("🔍 Vérifier mes saisies avant validation"):
                st.write("Relation 1 :",relation1 if relation1 else "Aucune saisie")
                st.write("Relation 2 :",relation2 if relation2 else "Aucune saisie")
                st.write("Relation 3 :",relation3 if relation3 else "Aucune saisie")
                st.write("Relation 4 :",relation4 if relation4 else "Aucune saisie")
                st.write("Relation 5 :",relation5 if relation5 else "Aucune saisie")
                st.write("Relation 6 :",relation6 if relation6 else "Aucune saisie")
            # ----------------------------------
            # VALIDATION
            # ----------------------------------
            # Affichage du schéma
            fig = schema_circuit()
            st.pyplot(fig, use_container_width=True)
            if not st.session_state.etape2_validee:
                if st.button("✅ Valider les relations",key="valider_relations"):
                    score = 0
                    r1 = relation1.upper().replace(" ", "")
                    r2 = relation2.upper().replace(" ", "")
                    r3 = relation3.upper().replace(" ", "")
                    r4 = relation4.upper().replace(" ", "")
                    r5 = relation5.upper().replace(" ", "")
                    r6 = relation6.upper().replace(" ", "")
                    if r1 in ["I1=I2+I8","I1=I8+I2","I2+I8=I1","I8+I2=I1"]:
                        score += 1
                    if r2 in ["I5=I3+I4","I5=I4+I3","I4+I3=I5","I3+I4=I5"]:
                        score += 1
                    if r3 in ["I8=I5=I6","I8=I6=I5","I5=I8=I6","I5=I6=I8","I6=I8=I5","I6=I5=I8"]:
                        score += 1
                    if r4 in ["I7=I2+I6","I7=I6+I2","I6+I2=I7","I2+I6=I7"]:
                        score += 1
                    if r5 in ["I6=I3+I4","I6=I4+I3","I3+I4=I6","I4+I3=I6"]:
                        score += 1
                    if r6 in ["I1=I7","I7=I1"]:
                        score += 1
                    if "" in [r1, r2, r3, r4, r5, r6]:
                        st.warning("⚠️ Complète toutes les relations avant de valider.")
                        st.stop()
                    erreurs = []
                    if r1 not in ["I1=I2+I8","I1=I8+I2","I2+I8=I1","I8+I2=I1"]:
                        erreurs.append(f"Relation 1 : {r1}")
                    if r2 not in ["I5=I3+I4","I5=I4+I3","I4+I3=I5","I3+I4=I5"]:
                        erreurs.append(f"Relation 2 : {r2}")
                    if r3 not in ["I8=I5=I6","I8=I6=I5","I5=I8=I6","I5=I6=I8","I6=I8=I5","I6=I5=I8"]:
                        erreurs.append(f"Relation 3 : {r3}")
                    if r4 not in ["I7=I2+I6","I7=I6+I2","I6+I2=I7","I2+I6=I7"]:
                        erreurs.append(f"Relation 4 : {r4}")
                    if r5 not in ["I6=I3+I4","I6=I4+I3","I3+I4=I6","I4+I3=I6"]:
                        erreurs.append(f"Relation 5 : {r5}")
                    if r6 not in ["I1=I7","I7=I1"]:
                        erreurs.append(f"Relation 6 : {r6}")
                    if erreurs:
                        st.error("Erreurs détectées :")
                        for e in erreurs:
                            st.write(e)
                    st.session_state.score_relations = score
                    st.session_state.etape2_validee = True
                    st.rerun()
        # ----------------------------------
        # RESULTATS ETAPE 2
        # ----------------------------------
        if st.session_state.etape == 2 and st.session_state.etape2_validee:
            # Ligne 1 : score + erreurs
            col1, col2 = st.columns(2)
            with col1:
                st.info(f"🎯 Score relations : "f"{st.session_state.score_relations}/6")
            with col2:
                nb_erreurs = 6 - st.session_state.score_relations
                if nb_erreurs == 0:
                    st.success("✅ 0 erreur")
                else:
                    st.error(f"❌ {nb_erreurs} erreur(s)")
            # Ligne 2 : étape suivante + correction
            col_next, col_corr = st.columns([1, 3])
            with col_next:
                if st.button("➡️ Étape suivante",key="vers_etape3"):
                    st.session_state.etape = 3
                    st.rerun()
            with col_corr:
                with st.expander("✅ Voir la correction"):
                    c1, c2, c3, c4, c5, c6 = st.columns(6)
                    c1.write("**I1=I2+I8**")
                    c2.write("**I5=I3+I4**")
                    c3.write("**I8=I5=I6**")
                    c4.write("**I7=I2+I6**")
                    c5.write("**I6=I3+I4**")
                    c6.write("**I1=I7**")
        # ==================================
        # ETAPE 3
        # ==================================
        if "version_partie" not in st.session_state:
            st.session_state.version_partie = 0
        if "partie_etape3" not in st.session_state:
            st.session_state.partie_etape3 = 1
        if "score_calculs" not in st.session_state:
            st.session_state.score_calculs = 0
        if "etape3_validee" not in st.session_state:
            st.session_state.etape3_validee = False
        if "score_calculs" not in st.session_state:
            st.session_state.score_calculs = 0
        if "erreurs_calculs" not in st.session_state:
            st.session_state.erreurs_calculs = []
        if st.session_state.etape == 3:
            st.subheader(f"🧮 Étape 3 - Partie {st.session_state.partie_etape3}/4")
            # ----------------------------------
            # Configuration des parties
            # ----------------------------------
            if st.session_state.partie_etape3 == 1:
                st.info(
                    "🔍 Partie 1 : ouvre uniquement l'interrupteur S4 puis calcule les intensités et reporte leurs valeurs sous le schéma.")
                # Données fournies après ouverture de S4
                courant1 = "I2"
                courant2 = "I3"
                courants_a_trouver = ["I4","I5","I6","I8","I7","I1"]
            elif st.session_state.partie_etape3 == 2:
                st.info(
                    "🔍 Partie 2 : ouvre uniquement l'interrupteur S3 puis calcule les intensités et reporte leurs valeurs sous le schéma.")
                # Données fournies après ouverture de S3
                courant1 = "I2"
                courant2 = "I4"
                courants_a_trouver = ["I3","I5","I6","I8","I7","I1"]
            elif st.session_state.partie_etape3 == 3:
                st.info("🔍 Partie 3 : ouvre uniquement l'interrupteur S2 puis calcule les intensités et reporte leurs valeurs sous le schéma.")
                # Données fournies après ouverture de S2
                courant1 = "I3"
                courant2 = "I8"
                courants_a_trouver = ["I1","I2","I4","I5","I6","I7"]
            elif st.session_state.partie_etape3 == 4:
                st.info("🔍 Partie 4 : ouvre uniquement l'interrupteur S1 puis calcule les intensités et reporte leurs valeurs sous le schéma.")
                # Données fournies après ouverture de S1
                courant1 = "I2"
                courant2 = "I7"
                courants_a_trouver = ["I3","I4","I5","I6","I8","I1"]
            # ----------------------------------
            # Boutons interrupteurs
            # ----------------------------------
            st.subheader("🔌 Interrupteurs")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if st.button(f"S1 {'🟢 Fermé' if st.session_state.S1 else '🔴 Ouvert'}",key="btnS1"):
                    st.session_state.S1 = not st.session_state.S1
                    st.rerun()
            with col2:
                if st.button(f"S2 {'🟢 Fermé' if st.session_state.S2 else '🔴 Ouvert'}",key="btnS2"):
                    st.session_state.S2 = not st.session_state.S2
                    st.rerun()
            with col3:
                if st.button(f"S3 {'🟢 Fermé' if st.session_state.S3 else '🔴 Ouvert'}",key="btnS3"):
                    st.session_state.S3 = not st.session_state.S3
                    st.rerun()
            with col4:
                if st.button(f"S4 {'🟢 Fermé' if st.session_state.S4 else '🔴 Ouvert'}",key="btnS4"):
                    st.session_state.S4 = not st.session_state.S4
                    st.rerun()
            # ----------------------------------
            # Intensités recalculées
            # ----------------------------------
            intensites = st.session_state.intensites.copy()
            if not st.session_state.S2:
                intensites["I2"] = 0
            if not st.session_state.S3:
                intensites["I3"] = 0
            if not st.session_state.S4:
                intensites["I4"] = 0
            # Lois des nœuds
            intensites["I5"] = intensites["I3"] + intensites["I4"]
            intensites["I6"] = intensites["I5"]
            intensites["I8"] = intensites["I5"]
            intensites["I7"] = intensites["I2"] + intensites["I6"]
            intensites["I1"] = intensites["I7"]
            # Cas particulier : S1 ouvert
            if not st.session_state.S1:
                intensites["I3"] = 0
                intensites["I4"] = 0
                intensites["I5"] = 0
                intensites["I6"] = 0
                intensites["I8"] = 0
                intensites["I7"] = intensites["I2"]
                intensites["I1"] = intensites["I7"]
            # ----------------------------------
            # Schéma
            # ----------------------------------
            fig = schema_circuit()
            st.pyplot(fig, use_container_width=True)
            # ----------------------------------
            # Courants donnés
            # ----------------------------------
            valeur1 = intensites[courant1]
            valeur2 = intensites[courant2]
            col1, col2 = st.columns(2)
            with col1:
                st.write("📌 Courants donnés :",f"**{courant1} = {valeur1:.2f} A**",f"**{courant2} = {valeur2:.2f} A**")
            with col2:
                if "reponses_calculs" not in st.session_state:
                    st.session_state.reponses_calculs = {}
                colonnes = st.columns(len(courants_a_trouver))
                for col, nom in zip(colonnes, courants_a_trouver):
                    with col:
                        saisie = st.text_area(nom,placeholder="?",height=70,key=f"calc_{nom}_{st.session_state.version_partie}_{st.session_state.get('id_eleve', 0)}")
                        # st.session_state.reponses_calculs[nom] = st.number_input(nom,value=None,placeholder="?",step=0.01,format="%.2f",key=f"calc_{nom}_{st.session_state.version_partie}")
        # Bouton aligné complètement à gauche
            verifier_calculs = st.button("✅ Vérifier les calculs")
            # ============================
            # Valeurs attendues
            # ============================
            I1 = intensites["I1"]
            I2 = intensites["I2"]
            I3 = intensites["I3"]
            I4 = intensites["I4"]
            I5 = intensites["I5"]
            I6 = intensites["I6"]
            I7 = intensites["I7"]
            I8 = intensites["I8"]
            # ============================
            # Validation
            # ============================
            if not st.session_state.etape3_validee:
                etat_ok = False
                if st.session_state.partie_etape3 == 1:
                    etat_ok = (not st.session_state.S4 and st.session_state.S1 and st.session_state.S2 and st.session_state.S3)
                elif st.session_state.partie_etape3 == 2:
                    etat_ok = (not st.session_state.S3 and st.session_state.S1 and st.session_state.S2 and st.session_state.S4)
                elif st.session_state.partie_etape3 == 3:
                    etat_ok = (not st.session_state.S2 and st.session_state.S1 and st.session_state.S3 and st.session_state.S4)
                elif st.session_state.partie_etape3 == 4:
                    etat_ok = (not st.session_state.S1 and st.session_state.S2 and st.session_state.S3 and st.session_state.S4)
                if verifier_calculs:
                    if not etat_ok:
                        st.error("⚠️ L'interrupteur demandé n'est pas dans la bonne position.")
                        st.stop()
                    # correction
                    score_calculs = 0
                    erreurs = []
                    for nom in courants_a_trouver:
                        valeur = intensites[nom]
                        reponse = st.session_state.reponses_calculs.get(nom)

                        if reponse is None or reponse.strip() == "":
                            erreurs.append(nom)
                            continue

                        try:
                            reponse = float(reponse.replace(",", "."))
                        except:
                            erreurs.append(nom)
                            continue

                        if round(reponse, 2) == round(valeur, 2):
                            score_calculs += 1
                        else:
                            erreurs.append(nom)
                    st.session_state.score_calculs += score_calculs
                    st.session_state.erreurs_calculs = erreurs
                    st.session_state.etape3_validee = True
                    st.rerun()
            # ============================
            # Résultat Étape 3
            # ============================
            if st.session_state.etape3_validee:
                # Ligne 1 : score + erreurs
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.info(f"🎯 Score calculs : {st.session_state.score_calculs}/24")
                with col2:
                    nb_erreurs = len(st.session_state.erreurs_calculs)
                    if nb_erreurs == 0:
                        st.success("✅ 0 erreur")
                    else:
                        st.error(f"❌ {nb_erreurs} erreur(s)")
                with col3:
                        if nb_erreurs > 0:
                            st.write("Courants incorrects :",", ".join(st.session_state.erreurs_calculs))
                        else:
                            st.write("Tous les calculs sont corrects")
                # Ligne 2 : étape suivante + correction
                col_next, col_corr = st.columns([1, 3])
                with col_next:
                    if st.session_state.partie_etape3 < 4:
                        if st.button("➡️ Partie suivante"):
                            st.session_state.partie_etape3 += 1
                            st.session_state.etape3_validee = False
                            st.session_state.reponses_calculs = {}
                            st.session_state.version_partie += 1
                            st.rerun()

                    else:

                        if st.button("➡️ Résultat final"):
                            st.session_state.etape = 4
                            st.rerun()
                with col_corr:
                    with st.expander("✅ Voir la correction"):
                        colonnes = st.columns(len(courants_a_trouver))
                        for col, nom in zip(colonnes, courants_a_trouver):
                            with col:
                                st.markdown(f"**{nom} = {intensites[nom]:.2f} A**")
        # ==================================
        # RESULTAT FINAL
        # ==================================
        if st.session_state.etape == 4:
            score_sens = st.session_state.get("score_sens", 0)
            score_relations = st.session_state.get("score_relations", 0)
            score_calculs = st.session_state.get("score_calculs", 0)
            total = score_sens + score_relations + score_calculs
            total_max = 8 + 6 + 24
            Pourcentage = round(total * 100 / total_max, 1)
            col1, col2, col3 = st.columns(3)
            with col2:
                st.warning("🔒 Activité terminée.")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.success(f"✅ Score sens : {score_sens}/8")
            with col2:
                st.success(f"✅ Score relations : {score_relations}/6")
            with col3:
                st.success(f"✅ Score calculs : "f"{score_calculs}/24")
            col1, col2, col3 = st.columns(3)
            with col2:
                st.subheader("🏆 Résultat final")
            # ==================================
            # MESSAGE PEDAGOGIQUE
            # ==================================
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"✅ Score global : {Pourcentage}%")
            with col2:
                if Pourcentage >= 90:
                    st.success("🌟 Excellent travail !")
                    st.balloons()
                elif Pourcentage >= 75:
                    st.success("✅ Très bon travail.")
                elif Pourcentage >= 50:
                    st.warning("⚠️ Résultat satisfaisant.")
                else:
                    st.error("❌ Les lois des intensités ne sont pas encore acquises.")
            # ==================================
            # ENVOI DES RESULTATS
            # ==================================
            col1, col2, col3 = st.columns(3)
            with col1:
                nom_eleve = st.text_input("🧑 Nom et prénom de l'élève")
            with col3:
                if "resultat_envoye" not in st.session_state:
                    st.session_state.resultat_envoye = False
                if not st.session_state.resultat_envoye:
                    if st.button("📤 Envoyer mes résultats"):
                        if nom_eleve.strip() == "":
                            st.warning("⚠️ Saisissez votre nom et prénom.")
                        else:
                            enregistrer_resultat(nom_eleve,score_sens,score_relations,score_calculs,Pourcentage)
                            st.session_state.resultat_envoye = True
                            st.rerun()
                else:
                    st.success("✅ Résultats déjà envoyés au professeur.")
            # ==================================
            # NOUVEL ÉLÈVE
            # ==================================
            col1, col2, col3 = st.columns(3)

            with col2:
                if st.button("👨‍🎓 Nouvel élève", key="nouvel_eleve"):

                    nouvel_id = st.session_state.get("id_eleve", 0) + 1

                    st.session_state.clear()

                    st.session_state.id_eleve = nouvel_id
                    st.session_state.page = "cours"

                    st.rerun()
if __name__ == "__main__":
    afficher()