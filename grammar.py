'''
Before running this file. Start the server

java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation,sentiment,truecase,cleanxml,relation,natlog,quote" -port 9000 -timeout 30000 --add-modules java.se.ee

'''
from stanfordcorenlp import StanfordCoreNLP
import logging
import json
import pdb

class StanfordNLP:
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000) #quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,'
                          'relation,sentiment,truecase,cleanxml,relation,natlog,quote',
            'pipelineLanguage': 'en',
            'outputFormat': 'json',
            'options' : {"ner.useSUTime": False},
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    def getnlp(self):
        return self.nlp

    @staticmethod
    def tokens_to_dict(_tokens):
        tokens = defaultdict(dict)
        for token in _tokens:
            tokens[int(token['index'])] = {
                'word': token['word'],
                'lemma': token['lemma'],
                'pos': token['pos'],
                'ner': token['ner']
            }
        return tokens

if __name__ == '__main__':
    sNLP = StanfordNLP()
    text = 'A blog post using Stanford CoreNLP Server. Visit www.khalidalnajjar.com for more details.'
    # print("Annotate:", sNLP.annotate(text))
    # print("POS:", sNLP.pos(text))
    # print("Tokens:", sNLP.word_tokenize(text))
    # print("NER:", sNLP.ner(text))
    # print("Parse:", sNLP.parse(text))
    # print("Dep Parse:", sNLP.dependency_parse(text))
    import pdb
    pdb.set_trace()
    sNLP.getnlp()._request(annotators='natlog', data=text)