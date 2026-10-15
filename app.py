import streamlit as st

from chute_libre import afficher as chute_libre
from calcul_req import afficher as calcul_req


st.set_page_config(
    page_title="Simulations Physique-Chimie",
    page_icon="🔬",
    layout="wide"
)

# ==========================
# Navigation
# ==========================

st.sidebar.title("📚 Navigation")

page = st.sidebar.radio(
    "Choisissez une simulation",
    [
        "🏠 Accueil",
        "🎯 Tir parabolique",
        "⚡ Calcul Req"
    ]
)

# ==========================
# ACCUEIL
# ==========================

if page == "🏠 Accueil":

    st.title("🔬 Simulations Interactives de Physique-Chimie")

    st.info(
        "Une plateforme dédiée à la compréhension des phénomènes physiques et chimiques grâce à la simulation numérique."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Simulations disponibles", "2")
    col2.metric("Domaines", "Physique & Chimie")
    col3.metric("Version", "1.0")

    st.markdown("---")

    st.header("👨‍🏫 À propos")

    st.markdown("""
**Driss BIDAH**

Docteur en chimie des matériaux.

Ancien chercheur au laboratoire de chimie industrielle de l'Université Jean Monnet à Saint-Étienne et Professeur en BTS Métiers de l'eau et Systèmes constructifs Bois Habitats.

Auteur de cinq publications scientifiques internationales dans le domaine des formes galéniques et des systèmes de libération contrôlée des médicaments.

Passionné par l'enseignement des sciences, la modélisation numérique et la programmation Python appliquée à la Physique-Chimie.

Cette plateforme est le fruit d'une double expérience de chercheur et d'enseignant, avec pour objectif de rendre les phénomènes scientifiques plus accessibles grâce à l'expérimentation virtuelle.
""")

    st.markdown("---")

    st.header("🎯 Objectifs de la plateforme")

    st.markdown("""
- Visualiser les phénomènes physiques et chimiques.
- Comprendre l'influence des paramètres expérimentaux.
- Vérifier les lois étudiées en classe.
- Favoriser l'apprentissage par l'investigation.
- Développer l'autonomie des élèves.
- Compléter les expériences réalisées en laboratoire.
""")

    st.markdown("---")

    st.header("⚛️ Simulations de Physique")

    st.markdown("""
- 🎯 Tir parabolique
- 🪂 Chute libre
- 🪐 Pendule simple
- ⚡ Loi d'Ohm
- 🔋 Circuits électriques
- ⚙️ Associations de résistances
- 🌈 Optique géométrique
- 🔊 Acoustique
- 🌡️ Thermodynamique
""")

    st.markdown("---")

    st.header("🧪 Simulations de Chimie")

    st.markdown("""
- 🧫 Cinétique chimique
- 🧪 Calcul du pH
- ⚗️ Dosages acide-base
- 🔋 Oxydo-réduction
- 🌡️ Thermochimie
- ⚛️ Équilibres chimiques
- 💊 Libération contrôlée des médicaments
""")

    st.markdown("---")

    st.header("🛠️ Technologies utilisées")

    st.markdown("""
- Python
- Streamlit
- NumPy
- Matplotlib
- Plotly
""")

    st.markdown("---")

    st.success(
        "Cette plateforme est en développement continu. De nouvelles simulations seront régulièrement ajoutées."
    )

    st.markdown("---")

    st.caption(
        "© Driss BIDAH - Plateforme de simulations interactives en Physique-Chimie"
    )

# ==========================
# TIR PARABOLIQUE
# ==========================

elif page == "🎯 Tir parabolique":

    chute_libre()

# ==========================
# CALCUL REQ
# ==========================

elif page == "⚡ Calcul Req":

    calcul_req()
