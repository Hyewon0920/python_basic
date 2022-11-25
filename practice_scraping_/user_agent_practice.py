#아까 requests했을 때 제대로 못가져온 url도 가져올 수 있게끔 함 
import requests
urls = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(urls, headers = headers)
res.raise_for_status() 

with open("nadocoding.html", "w", encoding= "utf8") as f :
    f.write(res.text)
    #f.write(soup.prettify()) 하면 예쁘게 출력가능
#user agent 우리가 했던 mozilla그거    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    