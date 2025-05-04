import streamlit as st
from openai_helper import get_detailed_response

st.set_page_config(page_title="RADIA +", page_icon=":hospital:", layout="centered")

# Imagen superior (RADIA logo)
st.image("RADIA IMAGEN.WEBP", width=220)

st.title("RADIA + – Asistente virtual en radioterapia")
st.subheader("Servicio de Oncología Radioterápica · H.U. Arnau de Vilanova – Lleida")
st.markdown("---")

class RADIAChatbot:
    def __init__(self):
        self.categories = {
            "Inicio del tratamiento": {
                "¿Cuándo empezaré el tratamiento?": "Tras el estudio de planificación, te llamaremos para darte la fecha de inicio.",
                "¿Por qué tarda en empezar el tratamiento después de la primera consulta?": "La planificación precisa y los cálculos para tu seguridad requieren varios días."
            },
            "Durante el tratamiento": {
                "¿Duele recibir radioterapia?": "No, la radioterapia es indolora.",
                "¿Cuánto dura cada sesión?": "Cada sesión dura entre 10 y 30 minutos en total.",
                "¿Qué ropa debo usar para venir a la radioterapia?": "Usa ropa cómoda, holgada y preferiblemente de algodón."
            },
            "Efectos secundarios": {
                "¿Voy a perder el pelo con la radioterapia?": "Solo si la zona tratada es el cuero cabelludo.",
                "¿Cómo puedo aliviar la irritación en la piel?": "Usa cremas recomendadas y evita el sol en la zona tratada."
            },
            "Vida diaria y transporte": {
                "¿Podré seguir trabajando durante el tratamiento?": "Sí, si te sientes con energía suficiente.",
                "¿Voy a ser radiactivo después del tratamiento?": "No, puedes convivir con normalidad.",
                "¿Cómo llego al hospital si tengo dificultades de movilidad?": "Consulta si puedes acceder a transporte sanitario."
            },
            "Sexualidad y fertilidad": {
                "¿Puedo mantener relaciones sexuales durante el tratamiento?": "Sí, salvo molestias en caso de radioterapia pélvica.",
                "¿La radioterapia afecta la fertilidad?": "Puede afectar si el tratamiento es en la zona pélvica."
            }
        }

    def get_response(self, category, question):
        return self.categories.get(category, {}).get(question, "Lo siento, no encuentro respuesta para esa pregunta.")

radia = RADIAChatbot()

st.write("Selecciona una categoría y una pregunta para obtener una respuesta clara.")

category = st.selectbox("Categoría", list(radia.categories.keys()))
question = st.selectbox("Pregunta", list(radia.categories[category].keys()))
response = radia.get_response(category, question)

st.success(f"💬 {response}")

if st.button("Ampliar información sobre este tema con IA"):
    with st.spinner("Consultando..."):
        detailed = get_detailed_response(question)
        st.info(f"{detailed}

🧠 *Esta respuesta ha sido generada por un modelo de inteligencia artificial y no representa necesariamente la opinión del Servicio de Oncología Radioterápica.*")

st.markdown("---")
st.caption("RADIA + © 2025 · Hospital Universitari Arnau de Vilanova – Lleida")
