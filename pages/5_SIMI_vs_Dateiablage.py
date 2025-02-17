import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(
    page_title="SIMI vs Dateiablage"
)

st.markdown("# SIMI vs Dateiablage")

st.write(
    """Es wird geprüft, ob die Themen auf der Dateiablage (files.geo.so.ch) mit den Themenpublikationen in SIMI übereinstimmen."""
)

duckdb.sql("ATTACH IF NOT EXISTS 'https://sos-ch-dk-2.exo.io/ch.so.agi.betrieb.qm/qmbetrieb.duckdb' AS qmbetrieb (READ_ONLY);")

df = duckdb.sql("SELECT kennung, kategorie FROM qmbetrieb.main.diff_kennung_simi_datenabgabe ORDER BY kennung, kategorie;").df()

st.dataframe(
    df,
    column_config={
        "kennung": "Kennung",
        "kategorie": "Kategorie"
    },
    hide_index=True,
    use_container_width=True
) 


