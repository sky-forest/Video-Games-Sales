import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt

def app_2():
    df= pd.read_csv('Video_Games_Sales_new.csv', index_col= 0)
    st.dataframe(df)
    st.dataframe(df.describe())