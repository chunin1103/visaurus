from urllib.request import urlopen
from bs4 import BeautifulSoup
# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"E:\Projects\.new_chapter_for_thesaurus\Credentials\vi-thesaurus-c8077aebe0c3.json"

def crawlThesaurus(word):
    # Url crawl
    ini_url = "https://www.thesaurus.com/browse/"
    url = ini_url + word
    try:
        # bs4 connect 
        conn = urlopen(url)
        urlopen(url)
        raw_data = conn.read()
        webpage_text = raw_data.decode("utf-8")

        # Crawl all page with soup
        soup = BeautifulSoup(webpage_text, "html.parser")

        # Get all words
        section = soup.find("section", {'class': "css-1fzg0m e1v16r9g0"})
        ul      = section.find("div", {'class': "css-1fsijta eebb9dz0"})
        li_list = ul.find_all("li")

        symnonym_list = []
        for __ in li_list:
            global word_crawled
            word_crawled = __.text.strip()
            symnonym_list.append(word_crawled)
        return symnonym_list, word_crawled
    except:
        pass 

crawlThesaurus('rebel')