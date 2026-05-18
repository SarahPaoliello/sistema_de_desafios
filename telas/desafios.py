import streamlit as st

from services.desafio_service import listar_desafios


def tela_desafios():

    st.title("📋 Desafios")

    desafios = listar_desafios()

    if not desafios:

        st.info("Nenhum desafio disponível")

        return

    for d in desafios:

        with st.container(border=True):

            st.subheader(d["titulo"])

            st.write(d["descricao"])

            st.caption(f"Status: {d['status']}")

            if st.button(
                "Acessar",
                key=d["id"]
            ):

                st.session_state.desafio = d
                st.session_state.pagina = "votacao"

                st.rerun()
