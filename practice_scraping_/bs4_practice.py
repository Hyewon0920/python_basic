import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/creation"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#lxml을 통해 html코드를 뷰티풀숲으로 다 만듦

print(soup.title)
#get_text를 하면 타이틀 정보를 받아옴
print(soup.title.get_text())
#title의 글자만 빼옴
print(soup.a)
#<a href=~~~~~>가 출력됨 soup에서 발견되는 제일 먼저의 a를 출력함
print(soup.a.attrs) 
#attributes를 보여줌 원하는 값은 soup.a["href"]이런식으로 대괄호 안에 넣어주기

soup.find("a", attrs={"class" : "~~~"})
#a 아래의 클래스가 ""인것만 찾음

