import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt

def app_3():

    df= pd.read_csv('Video_Games_Sales_new.csv')

    st.subheader('게임 검색하기')

    game_name= st.text_input('찾는 게임의 이름을 입력하세요.')
        if (df2['Game Title'].str.contains('wii', case= False) == True).any():
        st.dataframe(df2[df2['Game Title'].str.contains('wii', case= False)])

    