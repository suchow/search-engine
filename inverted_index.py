"""Create an inverted index for jeopardy questions."""

import csv

inverted_idx = {}

docs = []

with open("JEOPARDY_CSV.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for i, row in enumerate(reader):
        print(i)
        text = " ".join([row[3], row[5], row[6]]).split()
        text = [word.lower() for word in text]
        text = list(set(text))
        for word in text:
            if word not in inverted_idx:
                inverted_idx[word] = []
            inverted_idx[word].append(i)
        docs.append(" ".join(row))

print(docs[0])

def retrieve(query):
    query_terms = query.split()
    results = []
    for term in query_terms:
        results.extend(inverted_idx[term.lower()])
    results = list(set(results))
    return [docs[r] for r in results]

r = retrieve("Pentateuch, Deuteronomy")
print(r)

r = retrieve("colorless green ideas sleep furiously")
print(r)
