## Overview

1. Kaggle 에서 Discovering Hidden Trends in Global Video Games 데이터를 가져왔습니다.

2. 코드 작성 및 보는 사람의 편의성을 위해 jupyter notebook 을 사용하여 컬럼의 이름을 한글로 rename 하였습니다.

3. 컬럼명을 수정한 데이터 프레임을 csv 파일로 새로 저장하였습니다.

4. 수정한 csv 파일을 jupyter notebook 에서 분석했습니다.

5. 분석한 자료를 가지고 visual studio code 에서 코드 작성을하였습니다.

6. visual studio code 를 AWS의 EC2 서버에 연결시킨 후 streamlit 웹 대시보드를 생성하였습니다.

7. 터미널 접속을 끊어도 대시보드가 계속 유지되도록 백그라운드로 실행하였습니다.



## Repository File Structure

1. app_base: 앱 실행시 기초 베이스가 되는 파일
2. app_main: 가장 먼저 보여지는 메인화면
3. app_list: 데이터를 표 형태로 출력
4. app.search: 데이터를 검색하는 화면
5. app_chart: 데이터를 분석하여 차트 형태로 출력


## use library
streamlit
```
pip install streamlit
```

pandas
```
pip install pandas
```

matplotlib
```
pip install matplotlib
```

seaborn
```
pip install seaborn
```

plotly
```
pip install plotly
```


## Screenshots
![캡처5](https://user-images.githubusercontent.com/120348588/209500425-0adabe24-4329-4c46-9d6f-1a7e2507d960.PNG)

![캡처6](https://user-images.githubusercontent.com/120348588/209500426-20066838-f58d-43b7-9870-3109c7e159d9.PNG)

![캡처7](https://user-images.githubusercontent.com/120348588/209500430-660ff445-484a-438b-9c98-0b2697d5ad9f.PNG)

![캡처8](https://user-images.githubusercontent.com/120348588/209500431-5c9422dd-8afe-4cc2-82a4-bc7106784824.PNG)






## Dataset

Kaggle

https://www.kaggle.com/datasets/thedevastator/discovering-hidden-trends-in-global-video-games
