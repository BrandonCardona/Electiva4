import streamlit as st
from portada import mostrar_portada
from entrenamiento import mostrar_entrenamiento
from predicciones import mostrar_predicciones

# Configuración de la página
st.set_page_config(page_title="Emprendimiento Juvenil", page_icon="💡", layout="wide")

# Variable de sesión para sección
if "seccion" not in st.session_state:
    st.session_state.seccion = "Portada"

# Lista de secciones y emojis
secciones = [
    ("💡 Portada", "Portada"),
    ("🤖 Entrenamiento", "Entrenamiento de Modelo"),
    ("🎯 Predicciones", "Predicciones")
]

# --- Menú lateral como radio group ---
opcion = st.sidebar.radio(
    "📂 Menú Principal",
    options=[valor for nombre, valor in secciones],
    format_func=lambda x: next(nombre for nombre, valor in secciones if valor == x)
)

st.session_state.seccion = opcion

# --- Mostrar la sección seleccionada ---
if st.session_state.seccion == "Portada":
    mostrar_portada()
elif st.session_state.seccion == "Entrenamiento de Modelo":
    mostrar_entrenamiento()
elif st.session_state.seccion == "Predicciones":
    mostrar_predicciones()
