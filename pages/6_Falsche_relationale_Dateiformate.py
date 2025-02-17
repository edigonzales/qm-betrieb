import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(
    page_title="Falsche relationale Dateiformate"
)

st.markdown("# Falsche relationale Dateiformate")

st.write(
    """Es wird geprüft, ob bei relationalen Themenpublikationen falsche Dateiformate vorhanden sind."""
)

df = duckdb.sql("SELECT kennung FROM qmbetrieb.main.superflous_publication_formats ORDER BY kennung;").df()

st.dataframe(
    df,
    column_config={
        "kennung": "Kennung"
    },
    hide_index=True,
    use_container_width=True
) 


