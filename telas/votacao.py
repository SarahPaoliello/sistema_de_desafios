import streamlit as st

from services.voto_service import votar


def tela_votacao():

    desafio = st.session_state.desafio

    st.title("Votação")

    st.subheader(desafio["titulo"])

    voto = st.radio(
        "Escolha",
        ["Bom", "Regular", "Ruim"]
    )

    participante_id = 1

    if st.button("Enviar voto"):

        resultado = votar(
            st.session_state.usuario["id"],
            participante_id,
            voto
        )

        if resultado == "ok":

            st.success("Voto registrado")

        else:
            st.warning(resultado)
