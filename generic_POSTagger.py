#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:48:56 2018

@author: csrc
"""


import glob
import nltk
import ntpath


def posTagger(text):
    tagged = nltk.pos_tag(text)
    return tagged

fileout = open('/Users/apple/Desktop/ChestaFolder/pythonWorkspace/cleanedText/taggedfile.csv','a')
#fileoutNoun = open('/Users/apple/Desktop/ChestaFolder/pythonWorkspace/cleanedText/taggedNounsfile.csv','a')
inputfolder = glob.glob('/Users/apple/Desktop/ChestaFolder/pythonWorkspace/cleanedText/cleanedTweetText/*')
print(inputfolder)
for files in inputfolder:
    out_filename = ntpath.basename(files)
    fileoutNoun = open('/Users/apple/Desktop/ChestaFolder/pythonWorkspace/cleanedText/Nouns/' + out_filename + '.txt','a')
    file = open(files,'r')
    for lines in file:
        #print(lines)
        tokenized = nltk.word_tokenize(lines)
        #print(tokenized)
        tagged = nltk.pos_tag(tokenized)
        #print('----->>>>>>>>')
        for items in tagged:
            #fileout.write(items[0] + ',' + items[1] + '\n')
            if (items[1] == 'NN') or (items[1] == 'NNS') or (items[1] == 'NNP') or (items[1] == 'NNPS'):
                #print('noun')
                fileoutNoun.write(items[0] + '\n')
                
            
    