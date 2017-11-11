from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "czech"
SENTENCES_COUNT = 10


class urlList(APIView):

    def get(self, request):
        pass
        # urls = Summarize.objects.all()
        # return Response(serializer.data)
        # serializer = summarizeSerializer(urls, many=True)

    def post(self, request):
        posturl = request.data['url']  # url to be summarized
        parser = HtmlParser.from_url(posturl, Tokenizer(LANGUAGE))
        # or for plain text files
        # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        summary = ''
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            summary += str(sentence)
        # foo_instance = Summarize.objects.create(url=posturl, summarized=summary)
        html = "%s" % summary

        return Response(html)




