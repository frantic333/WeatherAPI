TOKEN = '5373182818:AAHr2cSAVSq3oSQKsaYZQjSO8jcmmcKpBEM'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = [1203689969,1267050665,5204450846]
#MY_ID  = 1267050665
#MY_ID = 5204450846
UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID =data

WEATHER_TOKEN = 'e1dcdd65fca0c95c3e4b86de08ccdcca'

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

