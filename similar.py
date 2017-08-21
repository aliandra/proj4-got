'''import flask
import numpy as np
import pandas as pd
import gensim

# Initialize the app
app = flask.Flask(__name__)

# Read in word2vec
thrones2vec = gensim.models.Word2Vec.load('thrones2vec')


@app.route("/")
def viz_page():
    with open("d3.html", 'r') as viz_file:
        return viz_file.read()


@app.route("/gof", methods=["POST"])
def score():
    """
    When A POST request with json data is made to this url,
    Read the grid from the json, update and send it back
    """
    data = flask.request.json
    words = thrones2vec.most_similar(data)
    return flask.jsonify({'words': words})

# --------- RUN WEB APP SERVER ------------ #

# Start the app server on port 80
# (The default website port)


app.run(host='0.0.0.0', port=5000)
'''