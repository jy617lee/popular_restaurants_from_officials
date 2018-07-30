# popular_restaurants_from_officials
업무추진비를 통해 분석한 공무원 맛집리스트!

## ToDo
#### 1. Data Analysys
- 가중치 부여 : 급수/카드사용빈도에 따른 가중치 부여

#### 2. Web
- 여러 기준으로 sort
- Map 기능

#### 3. Backend
- pixel, analytics로 user tracking 기능
- 크롤링 및 데이터 반영 자동화

## Done
- 서울시 업무추진비 크롤링
- 1차 Tidy 작업 완료
    - 상위 집행부서 column 추가
    - 장소/주소 column 분리
    - 방문시간을 년/월/일/시간으로 
- 2차 Tidy 작업 완료
    - 프랜차이즈 제외
    - 카페/커피/매점 등 키워드 제거
    - 부서별 특징 파악
