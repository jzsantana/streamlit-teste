import streamlit as st
import pandas as pd


st.set_page_config(page_title="Streamlit")


with st.container():
    st.subheader("My first website with Streamlit")
    st.title("Contracts Dashboard")


# essa decoration serve para armazenar os dados no cache do navegador
# assim, ele nao vai ficar fazendo varias requisições na api por exemplo
@st.cache_data
def load_data():
    table = pd.read_csv("../data/resultados.csv")
    return table


with st.container():
    st.write("---")
    qtd_dias = st.selectbox("Selecione o periodo", ["12M", "3M"])
    num_dias = int(qtd_dias.replace("M", ""))
    dados = load_data()
    dados = dados[-num_dias:]
    
    st.area_chart(dados, x="Data", y="Contratos")

