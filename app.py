import streamlit as st
from chute_libre import afficher as chute_libre
from calcul_req import afficher as calcul_req

st.set_page_config(page_title="Simulations Physique-Chimie",page_icon="🔬",layout="wide")
# ==========================
# Navigation
# ==========================
st.sidebar.title("📚 Navigation")
page = st.sidebar.radio("",["👨‍🏫 Parcours & Travaux","🔬 Simulations"])
# ==========================
# ACCUEIL
# ==========================
# ==========================
# PARCOURS & TRAVAUX
# ==========================
if page == "👨‍🏫 Parcours & Travaux":
    st.title("🔬 Simulations Interactives de Physique-Chimie")
    st.info("Une plateforme dédiée à la compréhension des phénomènes physiques et chimiques grâce à la simulation numérique.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Simulations disponibles", "2")
    col2.metric("Domaines", "Physique & Chimie")
    col3.metric("Version", "1.0")
    st.markdown("---")
    st.header("👨‍🏫 À propos")
    st.markdown("""
**Driss BIDAH**
Docteur en chimie des matériaux.
Ancien chercheur au laboratoire de chimie industrielle de l'Université Jean Monnet à Saint-Étienne.
Auteur de six publications scientifiques internationales dans le domaine des formes galéniques et des systèmes de libération contrôlée des médicaments.
Passionné par l'enseignement des sciences, la modélisation numérique et la programmation Python appliquée à la Physique-Chimie.
Cette plateforme est le fruit d'une double expérience de chercheur et d'enseignant.
""")
    st.page_link("pages/Publications.py",label=" Publications scientifiques",icon="📚")
# ==========================
# SIMULATIONS
# ==========================
elif page == "🔬 Simulations":
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔬 Choisissez une simulation")
    simulation = st.sidebar.radio("",["Choisir une simulation...","🎯 Tir parabolique","⚡ Calcul Req"])
    if simulation == "Choisir une simulation...":
        st.title("🔬 Simulations pédagogiques")
        st.info("Sélectionnez une simulation dans le menu de gauche.")
    elif simulation == "🎯 Tir parabolique":
        chute_libre()
    elif simulation == "⚡ Calcul Req":
        calcul_req()

