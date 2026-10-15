import streamlit as st
import matplotlib.pyplot as plt

# ==================================
# Codes couleurs
# ==================================

couleurs = {
    0: "black",
    1: "brown", 
    
    2: "red",
    3: "orange",
    4: "yellow",
    5: "green",
    6: "blue",
    7: "violet",
    8: "grey",
    9: "white"
}


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

    return (
        couleurs[d1],
        couleurs[d2],
        couleurs[mult],
        "gold"
    )


# ==================================
# Dessin résistance
# ==================================

def dessiner_resistance(ax, x, y, valeur, nom):

    c1, c2, c3, c4 = code_couleur(valeur)

    ax.add_patch(
        plt.Rectangle(
            (x, y - 0.25),
            2,
            0.5,
            facecolor="#F5DEB3",
            edgecolor="black",
            linewidth=2
        )
    )

    bandes = [
        (c1, x + 0.3),
        (c2, x + 0.7),
        (c3, x + 1.1),
        (c4, x + 1.6)
    ]

    for couleur, xpos in bandes:

        ax.add_patch(
            plt.Rectangle(
                (xpos, y - 0.25),
                0.08,
                0.5,
                color=couleur
            )
        )

    ax.text(
        x + 1,
        y + 0.55,
        f"{nom}\n{valeur:.0f} Ω",
        ha="center",
        fontsize=10,
        fontweight="bold"
    )


# ==================================
# Dessin ohmmètre
# ==================================

def dessiner_ohmmetre(ax, x, y, Req):

    cercle = plt.Circle(
        (x, y),
        0.7,
        fill=False,
        linewidth=2,
        color="blue"
    )

    ax.add_patch(cercle)

    ax.text(
        x,
        y + 0.2,
        "Ω",
        fontsize=18,
        fontweight="bold",
        ha="center"
    )

    ax.text(
        x,
        y - 0.25,
        f"{Req:.2f}",
        fontsize=9,
        color="red",
        ha="center"
    )


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

    dessiner_ohmmetre(
        ax,
        5,
        -1,
        Req
    )

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

    ax.plot([0, 2], [5, 5], "k", linewidth=2)
    ax.plot([4, 8], [5, 5], "k", linewidth=2)

    dessiner_resistance(
        ax,
        2,
        5,
        R1,
        "R1"
    )

    # R2

    ax.plot([0, 2], [3, 3], "k", linewidth=2)
    ax.plot([4, 8], [3, 3], "k", linewidth=2)

    dessiner_resistance(
        ax,
        2,
        3,
        R2,
        "R2"
    )

    # R3

    ax.plot([0, 2], [1, 1], "k", linewidth=2)
    ax.plot([4, 8], [1, 1], "k", linewidth=2)

    dessiner_resistance(
        ax,
        2,
        1,
        R3,
        "R3"
    )

    # Connexion ohmmètre

    ax.plot([0, 0], [0, -1], "b")
    ax.plot([8, 8], [0, -1], "b")

    ax.plot([0, 3.3], [-1, -1], "b")
    ax.plot([4.7, 8], [-1, -1], "b")

    dessiner_ohmmetre(
        ax,
        4,
        -1,
        Req
    )

    ax.set_xlim(-1, 9)
    ax.set_ylim(-2, 6.5)

    ax.axis("off")

    return fig

def schema_mixte1(R1, R2, R3, Req):

    fig, ax = plt.subplots(figsize=(12, 6))

    # Branche supérieure
    ax.plot([0, 1], [4, 4], "k", lw=2)

    dessiner_resistance(ax, 1, 4, R1, "R1")

    ax.plot([3, 4], [4, 4], "k", lw=2)

    dessiner_resistance(ax, 4, 4, R2, "R2")

    ax.plot([6, 8], [4, 4], "k", lw=2)

    # Branche inférieure
    ax.plot([0, 1], [1, 1], "k", lw=2)

    dessiner_resistance(ax, 1, 1, R3, "R3")

    ax.plot([3, 8], [1, 1], "k", lw=2)

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

    # Branche haute
    dessiner_resistance(ax, 1, 3, R1, "R1")
    ax.plot([3, 5], [3, 3], "k", lw=2)

    # Branche basse
    dessiner_resistance(ax, 1, 1, R2, "R2")
    ax.plot([3, 5], [1, 1], "k", lw=2)

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
def schema_mixte3(R1, R2, R3, Req):

    fig, ax = plt.subplots(figsize=(12, 6))

    # Entrée
    ax.plot([0, 1], [2, 2], "k", lw=2)

    # R1
    dessiner_resistance(ax, 1, 2, R1, "R1")

    ax.plot([3, 4], [2, 2], "k", lw=2)

    # Noeud gauche du parallèle
    ax.plot([4, 4], [1, 3], "k", lw=2)

    # Branche haute : R2
    dessiner_resistance(ax, 4, 3, R2, "R2")
    ax.plot([6, 8], [3, 3], "k", lw=2)

    # Branche basse : R3
    dessiner_resistance(ax, 4, 1, R3, "R3")
    ax.plot([6, 8], [1, 1], "k", lw=2)

    # Noeud droit du parallèle
    ax.plot([8, 8], [1, 3], "k", lw=2)

    # Sortie
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

    montage = st.selectbox(
        "Type de montage",
        [
            "Série","Parallèle","(R1 + R2) // R3","(R1 // R2) + R3","R1 + (R2 // R3)"
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        R1 = st.number_input(
            "R1 (Ω)",
            min_value=1.0,
            value=100.0
        )

    with col2:
        R2 = st.number_input(
            "R2 (Ω)",
            min_value=1.0,
            value=220.0
        )

    with col3:
        R3 = st.number_input(
            "R3 (Ω)",
            min_value=1.0,
            value=330.0
        )

    if montage == "Série":
        Req = R1 + R2 + R3
        fig = schema_serie(R1, R2, R3, Req)

    elif montage == "Parallèle":
        Req = 1 / (1/R1 + 1/R2 + 1/R3)
        fig = schema_parallele(R1, R2, R3, Req)

    elif montage == "(R1 + R2) // R3":
        Req = 1 / (1/(R1 + R2) + 1/R3)
        fig = schema_mixte1(R1, R2, R3, Req)

    elif montage == "(R1 // R2) + R3":
        Req = (R1 * R2)/(R1 + R2) + R3
        fig = schema_mixte2(R1, R2, R3, Req)

    elif montage == "R1 + (R2 // R3)":
        Req = R1 + (R2 * R3)/(R2 + R3)
        fig = schema_mixte3(R1, R2, R3, Req)



    st.pyplot(fig)
