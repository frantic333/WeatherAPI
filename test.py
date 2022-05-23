import requests
import json
from pprint import pprint

TOKEN = '5373182818:AAHr2cSAVSq3oSQKsaYZQjSO8jcmmcKpBEM'

URL = 'https://api.telegram.org/bot{TOKEN}/{method}'

updates = 'getUpdates'
send = 'sendMessage'

url = URL.format(TOKEN = TOKEN, method = updates)
#print(url)

response = requests.get(url)

content = response.text


data = json.loads(content)

result = data['result'][::-1]


pprint(result)

#list_of_messages = []


#result = data['result']


'''
for i in result:
    list_of_messages.append(i['message']['text'])
print(list_of_messages)

'''

