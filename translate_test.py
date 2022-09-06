import requests
word = 'Tôi là Quân'
url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=en&q=" + word
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

try:
    request_result = requests.get(url, headers=headers).json()
    
    print(request_result)
    print('[In English]: ' + request_result['alternative_translations'][0]['alternative'][0]['word_postproc'])
    print('[Language Dectected]: ' + request_result['src'])
except:
     pass