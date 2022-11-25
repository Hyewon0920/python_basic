import requests
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers= headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(res.text)


#get : 누구나 볼 수 있도록 ?뒤에가 변수임
#post : 보안데이터 숨겨서 보냄, 크기 제한 없음 
item = soup.find_all("li",attrs = {"class":res.compile("^search-product ")})
#print(item[0].find("div",attrs = {"class":"name"}).get_text())
    
#name = soup.find_all("div", attrs={"class":"name"})
#for x in name :
    #item = x.get_text()   
    
for items in item : 
    ad = item.find("span", artts = {"class":"ad-badge-text"})
    if ad :
        print("광고상품제외합니다")
        continue
    name = item.find("div",attrs = {"class":"name"}).get_text()
    price = item.find("strong",attrs = {"class":"price-value"}).get_text()
    stars = item.find("em",attrs = {"class":"rating"})
    if stars :
        stars.get_text()
    else : 
        stars = "평점없음"
    reviews = item.find("span",attrs = {"class":"rating-total-count"})
    if reviews :
        reviews.get_text()
    else : 
        reviews = "평점없음"
    #em태그에 텍스트가 없다고 뜰거임 -> 평점이 없는 상품이 있을 수 있음 그러면 조건문 걸기
    #stars = item.find("em",artts = {"class":"rating"}).get_text()에서 get_text()없애고 if 걸기
   #평점 수도 마찬가지 
   #평점수는 (26) 이런식으로 괄호로 나옴
    
    
    
    #광고 붙은거 제외하기
    ad = item.find("span", artts = {"class":"ad-badge-text"})
    if ad :
        print("광고상품제외합니다")
        continue
    
    
    #리뷰 100개 이상 평점 4.5이상
    if stars :
        stars.get_text()
    else : 
        #stars = "평점없음"
        print("평점없는 상품 제외합니다.")
        continue
    
    reviews = item.find("span",attrs = {"class":"rating-total-count"})
    if reviews :
        reviews.get_text()
    else : 
        print("평점 수 없는 상품 제외합니다.")
        continue
    
    if float(stars) >= 4.5 and int(reviews[1:2]) >= 100 :
        print(name, price, stars, reviews)
        
        

#애플 제품 제외하기
    name = item.find("div",attrs = {"class":"name"}).get_text()
    if "Apple" in name :
        print("애플제품 제외합니다")
        continue



#url 페이지 바꾸기
for i in range(1,6) :
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)
 #page number가 바뀌는 곳에 {}하고 뒤에 .format(i) 해주면 1부터 5까지 페이지숫자가 바뀜
    
    
    
    
    