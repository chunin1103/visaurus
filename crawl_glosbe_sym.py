from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_glosbe(word):
    ini_url = "https://vi.glosbe.com/en/vi/"
    word = word.replace(' ', "+")
    word = word.replace('!', '')
    word = word.replace('?', '')
    word = word.strip()
    url     = ini_url + word

    conn = urlopen(url)
    raw_data = conn.read()
    webpage_text = raw_data.decode("utf-8")
    soup = BeautifulSoup(webpage_text, "html.parser")

    div1        = soup.find("div",{'class': 'phrase__translation__section'})
    div2        = div1.find_next("ul",{'class': 'translations__list'})
    all_li      = div2.find_all("li", {'class': 'translation__item'})
    sym_list = []

    for li in all_li:
        all_span    = li.find_all('span', {'class': 'translation__item__phrase'})
        for span in all_span:
            span = span.text
            span = span.strip()
            sym_list.append(span)

    # less frequent
    try:
        div3        = soup.find("div", {'class', 'px-2 text-sm font-medium less-frequent-translations__list-compact'})
        for span in div3:
            span = span.text
            span = span.strip()
            if span != "·":
                sym_list.append(span)
    except:
        pass
    return sym_list


get_glosbe('easy')