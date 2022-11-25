import requests
res = requests.get("http://naver.com")
#잘 가져온 것 같은데 잘못됐을 수도 있음 그러면 응답코드를 가져와서 잘 갖고 왔는지 확인하면 됨

print("응답코드 : ", res.status_code ) 
#200이면 정상임 = requests.codes.ok를 print하면 200이 나옴 얘는 다른 값 못가지고 ok가 되면 무조건 200임


res.raise_for_status() 
#html이나 정상적으로 url을 가져온 경우 괜찮은데 만약 그렇지 않으면 에러를 뱉고 프로그램을 종료시킴
#따라서 뒤의 두줄은 습관적으로 사용하면 됨
res = requests.get("http://naver.com")
res.raise_for_status() 
print(len(res.text))
#