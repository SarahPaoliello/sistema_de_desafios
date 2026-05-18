import streamlit as st

from services.auth_service import login


def tela_login():

    st.title("Login")

    email = st.text_input(
        "Email",
        key="login_email"
    )

    senha = st.text_input(
        "Senha",
        type="password",
        key="login_senha"
    )

    if st.button(
        "Entrar",
        key="btn_login"
    ):

        usuario = login(email, senha)

        if usuario:

            st.session_state.usuario = usuario

            st.success("Login realizado!")

            st.rerun()

        else:
            st.error("Credenciais inválidas")
