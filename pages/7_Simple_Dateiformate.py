import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(
    page_title="Simple Dateiformate"
)

st.markdown("# Simple Dateiformate")

st.write(
    """Es werden für "simple" Themenpublikationen die Dateiformate pro Thema (inkl. Anzahl) aufgelistet."""
)

df = duckdb.sql("SELECT kennung, xtf, gpkg, shp, dxf FROM qmbetrieb.main.count_simple_publication_formats ORDER BY kennung;").df()

st.dataframe(
    df,
    column_config={
        "kennung": "Kennung"
    },
    hide_index=True,
    use_container_width=True
) 


