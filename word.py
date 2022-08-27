key_word = input("You're finding the symnonym of: ")

# # to start, terminal initiate: pipenv shell -> flask run
# from flask import Blueprint, request
# from flask.templating import render_template
# import requests

# from .google_translate_ import *

# # word = 'fast'
# # word.encode('utf-8')


# # word = translate_text('en', word)
# # word = word.strip()
# # word = word.replace(' ', '-')
# # print(word)
# main = Blueprint('main', __name__)

# # not yet dohne
# @main.route('/', methods = ["GET", "POST"])
# def index():
#     if request.method == "GET":
#         return render_template("index.html")
    
#     elif request.method == "POST":
#         global key_word
#         form        = request.form
#         key_word    = form['search_engine']
#         key_word = translate_text('en', key_word)
#         key_word = key_word.strip()
#         key_word = key_word.replace(' ', '-')
#         from .result import final_viet
    
#         return render_template('render_word.html', symnonyms = final_viet, key_word = key_word)