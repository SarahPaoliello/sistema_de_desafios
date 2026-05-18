import streamlit as st

from services.auth_service import criar_usuario


def tela_cadastro():

    st.title("Cadastro")

    nome = st.text_input(
        "Nome",
        key="cad_nome"
    )

    email = st.text_input(
        "Email",
        key="cad_email"
    )

    tipo = st.selectbox(
        "Tipo",
        ["aluno", "professor"],
        key="cad_tipo"
    )

    senha = st.text_input(
        "Senha",
        type="password",
        key="cad_senha"
    )

    confirmar = st.text_input(
        "Confirmar senha",
        type="password",
        key="cad_confirmar"
    )

    if st.button(
        "Cadastrar",
        key="btn_cadastro"
    ):

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
