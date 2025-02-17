import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(
    page_title="SIMI-Tabellen ohne Tableview"
)

st.markdown("# SIMI-Tabellen ohne Tableview")

st.write(
    """Es wird geprüft, ob jede Tabelle in SIMI mit mindestens einer Tableview verknüpft ist."""
)

duckdb.sql("ATTACH IF NOT EXISTS 'https://sos-ch-dk-2.exo.io/ch.so.agi.betrieb.qm/qmbetrieb.duckdb' AS qmbetrieb (READ_ONLY);")

df = duckdb.sql("SELECT schema_name, table_name FROM qmbetrieb.main.simi_table_ohne_tableview ORDER BY schema_name, table_name;").df()

st.dataframe(
    df,
    column_config={
        "schema_name": "Schema",
        "table_name": "Tabelle"
    },
    hide_index=True,
    use_container_width=True
) 


