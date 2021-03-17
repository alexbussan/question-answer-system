import json

from answer_finder import BertAnswerFinder
from data_connectors_qna.reader import CsvReader
from data_connectors_qna.writer import CsvWriter

# TODO: add values, or pass from lambda to lambda
ANSWERS_PATH = ""
CORPUS_PATH = ""


# Todo: restructure into smaller methods like embed_documents handler
class FindAnswers:
    def handle(self, event, context):
        # read data
        reader = CsvReader()
        query_text = event["query_text"]
        flow_id = event["flow_id"]
        candidate_indicies = event["candidate_indicies"]
        documents = reader.read(f"{CORPUS_PATH}/documents-{flow_id}.csv")

        for doc_id in candidate_indicies:
            documents.append(
                documents[doc_id]
            )
    
        # scan each doc with bert q and a
        # TODO: change logic so that this lambda is mapped parallelly in step functions
        answer_finder = BertAnswerFinder()
        results = []
        for i, document in enumerate(documents):
            results.append(answer_finder.process(i, document, query_text))
    
        # write out result
        writer = CsvWriter()
        writer.write(f"{ANSWERS_PATH}/answers-{flow_id}", results)

        return "SUCCESS"


def handler(event, context):
    return FindAnswers().handle(event, context)