import streamlit as st
import pandas as pd

st.write('CMPD Traffic Stops')
st.write('Joe Burns was here!')

@st.cache_data  # 👈 Add the caching decorator
def load_data(csv):
    df = pd.read_csv(csv)
    return df


stops = load_data("data/Officer_Traffic_Stops.csv")

st.dataframe(stops)


# Joe was here sdfsd