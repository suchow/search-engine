"""Create an inverted index."""

import csv

import spacy

inverted_idx = {}

with open('JEOPARDY_CSV.csv') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for i, row in enumerate(reader):
        print(i)
        text = " ".join([row[3], row[5], row[6]]).split()
        text = [word.lower() for word in text]
        text = list(set(text))  # deduplication
        for word in text:
            if word not in inverted_idx:
                inverted_idx[word] = []
            inverted_idx[word].append(i)
    print(inverted_idx)


def search(query):
    raise NotImplementedError
