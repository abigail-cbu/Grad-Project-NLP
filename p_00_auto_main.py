# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:21:55 2020

@author: acorso
"""

import p_02_auto_corpus_loader

import p_04_auto_corpus_normalizer

import p_06_auto_encoding_bow

import p_06_auto_encoding_nltk

import p_06_auto_encoding_scikit

import p_06_auto_encoding_gensim

import numpy as np

import time


def main():
    print('\n\n' * 30)
    
    print("Hello From Main")
    print()
    print('Corpus from load_corpus_dict() function noted below:')
    print()
    """load_corpus_dict function takes a file name; .dat project files are noted below"""
    #Identify .dat file to read; 5 lines below were used for testing
    #file_dat = open('D:\\04_Research\\04_Code\\Hovig12\\Data3_Corpus_DIC\\GM_DIC\\GM_DIC_Corpus.dat', 'rb')
    #file_dat = open('D:\\04_Research\\04_Code\\Hovig12\\Data3_Corpus_DIC\\GN_DIC\\GN_DIC_Corpus.dat', 'rb')
    #file_dat = open('D:\\04_Research\\04_Code\\Hovig12\\Data3_Corpus_DIC\\NM_DIC\\NM_DIC_Corpus.dat', 'rb')
    #file_dat = open('D:\\04_Research\\04_Code\\Hovig12\\Data3_Corpus_DIC\\TM_DIC\\TM_DIC_Corpus.dat', 'rb')
    #file_dat = open('D:\\04_Research\\04_Code\\Hovig12\\Data3_Corpus_DIC\\ZT_DIC\\ZTest_DIC_Corpus.dat', 'rb')

    #p_02_auto_corpus_loader.corpus_function()

    #real code:
    #corpus_one = p_02_auto_corpus_loader.load_corpus_dict('D:\\04_Research\\04_Code\\Hovig12\\Data3_Corpus_DIC\\ZT_DIC\\ZTest_DIC_Corpus.dat', 'rb')
    #corpus_one = p_02_auto_corpus_loader.load_corpus_dict('D:\\04_Research\\04_Code\\Hovig12\\Data3_Corpus_DIC\\TM_DIC\\TM_DIC_Corpus.dat', 'rb')

    print('Which file do you want to normalize: ')
    print('1: ZTest_DIC_Corpus.dat')
    print('2: NM_DIC_Corpus.dat')
    selected_file = input('Input the number that corresponds to the file and then press Enter: ')
    try:
        selected_file = int(selected_file)
    except ValueError:
        print("That's not an int!")
            
    if selected_file == 1:
        print('ZTest selected. Processing data -----')
        corpus_one = p_02_auto_corpus_loader.load_corpus_dict('//Users//abigaillu//repos//Hovig12//Data3_Corpus_DIC//ZT_DIC//ZTest_DIC_Corpus.dat', 'rb')
        normalize_file_name = 'ZTest'
    elif selected_file == 2:
        print('NM selected. Processing data -----')
        corpus_one = p_02_auto_corpus_loader.load_corpus_dict('//Users//abigaillu//repos//Hovig12//Data3_Corpus_DIC//NM_DIC//NM_DIC_Corpus.dat', 'rb')
        normalize_file_name = 'NM'
    else:
        print('file not found')
        print('using ZTest')
        corpus_one = p_02_auto_corpus_loader.load_corpus_dict('//Users//abigaillu//repos//Hovig12//Data3_Corpus_DIC//ZT_DIC//ZTest_DIC_Corpus.dat', 'rb')
        normalize_file_name = 'ZTest'

    #print('corpus_one===================>>>')
    #print(corpus_one)
    #print('corpus_one===================>>>')

    start_time = time.time()
    #print()
    #p_04_auto_corpus_normalizer.test()
    #corpus_normalized_orig = p_04_auto_corpus_normalizer.auto_corpus_normalize(corpus_one)
    normalized = p_04_auto_corpus_normalizer.auto_corpus_normalize(corpus_one)
    np.save(normalize_file_name + '_normalizedCorpus.npy', normalized)
    print("=====Time to normalize corpus--- %s seconds ---\n" % (time.time() - start_time))
    
    corpus_normalized = np.load(normalize_file_name + '_normalizedCorpus.npy') # load normalized corpus

    #print(corpus_normalized)
    #print('\n\n')

#    start_time = time.time()
#    print()
#    #print('corpus_bow===================>>>')
#    p_06_auto_encoding_bow.test()
#    for x in corpus_normalized_orig:
#        p_06_auto_encoding_bow.encoding_bow(x, normalize_file_name + '_encoding_bow.npy')
#    p_06_auto_encoding_bow.encoding_bow(corpus_normalized, normalize_file_name + '_encoding_bow.npy')
##    for x in corpus_normalized:
##        p_06_auto_encoding_bow.encoding_bow(x)
#    #print('corpus_bow===================>>>')
#    print("p_06_auto_encoding_bow.encoding_bow--- %s seconds ---" % (time.time() - start_time))


### NLTK is DONE
#    start_time = time.time()
##    print()
#    p_06_auto_encoding_nltk.test()
#    p_06_auto_encoding_nltk.nltk_fq(corpus_normalized, normalize_file_name)
#    #print('one hot')
#    p_06_auto_encoding_nltk.nltk_one_hot(corpus_normalized, normalize_file_name)
#    #print('tf idf')
#    tf = p_06_auto_encoding_nltk.nltk_tf_idf(corpus_normalized, normalize_file_name)
#
#    f = open(normalize_file_name + '_nltk_tf_idf2.txt', 'w+')
#    for x in tf:
#        #print(x)
#        f.write(str(x) + "\n")
#        
#    f.close()
#    print('---------finish nltk_tf_idf')
#        
#    #save_write_file(normalize_file_name + '_nltk_tf_idf.txt', ''.join(list(tf)))
#     
#    print("=====p_06_auto_encoding_nltk--- %s seconds ---\n" % (time.time() - start_time))
#    
    

    start_time = time.time()
    #print()
    p_06_auto_encoding_scikit.test()
    p_06_auto_encoding_scikit.scikit_fq(corpus_normalized)
    print('one hot')
    #p_06_auto_encoding_scikit.scikit_one_hot(corpus_normalized)
    print('TF-IDF')
    p_06_auto_encoding_scikit.scikit_tf_idf(corpus_normalized)#corpus_normalized)
    print("=====p_06_auto_encoding_nltk--- %s seconds ---\n" % (time.time() - start_time))



    print()
    #p_06_auto_encoding_gensim.test()
    #p_06_auto_encoding_gensim.gensim_fq(corpus_normalized)
    #p_06_auto_encoding_gensim.gensim_one_hot(corpus_normalized)
    #p_06_auto_encoding_gensim.gensim_tf_idf(corpus_normalized)
    print('\n\n\n\n\n')
    

def save_write_file(file_name, text):      
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
        string = string + str(x.value)
        
    return string





main()












