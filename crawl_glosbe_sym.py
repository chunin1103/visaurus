from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import urllib.request


def get_glosbe(word):
    ini_url = "https://vi.glosbe.com/en/vi/"
    word = word.replace(' ', "+")
    word = word.replace('!', '')
    word = word.replace('?', '')
    word = word.strip()
    url     = ini_url + word
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36' }

    req = urllib.request.Request(url, headers=hdr)
    response = urllib.request.urlopen(req)
    raw_data = response.read()

    webpage_text = raw_data.decode("utf-8")
    soup = BeautifulSoup(webpage_text, "html.parser")
    div1        = soup.find("main",{'id': 'dictionary-content'})
    div2        = div1.find_next("section",{'class': 'bg-white px-1'})
    div3        = div2.find_next("div",{"class": "pl-1"})
    div4        = div3.find_next("ul",{"class": "pr-1"})
    all_li      = div4.find_all("li")

    sym_list = []

    for i in all_li:
        i = i.find_next("h3")
        i = i.text
        sym_list.append(i)
    print(sym_list)
    return sym_list


    # all_li      = div2.find_all("li", {'class': 'translation__item'})
    # sym_list = []
    
    # for li in all_li:
    #     all_span    = li.find_all('span', {'class': 'translation__item__phrase'})
    #     for span in all_span:
    #         span = span.text
    #         span = span.strip()
    #         sym_list.append(span)

    # # less frequent
    # try:
    #     div3        = soup.find("div", {'class', 'px-2 text-sm font-medium less-frequent-translations__list-compact'})
    #     for span in div3:
    #         span = span.text
    #         span = span.strip()
    #         if span != "·":
    #             sym_list.append(span)
    # except:
    #     pass
    # print(sym_list)
    # return sym_list
