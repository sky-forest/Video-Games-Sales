import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt

def app_1():
    st.subheader('반갑습니다.')
    st.text('해당 자료는 1983 ~ 2012 출시된 비디오게임의 데이터로 이루어졌습니다.')
    st.text('원하는 게임을 검색하거나, 두 게임을 비교분석 할 수있습니다.')

    st.image('https://storage.googleapis.com/kaggle-datasets-images/2699607/4643723/850b03586df0489cd97b7c1d5cd93258/dataset-cover.png?t=2022-12-03-11-22-57')