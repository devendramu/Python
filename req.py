import requests

'''
url= 'https://csdev.dnpg.com/cgi/login'
data = { "username": "6XZNRUZ2S8.administrator", "password": "wzjUbp9x7fhxjA=="}
r=requests.post(url,data=data,verify=False)
print r.status_code
print r.text


url = 'https://cgssso.xmqa.cloud.com:4443/xenmobile/api/v1/authentication/login'
data = {"username": "6XZNRUZ2S8.administrator", "password": "wzjUbp9x7fhxjA=="}

headers={'Host': 'cgssso.xmqa.cloud.com',
'Content-Type': 'application/json',
'Cache-Control': 'no-cache'
}
r=requests.post(url,data=data,headers=headers)
print r.status_code
print r.text
'''

url='https://cgssso.xmqa.cloud.com:4443/xenmobile/api/v1/serverproperties'

headers={'Host': 'cgssso.xmqa.cloud.com:4443',
'Content-Type': 'application/json',
"auth_token":"3ndxBs5PPqydqKPSwRWuOhoP:ebe53100f9a6e2f01a030b551569ce94",
'Cache-Control': 'no-cache',
'Postman-Token': 'e4509d72-cbd0-aa30-5d82-8f6c9548aa1a',
'Content-Length': '235'
}

data={
"name": "athena.dsauth.url",
"value": "https://accounts-dsauthweb.cloudburrito.com/.well-known/dsauth-configuration",
"displayName": "athena.dsauth.url",
"description": "athena.dsauth.url"
}
r=requests.post(url,headers=headers,data=data)
print r.status_code
print r.text