# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:52:45 2020

@author: acorso
"""

import nltk
import numpy as np
import json
#import numpy as np

'''Bengfort Page 57'''
from collections import defaultdict ##Good import

'''Bengfort Page 63'''
from nltk.text import TextCollection ##Good import

def test():
    print('nltk')



def vectorize_nltk_fq(doc):
    features = defaultdict(int)
    for token in nltk.word_tokenize(doc):
        features[token] += 1
    return features


def nltk_fq(corpus_one, file_name):
    #"""
   # print('''***********************fq--Encoding--nltk***********************''')
    #"""

    #"""

    print('-----starting nltk_fq')
    #Use default corpus below (yes); but needs to be in denltk_fqfault dictionary
    vectors_final_nltk = map(vectorize_nltk_fq, corpus_one)
    #testarr = np.array(vectors_final_nltk)
    ###np.save(file_name + '_nltk_fq.npy', vectors_final_nltk)
    #np.savetxt(file_name + '_nltk_fq.txt', testarr) #needs array
   # print(vectors_final_nltk) #this was here before
    
    f = open(file_name + '_nltk_fq2.txt', 'w+')
    for x in vectors_final_nltk:
        #print(x)
        f.write(str(x) + "\n")
        
    f.close()
        
    ##save_write_file(file_name + '_nltk_fq.txt', build_string(vectors_final_nltk))

    """
    print('These are the individual nltk vectors:')
    for x in vectors_final_nltk:
        print(x)
        print()
    """
    print('---------finished nltk_fq')


def vectorize_nltk_one_hot(doc):
    doc = nltk.word_tokenize(doc)
    return {token: True for token in doc}


def nltk_one_hot(corpus_one, file_name):
    print('-----starting nltk_one_hot')

    vectors_final_nltk_one_hot = map(vectorize_nltk_one_hot, corpus_one)
   
    f = open(file_name + '_nltk_one_hot2.txt', 'w+')
    for x in vectors_final_nltk_one_hot:
        #print(x)
        f.write(str(x) + "\n")
    
    f.close() 
    
    """
     # this is how it was before
    #string = "" # build data as string to save to file

#    for x in vectors_final_nltk_one_hot:
#        print(x)
#        string = string + str(x)
    #np.save(file_name + '_nltk_one_hot.npy', vectors_final_nltk_one_hot) #saving as numpy 
   # save_write_file(file_name + '_nltk_one_hot.txt', string) # me trying to save, works
    """
    print('---------finished nltk_one_hot')
    
def nltk_tf_idf(corpus_one, file_name):
    print('-----starting nltk_tf_idf')
    corpus_one = [nltk.word_tokenize(doc) for doc in corpus_one]
    texts = TextCollection(corpus_one)

    for doc in corpus_one:
        yield {term: texts.tf_idf(term, doc) for term in doc}


"""
def save_write_file(file_name, text):
#    text = ""
#    # build string version of vectors
#    for x in mapped_data:
#        text = text + str(x)
        
    f = open(file_name, 'w+')
    f.write(text)
    f.close
        
    print('---------' + file_name + '----------')
    f = open(file_name, "r")
    print(f.read())
    f.close


def build_string(mapped_data):
    string = ""
    for x in mapped_data:
        string = string + str(x)
        
    return string
"""




