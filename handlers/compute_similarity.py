import json
import boto3

from similarity_finder import SimilarityFinder
from data_connectors.reader import CsvReader
from data_connectors.writer import CsvWriter


def compute_similarity(event, context):

    event_body = event["body"]

    # read data
    # TODO: make input_path a parameter for read()
    reader = CsvReader()
    query_embedding = event["query_embedding"]
    corpus_embeddings = reader.read(event_body["embeddings_input_path"])

    # do similarity computation
    # this df is just a list of most similar document_ids
    similarity_df = SimilarityFinder(
        query_embedding=query_embedding,
        corpus_embeddings=corpus_embeddings
    ).process()

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
