import numpy as np

from data_connectors.reader import CsvReader
from processors.preprocessor.preprocessor.core import SquadDatasetTransformer
from processors.embedder.embedder.core import TfidfEmbedder


csv_reader = CsvReader()
csv_reader.read("/Users/alex/Downloads/dev-v2.0.json")
dataset = csv_reader.deserialized_data

transformer = SquadDatasetTransformer()
paragraphs, questions = transformer.process(dataset)

num_paragraphs = len(paragraphs)
num_questions = len(questions)

embedder = TfidfEmbedder()
corpus_embeddings, vocab = embedder.process(paragraphs)
corpus_lemmas = embedder.lemmas
print(corpus_embeddings)

question_embedder = TfidfEmbedder()
question = "When were the Normans in Normandy?"
query_embeddings, vocab = question_embedder.process([question])

scores = (np.array(corpus_embeddings) * np.array(query_embeddings).T)
results = (np.flip(np.argsort(scores, axis=0)))
candidate_docs = [corpus_lemmas[i] for i in results[:3, 0]]
print(candidate_docs)

# keys = dataset.keys()
# doc_type = type(dataset["data"])
# doc_len = len(dataset["data"])


# some_paragraphs = random.sample(paragraphs, 2)
# some_questions = random.sample(questions, 5)

