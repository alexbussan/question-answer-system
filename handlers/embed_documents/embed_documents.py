import json
import boto3
import logging

from handlers.base_handler import HandlerBase
from embedder.embedder.core import TfidfEmbedder
from data_connectors.reader import CsvReader
from data_connectors.writer import CsvWriter


# TODO: what functionality can move to base class?
class EmbedDocuments(HandlerBase):
    def __init__(self, event, context):
        self.event = event
        self.context = context
        self.input_data = None
        self.output_data = None

    def read_data(self, input_path):
        # TODO: make input_path a parameter for read()
        reader = CsvReader()
        self.input_data = reader.read(input_path)

    def embed(self):
        embedder = TfidfEmbedder(corpus=self.input_data)
        self.output_data = embedder.process()

    def write_data(self, output_path, data):
        writer = CsvWriter()
        writer.write(output_path, self.output_data)

    def handle(self, event, context=None):
        event_body = event["body"]

        # read data
        self.read_data(event_body["input_path"])

        # create embeddings df
        self.embed()

        # write embeddings
        self.write_data(event_body["output_path"])

        return "SUCCESS"


def handler(event, context):
    return EmbedDocuments(event, context).handle()


