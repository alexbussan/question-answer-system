from abc import ABC, abstractmethod

import boto3


class Reader(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def read_s3(self):
        pass

    @abstractmethod
    def read_local(self):
        pass


class CsvReader(Reader):
    def __init__(self, input_path):
        self.input_path = input_path
        self.deserialized_data = None

    def read(self):
        # TODO: add exceptions
        if "s3://" in self.input_path:
            self.read_s3()
        else:
            self.read_local()

    def read_s3(self):
        # boto code to create s3 client
        # read data from s3 client -> data
        # self.deserialized_data = data
        pass

    def read_local(self):
        # read from local file with context manager
        # self.deserialized_data = data
        pass