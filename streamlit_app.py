import streamlit as st
import json
import os

st.set_page_config(page_title=" FTDStudio | Mi Índice de Proyectos", layout="wide")

st.title("📂 Mi Portafolio de Proyectos")
st.write("Explora mis últimos experimentos. Contacto a anotami@gmail.com ")

# Función para cargar los proyectos desde el JSON
def cargar_proyectos():
    if os.path.exists('projects.json'):
        with open('projects.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

proyectos = cargar_proyectos()

# Mostrar proyectos en una cuadrícula
if proyectos:
    # Definimos cuántas columnas queremos (por ejemplo, 3)
    cols = st.columns(3)
    
    for i, p in enumerate(proyectos):
        with cols[i % 3]:
            # Mostrar la imagen del proyecto
            if os.path.exists(p["imagen"]):
                st.image(p["imagen"], use_container_width=True)
            else:
                # Imagen por defecto si no encuentra la ruta
                st.warning("Imagen no encontrada")
            
            st.subheader(p["titulo"])
            st.caption(f"Categoría: {p['tag']}")
            st.write(p["descripcion"])
            st.link_button("Ver Proyecto", p["link"])
            st.container(height=20, border=False) # Espaciador
else:
    st.info("Aún no hay proyectos registrados en projects.json")
