import requests
import collections

def crawlOnelook(word):
    try:
        word = word.replace(' ', "+")
        word = word.replace('!', '')
        word = word.replace('?', '')
        word = word.strip()
        ini_url = "https://api.onelook.com/words?v=ol_gte3&ml=%20{{ u }}&qe=ml&md=dp&max=1000&k=olthes_r4"
        url = ini_url.replace("{{ u }}", word)
        r = requests.get(url)
        data = r.json()

        global tu_dong_nghia
        tu_dong_nghia =[]
        # for _ in range (0, 25):
        #     if data[_]['word'] is not None:
        #         tu_dong_nghia.append(data[_]['word'])
        n = 0
        for i in data:
            n += 1
            if i['word'] is not None and n <= 100:
                i['word'] = i['word'].strip()
                tu_dong_nghia.append(i['word'])
        return tu_dong_nghia
    except TypeError as e:
        print(e)
        print("handled successfully")
    print(tu_dong_nghia)

