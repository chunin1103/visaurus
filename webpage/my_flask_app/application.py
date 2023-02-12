import sqlite3
from flask import Flask, request, render_template

application= app =Flask(__name__)

def get_synonyms(word):
    conn = sqlite3.connect("synonyms.db")
    cur = conn.cursor()
    cur.execute("SELECT synonyms FROM symnonyms WHERE word=?", (word,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else "Word not found."

@application.route('/')
def index():
    return render_template('index.html')

@application.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        word = request.form["word"]
        synonyms = get_synonyms(word)
        return render_template("search.html", word=word, synonyms=synonyms)
    return render_template("search.html")

if __name__ == "__main__":
    application.run(debug=True)