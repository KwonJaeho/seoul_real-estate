import pandas as pd
import requests, json

def get_location(address):
  url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
  # 'KaKaoAK '는 그대로 두시고 개인키만 지우고 입력.
  headers = {"Authorization": "KakaoAK 개인키"}
  api_json = json.loads(str(requests.get(url,headers=headers).text))
  address = api_json['documents'][0]['address']
  crd = {"lat": str(address['y']), "lng": str(address['x'])}
  address_name = address['address_name']

  return crd
info = pd.read_csv('./sample.csv')

address=[] ## 주소 정리
for i in range(len(info)):
  address_text1 = info.values[i,3]
  address_text2 = info.values[i,4]
  address_text3 = info.values[i,5]
  address_text = ("%s %s %s"%(address_text1,address_text2,address_text3))
  address.append(address_text)
print(address)
x=[] #위도
y=[] #경도
for i in range(len(address)):
  crd = get_location(address[i])
  x.append(crd['lat'])
  y.append(crd['lng']) 

df = pd.DataFrame(info)
print(df)
df.loc[:,'x']=x
df.loc[:,'y']=y
df.to_csv("test.csv", sep=',', index = False, encoding = 'utf-8')
