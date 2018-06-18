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

    # get tokens of sentence
    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    # get pos counts for a given sentence
    def pos(self, sentence):
        posCount = {}
        tags_list= self.nlp.pos_tag(sentence)
        for items in tags_list:
            if items[1] in posCount.keys():
                posCount[items[1]] += 1
            else:
                posCount[items[1]] = 1

        return posCount

    # get sentiment(positive, neutral, negative) count for given sentence
    def sentiment(self, sentence):
        val = self.nlp._request(annotators='sentiment', data=sentence)
        count = {}
        for sentence in val['sentences']:
            sentiment = sentence['sentiment']
            if sentiment not in count.keys():
                count[sentiment] = 0
            else:
                count[sentiment] += 1
        return count

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def question(self, sentence):
        parsed = self.parse(sentence)[:15].split('(')
        if 'SQ ' in parsed:
            return "Inverted question"
        elif 'SBARQ\n' in parsed:
            return "Direct question"
        return "No question"

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
    text += ' ' + text
    # print("Annotate:", sNLP.annotate(text))
    # print("POS:", sNLP.pos(text))
    # print("Tokens:", sNLP.word_tokenize(text))
    # print("NER:", sNLP.ner(text))
    # print("Parse:", sNLP.parse(text))
    # print("Dep Parse:", sNLP.dependency_parse(text))
    print(sNLP.question(text))
    # val = sNLP.getnlp()._request(annotators='sentiment', data=text)

