#107.0.5304.107(공식 빌드) (64비트)
import time
from selenium import webdriver

browser = webdriver.Chrome("C:/Users/hop09/Desktop/python/chromedriver.exe")
browser.get("http://naver.com")

#터미널에서도 가능 터미널에 python입력 후 위의 세문장 입력해주면 네이버 페이지 뜸
#로그인페이지로 바로 이동하고 싶다고 하면
#elem = browser.find_element_by_class_name("link_login")
#하고 elem치고 엔터누르면 됨 
#그리고 elem.click()치면 로그인페이지로 넘어감
#이전페이지 : browser.back() 
#이후페이지 browser.forward()
#새로고침 .refresh()
#특정 id,class를 가져오고 싶다면 : elem = browser.find_element_by_id("query(id임)")
#검색 : elem.send_keys("검색하고싶은 단어")
#엔터 : elem.send_keys(Keys.ENTER)
#f12에서 보이는 a라는 태그의 어떤 것을 가져오고 싶다면 : elem = browser.find_element_by_tag("a")
#종료 : browser.close() -> 지금 페이지만 
#아예 끄기 browser.quit()


#네이버 이동하고 로그인 버튼 클릭하기 
elem = browser.find_element_by_class_name("link_login")
elem.click


#id, pwd 입력
browser.find_element_by_id("id").send_keys("#id입력")
browser.find_element_by_id("pw").send_keys("#pw입력")


#로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

#다시 입력
time.sleep(3)
#화면 전환을 자동으로 3초정도 기다리게 해줌
browser.find_element_by_id_("id").clear()
#전에 썼던 아이디 지우기
browser.find_element_by_id("id").send_keys("#@1")



# html정보 출력
print(browser.page_source)


# 브라우저 종료
browser.quit() # 전체 종료
browser.clear() #현재페이지 종료

#
#
#
#
#
#
#
