import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt

def app_3():

    df= pd.read_csv('Video_Games_Sales_new.csv')

    column_list = df.columns

    selected_list1 = st.selectbox('확인할 데이터를 선택하세요.', column_list)

    flg1= px.pie(df, values= df.groupby('Year').count(), names= df.index)
    st.plotly_chart(flg1)
    