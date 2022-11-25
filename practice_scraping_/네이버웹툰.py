#import requests
#from bs4 import BeautifulSoup
#url = "https://comic.naver.com/webtoon/weekday.nhn"
#res = requests.get(url)
#res.raise_for_status()

#soup = BeautifulSoup(res.text, "lxml")

#1. 형제들을 찾고 싶을 때, 연애혁명 다음 rank를 프린트하고 싶을 때 
#print(soup.find("li" ,attrs = {"class" : "rank01"} ))
#rank1 = soup.find("li" ,attrs = {"class" : "rank01"})
#print(rank1.a.get_text())
#print(rank1.next_sibling)
#만약 출력이 안되면 next_sibling을 한번 더 쳐보기 -> 애들 사이에 줄바꿈이 있으면 원하는 내용이 출력 안될 수도
#다음 형제는 next_sibling인데, 기존 형제는 previous_sibling임
#부모는 rank1.paraent하면 됨
#next_sibling을 하는데 조건을 넣어서 찾고싶으면 괄호 열고 조건 적어주기
#rank1.next_sibling("li") -> 이러면 줄바꿈 고려 안해도 됨!
#형제들이 여럿일 경우 next_siblings << s붙이면 됨
#ranks = rank1.find.next_siblings("li")
#print(ranks.a.get_text())

#webtoon = soup.find('a', text="비즈니스 여친")
#text비교, text는 <a로 열고 닫은> 
#<a onclick="nclk_v2(event,'rnk*p.cont','791253','6')
# " href="/webtoon/detail?titleId=791253&amp;no=39" 
# title="비즈니스 여친-39화">비즈니스 여친-39화</a>
# <a ~~~~> 뒤 </a>앞 한글, 영어 -> 이게 텍스트임
#텍스트로 찾을 수 있음


#<네이버 웹툰 제목 정보 전부 끌고 오기>
#f12눌러서 확인해보면 class = title인 것들이 웹툰의 제목임을 알 수 있음

#soup = BeautifulSoup(res.text,"lxml")
#cartoons = soup.find_all("a", attrs = {"class": "title"})
#반복문을 통해서 title 빼오기
#for x in cartoons : 
    #print(x.get_text())
    

#<만화 회차 제목 가져오기>
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/list?titleId=783769&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#title = soup.find_all("a",attrs = {"class":"title"})
#print(title)

#class 앞에 붙어있는 보라색을 넣어줘야함 (a는 출력이 안되는데 td는 출력이 되는 이유)

#for cartoon in cartoons :
    #titles = cartoon.a.get_text()
    #link = "https://comic.naver.com" + cartoon.a["href"]
    #print(titles, link)


#인덱스 넘버를 변경해주면 바꿀 수 있음
#링크까지 같이 가져오기
#link = name[0].a["href"]
#print(title)
#print("https://comic.naver.com"+link)

#<평점 가져오기>

import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/list?titleId=783769&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

rating = soup.find_all("div", attrs = {"class":"rating_type"})
print(rating)
for ratings in rating: 
    
    rating_number = ratings.find("strong").get_text()
    print(rating_number)
#시바 어떤거는 a.get_text()만 해도 나오고 어떤건 왜 안나오는데

#터미널에 python치고 한줄한줄 결과 바로 나오게 할 수도 있음 방향키 위를 누르면 방금 적었던 코드 그대로 복사해줌
#빠져나가고 싶으면 exit()치면 됨
























