import requests

auth_token='???????'
hed = {'Authorization': 'Bearer ' + auth_token}
data = {
    "to": "????",
    "messages":[
        {
            "type":"text",
            "text":"Hello, world1"
        },
        {
            "type":"text",
            "text":"Hello, world2"
        }
    ]
}

url = 'https://api.line.me/v2/bot/message/push'
response = requests.post(url, json=data, headers=hed)
print(response)
print(response.json())