import json
import time
import requests
import streamlit as st
import pandas as pd

st.header("Show data index price")
df = pd.read_csv("./data/stock_index_price.csv")
st.write(df.head(10))

st.header("Show Chart index price")
st.line_chart(
   df, x="stock_index_price", y=["interest_rate", "unemployment_rate"], color=["#FF0000", "#0000FF"]  # Optional
)

