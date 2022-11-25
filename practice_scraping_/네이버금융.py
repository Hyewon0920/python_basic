#csv로 저장하는 방법
import csv
import requests
from bs4 import BeautifulSoup


for i in range(1,6) :
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page={}".format(i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
    res = requests.get(url, headers= headers)
    res.raise_for_status()
     
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    
    for row in data_rows :
        columns = row.find_all("td")
        data = [column.get_text() for column in columns]
        print(data)
    
    #1등부터 50등 까지 다 가져옴 (불필요한 줄바꿈, 빈칸 포함)
    
    #의미 없는 데이터 스킵
    
for i in range(1,6) :
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page={}".format(i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
    res = requests.get(url, headers= headers)
    res.raise_for_status()
     
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    
    for row in data_rows :
        columns = row.find_all("td")
        if len(columns) <=1 :
            continue
        #의미없는 데이터 스킵
        data = [column.get_text().strip() for column in columns]
        print(data)    
    
    
#csv 저장하기

filename = "시가총액 1-200"
f = open(filename,"w", encoding="utf8", newline="")
#newline써주는 이유는 안써주면 42 코웨이 ... //(엔터두번) 43,네이버... 이렇게 불필요한 엔터가 들어가서
writer = csv.writer(f)
#만약 한글이 깨지면 encoding="utf-8-sig"해주면 됨

for i in range(1,6) :
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page={}".format(i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
    res = requests.get(url, headers= headers)
    res.raise_for_status()
     
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    
    for row in data_rows :
        columns = row.find_all("td")
        data = [column.get_text() for column in columns]
        print(data)   
        writer.writerow(data)
    #writer.writerow(data) < csv에 넣어주는 작업
    

#타이틀 집어넣기

filename = "시가총액 1-200"
f = open(filename,"w", encoding="utf8", newline="")
#newline써주는 이유는 안써주면 42 코웨이 ... //(엔터두번) 43,네이버... 이렇게 불필요한 엔터가 들어가서
writer = csv.writer(f)
#만약 한글이 깨지면 encoding="utf-8-sig"해주면 됨

title = "N  종몽멱  현재가  전일비  등락률  액면가  시가총액    상장주식수  외국인비율  거래량  PER ROE".split("\t")
#타이틀 리스트 형태로 찍어주기
writer.writerow(title)

for i in range(1,6) :
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page={}".format(i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
    res = requests.get(url, headers= headers)
    res.raise_for_status()
     
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    
    for row in data_rows :
        columns = row.find_all("td")
        data = [column.get_text() for column in columns]
        print(data)   
        writer.writerow(data)
    #writer.writerow(data) < csv에 넣어주는 작업
    