import json

from candidate_finder import DotProductFinder
from data_connectors_qna.reader import CsvReader
from data_connectors_qna.writer import CsvWriter


def compute_similarity(event, context):

    event_body = event["body"]

    # read data
    reader = CsvReader()
    question_embedding = event["question_embedding"]
    corpus_embeddings = reader.read(event_body["embeddings_input_path"])
    lemmas = reader.read(event_body["lemas_input_path"])

    # do similarity computation
    candidate_docs, results_indicies = DotProductFinder().process(
        corpus_embeddings, question_embedding, lemmas
    )

    # return similarity list to stepfunctions

    body = {
        "message": "Function executed successfully",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
