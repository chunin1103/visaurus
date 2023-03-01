import requests
from bs4 import BeautifulSoup
import time
import csv

# session = requests.Session()

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
# }
# response = session.get("""https://vtudien.com/viet-anh/dictionary/nghia-cua-tu-t%E1%BB%A9%20di%E1%BB%87n""", headers=headers)
# time.sleep(10)
# soup = BeautifulSoup(response.text, "html.parser")
# time.sleep(10)
# section = soup.find("div", {'id': "divngoai"})
# print(soup)

url = 'https://vtudien.com/dstu'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}
data = {
    'tu': 'á',
    'src': 'viet',
    'tgt': 'viet',
    'tudien': 'dictionary'
}

response = requests.post(url, headers=headers, data=data)
response = response.text
response = response.split("||")
target = response[(len(response)-1)] 
# Print the response body
print(response)
