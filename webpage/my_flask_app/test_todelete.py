import requests
import json

def get_translations(text, src='vi', dest='en'):
    url = f'https://translator-api.glosbe.com/translateByLangWithScore?sourceLang={src}&targetLang={dest}'
    headers = {
        'Content-Type': 'text/plain;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Origin': 'https://vi.glosbe.com',
        'Referer': 'https://vi.glosbe.com/',
    }
    response = requests.post(url, headers=headers, data=text.encode('utf-8'))
    print(response.text)

get_translations('ngạc nhiên')
#     if response.status_code == 200:
#         translations = response.json()
#         return translations
#     else:
#         return None

# text = 'ấn tượng'
# translations = get_translations(text)

# if translations:
#     print(translations['translation'])
# else:
#     print('No translations found.')