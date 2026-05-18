import streamlit as st


def navbar():

    st.sidebar.title("Sistema")

    pagina = st.sidebar.radio(
        "Menu",
        [
            "Home",
            "Desafios",
            "Mini Provas"
        ]
    )

    return pagina
