import streamlit as st
from streamlit_js_eval import streamlit_js_eval, get_geolocation

st.title("📍 Localização do Usuário (via GPS do Celular)")

# Obtém localização com precisão, se o navegador permitir
location = get_geolocation()

if location:
    st.success("Localização detectada com sucesso!")
    st.write("🔵 Latitude:", location["coords"]["latitude"])
    st.write("🔴 Longitude:", location["coords"]["longitude"])
    st.write("📶 Precisão (em metros):", location["coords"]["accuracy"])
    st.write("📍 Fonte de dados:", "Possivelmente GPS se a precisão for < 10 metros")
else:
    st.warning("Aguardando permissão para acessar a localização...")
