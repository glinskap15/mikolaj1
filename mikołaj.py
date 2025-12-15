import streamlit as st
import matplotlib.pyplot as plt
import io

def draw_santa_matplotlib_full_costume():
    """
    Rysuje obraz Mikołaja z pełnym kostiumem (kurtka, pas, broda) 
    za pomocą Matplotlib.
    """
    
    # 1. Konfiguracja płótna
    # Zwiększamy rozmiar Y, aby zmieścić cały tułów
    fig, ax = plt.subplots(figsize=(4, 6)) 
    
    # Ustawienia tła i osi
    ax.set_facecolor('#B0E0E6')  # Jasnoniebieskie tło
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-2.0, 1.5)  # Większy zakres Y
    ax.set_aspect('equal')
    ax.axis('off')
    
    # --- Kolory ---
    RED = '#D93025'
    WHITE = '#FFFFFF'
    SKIN = '#F2C8AD'
    BLACK = '#000000'
    GOLD = '#FFD700'
    
    # --- Rysowanie Elementów ---
    
    # 2. Kurtka (Główny Korpus, Czerwony Prostokąt)
    # Rysujemy poniżej linii talii (y=0.0)
    ax.fill([-1.0, 1.0, 1.0, -1.0], [0.0, 0.0, -2.0, -2.0], color=RED, zorder=1) 
    
    # 3. Pas (Czarny Prostokąt)
    ax.fill([-1.2, 1.2, 0.4, 0.4], [0.1, 0.1, -0.3, -0.3], color=BLACK, zorder=2) # Czarny pasek
    
    # Klamra Paska (Złoty/Żółty Kwadrat)
    ax.fill([-0.25, 0.25, 0.25, -0.25], [0.0, 0.0, -0.2, -0.2], color=GOLD, zorder=3)
    
    # 4. Brody (Duży biały kształt, który zachodzi na kurtkę i twarz)
    # Biała broda (duże koło/owal, który maskuje część kurtki)
    beard_oval = plt.Circle((0, -0.2), 0.9, color=WHITE, zorder=4)
    ax.add_artist(beard_oval)
    
    # 5. Twarz (Koło)
    face = plt.Circle((0, 0.3), 0.4, color=SKIN, zorder=5)
    ax.add_artist(face)
    
    # 6. Kapelusz
    # Czerwony Kapelusz (Trójkąt)
    hat_x = [-0.6, 0.6, 0]
    hat_y = [0.65, 0.65, 1.4]
    ax.fill(hat_x, hat_y, color=RED, zorder=6)
    
    # Biały Brzeg Kapelusza (Prostokąt)
    ax.fill([-0.7, 0.7, 0.7, -0.7], [0.55, 0.55, 0.75, 0.75], color=WHITE, zorder=7)
    
    # Pompon (Małe koło)
    pom_pom = plt.Circle((0, 1.4), 0.1, color=WHITE, edgecolor=BLACK, linewidth=0.5, zorder=8)
    ax.add_artist(pom_pom)
    
    # 7. Oczy i Nos
    eye1 = plt.Circle((-0.15, 0.35), 0.05, color=BLACK, zorder=9)
    eye2 = plt.Circle((0.15, 0.35), 0.05, color=BLACK, zorder=9)
    ax.add_artist(eye1)
    ax.add_artist(eye2)
    
    # Nos (małe koło na twarzy)
    nose = plt.Circle((0, 0.2), 0.1, color=SKIN, zorder=10)
    ax.add_artist(nose)
    
    # 8. Biała Krawędź Kurtki (Pionowy Biały Pasek)
