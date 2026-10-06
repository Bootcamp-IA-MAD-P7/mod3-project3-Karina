import os
import streamlit as st
from dotenv import load_dotenv
from src.chains import build_chain
from srcprompts.content_prompt import PROMPTS

load_dotenv()

st.set_page_config(page_title="Generador de Contenido", page_icon="✍️", layout="centered")

with st.sidebar:
    st.header("⚙️ Configuración del modelo")
    provider = st.radio("Proveedor", ["Ollama (local)", "Groq (nube)"])

    if provider == "Ollama (local)":
        selected_provider = "ollama"
        model = st.selectbox("Modelo", ["llama3", "mistral", "gemma", "phi3"])
        st.info("Requiere Ollama corriendo localmente.")
    else:
        selected_provider = "groq"
        model = st.selectbox("Modelo", ["openai/gpt-oss-20b", "openai/gpt-oss-120b", "qwen/qwen3.8-27b", "allam-2-7b"])
        st.success("API Key cargada desde .env ✓")

st.title("✍️ Generador de Contenido con IA")
st.markdown("Genera contenido personalizado usando un modelo de lenguaje.")

with st.form("content_form"):
    content_type = st.selectbox("Tipo de contenido", list(PROMPTS.keys()))
    topic = st.text_input("Tema", placeholder="Ej: beneficios del ejercicio en la mañana")
    tone = st.selectbox("Tono", ["Profesional", "Casual", "Motivacional", "Informativo", "Humorístico"])
    length = st.selectbox("Longitud", ["Corto (100-200 palabras)", "Medio (300-500 palabras)", "Largo (600+ palabras)"])
    submitted = st.form_submit_button("Generar contenido")

if submitted:
    if not topic.strip():
        st.warning("Por favor ingresa un tema.")
    elif selected_provider == "groq" and not os.getenv("GROQ_API_KEY"):
        st.error("No se encontró GROQ_API_KEY en el archivo .env")
    else:
        template, input_variables = PROMPTS[content_type]
        chain = build_chain(prompt_template=template, input_variables=input_variables, provider=selected_provider, model=model)
        inputs = {"topic": topic, "tone": tone, "length": length}
        st.subheader("Resultado")
        output = st.write_stream(chain.stream(inputs))
        st.download_button("Descargar contenido", data=output, file_name="contenido.txt", mime="text/plain")
