import streamlit as st
import matplotlib.pyplot as plt
import io

def draw_santa_matplotlib_fixed():
    """
    Rysuje prosty obraz Mikołaja za pomocą Matplotlib,
    używając bardziej stabilnych metod rysowania (fill).
    """
    
    # 1. Konfiguracja płótna
    # Używamy mniejszego figsize dla lepszego dopasowania
    fig, ax = plt.subplots(figsize=(4, 5)) 
    
    # Ustawienia tła i osi
    ax.set_facecolor('#B0E0E6')  # Jasnoniebieskie tło
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off') # Ukrywamy osie
    
    # --- Kolory ---
    RED = '#D93025'
    WHITE = '#FFFFFF'
    SKIN = '#F2C8AD'
    BLACK = '#000000'
    
    # --- Rysowanie Elementów ---

    # 2. Brody (Duży prostokąt, jako tło dla brody i tułowia)
    ax.fill([-1.0, 1.0, 1.0, -1.0], [-1.5, -1.5, 0.0, 0.0], color=WHITE)
    
    # 3. Twarz (Koło)
    # Tworzymy obiekt koła
    face = plt.Circle((0, 0.3), 0.4, color=SKIN)
    ax.add_artist(face)
    
    # 4. Kapelusz
    # Czerwony Kapelusz (Trójkąt)
    hat_x = [-0.6, 0.6, 0]
    hat_y = [0.65, 0.65, 1.4]
    ax.fill(hat_x, hat_y, color=RED)
    
    # Biały Brzeg Kapelusza (Prostokąt)
    ax.fill([-0.7, 0.7, 0.7, -0.7], [0.55, 0.55, 0.75, 0.75], color=WHITE)
    
    # Pompon (Małe koło)
    pom_pom = plt.Circle((0, 1.4), 0.1, color=WHITE, edgecolor=BLACK, linewidth=0.5)
    ax.add_artist(pom_pom)
    
    # 5. Oczy (Małe czarne koła)
    eye1 = plt.Circle((-0.15, 0.35), 0.05, color=BLACK)
    eye2 = plt.Circle((0.15, 0.35), 0.05, color=BLACK)
    ax.add_artist(eye1)
    ax.add_artist(eye2)
    
    # 6. Wąsy/Nos (Biały łuk na brodzie, symulujący wąsy/górną część brody)
    # Dodanie prostego owalu/koła na twarzy jako nos lub wąsy
    nose = plt.Circle((0, 0.2), 0.1, color=SKIN)
    ax.add_artist(nose)
    
    # Poprawienie kształtu brody/wąsów
    mustache = plt.Circle((0, 0.1), 0.45, color=WHITE, clip_box=ax.bbox)
    ax.add_artist(mustache)


    # Usunięcie zbędnych marginesów
    fig.tight_layout(pad=0) 
    
    return fig

# --- Interfejs Użytkownika Streamlit ---

st.title("🎅 Generator Mikołaja (Naprawiony Matplotlib)")
st.caption("Obraz Mikołaja generowany dynamicznie za pomocą Matplotlib w Streamlit.")

# Przycisk do generowania obrazu
if st.button("Wygeneruj Mikołaja"):
    
    # Generowanie obiektu Matplotlib Figure
    santa_figure = draw_santa_matplotlib_fixed()
    
    # Wyświetlanie obrazu w Streamlit
    st.pyplot(santa_figure)
    
    # Opcja pobrania obrazu
    buffer = io.BytesIO()
    # Zapisujemy figurę do bufora w formacie PNG
    santa_figure.savefig(buffer, format="png")
    
    st.download_button(
        label="Pobierz obraz jako PNG",
        data=buffer.getvalue(),
        file_name="mikolaj_matplotlib_poprawiony.png",
        mime="image/png"
    )
    
    # Zamknięcie figury, aby zwolnić pamięć i uniknąć ostrzeżeń Streamlit
    plt.close(santa_figure)
