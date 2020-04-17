# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:53:41 2020

@author: acorso
"""

import nltk

import gensim

'''Bengfort Page 57'''
from collections import defaultdict ##Good import

gensimFileName = 'gensim_vectors.txt'

def test():
    print('gensim')
    

def vectorize_gensim(doc):
    features = defaultdict(int)
    for token in nltk.word_tokenize(doc):
        features[token] += 1
    return features


def gensim_fq(corpus_one):
    #"""
    print('''**********************fq--Encoding--gensim**********************''')
    #"""

    #"""
    corpus_one = [vectorize_gensim(corpus_one_gensim) for corpus_one_gensim in corpus_one]
    id2word = gensim.corpora.Dictionary(corpus_one)
    vectors_final_gensim = [id2word.doc2bow(corpus_one_gensim) for corpus_one_gensim in corpus_one]
    
    print('These are the gensim fq vectors:')
    print(vectors_final_gensim)
    print()
    for x in vectors_final_gensim:
        print(x)
        
    f = open(gensimFileName, 'a+')
    f.write(str(vectors_final_gensim))
    f.close
    #"""



def gensim_one_hot(corpus_one):
    print()
    print('These are the gensim one hot vectors:')
    corpus_one = [vectorize_gensim(corpus_one_gensim) for corpus_one_gensim in corpus_one]
    id2word = gensim.corpora.Dictionary(corpus_one)
    vectors_final_gensim = [[(token[0], 1) for token in id2word.doc2bow(doc)] for doc in corpus_one]
    print(vectors_final_gensim)
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    for x in vectors_final_gensim:
        print(x)
        
    f = open(gensimFileName, 'a+')
    f.write(str(vectors_final_gensim))
    f.close


def gensim_tf_idf(corpus_one):
    print()
    print('These are the gensim tf idf vectors:')
    corpus_one = [vectorize_gensim(corpus_one_gensim) for corpus_one_gensim in corpus_one]
    lexicon = gensim.corpora.Dictionary(corpus_one)
    tfidf = gensim.models.TfidfModel(dictionary=lexicon, normalize = True)
    vectors_final_gensim = [tfidf[lexicon.doc2bow(corpus_one_gensim)] for corpus_one_gensim in corpus_one]
    #print(vectors_final_gensim)
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    for x in vectors_final_gensim:
        print(x)
        print()
        print()
        
    f = open(gensimFileName, 'a+')
    f.write(str(vectors_final_gensim))
    f.close






