import requests
import json

TOKEN = '5373182818:AAHr2cSAVSq3oSQKsaYZQjSO8jcmmcKpBEM'

URL = 'https://api.telegram.org/bot{TOKEN}/{method}'

updates = 'getUpdates'
send = 'sendMessage'
test = 'getMe'

#url = URL.format(TOKEN = TOKEN, method = updates)

#response = requests.get(url)

data = {
    'chat_id': '1203689969',
    'text': 'Hello from bot (LAST Message)'
}
# связывание вметсе трех переменных: URL,send, TOKEN с помощью метода format
url = URL.format(TOKEN=TOKEN, method = test)
#response = requests.post(url, data=data)
#print(response.text)
print(url)
