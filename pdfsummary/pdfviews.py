from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals


from rest_framework.views import APIView
from rest_framework.response import Response

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from isummary.Parser.plaintext import PlaintextParser
from isummary.Tokenizer.tokenizer import Tokenizer
from isummary.Summary.textrank import LsaSummarizer as Summarizer
from isummary.Tokenizer.stem import Stemmer
from isummary.Tokenizer.getstopwords import get_stop_words

LANGUAGE = "czech"
SENTENCES_COUNT = 10


class pdfSummary(APIView):

    def get(self, request):
        pass

    def post(self, request):
        text = request.data['text']  # text to be summarized
        output = ""
        parser = PlaintextParser.from_string(text, Tokenizer("czech"))
        summarizer = LexRankSummarizer()
        summary = summarizer(parser.document, 20)
        for sentence in summary:
            sentence = str(sentence)
            output += sentence

        output1 = {'resp' : output}

        return Response(output1)




