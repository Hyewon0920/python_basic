#이미지 다운로드 받는 방법

import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers= headers)
res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")


images = soup.find_all("img", attrs={"class":"thumb_img"})

#이미지들이 url정보로 저장되어 있어서 그거 불러옴 
for image in images :
    #print(image["src"])
    image_url = image["scr"]
    if image_url.startwith("//") :
        image_url = "http:" + image_url
    
    #접속해서 파일 저장?
    
    for idx, image in enumerate(images) :
        #print(image["src"])
        image_url = image["scr"]
        if image_url.startwith("//") :
            image_url = "http:" + image_url
    
    print(image_url)
    image_res = requests.get(image_url)
    image_url.res.raise_for_status()
    
    with open("movie{}.jpg".format(idx+1)) as f :
        f.write(image_res.content)
    #1등부터 30등까지 거기에다 페이지에 있는 모든 이미지 다 가져오는 것
    #image_res.content = requests.get(image_url).content이므로 url에 직접 접속해서 바로다운로드 후 파일에 저장됨
    #idx가 0이면 1등 영화 이미지를 다운로드 받음 -> 5등까지 받고 싶다면 4까지 idx를 적용하면 됨
    
    if idx>=4 : #상위 5개 이미지까지만 다운로드
        break
    
    
    
    
    
    #2015 ~ 2019년까지 상위 5개 영화이미지 다운로드
    
    for year in range(2015,2020) :
        url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

        res = requests.get(url, headers= headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        images = soup.find_all("img", attrs={"class":"thumb_img"})

        for idx, image in enumerate(images) :
            #print(image["src"])
            image_url = image["scr"]
            if image_url.startwith("//") :
                image_url = "http:" + image_url
            
            print(image_url)
            image_res = requests.get(image_url)
            image_url.res.raise_for_status()
            
            with open("movie{}_{}.jpg".format(year, idx+1),"wb") as f :
                f.write(image_res.content)
            #movie{}_{}하는 이유는 1234 하고 다시 2017로 년도 바뀐 뒤 1234 하고 2018년도로 변경 -> 같은 이름으로 계속 덮어써져서 구분짓기 위해
            
                  
            






