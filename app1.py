import streamlit as st

def app_1():
    st.subheader('반갑습니다.')
    st.text('해당 자료는 1983년 부터 2012년 까지 출시된 비디오게임의 데이터들입니다.')
    st.text('원하는 게임을 검색하거나, 두 게임을 비교분석 할 수있습니다.')

    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFRhKo1StjpdtSIg0MheVyZWgq9mF1NNubNQ&usqp=CAU')
    st.image('https://storage.googleapis.com/kaggle-datasets-images/2699607/4643723/850b03586df0489cd97b7c1d5cd93258/dataset-cover.png?t=2022-12-03-11-22-57')

    st.info('자료 출처: https://www.kaggle.com/datasets/thedevastator/discovering-hidden-trends-in-global-video-games')