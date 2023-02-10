import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

def get_synonyms(word):
    conn = sqlite3.connect("synonyms.db")
    cur = conn.cursor()
    cur.execute("SELECT synonyms FROM symnonyms WHERE word=?", (word,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else "Word not found."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == 'POST':
#         word = request.form['word']
#         con = sqlite3.connect('synonyms.db')
#         cur = con.cursor()
#         query = "SELECT synonyms FROM symnonyms WHERE word='{}'".format(word)
#         cur.execute(query)
#         result = cur.fetchone()
#         con.close()
#         if result:
#             return result[0]
#         else:
#             return "Word not found"
#     return render_template('search.html')
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        word = request.form["word"]
        synonyms = get_synonyms(word)
        return render_template("search.html", word=word, synonyms=synonyms)
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)