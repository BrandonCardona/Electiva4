import streamlit as st
import pickle

def mostrar_entrenamiento():
    # 🌟 Título principal
    st.title("🤖 Entrenamiento de Modelo")

    # 🧩 Primera imagen — Método del Codo (Sebastian Raschka)
    st.subheader("📉 Análisis del número óptimo de Clusters")
    st.image(
        "imagenes/img1.png",
        caption="Figura 1. Método del Codo para determinar el número óptimo de clusters. Fuente: Adaptado de Sebastian Raschka.",
        width=800
    )

    st.info(
        "💡 Con base en este resultado, el modelo K-Means se entrenó utilizando **3 clusters**, "
        "correspondientes a emprendimientos con bajo, medio y alto sostenimiento."
    )

    # 🧩 Segunda imagen — Método del Codo (Indraneel Dutta Baruah)
    st.subheader("📊 Evaluación del número óptimo de Clusters con KElbowVisualizer")
    st.image(
        "imagenes/img2.png",
        caption="Figura 2. Visualización del Método del Codo utilizando el KElbowVisualizer. Fuente: Adaptado de Indraneel Dutta Baruah.",
        width=800
    )

    st.success(
        "✅ Ambos métodos confirman que el número óptimo de clusters para este modelo es **3**, "
        "lo que refuerza la validez del resultado obtenido en el proceso de entrenamiento."
    )

    # 🧩 Tercera imagen — Importancia de las variables
    st.subheader("📈 Principales Variables que Influyen en la Sostenibilidad del Emprendimiento")
    st.image(
        "imagenes/img3.png",
        caption="Figura 3. Top 8 variables con mayor importancia en el modelo. Fuente: Elaboración propia a partir del análisis de características del dataset.",
        width=800
    )

    st.info(
        "📊 Este gráfico muestra las **8 variables más influyentes** en la determinación de la sostenibilidad de los emprendimientos. "
        "Estas características fueron clave para el entrenamiento del modelo y ayudan a comprender los factores que más afectan el desempeño emprendedor."
    )

    # 🧩 Cuarta imagen — Matriz de correlación
    st.subheader("🔍 Análisis de Correlación entre Variables Seleccionadas")
    st.image(
        "imagenes/img4.png",
        caption="Figura 4. Matriz de correlación de las variables empleadas en el modelo. Fuente: Elaboración propia.",
        width=1000
    )

    st.info(
        "📘 Esta matriz de correlación permite observar **cómo se relacionan entre sí las variables** empleadas en el modelo. "
        "Las tonalidades más intensas indican una relación más fuerte (positiva o negativa), lo que ayuda a identificar posibles redundancias o dependencias entre características."
    )

    # 🧩 Quinta imagen — Dispersión con las 2 variables más importantes
    st.subheader("🌌 Distribución de los Emprendimientos según las Variables más Relevantes")
    st.image(
        "imagenes/img5.png",
        caption="Figura 5. Dispersión de los datos en función de las dos variables más importantes del modelo. Fuente: Elaboración propia.",
        width=800
    )

    st.info(
        "🧭 Este gráfico permite visualizar **cómo se distribuyen los emprendimientos** según las dos variables más influyentes detectadas en el análisis. "
        "Cada punto representa un emprendimiento, y su posición refleja su desempeño en esas dos dimensiones clave."
    )

    # ============================================================
    # 🔽 NUEVA SECCIÓN: MODELOS SUPERVISADOS
    # ============================================================
    st.header("🧠 Modelos Supervisados")

    # Intentar cargar el archivo PKL con métricas
    try:
        with open("models/modelos_y_metricas.pkl", "rb") as file:
            bundle = pickle.load(file)
            metrics = bundle["metrics"]
    except Exception as e:
        st.error(f"⚠️ No se pudo cargar el archivo 'modelos_y_metricas.pkl': {e}")
        return

    # ==================== 🔹 SVM ==================== #
    st.subheader("📘 Modelo SVM (Máquinas de Vectores de Soporte)")
    st.image(
        "imagenes/SVM.png",
        caption="Figura 6. Clasificación con el modelo SVM. Fuente: Elaboración propia.",
        width=800
    )

    svm_metrics = metrics.get("SVM", {})
    st.write("**Métricas del modelo SVM:**")
    st.table({
        "Métrica": ["Accuracy", "Recall", "F1-Score"],
        "Valor": [
            round(svm_metrics.get("Accuracy", 0), 3),
            round(svm_metrics.get("Recall", 0), 3),
            round(svm_metrics.get("F1-Score", 0), 3)
        ]
    })

    st.info(
        "💬 El modelo **SVM** mostró una buena capacidad de clasificación lineal, "
        "identificando correctamente los emprendimientos en función de las variables analizadas."
    )

    # ==================== 🔹 Naive Bayes ==================== #
    st.subheader("📙 Modelo Naive Bayes")
    st.image(
        "imagenes/NB.png",
        caption="Figura 7. Resultados del modelo Naive Bayes. Fuente: Elaboración propia.",
        width=800
    )

    nb_metrics = metrics.get("NaiveBayes", {})
    st.write("**Métricas del modelo Naive Bayes:**")
    st.table({
        "Métrica": ["Accuracy", "Recall", "F1-Score"],
        "Valor": [
            round(nb_metrics.get("Accuracy", 0), 3),
            round(nb_metrics.get("Recall", 0), 3),
            round(nb_metrics.get("F1-Score", 0), 3)
        ]
    })

    st.info(
        "📊 El modelo **Naive Bayes** resultó eficiente para datos con distribuciones simples, "
        "aunque su desempeño fue ligeramente inferior al de los otros modelos."
    )

    # ==================== 🔹 KNN ==================== #
    st.subheader("📗 Modelo K-Nearest Neighbors (KNN)")
    st.image(
        "imagenes/KNN.png",
        caption="Figura 8. Clasificación con el modelo KNN. Fuente: Elaboración propia.",
        width=800
    )

    knn_metrics = metrics.get("KNN", {})
    st.write("**Métricas del modelo KNN:**")
    st.table({
        "Métrica": ["Accuracy", "Recall", "F1-Score"],
        "Valor": [
            round(knn_metrics.get("Accuracy", 0), 3),
            round(knn_metrics.get("Recall", 0), 3),
            round(knn_metrics.get("F1-Score", 0), 3)
        ]
    })

    st.info(
        "📈 El modelo **KNN** demostró una sólida capacidad predictiva, "
        "especialmente en la clasificación de emprendimientos con características similares."
    )
