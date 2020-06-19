# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 09:56:45 2019
Updated on Sun Jan 06 14:12:45 2020
Updated on Mon Jan 20 12:00:00 2020

@author: acorso
##Double comments are test code lines.  This code will build a test dictionary given 
the corpus_one variable noted below.  It will also test the dictionary.  It is 
intended to be used with the Bengfort text page 56 to validate code from the text 
and the auto project's code.'

The code and be executed as many times as needed; it simply rewrites the dictionary 
referenced in the file_open_write variable noted below.

"""

import pickle

#Define dictionary file to write to
file_open_write = open('D:\\04_Research\\04_Code\\Hovig12\\Data3_Corpus_DIC\\ZT_DIC\\ZTest_DIC_Corpus.dat', 'wb')

document_count_final = 0 #Define variable to count documents

auto_dict = {} #Define the dictionary name to use for the corpus

#Define the test corpus as noted from the Bengfort text
# corpus_one = [
#     "The elephant sneezed at the sight of potatoes.",
#     "Bats can see via echolocation. See the bat sight sneeze! But I am going to talk about another studio and ever more stuff",
#     "Bats can see via echolocation. See the batabout another studio and ev",
#     "Wondering, she opened the door to the studio."
#     ]

corpus_one = [
    "The up up up up up up ? ! , . [] {} up elephant sneezed at the sight of potatoes.",
    "Bats can see via up up up up up echolocation. See the bat sight sneeze! But I am going to talk about another studio and ever more stuff",
    "Bats can see via echolocation. See up up up up up up up up the batabout another studio and : ? ! ; , ev",
    "Wondering, she opened the door to the studio up up up up up up."
    ]


#Loop the corpus and build the dictionary
for token_XX in corpus_one:
    print(token_XX) ##Test line to see each token in corpus; currently a list []
    document_count_final += 1 #Count number of documents
    
    #Extract document ID; build document and date for dictionary
    auto_dict[document_count_final] = token_XX, '2020' #Starting count at 1
 
print()##Print line break
print(auto_dict)##Print the dictionary

#Write the dictionary to file
pickle.dump(auto_dict, file_open_write, protocol=2)

#Close dictionary file
file_open_write.flush()
file_open_write.close()

print()
print('This is the document count:', document_count_final)
print()


"""
Below code opens and checks the dictionary; valid structure is (ID: (Text, Year))
"""
file_open_dat = open('D:\\04_Research\\04_Code\\Hovig12\\Data3_Corpus_DIC\\ZT_DIC\\ZTest_DIC_Corpus.dat', 'rb')

#Load the .dat file
all_items = pickle.load(file_open_dat)
for x in all_items.items():
    print(x)
 
file_open_dat.flush()
file_open_dat.close()

