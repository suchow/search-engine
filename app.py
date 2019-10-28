from flask import Flask, request, render_template
import numpy as np
import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    query = request.args.get("query", None)
    if query:
        results = retrieve(query)
        return render_template('results.html', query=query, results=results)
    else:
        return render_template('index.html')


def retrieve(query):
    return ["https://google.com/" for i in range(10)]
