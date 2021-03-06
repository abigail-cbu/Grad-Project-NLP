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


scikitFile = 'scikit_vectors.txt'

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
    ##print(vectors_final_scikit) ##don't need this anymore :)
    ##print()
    
    # write to single fine
    f = open('scikit_fq.txt', 'w+')
    f.write(str(vectors_final_scikit))
    f.close()
    
    # add to existing global file
    g = open(scikitFile, 'a+')
    g.write("\n" + str(vectors_final_scikit))
    g.close()
    #"""


def scikit_one_hot(corpus_one):
    print('scikit_one_hot')
    ##print(corpus_one) ##don't need this anymore :)
    # write to single file
    f = open('scikit_one_hot.txt', 'w+')
    f.write(str(corpus_one))
    f.close()
    #corpus_one = nltk.sent_tokenize(corpus_one)
    # for x in corpus_one:
    #     print(x)
    #     x = nltk.sent_tokenize(x)

    # add to existing global file
    g = open(scikitFile, 'a+')
    g.write("\n" + str(corpus_one))

    vectors_final_scikit_one_hot = CountVectorizer()
    vectors_final_scikit_one_hot.fit(corpus_one)
    print('-----------------------------------------------------')
    ##print(vectors_final_scikit_one_hot.vocabulary_) ## don't need this anymore :)
    f = open('scikit_one_hot_vocabulary.txt', 'w+')
    f.write(str(vectors_final_scikit_one_hot.vocabulary_))
    f.close()
    
    g.write("\n" + str(vectors_final_scikit_one_hot.vocabulary_))


    # vector_one_hot = Binarizer().fit(corpus_final)
    vector_all = vectors_final_scikit_one_hot.transform(corpus_one)
    ##print(vector_all) ## don't need this anymore :)
    f = open('scikit_one_hot_vector_all.txt', 'w+')
    f.write(str(vector_all))
    f.close()
    
    g.write("\n" + str(vector_all))

    ##print(vectors_final_scikit_one_hot.fit_transform(corpus_one).toarray()) ## don't need this anymore :)
    f = open('scikit_one_hot_vector_all_array.txt', 'w+')
    f.write(str(vectors_final_scikit_one_hot.fit_transform(corpus_one).toarray()))
    f.close()
    
    g.write("\n" + str(vectors_final_scikit_one_hot.fit_transform(corpus_one).toarray()))
    # print('-----------------------------------------------------')
    
    # corpus_final = vector_one_hot.fit_transform(corpus_one)
    # for x in corpus_final:
    #     print(x)


    g.close()

def scikit_tf_idf(corpus_one):
    print('scikit_tf_idf')
    tfidf = TfidfVectorizer()
    corpus = tfidf.fit_transform(corpus_one)
    ##print(corpus) ## don't need this anymore :)
    f = open('scikit_tf_idf.txt', 'w+')
    f.write(str(corpus))
    f.close()
    
    # add to existing global file
    g = open(scikitFile, 'a+')
    g.write("\n" + str(corpus))
    g.close()














