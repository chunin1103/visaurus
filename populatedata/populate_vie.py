import requests
from bs4 import BeautifulSoup
import time
import csv

url = """https://vi.wiktionary.org/w/index.php?title=Th%E1%BB%83_lo%E1%BA%A1i:Danh_t%E1%BB%AB_ti%E1%BA%BFng_Vi%E1%BB%87t&from=A"""

li_list = []
while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find("div", {'id': "mw-pages"})
    category_group = section.find_all("div", {'class': "mw-category-group"})

    for categry in category_group:
        ul = categry.find("ul")
        all_li = ul.find_all("li")
        for li in all_li:
            li = li.text
            li_list.append(li)
    print(li_list)  
        
    # Find the link to the next page

    link = soup.find("a", string="Trang sau")

    #  your code to find the link to the next page
    if link:
        next_page_link = "https://vi.wiktionary.org/" + link['href']
        print(next_page_link)
        url = next_page_link
        time.sleep(0.3)
    else:
        with open('words.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for word in li_list:
                writer.writerow([word])
