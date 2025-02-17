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

duckdb.sql("ATTACH IF NOT EXISTS 'https://sos-ch-dk-2.exo.io/ch.so.agi.betrieb.qm/qmbetrieb.duckdb' AS qmbetrieb (READ_ONLY);")

df = duckdb.sql("SELECT kennung FROM qmbetrieb.main.superflous_publication_formats ORDER BY kennung;").df()

st.dataframe(
    df,
    column_config={
        "kennung": "Kennung"
    },
    hide_index=True,
    use_container_width=True
) 


