from selenium import webdriver
browser = webdriver.Chrome("C:/Users/hop09/Desktop/python/chromedriver.exe")
browser.maximize_window()
#창 최대화

url = "https://m-flight.naver.com/"
browser.get(url)


#가는날 선택
browser.find_element_by_link_text("가는날 선택").click()

#이번달 27일, 28일 선택
browser.find_elements_by_link_text("27")[0].click() #[0] -> 이번달
#find_elements를 하는건 매달 27일이 있기 떄문이다 이때는 []로 특정을 해줘야함
browser.find_elements_by_link_text("28")[0].click()

#다음달 27,28 선택
browser.find_elements_by_link_text("27")[1].click() #[1] -> 다음달
#find_elements를 하는건 매달 27일이 있기 떄문이다 이때는 []로 특정을 해줘야함
browser.find_elements_by_link_text("28")[1].click()

#목적지 선택 -> xpath쓰기
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div/h3")

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()
#만약 안되면 xpath가 문제인거니까 우클릭 후 상위 클래스 xpath로 copy해오기

#로딩 기다리는 방법
#1. 엘레먼트 나올때까지만 기다려라 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

#우선 이 세개 import해주기

elem = WebDriverWait(browser,10).until(E.presence_of_element_located((By.XPATH, "기다릴 xpath")))
#until -> 이 xpath가 열릴때까지 10초 기다리셈





