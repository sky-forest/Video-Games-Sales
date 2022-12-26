import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib import rcParams

rcParams['font.family'] = 'Malgun Gothic'


def app_4():

    df= pd.read_csv('Video_Games_Sales_new2.csv', index_col=0)

    st.image('https://img.freepik.com/premium-photo/top-view-a-gaming-gear_160097-847.jpg?w=2000')

    
    if st.checkbox('수치 데이터 별로 정보 확인하기'):
    

        column_list1 = df.columns[1:5]

        selected_list1 = st.selectbox('확인할 정보를 선택하세요.', column_list1)

        df2= df.groupby(selected_list1).count()

        flg1= px.pie(df2, values= df2['게임 제목'], names= df2.index)
        st.plotly_chart(flg1)


    if st.checkbox('수치 데이터 상관관계 확인하기'):

        column_list2= df.columns[5:]

        selected_list2 = st.multiselect('상관관계를 확인할 정보를 선택하세요.', column_list2)

        
        if len(selected_list2) >= 2 :

            df_corr = df[selected_list2].corr()

            fig = plt.figure()
            sb.heatmap(data= df_corr, annot=True, fmt='.2f', cmap='coolwarm', vmin= -1, vmax= 1, linewidths=0.5)
            st.pyplot(fig)