import streamlit as st

from services.auth_service import criar_usuario


def tela_cadastro():

    st.title("📝 Cadastro")

    nome = st.text_input("Nome")

    email = st.text_input("Email")

    tipo = st.selectbox(
        "Tipo",
        ["aluno", "professor"]
    )

    senha = st.text_input(
        "Senha",
        type="password"
    )

    confirmar = st.text_input(
        "Confirmar senha",
        type="password"
    )

    if st.button("Cadastrar"):

        if senha != confirmar:
            st.error("Senhas diferentes")
            return

        resultado = criar_usuario(
            nome,
            email,
            tipo,
            senha
        )

        if resultado == "ok":

            st.success("Conta criada!")

        else:
            st.error(resultado)
