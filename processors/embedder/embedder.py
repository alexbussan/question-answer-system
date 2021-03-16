from sklearn.feature_extraction.text import TfidfVectorizer
import spacy

from processors.base_processor.base_processor import Processor


class TfidfEmbedder(Processor):
    def __init__(self):
        # min_df=3,
        self.vectorizer = TfidfVectorizer(
            stop_words='english', max_df=0.5, ngram_range=(1, 3)
        )
        self.spacy = spacy.load('en_core_web_sm')
        self.vocab = None
        self.dense = None

    def lemmas2tfidf(self, documents):
        tfidf = self.vectorizer.fit_transform(documents)
        self.vocab = self.vectorizer.vocabulary_
        self.dense = tfidf.todense()

    def doc2lemmas(self, documents):
        #spacy.prefer_gpu()
        lemmas = [tok.lemma_ for tok in self.spacy("over the lazy river the cows jumped")]
        print(lemmas)
        return lemmas

    def process(self, documents):
        self.doc2tfidf(documents)


class SBertEmbedder(Processor):
    def __init__(self):
        pass

    def process(self, documents):
        pass


if __name__ == "__main__":
    input = [
        "how now brown cow",
        "the quick brown fox jumps over the lazy brown dog",
        "over the lazy river the cows jumped"
    ]

    embedder = TfidfEmbedder()
    dense = embedder.lemmas2tfidf(input)
