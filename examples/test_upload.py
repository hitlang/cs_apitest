import requests

url = "http://116.85.42.10/home/useredit"

payload = {'old_user_avatar': '/public/upload/user/avatar/1_1603272249.jpg',
'user_name': 'test1',
'user_email': 'test11@dt.com',
'user_sex': '1',
'user_phone': '',
'user_birthday': ''}
files = [
  ('user_avatar', open('/D:/pic/test_04.jpg','rb'))
]
headers = {
  'Cookie': 'PHPSESSID=tm5fq39s9g9oimmqte4mpf38q4'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))