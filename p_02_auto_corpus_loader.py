# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:40:16 2020

@author: acorso
"""

import pickle

##Testing function; to remove???
def corpus_function():
    print('corpus loader functions')
    print('******************************************************************')


#Function takes a .dat file_name and file_option to open it
def load_corpus_dict(file_name, file_option):
    #Variable to create list for dictionary documents
    all_items_list = []

    #Variable for document count; set at -1 for zero indexing to match list counts
    final_count_all = 0

    file_dat = open(file_name, file_option)

    #Load the .dat file as a list
    all_items = pickle.load(file_dat)

    #Count and view keys; comment out print()s as needed. Do not use print()s 
    #with a large corpus. A large corpus size causes console crash!!!
    for key in all_items:
        #print(key, all_items[key][0]) #, all_items[key]) ##View all; code below to view each element
        #print()
        #print(all_items[key][0])
        all_items_list.append(all_items[key][0])#Do not comment or delete this line!!!
        #print()
        #print(all_items[key][1])
        final_count_all += 1 #Add to count; do not comment or delete this line!!!
        #print()
        #print(all_items.items())
        #print('=====================================================================')

    print('The number of documents is===============================>>', final_count_all)
    return all_items_list
    file_dat.flush()##Flush for .dat file
    file_dat.close()##Close for .dat file


#Uncomment to test load_corpus_dict() function defined above
#load_corpus_dict('D:\\04_Research\\04_Code\\Hovig12\\Data3_Corpus_DIC\\ZT_DIC\\ZTest_DIC_Corpus.dat', 'rb')
