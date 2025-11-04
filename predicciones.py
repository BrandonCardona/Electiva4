import streamlit as st
import numpy as np
import pandas as pd
import pickle

def mostrar_predicciones():
    st.title("🎯 Predicciones de Sostenibilidad del Emprendimiento")
    st.markdown(
        "Completa la siguiente encuesta para estimar el **nivel de sostenibilidad** de un emprendimiento. "
        "Responde cada ítem en una escala del **0 al 7** (0 = Muy Bajo, 7 = Muy Alto)."
    )

    # ======================================================
    # 🧩 1️⃣ Preguntas de la encuesta (variables más importantes)
    # ======================================================
    st.subheader("📝 Responde las siguientes preguntas:")
    opciones = list(range(0, 8))  # Escala 0–7

    liderazgo = st.selectbox("1️⃣ Nivel de liderazgo:", opciones)
    creatividad_originalidad = st.selectbox("2️⃣ Nivel de creatividad y originalidad:", opciones)
    resolucion_problemas = st.selectbox("3️⃣ Capacidad de resolución de problemas:", opciones)
    pensamiento_alto = st.selectbox("4️⃣ Nivel de pensamiento alto (crítico y reflexivo):", opciones)
    e_pasion = st.selectbox("5️⃣ Nivel de entusiasmo o pasión por el emprendimiento:", opciones)
    gestion_tiempo = st.selectbox("6️⃣ Nivel de gestión del tiempo:", opciones)
    pensamiento_analitico = st.selectbox("7️⃣ Capacidad de pensamiento analítico:", opciones)
    inteligencia_emoc = st.selectbox("8️⃣ Inteligencia emocional:", opciones)

    # ======================================================
    # 🧩 2️⃣ Crear DataFrame con respuestas
    # ======================================================
    input_data = np.array([
        liderazgo,
        creatividad_originalidad,
        resolucion_problemas,
        pensamiento_alto,
        e_pasion,
        gestion_tiempo,
        pensamiento_analitico,
        inteligencia_emoc
    ]).reshape(1, -1)

    df_input = pd.DataFrame(input_data, columns=[
        "liderazgo",
        "creatividad_originalidad",
        "resolucion_problemas",
        "pensamiento_alto",
        "e_pasion",
        "gestion_tiempo",
        "pensamiento_analitico",
        "inteligencia_emoc"
    ])

    st.markdown("📊 **Valores seleccionados:**")
    st.dataframe(df_input, hide_index=True)

    # ======================================================
    # 🧩 3️⃣ Normalizar los datos usando el scaler del pkl
    # ======================================================
    try:
        with open("models/modelos_y_metricas.pkl", "rb") as file:
            bundle = pickle.load(file)
            modelos = bundle["models"]
            metrics = bundle.get("metrics", {})
            scaler = bundle["scaler"]  # <- Usamos el scaler entrenado previamente

        # Transformar los datos del usuario con el scaler guardado
        df_scaled = pd.DataFrame(scaler.transform(df_input), columns=df_input.columns)

    except FileNotFoundError:
        st.error("⚠️ No se encontró el archivo `models/modelos_y_metricas.pkl`. Entrena los modelos primero o ajusta la ruta.")
        return
    except Exception as e:
        st.error(f"⚠️ Ocurrió un error al cargar el scaler: {e}")
        return

    # ======================================================
    # 🧩 4️⃣ Seleccionar el modelo
    # ======================================================
    st.subheader("⚙️ Selecciona el modelo para realizar la predicción:")
    modelo_elegido = st.selectbox("Modelo supervisado:", ["SVM", "NaiveBayes", "KNN"])

    # ======================================================
    # 🧩 5️⃣ Realizar predicción
    # ======================================================
    if st.button("🚀 Realizar Predicción"):
        model = modelos.get(modelo_elegido)
        if model is None:
            st.error("❌ El modelo seleccionado no se encuentra en el archivo `.pkl`.")
            return

        try:
            prediccion = model.predict(df_scaled)[0]

            # ======================================================
            # 🧩 6️⃣ Mostrar resultado
            # ======================================================
            st.success(f"✅ Resultado de la predicción con **{modelo_elegido}**: **{prediccion}**")

            if prediccion == 0:
                st.error("📉 El emprendimiento tiene **baja sostenibilidad**.")
            elif prediccion == 1:
                st.warning("📊 El emprendimiento tiene **sostenibilidad media**.")
            elif prediccion == 2:
                st.success("🚀 El emprendimiento tiene **alta sostenibilidad**.")

        except Exception as e:
            st.error(f"⚠️ Ocurrió un error al realizar la predicción: {e}")
