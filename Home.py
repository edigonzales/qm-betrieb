import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(
    page_title="QM Betrieb",
    #page_icon="👋",
)

st.title('QM Datenmanagement')

duckdb.sql("DETACH DATABASE IF EXISTS qmbetrieb;")
duckdb.sql("ATTACH IF NOT EXISTS 'https://sos-ch-dk-2.exo.io/ch.so.agi.betrieb.qm/qmbetrieb.duckdb' AS qmbetrieb (READ_ONLY);")
