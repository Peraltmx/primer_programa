import streamlit as st
import pandas as pd

# Inicializar almacenamiento de datos
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=['Fecha', 'Despachos', 'Planta', 'Planificados', 'Despachados', 'Cumplimiento (%)'])

st.title("Gestión de Despachos")

# Formulario de entrada de datos
with st.form("entry_form"):
    fecha = st.date_input("Fecha")
    despachos = st.text_input("Despachos")
    planta = st.selectbox("Planta", ["Celulosa", "MDF", "Aserradero", "CLB"])
    planificados = st.number_input("Planificados", min_value=0, step=1)
    despachados = st.number_input("Despachados", min_value=0, step=1)
    submitted = st.form_submit_button("Agregar")

# Procesar el formulario
if submitted:
    cumplimiento = (despachados / planificados * 100) if planificados > 0 else 0
    nuevo_registro = {
        'Fecha': fecha,
        'Despachos': despachos,
        'Planta': planta,
        'Planificados': planificados,
        'Despachados': despachados,
        'Cumplimiento (%)': round(cumplimiento, 2)
    }
    st.session_state['data'] = st.session_state['data'].append(nuevo_registro, ignore_index=True)
    st.success("Datos agregados exitosamente!")

# Mostrar tabla de datos
data = st.session_state['data']
if not data.empty:
    orden = st.selectbox("Ordenar por", ["Fecha", "Planta", "Cumplimiento (%)"], index=0)
    data = data.sort_values(by=orden)
    st.dataframe(data)
