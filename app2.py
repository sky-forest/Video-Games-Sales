import streamlit as st
import numpy as np
import pandas as pd

def app_2():

    df= pd.read_csv('Video_Games_Sales_new.csv')


    if st.checkbox('전체 데이터 확인하기'):
    
        st.dataframe(df)

        if st.checkbox('컬럼 설명 확인하기'):

            st.text('Rank: 전세계 판매량 순위')
            st.text('Game Title: 게임 제목')
            st.text('Platform: 실행시킬 수 있는 플랫폼')
            st.text('Year: 출시 년도')
            st.text('Genre: 장르')
            st.text('Publisher: 배급사')
            st.text('North America: 북미 판매량(단위: 백만)')
            st.text('Europe: 유럽 판매량(단위: 백만)')
            st.text('Japan: 일본 판매량(단위: 백만)')
            st.text('Rest of World: 그 외 국가 판매량 총합(단위: 백만)')
            st.text('Global: 전세계 판매량(단위: 백만)')
            st.text('Review: 리뷰 점수')


    st.image('http://cdn.gameple.co.kr/news/photo/202003/152649_157010_2449.jpg')


    if st.checkbox('게임 이름으로 검색하기'):

        game_name= st.text_input('게임 이름을 입력하세요.')
    
        if len(game_name) == 0:
            pass

        elif (df['Game Title'].str.contains(game_name, case= False) == False).all():
            st.error('그런 이름의 게임이 존재하지 않습니다!')

        elif (df['Game Title'].str.contains(game_name, case= False) == True).any():
            st.dataframe(df[df['Game Title'].str.contains(game_name, case= False)])



    if st.checkbox('조건에 맞는 게임 검색하기'):
        
        platform_list= df['Platform'].sort_values(ascending= True).unique()
        platform= st.selectbox('플랫폼을 선택하세요.', platform_list)

        year_list= df['Year'].sort_values(ascending= True).unique()
        year= st.selectbox('출시연도를 선택하세요.', year_list)

        select_list= ['격투', '레이싱', '롤플레잉', '슈팅', '스포츠', '시뮬레이션', '액션', '어드밴처', '전략', '퍼즐', '플랫포머', '기타 등등...']
        genre =st.selectbox('장르를 선택하세요.', select_list)

        if genre == '격투':
            genre= 'Fighting'

        elif  genre == '레이싱':
            genre= 'Racing'

        elif genre == '롤플레잉':
            genre= 'Role-Playing'

        elif genre == '슈팅':
            genre= 'Shooter'

        elif genre == '스포츠':
            genre= 'Sports'

        elif genre == '시뮬레이션':
            genre= 'Simulation'

        elif genre == '액션':
            genre= 'Action'

        elif genre == '어드밴처':
            genre= 'Adventure'

        elif genre == '전략':
            genre= 'Strategy'

        elif genre == '퍼즐':
            genre= 'Puzzle'

        elif genre == '플랫포머':
            genre= 'Platform'
        
        elif genre == '기타 등등...':
            genre= 'Misc'   
            
        user_select= df[(df['Platform'] == platform) & (df['Year'] == year) & (df['Genre'] == genre)]

        if len(user_select) == False:
            st.error('조건을 만족하는 게임이 없습니다!')

        else:
            st.dataframe(user_select)

        


        