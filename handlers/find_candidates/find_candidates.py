import json

from candidate_finder import DotProductFinder
from data_connectors_qna.reader import CsvReader
from data_connectors_qna.writer import CsvWriter


# Todo: restructure into smaller methods like embed_documents handler
class FindCandidates:
    def handle(self, event, context):
        event = event["body"]
    
        # read data
        reader = CsvReader()
        question_embedding = event["question_embedding"]
        flow_id = event["flow_id"]
        corpus_embeddings = reader.read(event["embeddings_input_path"])
        lemmas = reader.read(event["lemmas_input_path"])
    
        # do similarity computation
        candidate_docs, candidate_indicies = DotProductFinder().process(
            corpus_embeddings, question_embedding, lemmas
        )
    
        # return similarity list to step functions output
        body = {
            "flow_id": flow_id,
            "candidate_indicies": candidate_indicies,
            "embeddings_path": event["embeddings_input_path"]
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        return response


def handler(event, context):
    return FindCandidates().handle(event, context)
