# matkok

This project is My First Project. Language : SQL, Python
---

## 맛콕

### 기능
맛집 탐색 도구
---

### 기능
- 맛집 검색 기능 : 키워드 입력시 크롤링 하여 음식점 정보를 가져옴.
- 맛집 지도 핀 기능 : 지도API를 연동하여 음식점 좌표에다가 핀 꽂아줌. 
- 주변 맛집 정보 : '구', '동' 입력시 근처에 맛집 정보 출력
- 사용자 별로 관리 : 로그인 시스템을 구현하여 사용자 맞춤형 즐겨찾기 가능
- 개인 맛집 데이터 엑셀로 분리 : 엑셀 추출 버튼 누르면 데이터베이스에 있는 데이터 엑셀로 추출하도록

---

### 설계

1. pyqt5로 기본 GUI 구현 - 메인창(검색창, 유저 즐겨찾기 정보), 로그인창
2. 검색 시 Requests로 데이터 크롤링 하여 GUI에 표현.
3. Database
- user 테이블(UserID, UserPW)
- matzip 테이블(음식점 고유ID ,음식점 이름, 지역, 가까운역, 가게, 분류, 전화번호, 영업시간, 평점 ,좌표)
- personalPage 테이블(UserID(외래키), 음식점 고유ID(외래키))

사용자 즐기찾기 목록 조회시 personalPage와 matzip 테이블 JOIN
...
이 부분은 좀 더 생각해보자
...

--- 

### 프로그래밍 개요

Python : ~~셀리니움(크롤링)~~, requests(크롤링), pyqt5(GUI)

DataBase : user 테이블, matzip 테이블, personalPage 테이블

---

### 셀레니움 환경 구축

~~[셀레니움 환경구축](https://blog.naver.com/sosow0212/222202718366)~~

---

### 참조

---
