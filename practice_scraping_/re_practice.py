#<정규식>
#re 를 사용함
#우리가 주민등록번호가 13자리로 이루어진 것, 이메일에 @ 하고 사이트 주소를 넣는 것처럼 html에도 정규식(포맷)이 존재
#정규식을 찾고 싶을 때
#정규식이 abcd,2345처럼 네자리 일련문자로 이루어져있을 때 cd로 시작하고 마지막 문자가 e인 애들을 전부 찾으려면 cd.e를 하면됨
import re
p = re.compile('ca.e') 
#p는 패턴을 의미
#cd.의 .은 문자열 하나를 의미 
# ^ : 문자열의 시작 ^de -> desk dept , case는 안됨 c로 시작하니까
# $ (se$) : 문자열의 끝 -> case, base다 됨. desk는 안됨

m = p.match("case")
#print(m.group()) 
#match의 case가 ca.e의 규칙과 맞으면 출력, 아니면 에러
#주어진 문자열의 처음부터 일치하는지 확인 만약 careless를 넣으면 ca.e이므로 care까지만 출력함


#if m : 
    #print(m.group())
    #print(m.string) #입력받은 문자열 그대로 입력
    #print(m.start()) # 일치하는 문자열의 시작 index
    #print(m.end()) # 일치하는 문자열의 끝 index
    #print(m.span()) # 일치하는 문자열의 시작/끝 index

#else : 
    #print("매칭되지 않음")
#-> m은 부울값으로 나오므로 걍 m만 하면 됨


#a = p.search("good care")
#주어진 문자열 중에 일치하는게 있는가 (처음부터 시작 안함) good care도 됨

if m : 
    print(m.group())
    print(m.string) #입력받은 문자열 그대로 입력
    print(m.start()) # 일치하는 문자열의 시작 index
    print(m.end()) # 일치하는 문자열의 끝 index
    print(m.span()) # 일치하는 문자열의 시작/끝 index

else : 
    print("매칭되지 않음")

lst = p.findall('good care cafe') #일치하는 모든 것을 리스트 형태로 반환
#print하면 ca.e에 일치하는게 care, cafe두개이므로 이 두개를 리스트로 출력해줌

#<정리>
#re.complie("원하는 형태 = 정규식")
#m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
#m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는지 확인
#lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환    



























