from json import loads
from requests import get
request_result = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=vi&tl=en&q=an+cư")
translated_text = loads(request_result.text)[0][0][0]
print(translated_text)