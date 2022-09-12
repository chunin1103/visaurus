from json import loads
from requests import get

def GGtrans(wordname):
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=en&tl=vi&q=" + wordname
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    try:
        request_result = get(url, headers=headers)
        global translated_result
        translated_result = loads(request_result.text)[0][0][0]
        print(translated_result)
        return translated_result     

    except:
        pass
