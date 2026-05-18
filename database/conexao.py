from supabase import create_client
import streamlit as st

try:

    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]

    st.write("URL:", url)

    supabase = create_client(url, key)

    teste = (
        supabase
        .table("usuarios")
        .select("*")
        .limit(1)
        .execute()
    )

    st.success("Supabase conectado!")

except Exception as e:

    st.error("ERRO NA CONEXÃO")
    st.exception(e)
