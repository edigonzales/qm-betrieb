import streamlit as st
import duckdb
import pandas as pd

st.title('Hallo Welt')

#duckdb.sql("SELECT 42").show()

duckdb.sql("ATTACH IF NOT EXISTS 'https://sos-ch-dk-2.exo.io/ch.so.agi.fubar1/qmbetrieb.duckdb' AS qmbetrieb (READ_ONLY);")

df = duckdb.sql("SELECT schema_stamm, version_anzahl, datenbank FROM qmbetrieb.main.geo_doppelte_schemas").df()

#print(df)

st.dataframe(
    df,
    column_config={
        "schema_stamm": "Schema-Stamm",
        "version_anzahl": "Anzahl Versionen",
        "datenbank": "Datenbank"
    },
    hide_index=True,
    use_container_width=True
) 