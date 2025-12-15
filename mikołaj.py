import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import io

# --- 1. FUNKCJA RYSOWANIA MIKOŁAJA (Z kształtów) ---

def draw_santa(ax, center_x, center_y, scale, color_hat, color_beard, color_skin, color_coat):
    """
    Rysuje Mikołaja jako zbiór kształtów Matplotlib.
    :param ax: Obiekt Axes Matplotlib do rysowania.
    :param center_x, center_y: Centralna pozycja Mikołaja.
    :param scale: Współczynnik skalowania.
    :param color_*: Kolory elementów.
    """
    
    # --- Wymiary i Kolory ---
    RED = color_hat
    WHITE = color_beard
    SKIN = color_skin
    COAT = color_coat
    BLACK = '#000000'
    GOLD = '#FFD700'

    # Wymiary skalowane
    R_FACE = 0.4 * scale
    R_POMPOM = 0.1 * scale
    H_HAT = 1.0 * scale
    W_COAT = 1.0 * scale
    H_COAT = 1.2 * scale
    
    # --- Rysowanie Elementów (Zorder zapewnia poprawne warstwy) ---
    
    # 1. Tułów (Płaszcz) - zorder=1
    ax.fill([center_x - W_COAT/2, center_x + W_COAT/2, center_x + W_COAT/2, center_x - W_COAT/2],
            [center_y - H_COAT, center_y - H_COAT, center_y, center_y],
            color=COAT, zorder=1)

    # 2. Broda (Duży Biały Owal/Kształt) - zorder=2
    # Używamy elipsy dla lepszego kształtu brody
    beard = plt.Circle((center_x, center_y - R_FACE/2), R_FACE * 1.5, color=WHITE, zorder=2)
    ax.add_artist(beard)

    # 3. Twarz (Koło) - zorder=3
    face = plt.Circle((center_x, center_y + R_FACE), R_FACE, color=SKIN, zorder=3)
    ax.add_artist(face)

    # 4. Kapelusz (Trójkąt) - zorder=4
    ax.fill([center_x - R_FACE, center_x + R_FACE, center_x],
            [center_y + R_FACE*2, center_y + R_FACE*2, center_y + R_FACE*2 + H_HAT],
            color=RED, zorder=4)

    # 5. Biały Brzeg Kapelusza (Pasek) - zorder=5
    ax.fill([center_x - R_FACE*1.1, center_x + R_FACE*1.1, center_x + R_FACE*1.1, center_x - R_FACE*1.1],
            [center_y + R_FACE*1.8, center_y + R_FACE*1.8, center_y + R_FACE*2.2, center_y + R_FACE*2.2],
            color=WHITE, zorder=5)

    # 6. Pompon (Małe Koło) - zorder=6
    pom_pom = plt.Circle((center_x, center_y + R_FACE*2 + H_HAT), R_POMPOM, color=WHITE, edgecolor=BLACK, linewidth=0.5, zorder=6)
    ax.add_artist(pom_pom)

    # 7. Pas (Czarny Prostokąt) - zorder=7
    ax.fill([center_x - W_COAT/2 - 0.1, center_x + W_COAT/2 + 0.1, center_x + W_COAT/2 + 0.1, center_x - W_COAT/2 - 0.1]
