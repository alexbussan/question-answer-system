from sklearn.feature_extraction.text import TfidfVectorizer

from processors.base_processor.base_processor import Processor


class TfidfEmbedder(Processor):
    def __init__(self, corpus):
        self.corpus = corpus

    def process(self):
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf = vectorizer.fit_transform(corpus)
        vocab = vectorizer.vocabulary_
        dense = tfidf.todense()
        print("hello")

        # return dataframe


class SBertEmbedder(Processor):
    def __init__(self):
        pass

    def process(self):
        pass


if __name__ == "__main__":
    corpus = [
        "how now brown cow",
        "the quick brown fox jumps over the lazy brown dog",
        "over the lazy river the cows jumped"
    ]

    embedder = TfidfEmbedder(corpus)
    embedder.process()