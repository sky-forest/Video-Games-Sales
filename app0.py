import streamlit as st

from app1 import app_1
from app2 import app_2
from app3 import app_3


def main():
    st.title('Global Video Games List')

    menu = ['app1', 'app2', 'app3']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'app1':
        app_1()
    elif choice == 'app2' :
        app_2()
    elif choice == 'app3' :
        app_3()


if __name__ == '__main__' :
    main()