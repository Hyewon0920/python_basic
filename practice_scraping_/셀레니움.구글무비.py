#동적페이지 스크래핑
#사용자가 작업했을 떄 페이지가 뜸

#목적 : 할인하는 영화정보만 빼오기

import requests
from bs4 import BeautifulSoup

url = "http://play.google.com/store/movies/top"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})

#한글페이지 반환
#header {} 안에 "Accept-Language" : "ko_KR, ko"

#스크롤을 내릴때마다 뭔가 새로 뜬다 -> 동적페이지 -> 셀레니움으로 사용 


for movie in movies :
    title = movie.find("div", attrs={"class" : "WsMG1c nnK0zc"}).get_text()
    print(title)
    
#동적으로 스크롤 내리면서 리스트 가져오는 방법
from selenium import webdriver
browser = webdriver.Chrome("C:/Users/hop09/Desktop/python/chromedriver.exe")
browser.maximize_window()

url = "http://play.google.com/store/movies/top"
browser.get(url)


#스크롤 내리기
browser.execute_script("window.scrollTo(0,1080)") #1920X1080
#해상도 정보는 바탕화면- 디스플레이 - 화면 들어가면 됨
#이 문장은 수정없이 그대로 사용!
#1080높이만큼 스크롤 내림

#화면 맨 밑까지 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollingHeight)")

#document.body.scrollHeight는 사실 현재 문서 높이를 가져와서 이를 반복, 맨 밑까지 내리는 것! 현재문서 높이를 가져오려면
prev_height = browser.execute_script("return document.body.scrollHeight")

#그럼 반복문을 돌려야지
import time
while True :
    prev_height = browser.execute_script("return document.body.scrollHeight")
    time.sleep(10)
    #페이지 로딩 대기
    
    #현재 문서 높이를 가져와서 저장
    #스크롤을 맨밑으로 내리고 나서 -> 10초만큼 기다렸다가 -> 변경된 높이를 현재문서높이에 저장
    #근데 이전높이 = 바뀐현재높이 = 문서의 끝 -> 탈출
    
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height :
        break
    else :
        prev_height = curr_height

print("스크롤 완료")


#스크래핑

import requests
from bs4 import BeautifulSoup

url = "http://play.google.com/store/movies/top"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url, headers= headers)
res.raise_for_status()
     
soup = BeautifulSoup(res.text, "lxml")
#selenium쓸거면 이부분을 soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})









