import streamlit as st
import pandas as pd

def app_2():

    st.image('https://storage.googleapis.com/kaggle-datasets-images/2699607/4643723/850b03586df0489cd97b7c1d5cd93258/dataset-cover.png?t=2022-12-03-11-22-57')
    
    
    df= pd.read_csv('Video_Games_Sales_new2.csv', index_col=0)


    if st.checkbox('전체 정보 확인하기'):
    
        st.dataframe(df)



    if st.checkbox('수치 데이터별 상위 10개 게임 확인하기'):

        select_list1= df.columns[5:]

        user_select= st.selectbox('항목을 선택해주세요', select_list1)
        
        st.dataframe(df.sort_values(user_select, ascending= False).head(10))
    
