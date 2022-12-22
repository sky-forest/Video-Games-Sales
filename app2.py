import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt

def app_2():

    df= pd.read_csv('Video_Games_Sales_new.csv')

    st.subheader('전체 데이터')

    st.dataframe(df)

    st.info('Rank 열은 해당 게임의 전세계 판매량 순위를 나타낸것입니다.')
    st.info('North America~Global 열은 해당 국가에서 팔린 양을 뜻하며, 단위는 백만입니다.')
    st.info('Review 열은 해당 게임의 리뷰 점수를 뜻합니다.')