import numpy as np

from utils.data_connectors_qna.data_connectors_qna.reader import JsonReader
from processors.preprocessor_qna.preprocessor_qna.core import SquadDatasetTransformer
from processors.embedder.embedder.core import TfidfEmbedder
from processors.candidate_finder.candidate_finder.core import DotProductFinder
from processors.answer_finder.answer_finder.core import BertAnswerFinder

json_reader = JsonReader()
dataset = json_reader.read("/Users/alex/Downloads/dev-v2.0.json")

transformer = SquadDatasetTransformer()
documents, questions = transformer.process(dataset)

embedder = TfidfEmbedder()
corpus_embeddings = embedder.process(documents)
lemmas = embedder.get_lemmas()
vectorizer_id = embedder.get_vectorizer_id()

question_embedder = TfidfEmbedder(vectorizer_id)
question = "Who was the Norse leader?"
question_embedding = question_embedder.process([question])

candidate_finder = DotProductFinder()
candidate_docs, results = candidate_finder.process(corpus_embeddings, question_embedding, lemmas)
print(candidate_docs)

answer_finder = BertAnswerFinder()
answer_df = answer_finder.process(results, documents, question)
print(answer_df)





