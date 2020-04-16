# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:53:14 2020

@author: acorso
"""

import nltk

'''Bengfort Page 57'''
from sklearn.feature_extraction.text import CountVectorizer ##Good import

'''Bengfort Page 61'''
from sklearn.preprocessing import Binarizer ##Good import

'''Bengfort Page 64'''
from sklearn.feature_extraction.text import TfidfVectorizer ##Good import




def test():
    print('scikit')


def scikit_fq(corpus_one):
    #"""
    print('''**********************fq--Encoding--scikit**********************''')
    #"""
    #"""
    vectorizer = CountVectorizer()
    vectors_final_scikit = vectorizer.fit_transform(corpus_one)#Use default corpus yes
    print('These are the scikit vectors:')
    print(vectors_final_scikit)
    print()
    #"""


def scikit_one_hot(corpus_one):
    print('scikit_one_hot')
    print(corpus_one)
    #corpus_one = nltk.sent_tokenize(corpus_one)
    # for x in corpus_one:
    #     print(x)
    #     x = nltk.sent_tokenize(x)



    vectors_final_scikit_one_hot = CountVectorizer()
    vectors_final_scikit_one_hot.fit(corpus_one)
    print('-----------------------------------------------------')
    print(vectors_final_scikit_one_hot.vocabulary_)

    # vector_one_hot = Binarizer().fit(corpus_final)
    vector_all = vectors_final_scikit_one_hot.transform(corpus_one)
    print(vector_all)
    print(vectors_final_scikit_one_hot.fit_transform(corpus_one).toarray())
    # print('-----------------------------------------------------')
    
    # corpus_final = vector_one_hot.fit_transform(corpus_one)
    # for x in corpus_final:
    #     print(x)



def scikit_tf_idf(corpus_one):
    print('scikit_tf_idf')
    tfidf = TfidfVectorizer()
    corpus = tfidf.fit_transform(corpus_one)
    print(corpus)













