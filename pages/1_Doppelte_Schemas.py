import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(
    page_title="Doppelte Schemas"
)

st.markdown("# Doppelte Schemas")

st.write(
    """Es wird geprüft, ob es in der Edit- oder Pub-DB doppelte Schemas hat. Doppelt im Sinn von versioniert und die ältere Version ist noch vorhanden."""
)

duckdb.sql("ATTACH IF NOT EXISTS 'https://sos-ch-dk-2.exo.io/ch.so.agi.betrieb.qm/qmbetrieb.duckdb' AS qmbetrieb (READ_ONLY);")

df = duckdb.sql("SELECT schema_stamm, version_anzahl, datenbank FROM qmbetrieb.main.geo_doppelte_schemas").df()

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


