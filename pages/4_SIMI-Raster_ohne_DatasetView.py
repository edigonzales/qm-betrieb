import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(
    page_title="SIMI-Raster ohne DatasetView"
)

st.markdown("# SIMI-Raster ohne DatasetView")

st.write(
    """Es wird geprüft, ob alle Rasterfiles in SIMI mit einer Raster-View verknpüft sind."""
)

duckdb.sql("ATTACH IF NOT EXISTS 'https://sos-ch-dk-2.exo.io/ch.so.agi.betrieb.qm/qmbetrieb.duckdb' AS qmbetrieb (READ_ONLY);")

df = duckdb.sql("SELECT raster_path, raster_ds_id FROM qmbetrieb.main.simi_raster_ohne_datasetview ORDER BY raster_path;").df()

st.dataframe(
    df,
    column_config={
        "raster_path": "Raster-Pfad"
    },
    hide_index=True,
    use_container_width=True
) 


