import json

from base_handler.base import HandlerBase
from embedder.core import TfidfEmbedder
from data_connectors_qna.reader import JsonReader
from data_connectors_qna.writer import CsvWriter
from preprocessor_qna.core import SquadDatasetTransformer


# TODO: what can be moved to base class?
class EmbedDocuments(HandlerBase):
    def __init__(self):
        self.dataset = None
        self.documents = None
        self.embeddings = None
        self.lemmas = None
        self.vectorizer_id = None

    def read_data(self, documents_path):
        reader = JsonReader()
        self.dataset = reader.read(documents_path)

    def process_data(self, dataset):
        transformer = SquadDatasetTransformer()
        documents, questions = transformer.process(dataset)
        self.documents = documents

    def embed(self, documents):
        embedder = TfidfEmbedder(self.vectorizer_id)
        self.embeddings = embedder.process(documents)
        self.lemmas = embedder.get_lemmas()
        self.vectorizer_id = embedder.get_vectorizer_id()

    def write_data(self, embeddings_path, embeddings):
        writer = CsvWriter()
        writer.write(embeddings_path, embeddings)

    def return_response(self, embeddings_path, lemmas_path, vectorizer_id, flow_id):
        body = {
            "flow_id": flow_id,
            "embeddings_path": embeddings_path,
            "lemmas_path": lemmas_path,
            "vectorizer_id": vectorizer_id
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        return response

    def handle(self, event, context):
        # read data
        self.read_data(event['documents_path'])

        # preprocess data
        self.process_data(self.dataset)

        # create embeddings df
        if event['vectorizer_id']:
            event['vectorizer_id'] = event['vectorizer_id']
        self.embed(self.documents)

        # write embeddings
        embeddings_path = f"{event['output_path']}/embeddings-{event['id']}.csv"
        self.write_data(embeddings_path, self.embeddings)

        # write lemmas
        lemmas_path = f"{event['output_path']}/lemmas-{event['id']}.csv"
        self.write_data(lemmas_path, self.lemmas)

        # pass relevant information to next step in step functions
        self.return_response(
            embeddings_path, lemmas_path, self.vectorizer_id, event['id'])


def handler(event, context):
    return EmbedDocuments().handle(event, context)


