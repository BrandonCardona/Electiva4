import streamlit as st
import os
from PIL import Image

def mostrar_portada():

    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💡Emprendimiento Juvenil💡</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align: center; font-size: 18px; color: #ccc;">
        Análisis de la sostenibilidad de los <b>emprendimientos juveniles en Medellín</b>  
        utilizando <b>técnicas de machine learning no supervisado</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # ✅ Cargar imagen del logo usando ruta absoluta
    ruta_logo = os.path.join(os.path.dirname(__file__), "Logo", "logo.jpeg")

    try:
        logo = Image.open(ruta_logo)
        st.image(logo, use_container_width=False, width=900)
    except FileNotFoundError:
        st.error(f"⚠️ No se encontró el logo en la ruta: {ruta_logo}")

    # Sección descriptiva
    st.markdown(
        """
        ### 🌆 Descripción del proyecto
        Este proyecto busca comprender y evaluar los factores que influyen en la **sostenibilidad de los emprendimientos juveniles** 
        en la ciudad de **Medellín**, a partir del análisis de diferentes variables socioeconómicas, ambientales y de gestión.  
        A través de un enfoque de **clustering con K-Means**, se agrupan los emprendimientos según su nivel de desarrollo y permanencia 
        en el tiempo, facilitando la **identificación de patrones comunes** y posibles **oportunidades de mejora**.
        """
    )

    # Objetivo general
    st.markdown("### 🎯 Objetivo General")
    st.info(
        "Determinar la sostenibilidad de los emprendimientos juveniles en Medellín mediante técnicas de análisis de datos y clustering, "
        "para identificar factores clave que inciden en su éxito o permanencia."
    )

    # Objetivos específicos
    st.markdown("### 📘 Objetivos Específicos")
    st.markdown(
        """
        - Analizar las principales variables asociadas al emprendimiento juvenil en Medellín.  
        - Aplicar técnicas de **escalado y agrupamiento (K-Means)** para clasificar los emprendimientos según su sostenibilidad.    
        - Entrenar un modelo predictivo que permita anticipar la sostenibilidad de nuevos emprendimientos basados en sus características iniciales.  
        """
    )

    # Frase final
    st.markdown(
        """
        <div style="text-align:center; font-style:italic; color:#9E9E9E; margin-top: 30px;">
        “Impulsando el futuro emprendedor de Medellín a través de los datos.”
        </div>
        """,
        unsafe_allow_html=True
    )
