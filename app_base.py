import streamlit as st

from app_main import app_1
from app_list import app_2
from app_search import app_3
from app_chart import app_4


def main():
    st.title('Global Video Games')

    menu = ['메인화면', '표 데이터', '게임 검색', '데이터 확인']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == '메인화면':
        app_1()
    elif choice == '표 데이터' :
        app_2()
    elif choice == '게임 검색' :
        app_3()
    elif choice == '데이터 확인' :
        app_4()


if __name__ == '__main__' :
    main()