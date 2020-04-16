# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:52:25 2020

https://www.nltk.org/howto/twitter.html#simple

@author: acorso
"""
# from nltk.corpus import Tw

# from nltk.util import 

import json

import os

from six import string_types

from nltk.tokenize import TweetTokenizer

from nltk.corpus.reader.util import StreamBackedCorpusView, concat, ZipFilePathPointer

from nltk.corpus.reader.api import CorpusReader

from nltk.corpus.reader import TwitterCorpusReader

#class TwitterCorpusReader(CorpusReader):
print('hello class')


#https://www.nltk.org/_modules/nltk/corpus/reader/twitter.html
root = '.'
corpus_reader_tweet = TwitterCorpusReader(root, '.*\.json')

for tweet in corpus_reader_tweet.docs():
    print(json.dumps(tweet, indent=1, sort_keys=True))
#corpus_reader_tweet.ro




