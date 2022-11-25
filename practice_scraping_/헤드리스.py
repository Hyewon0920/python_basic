#굳이 브라우저를 안써도 될 때 크롬을 띄우지 않고 쓰기

from selenium import webdriver
 
options = webdriver.ChromeOptions() 
options.headless = True
#이 두줄을 추가하면 브라우저 안열어도 됨 
options.add_argument("window-size=1920x1080") 
#가상으로 열때 명시적으로 윈도우 사이즈를 명시해줌 

browser = webdriver.Chrome()
browser.maximaize_window()


#주의점
#1. user agent 값을 가져올 때 headlessChrome이라고 떠서 내 접속을 막을 가능성이 있다 
#2. 이럴경우 options.add_argument("user-agent=그 존나긴 줄")하면 해결됨
