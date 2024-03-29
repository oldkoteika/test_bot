import requests  
import json
#=================================Переменные=================================================================================================================
token = ''

#==================================бд========================================================================================================================

#=================================Функции====================================================================================================================
class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update
greet_bot = BotHandler(token)  

def main():
    new_offset = None
    api_url = "https://api.telegram.org/bot{}/".format(token)
    while True:
        try:
            
            greet_bot.get_updates(new_offset)
            last_update = greet_bot.get_last_update()
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = str (last_update['message']['chat']['id'])
           
            if last_chat_text=='Test':
                kebord1 ={"inline_keyboard":[[{"text":"Сайт", "url":"http://some.url"}]]}
                kebord1=json.dumps(kebord1)
                url =  api_url+'sendPhoto?chat_id='+last_chat_id+'&photo=AgADAgADx6sxGyQquEgHLPKTRL7prvPCtw8ABFg4CU5HNee7xm8AAgI&caption=Будет%20описание\nТел%20:%2089881634543\n&reply_markup='+kebord1
                requests.get(url=url)
        except:
            main()
 
             
        new_offset = last_update_id + 1
 #==========================================================================================================================================================       
if __name__ == '__main__':  
    try:    
        main()
    except KeyboardInterrupt:
        exit()