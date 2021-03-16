import json
import random

with open("/Users/alex/Downloads/dev-v2.0.json") as f:
    doc = json.load(f)
keys = doc.keys()
doc_type = type(doc["data"])
doc_len = len(doc["data"])

paragraphs = []
questions = []
for topic in doc["data"]:
    for pgraph in topic["paragraphs"]:
        paragraphs.append(pgraph["context"])
        for qa in pgraph["qas"]:
            if not qa["is_impossible"]:
                questions.append(qa["question"])

num_parahraphs = len(paragraphs)
num_questions = len(questions)
some_paragraphs = random.sample(paragraphs, 2)
some_questions = random.sample(questions, 5)