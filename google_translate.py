import requests
def GGtrans(wordname):
    url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=en&q=" + wordname
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    try:
        request_result = requests.get(url, headers=headers).json()
        global translated_result
        translated_result = request_result[0][0]
        print(translated_result) 
        return translated_result     
    except:
        pass
        

GGtrans('Tra từ tiếng Việt nè')
# print(translated_result)