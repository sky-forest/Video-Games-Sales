import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt

from app1 import app_1
from app2 import app_2


def main():
    st.title('비디오 게임')

    menu = ['app1', 'app2']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'app1':
        app_1()
    elif choice == 'app2' :
        app_2()


if __name__ == '__main__' :
    main()