import requests
import json
import time
from pprint import pprint

import const

'''
def answer_user_bot(data,chat):
    for i in const.MY_ID:
        if chat == i:
            data = {
                'chat_id' : i,
                'text': data
            }
            url = const.URL.format(token=const.TOKEN,
                                   method=const.SEND_METH)
            response = requests.post(url, data=data)
'''

def answer_user_bot(data, chat):
    for i in const.MY_ID:
        if chat == i:
            data = {
                'chat_id' : i,
                'text': data
            }
            url = const.URL.format(token=const.TOKEN,
                                   method=const.SEND_METH)
            response = requests.post(url, data=data)


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
    return parse_weather_data(data)

def get_message(data):
    return data['message']['text']


def get_chat_id(data):
    for elem in data:
        return elem['message']['chat']['id']



def save_update_id(update):
    with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    const.UPDATE_ID = update['update_id']
    return True


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
#            if elem['message']['chat']['id'] == const.MY_ID:
            needed_part = elem
            break

        #  проверка является последнее обработанное обновление тем, которое находится в файле
        # если нет, следовательно это новое обновление и мы не сохраняли его в наш файл
        if const.UPDATE_ID != needed_part['update_id']:
            # то мы обрабатываем это сообщение
            message = get_message(needed_part)
            msg = get_weather(message)
            chat = get_chat_id(result)
            answer_user_bot(msg,chat)
            # и сохраняем этот id
            save_update_id(needed_part)



            time.sleep(1)

if __name__ == '__main__':
    main()
