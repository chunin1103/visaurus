import sqlite3
import logging
import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, g, send_from_directory, request
# load dependencies
load_dotenv()

application= app =Flask(__name__)

# adding logs
app.logger.addHandler(logging.StreamHandler())
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


# get synonyms in db
def get_synonyms(word):
    conn = sqlite3.connect("synonyms.db")
    cur = conn.cursor()
    cur.execute("SELECT synonyms FROM symnonyms WHERE word=?", (word,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else "Word not found."

# index page
@application.route('/')
def index():
    return render_template('index.html')

# sitemap
@application.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, request.path[1:])

# search page
@application.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        word = request.form["word"]
        word = word.strip()
        word = word.lower()
        synonyms = get_synonyms(word)
        logging.info(f"Search request: word='{word}', synonyms='{synonyms}'")
        return render_template("search.html", word=word, synonyms=synonyms)
    return render_template("search.html")

# close the database connection when the Flask application is shutting down
@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()

# auto reload while debugging
app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == "__main__":
    application.run(debug=True)