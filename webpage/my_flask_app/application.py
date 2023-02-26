import psycopg2
import logging
from flask import Flask, request, render_template, g

application= app =Flask(__name__)

#adding logs
app.logger.addHandler(logging.StreamHandler())
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


conn = psycopg2.connect(
host="database-thesaurus.crnbbf6rv4rc.ap-southeast-1.rds.amazonaws.com",
port=5432,
database="postgres",
user="postgres",
password="Neji1103!!"
)

# get synonyms in db
def get_synonyms(word):
    cur = conn.cursor()
    cur.execute("SELECT synonyms FROM synonyms WHERE word=%s", (word,))
    result = cur.fetchone()
    return result[0] if result else "Word not found."

# index page
@application.route('/')
def index():
    return render_template('index.html')

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