from abc import ABC, abstractmethod

import boto3


class Writer(ABC):
    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def write_s3(self):
        pass

    @abstractmethod
    def write_local(self):
        pass


class CsvWriter(Writer):
    def __init__(self, output_path, serialized_data):
        self.output_path = output_path
        self.serialized_data = serialized_data

    def write(self):
        # TODO: add exceptions
        if "s3://" in self.output_path:
            self.write_s3()
        else:
            self.write_local()

    def write_s3(self):
        # boto code to create s3 client
        # write data from to s3 using self.serialized_data
        pass

    def write_local(self):
        # write to local file with context manager
        # and self.serialized_data
        pass
