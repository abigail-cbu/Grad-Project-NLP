# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:52:45 2020

@author: acorso
"""

import nltk

import numpy as np


def test():
    print('BOW')
    print('******************************************************************')


def encoding_bow(corpus_normalized, file_name):
    '''Bag-of-words'''

    vectorized_corpus = [] #overall vectors to save

    for vector in corpus_normalized:
        corpus_normalized = nltk.word_tokenize(corpus_normalized)
    
        wordfreq = {}
        for word in corpus_normalized:
            if word not in wordfreq.keys():
                wordfreq[word] = 1
            else:
                wordfreq[word] += 1
        
        # print()
        # print("The wordfreq new_corpus:")
        # print(wordfreq)
        # print('Number of documents:', len(wordfreq))
        
        # print()
        # print(wordfreq.keys())
        # print('Number of documents keys:', len(wordfreq.keys()))
        # print()
        # print(wordfreq.items())
        # print('Number of document items:', len(wordfreq.items()))
        # print()
    
    
        ##Sort and lambda source https://thispointer.com/python-how-to-sort-a-dictionary-by-key-or-value/
        listofTuples = sorted(wordfreq.items(), reverse = True, key=lambda x: x[1])
        for element in listofTuples:
            t = str(element[0]) + "\t\t\t " + str(element[1])
            print(t)
            vectorized_corpus.append(t)
            #print(element[0], "\t\t\t ", element[1])


    np.save(file_name, np.array(vectorized_corpus))
    
    