import streamlit as st

def app_1():
    st.subheader('반갑습니다.')
    st.text('해당 자료는 1983년 부터 2012년 까지 출시된 비디오게임의 정보들입니다.')
    st.text('게임을 검색하고, 정보를 확인 할 수있습니다.')

    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFRhKo1StjpdtSIg0MheVyZWgq9mF1NNubNQ&usqp=CAU')
    st.image('http://cdn.gameple.co.kr/news/photo/202003/152649_157010_2449.jpg')

    st.info('자료 출처: https://www.kaggle.com/datasets/thedevastator/discovering-hidden-trends-in-global-video-games')