from flask import Flask, request, render_template
import numpy as np
import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()

app = Flask(__name__)


import csv

inverted_idx = {}

docs = []

with open("JEOPARDY_CSV.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for i, row in enumerate(reader):
        app.logger.info(i)
        text = " ".join([row[3], row[5], row[6]]).split()
        text = [word.lower() for word in text]
        text = list(set(text))
        for word in text:
            if word not in inverted_idx:
                inverted_idx[word] = []
            inverted_idx[word].append(i)
        docs.append(" ".join(row))


@app.route('/')
def index():
    query = request.args.get("query", None)
    if query:
        app.logger.info("Query {} received".format(query))
        results = retrieve(query)
        return render_template('results.html', query=query, results=results)
    else:
        return render_template('index.html')


def retrieve(query):
    query_terms = query.split()
    results = []
    for term in query_terms:
        results.extend(inverted_idx[term.lower()])
    results = list(set(results))
    return [docs[r] for r in results]
