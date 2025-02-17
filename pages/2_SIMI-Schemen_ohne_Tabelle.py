import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(
    page_title="SIMI-Schemen ohne Tabelle"
)

st.markdown("# SIMI-Schemen ohne Tabelle")

st.write(
    """Es wird geprüft, ob jedes Schema in SIMI mit mindestens einer Tabelle verknüpft ist."""
)

duckdb.sql("ATTACH IF NOT EXISTS 'https://sos-ch-dk-2.exo.io/ch.so.agi.betrieb.qm/qmbetrieb.duckdb' AS qmbetrieb (READ_ONLY);")

df = duckdb.sql("SELECT schema_name, identifier FROM qmbetrieb.main.simi_schema_ohne_tabelle ORDER BY schema_name, identifier;").df()

st.dataframe(
    df,
    column_config={
        "schema_name": "Schema",
        "identifier": "Datenbank"
    },
    hide_index=True,
    use_container_width=True
) 


