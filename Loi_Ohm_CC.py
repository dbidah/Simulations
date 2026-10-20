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
        "gold")
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
            linewidth=2))
    bandes = [
        (c1, x + 0.3),
        (c2, x + 0.7),
        (c3, x + 1.1),
        (c4, x + 1.6)]
    for couleur, xpos in bandes:
        ax.add_patch(
            plt.Rectangle(
                (xpos, y - 0.25),
                0.08,
                0.5,
                color=couleur))
    ax.text(
        x + 1,
        y + 0.55,
        f"{nom}\n{valeur:.0f} Ω",
        ha="center",
        fontsize=10,
        fontweight="bold")
# ==================================
# Générateur CC
# ==================================
def dessiner_generateur(ax, x, y, U):
    cercle = plt.Circle(
        (x, y),
        0.7,
        fill=False,
        linewidth=2,
        color="blue")
    ax.add_patch(cercle)
    # Symbole G
    ax.text(
        x,
        y + 0.12,
        "G",
        fontsize=16,
        fontweight="bold",
        ha="center")
    # Tension
    ax.text(
        x,
        y - 0.30,
        f"{U:.1f} V",
        fontsize=9,
        color="blue",
        ha="center")
    # Bornes
    ax.text(
        x - 0.45,
        y,
        "+",
        fontsize=16,
        fontweight="bold",
        color="blue",
        ha="center",
        va="center")
    ax.text(
        x + 0.45,
        y,
        "-",
        fontsize=16,
        fontweight="bold",
        color="blue",
        ha="center",
        va="center")
# ==================================
# Ampèremètre
# ==================================
def dessiner_amperemetre(ax, x, y, I):
    cercle = plt.Circle(
        (x, y),
        0.45,
        facecolor=ax.get_facecolor(),   # masque le fil
        edgecolor="red",
        linewidth=2,
        color="red")
    ax.add_patch(cercle)
    ax.text(
        x,
        y + 0.05,
        "A",
        fontsize=12,
        fontweight="bold",
        ha="center")
    ax.text(
        x,
        y - 0.22,
        f"{I:.3f}",
        fontsize=8,
        color="red",
        ha="center")
# ==================================
# Voltmètre
# ==================================
def dessiner_voltmetre(ax, x, y, U):
    cercle = plt.Circle(
        (x, y),
        0.45,
        fill=False,
        linewidth=2,
        color="green")
    ax.add_patch(cercle)

    ax.text(
        x,
        y + 0.05,
        "V",
        fontsize=12,
        fontweight="bold",
        ha="center")
    ax.text(
        x,
        y - 0.22,
        f"{U:.2f}",
        fontsize=8,
        color="green",
        ha="center")
# ==================================
# Voltmètre branché aux bornes
# ==================================
def dessiner_voltmetre_resistance(ax, x_res, y_res, U):
    x_gauche = x_res
    x_droite = x_res + 2
    x_centre = x_res + 1
    y_volt = y_res - 0.9
    # Fils du voltmètre
    ax.plot(
        [x_gauche, x_gauche],
        [y_res, y_volt],
        color="green",
        linewidth=1.5)
    ax.plot(
        [x_droite, x_droite],
        [y_res, y_volt],
        color="green",
        linewidth=1.5)
    ax.plot(
        [x_gauche, x_centre - 0.45],
        [y_volt, y_volt],
        color="green",
        linewidth=1.5)
    ax.plot(
        [x_centre + 0.45, x_droite],
        [y_volt, y_volt],
        color="green",
        linewidth=1.5)
    # Voltmètre
    dessiner_voltmetre(
        ax,
        x_centre,
        y_volt,
        U)
# ==================================
# Flèche du courant
# ==================================
def dessiner_fleche_courant(ax, x1, y1, x2, y2):
    ax.arrow(
        x1,
        y1,
        x2 - x1,
        y2 - y1,
        length_includes_head=True,
        head_width=0.12,
        head_length=0.18,
        fc="red",
        ec="red",
        linewidth=2.5)
# ==================================
# Flèche de tension
# ==================================
def dessiner_fleche_tension(ax, x1, x2, y, nom):
    # ligne de tension
    ax.annotate(
        "",
        xy=(x2, y),
        xytext=(x1, y),
        arrowprops=dict(
            arrowstyle="<-",
            color="blue",
            lw=2))
    # nom de la tension
    ax.text(
        (x1 + x2) / 2,
        y + 0.15,
        nom,
        color="blue",
        fontsize=11,
        fontweight="bold",
        ha="center")
# ==================================
# Nom du courant
# ==================================
def dessiner_nom_courant(ax, x, y, nom):
    ax.text(
        x,
        y,
        nom,
        color="red",
        fontsize=11,
        fontweight="bold",
        ha="center")

# ==================================
# Schéma série
# ==================================
def dessiner_amperemetre(ax, x, y, I):
    # disque de fond pour masquer le fil
    fond = plt.Circle(
        (x, y),
        0.52,
        color="white",
        zorder=20)
    ax.add_patch(fond)
    # ampèremètre
    cercle = plt.Circle(
        (x, y),
        0.50,
        facecolor="white",
        edgecolor="red",
        linewidth=2,
        zorder=21)
    ax.add_patch(cercle)
    ax.text(
        x,
        y + 0.05,
        "A",
        fontsize=12,
        fontweight="bold",
        ha="center",
        zorder=22)
    ax.text(
        x,
        y - 0.22,
        f"{I:.3f}",
        fontsize=8,
        color="red",
        ha="center",
        zorder=22)
def schema_serie(R1, R2, R3,U,U1, U2, U3,It):
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.plot([0, 1], [0, 0], "k", linewidth=2)
    ax.plot([3, 4], [0, 0], "k", linewidth=2)
    ax.plot([6, 7], [0, 0], "k", linewidth=2)
    ax.plot([9, 10], [0, 0], "k", linewidth=2)
    dessiner_resistance(ax, 1, 0, R1, "R1")
    dessiner_resistance(ax, 4, 0, R2, "R2")
    dessiner_resistance(ax, 7, 0, R3, "R3")
    ax.plot([0, 0], [0, -2.2], "b")
    ax.plot([10, 10], [0, -2.2], "b")
    ax.plot([0, 4.3], [-2.2, -2.2], "b")
    ax.plot([5.7, 10], [-2.2, -2.2], "b")
    dessiner_generateur(ax, 5, -2.2, U)
    dessiner_voltmetre_resistance(ax, 1, 0, U1)
    dessiner_voltmetre_resistance(ax, 4, 0, U2)
    dessiner_voltmetre_resistance(ax, 7, 0, U3)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-3.5, 2)
    # Tension U1
    dessiner_fleche_tension(
    ax,
    1,
    3,
    1.2,
    "U1")
# Tension U2
    dessiner_fleche_tension(
    ax,
    4,
    6,
    1.2,
    "U2")
# Tension U3
    dessiner_fleche_tension(
    ax,
    7,
    9,
    1.2,
    "U3")
    dessiner_fleche_tension(
    ax,
    4.2,
    5.8,
    -3.4,
    "U")
    ax.axis("off")
    dessiner_amperemetre(ax, 7.2, -2.2, It)
# avant R1
    dessiner_fleche_courant(ax, 0.3, 0, 0.8, 0)
# entre R1 et R2
    dessiner_fleche_courant(ax, 3.2, 0, 3.7, 0)
# entre R2 et R3
    dessiner_fleche_courant(ax, 6.2, 0, 6.7, 0)
# après R3
    #dessiner_fleche_courant(ax, 9.2, 0, 9.7, 0)
# à gauche du générateur
    dessiner_fleche_courant(
    ax,
    4.0, -2.2,
    3.5, -2.2)
    dessiner_nom_courant(ax, 0.55, 0.35, "I1")
    dessiner_nom_courant(ax, 3.45, 0.35, "I2")
    dessiner_nom_courant(ax, 6.45, 0.35, "I3")
    dessiner_nom_courant(ax, 8.2, -1.9, "It")
    dessiner_nom_courant(ax, 3.5, -1.9, "It")
    return fig
# ==================================
# Schéma parallèle
# ==================================
def schema_parallele(R1, R2, R3,U,U1, U2, U3,I1, I2, I3,It):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot([0, 0], [0, 6], "k", linewidth=2)
    ax.plot([8, 8], [0, 6], "k", linewidth=2)
    # R1
    ax.plot([0, 3], [6, 6], "k", linewidth=2)
    ax.plot([5, 8], [6, 6], "k", linewidth=2)
    dessiner_resistance(
        ax,
        3,
        6,
        R1,
        "R1")
    # R2
    ax.plot([0, 3], [4, 4], "k", linewidth=2)
    ax.plot([5, 8], [4, 4], "k", linewidth=2)
    dessiner_resistance(
        ax,
        3,
        4,
        R2,
        "R2")
    # R3
    ax.plot([0, 3], [2, 2], "k", linewidth=2)
    ax.plot([5, 8], [2, 2], "k", linewidth=2)
    dessiner_resistance(
        ax,
        3,
        2,
        R3,
        "R3")
    ax.plot([0, 0], [0, 0], "b")
    ax.plot([8, 8], [0, 0], "b")
    ax.plot([0, 3.3], [0, 0], "b")
    ax.plot([4.7, 8], [0, 0], "b")
    dessiner_generateur(ax, 4, 0, U)
    dessiner_amperemetre(ax, 1.4, 6, I1)
    dessiner_amperemetre(ax, 1.4, 4, I2)
    dessiner_amperemetre(ax, 1.4, 2, I3)
    dessiner_voltmetre_resistance(ax, 3, 6, U1)
    dessiner_voltmetre_resistance(ax, 3, 4, U2)
    dessiner_voltmetre_resistance(ax, 3, 2, U3)
    dessiner_amperemetre(ax, -0.8, 3, It)
    ax.set_xlim(-1, 9)
    ax.set_ylim(-2, 6.5)
    ax.axis("off")
    return fig
# ==================================
# Montages mixtes
# ==================================
def schema_mixte1(R1, R2, R3):
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
    ax.set_xlim(-1, 9)
    ax.set_ylim(-2, 6)
    ax.axis("off")
    return fig
def schema_mixte2(R1, R2, R3):
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
    if "montage" not in st.session_state:
        st.session_state.montage = None

    if "calculer" not in st.session_state:
        st.session_state.calculer = False
    # ============================
    # Saisie des résistances
    # ============================
    st.subheader("Valeurs des résistances")
    col1, col2, col3 = st.columns(3)
    with col1:
        R1 = st.number_input(
        "R1 (Ω)",
        min_value=1.0,
        value=100.0)
    with col2:
        R2 = st.number_input(
        "R2 (Ω)",
        min_value=1.0,
        value=220.0)
    with col3:
        R3 = st.number_input(
        "R3 (Ω)",
        min_value=1.0,
        value=330.0)
    # ============================
    # Générateur CC
    # ============================
    st.subheader("Générateur de tension")
    U = st.slider(
    "Tension U (V)",
    min_value=1.0,
    max_value=30.0,
    value=12.0,
    step=0.5)
    # ============================
    # Choix du montage
    # ============================
    st.subheader("Dessiner un montage")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("Série"):
            st.session_state.montage = "Série"
            st.session_state.calculer = False
    with c2:
        if st.button("Parallèle"):
            st.session_state.montage = "Parallèle"
            st.session_state.calculer = False
    with c3:
        if st.button("(R1+R2)//R3"):
            st.session_state.montage = "(R1 + R2) // R3"
            st.session_state.calculer = False
    with c4:
        if st.button("(R1//R2)+R3"):
            st.session_state.montage = "(R1 // R2) + R3"
            st.session_state.calculer = False
    montage = st.session_state.montage
     # -----------------------------
    # Calculs
    # -----------------------------
    if montage is None:
        st.info("👆 Cliquer sur un montage pour vérifier")
        return
    if montage == "Série":
        Req = R1 + R2 + R3
        It = U / Req
        I1 = I2 = I3 = It
        U1 = I1 * R1
        U2 = I2 * R2
        U3 = I3 * R3
        fig = schema_serie(
            R1, R2, R3,
            U, U1, U2, U3, It)
    elif montage == "Parallèle":
        Req = 1 / (1/R1 + 1/R2 + 1/R3)
        I1 = U / R1
        I2 = U / R2
        I3 = U / R3
        It = I1 + I2 + I3
        U1 = U2 = U3 = U
        fig = schema_parallele(
            R1, R2, R3,
            U, U1, U2, U3,
            I1, I2, I3, It)
    elif montage == "(R1 + R2) // R3":
        R12 = R1 + R2
        Req = 1 / (1/R12 + 1/R3)
        It = U / Req
        I12 = U / R12
        I1 = I2 = I12
        I3 = U / R3
        U1 = I1 * R1
        U2 = I2 * R2
        U3 = U
        fig = schema_mixte1(
            R1, R2, R3)
    elif montage == "(R1 // R2) + R3":
        R12 = (R1 * R2) / (R1 + R2)
        Req = R12 + R3
        It = U / Req
        U3 = It * R3
        U12 = U - U3
        I1 = U12 / R1
        I2 = U12 / R2
        I3 = It
        U1 = U12
        U2 = U12
        fig = schema_mixte2(
            R1, R2, R3)
    st.pyplot(fig)
afficher()
