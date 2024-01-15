'''
Created on 2024. 1. 15.

@author: sdedu
'''
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1150062000
hc = HTTPConnection('www.kma.go.kr') # 서버 주소
hc.request('GET', '/wid/queryDFSRSS.jsp?zone=1150062000') # 요청 파라미터

res = hc.getresponse() # 응답
resBody = res.read() # 응답 내용
# print(resBody.decode()) # 출력 (한글처리)

# XML Parsing
# DOM 객체 여러개 찾기 : .getiterator('태그명') / .iter('태그명')
# DOM 객체 하나 찾기 : .find('태그명')

'''
kmaWeather = fromstring(resBody)
# print(kmaWeather)

weathers = kmaWeather.iter('data')
# print(weathers)

for i in weathers:
    print(i)
    print('*'*20)
'''

for i in fromstring(resBody).getiterator('data'):
    print(i.find('day').text,i.find('hour').text,i.find('temp').text,i.find('wfKor').text)
    print('*'*20)
    