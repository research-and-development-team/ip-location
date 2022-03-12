import requests

import json

print("""\033[92m

{}{}{}{}{}{}{}{}{}{}{}

SPY EYE 

{}{}{}{}{}{}{}{}{}{}{}

IP'den konum bulucu 

codes by : spyeye

""")

ip = input("\033[93mip giriniz örnek('147.229.2.90'): ")

url = "https://ipxapi.com/api/ip?ip="+ip

               

headers = {

  'Accept': "application/json",

  'Content-Type': "application/json",

  'Authorization': "Bearer 955|pQvR6oAhGBlrUxcZ7TSvFbZr4YDUTojj6d7Q1VuF",

  'cache-control': "no-cache"

 }

 

                

donus = requests.request("GET", url, headers=headers)   

bg = donus.text

ve = json.loads(bg)

for i in ve.items():

    print(i)
