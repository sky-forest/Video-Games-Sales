import streamlit as st
import pandas as pd



def app_3():


    st.image('https://previews.123rf.com/images/abluecup/abluecup1308/abluecup130800096/21301083-%EA%B2%8C%EC%9E%84-%ED%8C%A8%EB%93%9C-%EB%8F%8B%EB%B3%B4%EA%B8%B0-%EA%B2%8C%EC%9E%84-%ED%94%8C%EB%A0%88%EC%9D%B4.jpg')

    df= pd.read_csv('Video_Games_Sales_new2.csv', index_col=0)


    if st.checkbox('게임 제목으로 검색하기'):

        game_name= st.text_input('게임 제목을 입력하세요.')
    
        if len(game_name) == 0:
            pass

        elif (df['게임 제목'].str.contains(game_name, case= False) == False).all():
            st.error('그런 이름의 게임이 존재하지 않습니다!')

        elif (df['게임 제목'].str.contains(game_name, case= False) == True).any():
            st.dataframe(df[df['게임 제목'].str.contains(game_name, case= False)])



    if st.checkbox('조건에 맞는 게임 검색하기'):
        
        # platform_list= df['플랫폼'].sort_values(ascending= True).unique()
        # platform= st.selectbox('플랫폼을 선택하세요.', platform_list)

        # year_list= df['출시연도'].sort_values(ascending= True).unique()
        # year= st.selectbox('출시연도를 선택하세요.', year_list)

        platform_list= ['모든 플랫폼', '3DS', 'DC', 'DS', 'GB', 'GBA', 'GC', 'GEN', 'N64', 'NES', 'PC', 'PS', 'PS2', 'PS3', 'PSP', 'PSV', 'SAT', 'SCD', 'SNES', 'Wii', 'WiiU', 'X360', 'XB']
        platform= st.selectbox('플랫폼을 선택하세요.', platform_list)
        if platform == '모든 플랫폼':
            platform= df['플랫폼']

        year_list= ['모든연도', 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]
        year= st.selectbox('출시연도를 선택하세요.', year_list)
        if year == '모든연도':
            year= df['출시연도']

        select_list2= ['모든 장르', '격투', '레이싱', '롤플레잉', '슈팅', '스포츠', '시뮬레이션', '액션', '어드밴처', '전략', '퍼즐', '플랫포머', '기타 등등...']
        genre =st.selectbox('장르를 선택하세요.', select_list2)

        if genre == '모든 장르':
            genre= df['장르']
        
        elif genre == '격투':
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

            
        user_select= df[(df['플랫폼'] == platform) & (df['출시연도'] == year) & (df['장르'] == genre)]

        if len(user_select) == False:
            st.error('조건을 만족하는 게임이 없습니다!')

        else:
            st.dataframe(user_select)
