import streamlit as st
import requests

# Configuración
BACKEND_URL = "https://chatbot-backend-y8bz.onrender.com"  # URL de Render

st.title("Administra el conocimiento de tu Chatbot")

st.subheader("Sube un PDF")
pdf = st.file_uploader("Selecciona un PDF para alimentar el chatbot", type=["pdf"])

st.subheader("Agrega una URL")
url = st.text_input("Pega una URL para extraer conocimiento")

st.subheader("Agrega texto puro")
raw_text = st.text_area("Escribe o pega texto para alimentar el chatbot")

if st.button("Enviar PDF") and pdf:
    with st.spinner("Procesando PDF..."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/upload",
                files={"file": pdf},
                timeout=60
            )
            if response.status_code == 200:
                st.success("¡PDF procesado correctamente!")
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Fallo al conectar con el backend: {str(e)}")

if st.button("Enviar URL") and url:
    with st.spinner("Procesando URL..."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/upload",
                json={"url": url},
                timeout=60
            )
            if response.status_code == 200:
                st.success("¡URL procesada correctamente!")
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Fallo al conectar con el backend: {str(e)}")

if st.button("Enviar texto puro") and raw_text.strip():
    with st.spinner("Procesando texto..."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/upload",
                json={"text": raw_text},
                timeout=60
            )
            if response.status_code == 200:
                st.success("¡Texto procesado correctamente!")
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Fallo al conectar con el backend: {str(e)}")

# Puedes agregar aquí la configuración de colores, logo, etc. en el futuro.