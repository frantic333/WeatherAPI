import requests
import json
import const
import time
from pprint import pprint

TOKEN = '5373182818:AAHr2cSAVSq3oSQKsaYZQjSO8jcmmcKpBEM'

URL = 'https://api.telegram.org/bot{TOKEN}/{method}'

updates = 'getUpdates'
send = 'sendMessage'
'''
url = URL.format(TOKEN = TOKEN, method = updates)
#print(url)

response = requests.get(url)

content = response.text


data = json.loads(content)
print(data)


result = data['result'][::-1]


pprint(result)

#list_of_messages = []


#result = data['result']

'''


'''
for i in result:
    list_of_messages.append(i['message']['text'])
print(list_of_messages)

'''


def parse_weather_data(data):
    for elem in data['weather']:
        weather_state = elem['main']
    temp = round(data['main']['temp'] - 273.15, 2)
    city = data['name']
    msg = f'The weather in {city}: Temp is {temp}, State is {weather_state}'
    print(msg)
    return (msg)


def get_weather(location):
    url = const.WEATHER_URL.format(city=location,
                                   token=const.WEATHER_TOKEN)
    response = requests.get(url)
    if response.status_code != 200:
        return 'city not found'
    data = json.loads(response.content)
    return data



def get_message(data):
    return data['message']['text']

def main():
    while True:
        # отправка запроса
        url = const.URL.format(token=const.TOKEN, method=const.UPDATE_METH)
        # получение ответа и взятие и него контента(текста)
        content = requests.get(url).text

        # преобразование контента из json в объект python
        data = json.loads(content)
        # берем переменную result и сортируем ее в обратном порядке
        result = data['result'][::-1]
        needed_part = None

        # парсинг сообщений
        for elem in result:
            # проверка от меня ли это сообщение(по id)
            if elem['message']['chat']['id'] == const.MY_ID:
                needed_part = elem
                break



        #  проверка является последнее обработанное обновление тем, которое находится в файле
        # если нет, следовательно это новое обновление и мы не сохраняли его в наш файл
        if const.UPDATE_ID != needed_part['update_id']:
            with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
                file.write(str(needed_part['update_id']))
            const.UPDATE_ID = needed_part['update_id']
#            return True
            # то мы обрабатываем это сообщение
            message = get_message(needed_part)
            msg = get_weather(message)

#            chat = get_chat_id(result)
#            answer_user_bot(msg)
#            answer_user_bot(msg,chat)
            # и сохраняем этот id
#            save_update_id(needed_part)


#            time.sleep(1)
