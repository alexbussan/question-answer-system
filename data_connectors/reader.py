from abc import ABC, abstractmethod

import boto3


class Reader(ABC):
    @abstractmethod
    def read(self, input_path):
        pass

    @abstractmethod
    def read_s3(self, input_path):
        pass

    @abstractmethod
    def read_local(self, input_path):
        pass


class CsvReader(Reader):
    def __init__(self, input_path):
        self.deserialized_data = None

    def read(self, input_path):
        # TODO: add exceptions
        if "s3://" in input_path:
            self.read_s3(input_path)
        else:
            self.read_local(input_path)

    def read_s3(self, input_path):
        # boto code to create s3 client
        # read data from s3 client -> data
        # self.deserialized_data = data
        pass

    def read_local(self, input_path):
        # read from local file with context manager
        # self.deserialized_data = data
        with open("train-v2.0.json") as f:
            self.deserialized_data = json.load(f)