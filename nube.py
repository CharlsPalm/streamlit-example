import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generar_nube(palabras):
    # Crear la nube de palabras
    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = None, 
                min_font_size = 10).generate(palabras)

    # Mostrar la imagen de la nube de palabras
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    st.pyplot(plt.gcf())  # Mostrar la figura en Streamlit

# Crear una caja de texto para la entrada del usuario
palabras = st.text_area('Ingresa tus palabras aquí')

# Si el usuario ha ingresado palabras, generar la nube de palabras
if palabras:
    generar_nube(palabras)

#palabras ITIL Cloud BD IA Framework metodología efectividad eficiencia usuarios valor clientes empresa sistema administración recursos expectativas necesidades requerimientos estrategia implementación ejecución servicios consumidores software hardware optimización digitalización automatización diseño operación mejora