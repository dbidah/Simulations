import streamlit as st

from chute_libre import afficher as chute_libre
from calcul_req import afficher as calcul_req
from Loi_Ohm_CC import afficher as Loi_Ohm_CC
from Courant_electrique import afficher as Courant_electrique

# ==================================================
# CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Simulations Physique-Chimie",
    page_icon="🔬",
    layout="wide"
)

# ==================================================
# ACCUEIL
# ==================================================

st.title("🔬 Simulations Interactives de Physique-Chimie")

st.info(
    "Bienvenue sur cette plateforme dédiée à l'apprentissage de la Physique-Chimie par la simulation numérique."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Simulations disponibles", "4")

with col2:
    st.metric("Domaines", "Physique & Chimie")

with col3:
    st.metric("Version", "1.0")

st.markdown("---")

st.markdown("""
### 👨‍🏫 À propos

**Driss BIDAH**

Docteur en Chimie des Matériaux.

Ancien chercheur au Laboratoire de Chimie Industrielle de l'Université Jean Monnet de Saint-Étienne.

Auteur de six publications scientifiques internationales dans le domaine des formes galéniques et des systèmes de libération contrôlée des médicaments.

Passionné par l'enseignement des sciences, la modélisation numérique et la programmation Python appliquée à la Physique-Chimie.

Cette plateforme est le fruit d'une double expérience de chercheur et d'enseignant.
""")

st.markdown("---")

# ==================================================
# MENU LATERAL
# ==================================================

st.sidebar.title("🔬 Simulations Interactives")

matiere = st.sidebar.selectbox(
    "Discipline",
    [
        "Physique",
        "Chimie"
    ]
)

# ==================================================
# PHYSIQUE
# ==================================================

if matiere == "Physique":

    theme = st.sidebar.selectbox(
        "Thème",
        [
            "⚙️ Mécanique",
            "⚡ Électricité",
            "🔊 Acoustique",
            "🔭 Optique",
            "🌡️ Thermodynamique"
        ]
    )

    if theme == "⚙️ Mécanique":

        simulation = st.sidebar.radio(
            "Simulation",
            [
                "Choisir une simulation...",
                "🎯 Tir parabolique"
            ]
        )

    elif theme == "⚡ Électricité":

        simulation = st.sidebar.radio(
            "Simulation",
            [
                "Choisir une simulation...",
                "⚡ Calcul Req",
                "⚡ Loi d'Ohm en CC",
                "⚡ Courant électrique"
            ]
        )

    else:
        simulation = "Choisir une simulation..."

# ==================================================
# CHIMIE
# ==================================================

else:

    theme = st.sidebar.selectbox(
        "Thème",
        [
            "⚛️ Atomes",
            "🧪 Acides-Bases",
            "🔄 Oxydo-réduction"
        ]
    )

    simulation = "Choisir une simulation..."

# ==================================================
# LANCEMENT DES SIMULATIONS
# ==================================================

if simulation == "Choisir une simulation...":

    st.markdown("""
    ## 🚀 Démarrer une simulation

    Utilisez le menu de gauche pour sélectionner :

    - une discipline ;
    - un thème ;
    - une simulation.

    Les activités ont été conçues pour faciliter la compréhension des phénomènes physiques et chimiques grâce à l'expérimentation virtuelle.
    """)

elif simulation == "🎯 Tir parabolique":
    chute_libre()

elif simulation == "⚡ Calcul Req":
    calcul_req()

elif simulation == "⚡ Loi d'Ohm en CC":
    Loi_Ohm_CC()

elif simulation == "⚡ Courant électrique":
    Courant_electrique()