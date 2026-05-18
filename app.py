import streamlit as st

from telas.login import tela_login
from telas.cadastro import tela_cadastro
from telas.home import tela_home
from telas.desafios import tela_desafios
from telas.votacao import tela_votacao
from telas.mini_provas import tela_mini_provas

from components.navbar import navbar


st.set_page_config(
    page_title="Sistema de Desafios",
    layout="centered"
)

# SESSION

if "usuario" not in st.session_state:
    st.session_state.usuario = None

if "pagina" not in st.session_state:
    st.session_state.pagina = "home"

if "desafio" not in st.session_state:
    st.session_state.desafio = None

# LOGIN

if not st.session_state.usuario:

    aba1, aba2 = st.tabs([
        "Login",
        "Cadastro"
    ])

    with aba1:
        tela_login()

    with aba2:
        tela_cadastro()

else:

    usuario = st.session_state.usuario

    st.sidebar.success(
        f"{usuario['nome']}"
    )

    if st.sidebar.button("Sair"):

        st.session_state.usuario = None

        st.rerun()

    menu = navbar()

    if menu == "Home":
        tela_home()

    elif menu == "Desafios":
        tela_desafios()

    elif menu == "Mini Provas":
        tela_mini_provas()

    if st.session_state.pagina == "votacao":
        tela_votacao()
