from sklearn.feature_extraction.text import TfidfVectorizer

from processors.base_processor.base_processor import Processor


class TfidfEmbedder(Processor):
    def __init__(self, corpus):
        self.corpus = corpus

    def process(self):
        # vectorizer = TfidfVectorizer(stop_words='english')
        # tfidf = vectorizer.fit_transform(corpus)
        # vectorizer.vocabulary_, tfidf.todense()
        print("hello")

        # return dataframe


class SBertEmbedder(Processor):
    def __init__(self):
        pass

    def process(self):
        pass
