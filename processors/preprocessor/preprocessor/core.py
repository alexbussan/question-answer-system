from processors.base_processor.base_processor import Processor


class SquadDatasetTransformer(Processor):

    def process(self, dataset):
        paragraphs = []
        questions = []
        for topic in dataset["data"]:
            for pgraph in topic["paragraphs"]:
                paragraphs.append(pgraph["context"])
                for qa in pgraph["qas"]:
                    if not qa["is_impossible"]:
                        questions.append(qa["question"])

        return paragraphs, questions
