# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:51:45 2020

@author: acorso



p_04_auto_normalize
"""

import nltk
from nltk.corpus import stopwords
import string


def test():
    print('normalizer')
    print('******************************************************************')


def auto_corpus_normalize(corpus_one):
    #print(corpus_one)
    #print('The auto_tokenizer_list_clean()!!!')
    #print("auto_tokenizer_list_clean() return [something, something]")
    stop_words = stopwords.words('english')
    #print(stop_words)

    table = str.maketrans('', '', string.punctuation)
    #print(table)

    #print('---------------')
    stripped = [w.translate(table).lower()  for w in corpus_one]
    #print('\n\n==========================>>', stripped)
    #print('---------------')

    corpus_normalized = []
    for x in stripped:
        word_tokens = nltk.word_tokenize(x)
        x = [word for word in word_tokens if word not in stop_words]
        corpus_normalized.append(' '.join(x))
        #corpus_normalized.append(' '.join(nltk.word_tokenize(x)))

    #print(corpus_normalized)
    #print(x)
    # for x in corpus_normalized:
    #     print(x)

    return corpus_normalized



