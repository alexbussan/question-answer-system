import json
import boto3

from comprehender import Comprehender
from data_connectors.reader import CsvReader
from data_connectors.writer import CsvWriter


def compute_similarity(event, context):

    event_body = event["body"]

    # read data
    reader = CsvReader()
    query_text = event_body["query_text"]
    documents_to_scan = event_body["documents_to_scan"]
    corpus_path = event_body["corpus_path"]
    documents = []

    for doc_id in documents_to_scan:
        documents.append(
            reader.read(f"{corpus_path}/{doc_id}")
        )

    # scan each doc with bert q and a
    comprehender = Comprehender()
    results = []
    for doc in documents:
        results.append(comprehender.comprehend(query_text, doc))

    # write out result


    body = {
        "message": "Function executed successfully",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
