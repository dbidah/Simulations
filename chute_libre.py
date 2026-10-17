import streamlit as st
import numpy as np
import plotly.graph_objects as go


def afficher():

    st.title("🎯 Tir parabolique")

    # -----------------------
    # Choix de la planète
    # -----------------------

    planete = st.sidebar.selectbox(
        "🌍 Planète",
        ["Terre g = 9,81", "Lune g = 1,62", "Mars g = 3,71", "Jupiter g = 24,76"]
    )

    gravites = {
        "Terre": 9.81,
        "Lune": 1.62,
        "Mars": 3.71,
        "Jupiter": 24.79
    }

    g = gravites[planete]

    # -----------------------
    # Paramètres
    # -----------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        h0 = st.number_input(
            "H₀ (m)",
            value=10.0,
            min_value=0.0
        )

    with col2:
        v0 = st.number_input(
            "V₀ (m/s)",
            value=30.0,
            min_value=0.0
        )

    with col3:
        angle = st.number_input(
            "Angle (°)",
            value=45.0,
            min_value=0.0,
            max_value=90.0
        )

    # -----------------------
    # Calculs
    # -----------------------

    theta = np.radians(angle)

    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    delta = vy**2 + 2 * g * h0

    t_max = (vy + np.sqrt(delta)) / g

    t = np.linspace(0, t_max, 400)

    x = vx * t

    y = h0 + vy * t - 0.5 * g * t**2

    # -----------------------
    # Graphe interactif
    # -----------------------

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            customdata=t,
            mode="lines",
            line=dict(
                color="blue",
                width=4
            ),
            hovertemplate=
            "t = %{customdata:.2f} s<br>"
            "x = %{x:.2f} m<br>"
            "y = %{y:.2f} m"
            "<extra></extra>",
            name="Trajectoire"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[x[0]],
            y=[y[0]],
            mode="markers",
            marker=dict(
                size=15,
                color="red"
            ),
            name="Projectile"
        )
    )

    fig.update_layout(
        title=f"Tir parabolique sur {planete}",
        xaxis_title="Distance (m)",
        yaxis_title="Hauteur (m)",
        height=600,
        hovermode="closest",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info(
        "Déplacez la souris sur la trajectoire pour lire t, x et y."
    )
    
